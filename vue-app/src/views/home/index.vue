<template>
  <HomeLayout>
    <el-radio-group @change="changeRadio" v-model="selectIP" class="tw-mb-2">
      <el-radio :value="item.value" size="large" border v-for="(item, index) of Config.serverIps" :key="index">
        {{ item.label }}
      </el-radio>
    </el-radio-group>
    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
      <!--      <el-tab-pane label="基础" name="sysinfo">-->
      <!--        <SysInfoMonitor ref="sysInfoMonitorRef"/>-->
      <!--      </el-tab-pane>-->
      <el-tab-pane label="设置" name="setting">
        <Settings/>
      </el-tab-pane>
    </el-tabs>
  </HomeLayout>
</template>
<script lang="ts" setup>

import HomeLayout from "@/views/home/components/HomeLayout.vue";
import {onMounted, ref, watch} from "vue";
import {ElMessage, TabsPaneContext} from "element-plus";
import logger from "@/utils/logger.ts";
import Config from "@/config";
import {useHome} from "@/store/models/useHome.ts";
import Settings from "@/views/home/components/Settings/Settings.vue";

// const activeName = ref("sysinfo")
const homeStore = useHome()

const activeName = ref("setting")

function handleClick(tab: TabsPaneContext, event: Event) {
  console.log(tab, event)
}

const selectIP = ref()

function changeRadio(val: string) {
  logger.debug('当前选择项', val)
  const findData = Config.serverIps.find((item) => item.value === val);
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

onMounted(() => {

})
</script>
<style lang="scss" scoped></style>
