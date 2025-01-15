<template>
  <el-divider content-position="left">告警</el-divider>
  <el-form :model="form" :rules="rules">
    <el-form-item label="发送人邮箱" prop="sendPeople">
      <el-input v-model="form.sendPeople"/>
    </el-form-item>
    <el-form-item label="SMTP密码" prop="password">
      <el-input type="password" v-model="form.password"/>
    </el-form-item>
    <el-form-item label="SMTP服务器" prop="server">
      <el-input v-model="form.server"/>
    </el-form-item>
    <el-form-item label="端口" prop="port">
      <el-input v-model="form.port"/>
    </el-form-item>
    <el-form-item label="邮箱" prop="email">
      <el-input type="textarea" rows="5" v-model="form.email" placeholder="接收者邮箱，每行一个"/>
    </el-form-item>
    <el-form-item label="磁盘SMART异常" prop="">
      <el-radio-group v-model="form.diskAlarm">
        <el-radio value="1" size="large">打开</el-radio>
        <el-radio value="2" size="large">关闭</el-radio>
      </el-radio-group>
    </el-form-item>
  </el-form>
  <ul class="ul">
    <li>推荐使用465端口，协议为SSL/TLS</li>
    <li>25端口为SMTP协议，587端口为STARTTLS协议</li>
  </ul>
</template>
<script lang="ts" setup>
import {reactive, ref} from "vue";
import {FormRules} from "element-plus";

interface AlarmConfig {
  diskAlarm: string;
  sendPeople: string;
  password: string;
  server: string;
  port: number;
  email: string;
}

const form = ref<AlarmConfig>({
  diskAlarm: '1',
  sendPeople: "",
  password: "",
  server: "",
  port: 465,
  email: "",
})

const rules = reactive<FormRules<AlarmConfig>>({
  sendPeople: [
    {
      required: true,
      message: "请输入发送人邮箱",
      trigger: ['blur', 'change']
    },
  ],
  password: [
    {
      required: true,
      message: "请输入SMTP密码",
      trigger: ['blur', 'change']
    },
  ],
  server: [
    {
      required: true,
      message: "请输入SMTP服务器地址",
      trigger: ['blur', 'change']
    },
  ],
  port: [
    {
      required: true,
      message: "请输入端口",
      trigger: ['blur', 'change']
    },
  ],
  email: [
    {
      required: true,
      message: "请输入邮箱",
      trigger: ['blur', 'change']
    },
  ]
})
</script>
<style scoped lang="scss">
.ul {
  & > li {
    font-size: 13px;
    color: #6e6e6e;
    margin-top: 5px;
  }
}
</style>
