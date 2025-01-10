<template>
  <el-card  shadow="always">
    <el-row>
      <el-col :md="4" :xs="8">
        <div class="status-item">
          <SysInfoCPU :cpuInfo="cpuInfo"/>
        </div>
      </el-col>
    </el-row>
  </el-card>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import SysInfoCPU from "@/views/home/components/SysInfo/SysInfoCPU.vue";
import MonitorApi from "@/api/MonitorApi";
import logger from "@/utils/logger";
import {ICpu} from "@/interface/ISysInfo.ts";

const cpuInfo = ref<ICpu>()

function getSysInfo() {
  MonitorApi.sysCpuInfo().then(res=>{
    const data = res.data;
    cpuInfo.value = data;
    logger.debug('cpu信息', data)
    setTimeout(()=>{
      getSysInfo()
    }, 1000)
  })
}

onMounted(()=>{
  getSysInfo()
})
</script>

<style scoped lang="scss">
.status-item {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
