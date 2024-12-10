import {createRouter, createWebHashHistory, RouteRecordRaw} from "vue-router";
import Home from "@/views/home/index.vue"
import Test from '@/views/test/index.vue';

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        component: Home
    },
    {
        path: "/test",
        component: Test
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
