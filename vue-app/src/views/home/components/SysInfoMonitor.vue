
<template>
  <v-echarts class="chart" :option="option" />
</template>

<script setup lang="ts">
import { ref,computed } from 'vue';

//模拟数据value的字段对应Y轴，name字段对应X轴
const data=ref([
  {value:11,name:'A'},
  {value:31,name:'B'},
  {value:75,name:'C'},
  {value:25,name:'D'},
  {value:16,name:'E'},
])

const option=computed(()=>{
  return{
    xAxis:{
      type:'category',
      data:data.value.map(v=>v.name)
    },
    yAxis:{
      type:'value',
    },
    series:[
      {
        type:'line',
        data:data.value.map(v=>v.value)
      }
    ]
  }
})

// 定时更新数据 每一秒更新一次数据
setInterval(()=>{
  data.value=data.value.map(item=>({
    ...item,
    value:Math.random()*100,  //Math()随机函数，这里是随机生成100以内的数字
  }))
},1000)  //单位ms，1000ms即是1秒
</script>
<style>
.chart{
  height: 400px;
}
</style>
