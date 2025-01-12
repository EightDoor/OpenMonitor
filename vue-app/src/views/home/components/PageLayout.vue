<template>
  <div class="page-layout">
    <div class="title">
      <slot name="title"/>
    </div>
    <div class="content">
      <slot/>
    </div>
    <div class="bottom">
      <slot name="footer"/>
    </div>
  </div>
</template>
<script setup></script>
<style scoped lang="scss">
.page-layout {
  .title {
    text-align: center;
    font-size: 20px;
  }

  .content {
    margin-top: 15px;
  }

  .bottom {
    font-size: 15px;
    text-align: center;
  }
}
</style>
