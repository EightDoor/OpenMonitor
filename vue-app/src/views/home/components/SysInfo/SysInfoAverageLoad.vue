<template>
  <PageLayout>
    <template #title>
      负载状态
    </template>
    <div>
      <el-progress type="dashboard" :percentage="formatCount(data?.avg1)" :color="SysInfoUtil.colors"/>
    </div>
    <template #footer>
      <div :style="{'color': color}">
        {{ name }}
      </div>
    </template>
  </PageLayout>
</template>
<script setup lang="ts">
import PageLayout from "@/views/home/components/PageLayout.vue";
import {IAverageLoad} from "@/interface/ISysInfo.ts";
import SysInfoUtil from "@/views/home/components/SysInfo/SysInfoUtil.ts";
import {ref, watch} from "vue";

const props = defineProps<{
  data: IAverageLoad,
}>()

function formatCount(val: number) {
  return Math.ceil(val)
}

const name = ref()
const color = ref()
watch(() => props.data, (value) => {
  if (value) {
    const avg = value.avg1
    if (avg < 50) {
      name.value = '运行流畅'
      color.value = 'green'
    } else if (avg > 50 && avg < 90) {
      name.value = '运行正常'
      color.value = "blue"
    } else if (avg > 90) {
      name.value = "运行缓慢"
      color.value = "red"
    }
  }
}, {
  immediate: true,
  deep: true
})
</script>
<style scoped lang="scss"></style>
