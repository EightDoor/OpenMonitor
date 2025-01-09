import {createApp} from 'vue'
// 样式初始化
import "@/assets/styles/default.scss"
import '@/assets/styles/comm.scss'
import "normalize.css"

import App from './App.vue'
import router from './router'
import store from './store'

const app = createApp(App);

app.use(store)
app.use(router)
app.mount('#app')
