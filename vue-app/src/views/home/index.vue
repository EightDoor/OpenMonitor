<template>
  <HomeLayout>
    <el-radio-group @change="changeRadio" v-model="selectIP" class="tw-mb-2">
      <el-radio :value="item.value" size="large" border v-for="(item, index) of homeStore.getServerIps" :key="index">
        {{ item.label }}
      </el-radio>
    </el-radio-group>
    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
      <el-tab-pane v-if="homeStore.getServerIps.length > 0" label="基础" name="sysinfo">
        <SysInfoMonitor ref="sysInfoMonitorRef"/>
      </el-tab-pane>
      <el-tab-pane label="设置" name="setting">
        <Settings/>
      </el-tab-pane>
    </el-tabs>
  </HomeLayout>
</template>
<script lang="ts" setup>

import HomeLayout from "@/views/home/components/HomeLayout.vue";
import {onMounted, ref, watch} from "vue";
import {ElMessage, ElNotification, TabsPaneContext} from "element-plus";
import logger from "@/utils/logger.ts";
import {useHome} from "@/store/models/useHome.ts";
import Settings from "@/views/home/components/Settings/Settings.vue";
import SysInfoMonitor from "@/views/home/components/SysInfo/SysInfoMonitor.vue";
import BusinessUtil from "@/utils/BusinessUtil.ts";

const activeName = ref("sysinfo")
const homeStore = useHome()

// const activeName = ref("setting")

function handleClick(tab: TabsPaneContext, event: Event) {
  console.log(tab, event)
}

const selectIP = ref()

function changeRadio(val: string) {
  logger.debug('当前选择项', val)
  const findData = homeStore.getServerIps.find((item) => item.value === val);
  if (findData) {
    ElMessage.success(`切换 ${findData.label}`)
  }
  homeStore.setSelectIP(val)
  sysInfoMonitorRef.value?.refreshData()
}

watch(() => homeStore.getSelectIP, (value) => {
  if (value) {
    selectIP.value = value
  }
}, {
  immediate: true
})

const sysInfoMonitorRef = ref()


function getIps() {
  const ips = homeStore.getServerIps
  logger.debug('ips', ips)
  if (ips.length === 0) {
    ElNotification({
      title: '提示',
      type: 'warning',
      message: '请设置服务器地址',
    })
    activeName.value = 'setting'
  }
}

onMounted(() => {
  BusinessUtil.initStorage()
  getIps()
})
</script>
<style lang="scss" scoped></style>
