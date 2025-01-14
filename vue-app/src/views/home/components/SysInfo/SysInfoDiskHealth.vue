<template>
  <el-row :gutter="20">
    <el-col :md="12" :xs="24" v-for="(item, index) of data" :key="index"
            class="tw-flex tw-flex-row tw-justify-between tw-items-center">
      <div>{{ item.disk }}</div>
      <el-tag :type="formatType(item.smart_status)">{{ formatName(item.smart_status) }}</el-tag>
    </el-col>
  </el-row>
</template>
<script lang="ts" setup>

import {IDiskHealth} from "@/interface/ISysInfo.ts";

const props = defineProps<{
  data: IDiskHealth[]
}>()

function formatName(name: string) {
  switch (name) {
    case "PASSED":
      return "通过";
    case "FAILED":
      return "不通过"
    default:
      return ""
  }
}

function formatType(name: string) {
  switch (name) {
    case "PASSED":
      return "primary";
    case "FAILED":
      return "danger"
    default:
      return ""
  }
}
</script>
<style scoped lang="scss"></style>
