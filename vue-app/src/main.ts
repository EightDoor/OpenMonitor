import {createApp} from 'vue'
// 样式初始化
import "@/assets/styles/default.scss"
import '@/assets/styles/comm.scss'
import "normalize.css"

// echarts
import "echarts";

import App from './App.vue'
import router from './router'
import store from './store'

// element-plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App);

app.use(store)
app.use(router)
app.use(ElementPlus)
app.mount('#app')
