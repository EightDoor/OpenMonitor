<template>
  <ZCard title="系统信息">
    <el-row>
      <el-col :md="4" :xs="12">
        <div class="status-item">
          <SysInfoAverageLoad :data="averageLoad"/>
        </div>
      </el-col>
      <el-col :md="4" :xs="12">
        <div class="status-item">
          <SysInfoCPU :cpuInfo="cpuInfo"/>
        </div>
      </el-col>
      <el-col :md="4" :xs="12">
        <div class="status-item">
          <SysInfoMemoryUsageRate :data="memoryUsageRate"/>
        </div>
      </el-col>
    </el-row>
  </ZCard>
  <ZCard class="tw-mt-4" title="磁盘信息">
    <el-row>
      <el-col :md="24" :xs="24">
        <div class="status-item-disk">
          <SysInfoDisk :list="diskInfoList"/>
        </div>
      </el-col>
    </el-row>
  </ZCard>
  <el-row :gutter="20" class="tw-mt-4" v-if="hardwareTemperature?.length > 0">
    <el-col :md="24" :xs="24">
      <ZCard title="传感器数据">
        <SysInfoTemperatures :data="hardwareTemperature"/>
      </ZCard>
    </el-col>
  </el-row>
  <el-row :gutter="20" class="tw-mt-4" v-if="diskHealth?.length > 0">
    <el-col :md="24" :xs="24">
      <ZCard title="磁盘状态 SMART">
        <SysInfoDiskHealth :data="diskHealth"/>
      </ZCard>
    </el-col>
  </el-row>
  <el-row :gutter="20" class="tw-mt-4">
    <el-col :md="12" :xs="24" v-loading="!diskIO">
      <ZCard title="磁盘IO">
        <SysInfoDiskIO :data="diskIO"/>
      </ZCard>
    </el-col>
    <el-col :md="12" :xs="24">
      <ZCard title="流量">
        <SysInfoFlow :data="flowData"/>
      </ZCard>
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
import {onMounted, onUnmounted, ref} from "vue";
import SysInfoCPU from "@/views/home/components/SysInfo/SysInfoCPU.vue";
import MonitorApi from "@/api/MonitorApi";
import logger from "@/utils/logger";
import {IAverageLoad, ICpu, IDiskHealth, ISysInfoMemory} from "@/interface/ISysInfo.ts";
import SysInfoMemoryUsageRate from "@/views/home/components/SysInfo/SysInfoMemoryUsageRate.vue";
import SysInfoDisk from "@/views/home/components/SysInfo/SysInfoDisk.vue";
import SysInfoDiskIO from "@/views/home/components/SysInfo/SysInfoDiskIO.vue";
import ZCard from "@/components/ZCard.vue";
import {ISysInfoDiskInfo} from "@/interface/ISysInfoDisk.ts";
import SysInfoFlow from "@/views/home/components/SysInfo/SysInfoFlow.vue";
import {ISysInfoIOStatistics} from "@/interface/ISysInfoIOStatistics.ts";
import {ISysInfoTemperatures} from "@/interface/ISysInfoTemperatures.ts";
import SysInfoTemperatures from "@/views/home/components/SysInfo/SysInfoTemperatures.vue";
import SysInfoDiskHealth from "@/views/home/components/SysInfo/SysInfoDiskHealth.vue";
import {ElMessage} from "element-plus";
import SysInfoAverageLoad from "@/views/home/components/SysInfo/SysInfoAverageLoad.vue";


defineExpose({
  refreshData
})

// cpu
const cpuInfo = ref<ICpu>()
// 内存
const memoryUsageRate = ref<ISysInfoMemory>()
const intervalValue = ref()
// 3秒钟
const intervalTime = 3000;

function getSysDiskInfo(item) {
  const [device, path, fs_type, options] = item;
  diskInfoList.value = []
  MonitorApi.sysDiskInfo(path).then(res => {
    const data = res.data;
    const list = diskInfoList.value
    list.push({
      ...data,
      device,
      path,
      fs_type,
      options
    });
    diskInfoList.value = list.sort((a, b) => a.path!.length - b.path!.length)
    logger.debug(`磁盘信息: ${path}`, data)
  })
}

const averageLoad = ref<IAverageLoad>()

function sysAverageLoad() {
  MonitorApi.sysAverageLoad().then(res => {
    const data = res.data;
    averageLoad.value = data;
    logger.debug('cpu平均负载 1分钟、5分钟、15分钟', data);
  })
}

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
  sysAverageLoad()

  getDiskIO()
  getIOStatistics()
  getTemp()
}

// 磁盘
const diskList = ref<string[]>([])
const diskInfoList = ref<ISysInfoDiskInfo[]>([])
// 60秒
const intervalTimeDisk = 60000
const interValueDisk = ref()

function getSysDisk() {
  diskList.value = []
  return MonitorApi.sysDiskList().then(res => {
    const data = res.data
    diskList.value = data
    logger.debug('磁盘列表', data)
  })
}

function getSysDiskInfoInterval() {
  diskList.value.forEach((item) => {
    getSysDiskInfo(item)
  })
}

// 磁盘IO
const diskIO = ref()

function getDiskIO() {
  MonitorApi.sysDiskIO().then(res => {
    const data = res.data;
    diskIO.value = data;
    logger.debug('磁盘IO信息', data)
  })
}

// 流量
const flowData = ref<ISysInfoIOStatistics>()

function getIOStatistics() {
  MonitorApi.networkTrafficStatistics().then(res => {
    const data = res.data;
    logger.debug('流量统计信息', data)
    flowData.value = data;
  })
}

// 传感器数据
const hardwareTemperature = ref<ISysInfoTemperatures[]>([])

function getTemp() {
  MonitorApi.getTemp().then(res => {
    const data = res.data
    logger.debug('传感器数据', data);
    hardwareTemperature.value = data;
  })
}

function startInterval() {
  intervalValue.value = setInterval(getSysInfo, intervalTime)
  interValueDisk.value = setInterval(getSysDiskInfoInterval, intervalTimeDisk)
}

// 磁盘健康
const diskHealth = ref<IDiskHealth[]>([])

function getDiskHealth() {
  diskHealth.value = []
  diskList.value.forEach((item, index) => {
    const disk = item[0]
    MonitorApi.getDiskHealth(disk).then(res => {
      const data = res.data;
      logger.debug(`磁盘健康检查 -> ${index}`, data)
      if (data?.error) {
        ElMessage.error(data.error)
      } else {
        if (data?.disk) {
          diskHealth.value.push(data)
        }
      }
    })
  })
}

/**
 * 刷新数据
 */
async function refreshData() {
  await getSysDisk()
  getDiskHealth()
  getSysInfo()
  getSysDiskInfoInterval()
}

onUnmounted(() => {
  if (intervalValue.value) {
    clearInterval(intervalValue.value)
  }
  if (interValueDisk.value) {
    clearInterval(interValueDisk.value)
  }
})

onMounted(async () => {
  await refreshData()

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
  flex-wrap: wrap;
  flex: 1;
}
</style>
