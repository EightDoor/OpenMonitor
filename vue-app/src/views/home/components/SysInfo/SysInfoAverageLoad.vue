<template>
  <PageLayout>
    <template #title>
      负载状态
    </template>
    <div>
      <el-progress type="dashboard" :percentage="formatCount(data?.avg1)" :color="SysInfoUtil.colors"/>
    </div>
  </PageLayout>
</template>
<script setup lang="ts">
import PageLayout from "@/views/home/components/PageLayout.vue";
import {IAverageLoad} from "@/interface/ISysInfo.ts";
import SysInfoUtil from "@/views/home/components/SysInfo/SysInfoUtil.ts";

const props = defineProps<{
  data: IAverageLoad,
}>()

function formatCount(val: number) {
  return Math.ceil(val)
}
</script>
<style scoped lang="scss"></style>
