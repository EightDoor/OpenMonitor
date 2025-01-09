<template>
  <div class="layout">
    <slot/>
  </div>
</template>
<script setup>
  import { ref } from 'vue';
</script>
<style scoped lang="scss">
.layout {
  padding: 50px;
}
</style>
