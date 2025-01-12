<template>
  <div>
    <ul class="header-ul">
      <li v-for="(item, index) of headerList" :key="index">
        <div class="dot-container">
          <div class="dot" :style="{background: item.buttonColor}" v-if="item.buttonColor"></div>
          <div class="dot-title">{{ item.label }}</div>
        </div>
        <div class="title">
          {{ item.value }} {{ item.company }}
        </div>
      </li>
    </ul>
    <v-chart ref="chartRef" class="chart" :option="option"/>
  </div>
</template>
<script lang="ts" setup>
import VChart from "vue-echarts";
import {ref, watch} from "vue";
import {IOptions} from "@/interface/IOptions.ts";
import {ISysInfoDiskIO} from "@/interface/ISysInfoDisk.ts";
import dayjs from "dayjs";
import Utils from '@/utils/index.ts';

const color1 = '#ff6384'
const color2 = "#36a2eb"
const color3 = 'green'

interface IHeaderList extends IOptions {
  buttonColor?: string;
  color?: "green";
  company?: string;
}

const props = defineProps<{
  data: ISysInfoDiskIO
}>()

const headerList = ref<IHeaderList[]>([
  {
    label: "读取",
    value: 0,
    buttonColor: color1,
  },
  {
    label: "写入",
    value: 0,
    buttonColor: color2,
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
    color: color3
  }
])

const chartRef = ref()

const option = ref<any>({
  backgroundColor: 'white', // 自定义图表背景颜色
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: []
  },
  yAxis: {
    type: 'value',
    name: "单位：MB/s",
    nameTextStyle: {
      fontSize: 13, // 字体大小
    },
    // axisLabel: {
    //   formatter: '{value} MB' // 在刻度标签后加单位
    // }
  },
  series: [
    {
      data: [],
      type: 'line',
      areaStyle: {
        color: 'rgba(255, 99, 132, 0.5)' // 自定义面积图颜色
      },
      lineStyle: {
        color: color1 // 折线颜色
      }
    },
    {
      data: [],
      type: 'line',
      areaStyle: {
        color: 'rgba(54, 162, 235, 0.5)' // 自定义面积图颜色
      },
      lineStyle: {
        color: color2 // 折线颜色
      }
    },
  ]
});


function setOptions(ioValue: ISysInfoDiskIO) {
  const currentTime = dayjs(Date.now()).format("HH:mm:ss")
  if (option.value.xAxis.data.length > 5) {
    option.value.xAxis.data.shift()
    option.value.series[0].data.shift()
    option.value.series[1].data.shift()
  }
  option.value.xAxis.data.push(currentTime)
  option.value.series[0].data.push(Utils.bytesToMB(ioValue.read_bytes))
  option.value.series[1].data.push(Utils.bytesToMB(ioValue.write_bytes))
  headerList.value[0].value = Utils.formatBytes(ioValue.read_bytes)
  headerList.value[1].value = Utils.formatBytes(ioValue.write_bytes)
  headerList.value[2].value = ioValue.read_count + ioValue.write_count
  headerList.value[3].value = Math.round(ioValue.read_latency + ioValue.write_latency)
}

watch(() => props.data, (value) => {
  if (value) {
    setOptions(value)
  }
}, {
  immediate: true,
  deep: true
})
</script>
<style scoped lang="scss">
.header-ul {
  display: flex;
  flex-direction: row;
  justify-content: space-around;

  & > li {

  }

  .dot-container {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;

    .dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      margin-right: 5px;
    }

    .dot-title {
      font-size: 15px;
    }
  }

  .title {
    text-align: center;
    margin-top: 10px;
    font-size: 14px;
  }
}

.chart {
  width: 100%;
  height: 300px;
}
</style>
