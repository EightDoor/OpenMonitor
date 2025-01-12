<template>
  <PageLayout>
    <template #title>
      内存使用率
    </template>
    <div>
      <el-progress type="dashboard" :percentage="data?.memory.usage" :color="SysInfoUtil.colors"/>
    </div>
    <template #footer v-if="data">
      {{ Utils.bytesToMB(data.memory.other.used) }} / {{ Utils.bytesToMB(data.memory.total) }}(MB)
    </template>
  </PageLayout>
</template>
<script setup lang="ts">
import {ISysInfoMemory} from '@/interface/ISysInfo.ts';
import PageLayout from "@/views/home/components/PageLayout.vue";
import SysInfoUtil from "@/views/home/components/SysInfo/SysInfoUtil.ts";
import Utils from '@/utils/index.ts';

const props = defineProps<{
  data: ISysInfoMemory | undefined
}>()
</script>
<style scoped lang="scss"></style>
