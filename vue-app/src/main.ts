import {createApp} from 'vue'
// 样式初始化
import "@/assets/styles/default.scss"
import '@/assets/styles/comm.scss'
import "normalize.css"

// 引入echarts
import Echarts from 'vue-echarts'
import * as echarts from 'echarts'

import App from './App.vue'
import router from './router'
import store from './store'

const app = createApp(App);

app.component("v-echarts", Echarts)
app.use(store)
app.use(router)
app.mount('#app')
