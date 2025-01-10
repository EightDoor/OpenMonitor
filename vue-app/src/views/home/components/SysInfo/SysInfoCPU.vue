<template>
  <PageLayout>
    <template #title>
      cpu使用率
    </template>
    <div>
      <el-progress type="dashboard" :percentage="cpuInfo?.usage" :color="colors" />
    </div>
  </PageLayout>
</template>
<script setup lang="ts">
import {ref} from 'vue';
import PageLayout from "@/views/home/components/PageLayout.vue";
import {ICpu} from "@/interface/ISysInfo.ts";

const props = defineProps<{
  cpuInfo: ICpu | undefined
}>()

const colors = [
  { color: '#5cb87a', percentage: 20 },
  { color: '#5cb87a', percentage: 40 },
  { color: '#6f7ad3', percentage: 60 },
  { color: '#e6a23c', percentage: 80 },
  { color: '#f56c6c', percentage: 100 },
]

</script>
<style scoped lang="scss"></style>
