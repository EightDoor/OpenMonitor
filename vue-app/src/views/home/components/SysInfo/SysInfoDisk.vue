<template>
  <div class="tw-flex tw-flex-row tw-justify-center tw-items-center tw-flex-wrap">
    <div v-for="(item, index) of list" class="tw-mr-20" :key="index">
      <PageLayout>
        <template #title>
          {{ item.path }}
        </template>
        <div>
          <el-progress type="dashboard" :percentage="item.usage" :color="SysInfoUtil.colors"/>
        </div>
        <template #footer v-if="item">
          {{ Utils.mbToGB(item.used) }} / {{ Utils.mbToGB(item.total) }} GB
        </template>
      </PageLayout>
    </div>
  </div>
</template>
<script lang="ts" setup>
import SysInfoUtil from "@/views/home/components/SysInfo/SysInfoUtil.ts";
import PageLayout from "@/views/home/components/PageLayout.vue";
import Utils from "@/utils";
import {ISysInfoDiskInfo} from "@/interface/ISysInfoDisk.ts";

const props = defineProps<{
  list: ISysInfoDiskInfo[]
}>()
</script>
<style scoped lang="scss">

</style>
