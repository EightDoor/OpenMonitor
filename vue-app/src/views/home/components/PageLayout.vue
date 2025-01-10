<template>
  <div class="page-layout">
    <div class="title">
      <slot name="title"/>
    </div>
    <div class="content">
      <slot/>
    </div>
  </div>
</template>
<script setup>
  import { ref } from 'vue';
</script>
<style scoped lang="scss">
.page-layout {
  .title {
    font-size: 25px;
  }
  .content {
    margin-top: 15px;
  }
}
</style>
