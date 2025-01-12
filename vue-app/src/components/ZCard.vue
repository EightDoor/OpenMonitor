<template>
  <el-card shadow="always">
    <template #header v-if="title">
      <div class="title">
        {{ title }}
      </div>
    </template>
    <template #default>
      <slot/>
    </template>
    <template #footer v-if="slotFooter">
      <slot name="footer"/>
    </template>
  </el-card>
</template>
<script lang="ts" setup>
import {useSlots} from 'vue';

const slotFooter = !!useSlots().footer
const props = withDefaults(defineProps<{
  title?: string
}>(), {
  title: ""
})


</script>
<style scoped lang="scss">
.title {
  font-size: 25px;
}
</style>
