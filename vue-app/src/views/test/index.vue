<template>
  <div style="padding: 100px">
    element-plus 测试按钮
    <el-button type="primary">Primary</el-button>
    <el-divider/>
    pinia store
    <el-button @click="changeCount">count {{ testCount.getCount }}</el-button>
    <el-divider/>
    tailwindcss
    <div class="tw-text-3xl tw-font-bold tw-underline">
      Hello world!
    </div>
  </div>
</template>
<script lang="ts" setup>
import {useTestCount} from '@/store/models/useTest.ts';

const testCount = useTestCount();

function changeCount() {
  testCount.setCount(testCount.getCount + 1);
}
</script>
<style lang="scss" scoped></style>
