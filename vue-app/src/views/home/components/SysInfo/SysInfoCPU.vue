<template>
  <PageLayout>
    <template #title>
      cpu使用率
    </template>
    <div>
      <el-progress type="dashboard" :percentage="cpuInfo?.usage" :color="SysInfoUtil.colors"/>
    </div>
    <template #footer>
      {{ cpuInfo?.count }} 核心
    </template>
  </PageLayout>
</template>
<script setup lang="ts">
import PageLayout from "@/views/home/components/PageLayout.vue";
import {ICpu} from "@/interface/ISysInfo.ts";
import SysInfoUtil from "@/views/home/components/SysInfo/SysInfoUtil.ts";

const props = defineProps<{
  cpuInfo: ICpu | undefined,
}>()

</script>
<style scoped lang="scss"></style>
