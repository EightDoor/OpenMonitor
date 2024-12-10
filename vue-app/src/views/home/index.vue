<template>
    首页
    <el-button type="primary" @click="goTest">跳转测试页面</el-button>
</template>
<script lang="ts" setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function goTest() {
    router.push('/test')
}
</script>
<style lang="scss" scoped></style>
