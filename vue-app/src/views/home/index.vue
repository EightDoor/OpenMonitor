<template>
  <HomeLayout>
    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
      <el-tab-pane label="基础" name="sysinfo">
        <SysInfoMonitor/>
      </el-tab-pane>
      <el-tab-pane label="设置" name="setting">
        <Settings/>
      </el-tab-pane>
    </el-tabs>
  </HomeLayout>
</template>
<script lang="ts" setup>

import HomeLayout from "@/views/home/components/HomeLayout.vue";
import {ref} from "vue";
import Settings from "@/views/home/components/Settings/Settings.vue";
import {TabsPaneContext} from "element-plus";
import SysInfoMonitor from "@/views/home/components/SysInfo/SysInfoMonitor.vue";

const activeName = ref("sysinfo")

// const activeName = ref("setting")

function handleClick(tab: TabsPaneContext, event: Event) {
  console.log(tab, event)
}

</script>
<style lang="scss" scoped></style>
