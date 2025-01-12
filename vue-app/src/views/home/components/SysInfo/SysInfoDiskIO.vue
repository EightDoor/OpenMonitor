<template>
  <ul class="header-ul">
    <li v-for="(item, index) of headerList">
      <div class="dot-container">
        <div class="dot" v-if="item.buttonColor"></div>
        <div class="dot-title">{{ item.label }}</div>
      </div>
      <div class="title"></div>
    </li>
  </ul>
</template>
<script lang="ts" setup>

import {ref} from "vue";
import {IOptions} from "@/interface/IOptions.ts";

interface IHeaderList extends IOptions {
  buttonColor?: "red" | "blue";
  color?: "green";
  company?: string;
}

const headerList = ref<IHeaderList[]>([
  {
    label: "读取",
    value: 0,
    buttonColor: "red",
    company: "B"
  },
  {
    label: "写入",
    value: 0,
    buttonColor: "blue",
    company: "KB"
  },
  {
    label: "每秒读写",
    value: 0,
    company: "次"
  },
  {
    label: "IO延迟",
    value: 0,
    company: "ms",
    color: "green"
  }
])
</script>
<style scoped lang="scss">
.header-ul {
  .dot-container {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;

    .dot {

    }

    .dot-container {

    }
  }

  .title {

  }
}
</style>
