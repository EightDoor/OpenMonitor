<template>
  <el-card shadow="always">
    <el-row>
      <el-col :md="4" :xs="8">
        <div class="status-item">
          <SysInfoCPU :cpuInfo="cpuInfo"/>
        </div>
      </el-col>
      <el-col :md="4" :xs="8">
        <div class="status-item">
          <SysInfoMemoryUsageRate :data="memoryUsageRate"/>
        </div>
      </el-col>
      <el-col :md="16" :xs="12">
        <div class="status-item-disk">
          <SysInfoDisk :list="diskInfoList"/>
        </div>
      </el-col>
    </el-row>
  </el-card>
</template>

<script setup lang="ts">
import {onMounted, onUnmounted, ref} from "vue";
import SysInfoCPU from "@/views/home/components/SysInfo/SysInfoCPU.vue";
import MonitorApi from "@/api/MonitorApi";
import logger from "@/utils/logger";
import {ICpu, ISysInfoMemory} from "@/interface/ISysInfo.ts";
import SysInfoMemoryUsageRate from "@/views/home/components/SysInfo/SysInfoMemoryUsageRate.vue";
import SysInfoDisk from "@/views/home/components/SysInfo/SysInfoDisk.vue";

// cpu
const cpuInfo = ref<ICpu>()
// 内存
const memoryUsageRate = ref<ISysInfoMemory>()
const intervalValue = ref()
// 3秒钟
const intervalTime = 3000;

// 磁盘
const diskList = ref<string[]>([])
const diskInfoList = ref<ISysInfoDiskInfo[]>([])
// 60秒
const intervalTimeDisk = 60000
const interValueDisk = ref()

function getSysInfo() {
  MonitorApi.sysCpuInfo().then(res => {
    const data = res.data;
    cpuInfo.value = data;
    logger.debug('cpu信息', data)
  })

  MonitorApi.sysMemoryInfo().then(res => {
    const data = res.data
    memoryUsageRate.value = data
    logger.debug('内存信息', data)
  })
}

function getSysDisk() {
  diskInfoList.value = []
  MonitorApi.sysDiskList().then(res => {
    const data = res.data
    diskList.value = data
    data.forEach((item) => {
      getSysDiskInfo(item)
    })
    logger.debug('磁盘列表', data)
  })
}

function getSysDiskInfo(item) {
  const [device, path, fs_type, options] = item;
  MonitorApi.sysDiskInfo(path).then(res => {
    const data = res.data;
    diskInfoList.value.push({
      ...data,
      device,
      path,
      fs_type,
      options
    });
    logger.debug(`磁盘信息: ${path}`, data)
  })
}

function startInterval() {
  getSysInfo()
  intervalValue.value = setInterval(getSysInfo, intervalTime)

  getSysDisk()
  interValueDisk.value = setInterval(getSysDisk, intervalTimeDisk)
}

onUnmounted(() => {
  if (intervalValue.value) {
    clearInterval(intervalValue.value)
  }
  if (interValueDisk.value) {
    clearInterval(interValueDisk.value)
  }
})

onMounted(() => {
  startInterval()
})
</script>

<style scoped lang="scss">
.status-item {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.status-item-disk {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  margin-left: 40px;
}
</style>
