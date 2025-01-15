<template>
  <el-row :gutter="20" v-if="data">
    <el-col :span="12" v-for="(item, index) in data" :key="index"
    >
      <div class="temperatures">
        <div class="tw-mb-2">
          {{ item.name }}
        </div>
        <div v-if="item.temperatures">
          <div>{{ item.temperatures.current }}</div>
        </div>
        <div v-if="item.fans">
          <div>{{ item.fans }}</div>
        </div>
      </div>
    </el-col>
  </el-row>
</template>
<script lang="ts" setup>
import {ISysInfoTemperatures} from "@/interface/ISysInfoTemperatures.ts";

const props = defineProps<{
  data: ISysInfoTemperatures[]
}>()
</script>
<style scoped lang="scss">
.temperatures {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
</style>
