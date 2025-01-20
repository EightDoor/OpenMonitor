<template>
  <el-divider content-position="left">服务器地址</el-divider>
  <el-form
      ref="formRef"
      style="max-width: 600px"
      :model="dynamicValidateForm"
      label-width="auto"
      class="demo-dynamic"
  >
    <el-form-item
        v-for="(domain, index) in dynamicValidateForm.domains"
        :key="domain.key"
        :label="'地址' + (index + 1)"
        :prop="'domains.' + index + '.value'"
        :rules="{
        required: true,
        message: '请输入',
        trigger: 'blur',
      }"
    >
      <el-input placeholder="请输入地址描述" v-model="domain.label"/>
      <el-input class="tw-mt-2" placeholder="请输入http或者https URL地址" v-model="domain.value"/>
      <div class="tw-mt-4">
        <el-button @click="addDomain">添加</el-button>
        <el-button v-if="index !== 0" type="danger" @click.prevent="removeDomain(domain)">
          删除
        </el-button>
      </div>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm(formRef)">提交</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import {onMounted, reactive, ref} from 'vue'
import {ElMessage, FormInstance} from 'element-plus'
import logger from "@/utils/logger.ts";
import {useHome} from "@/store/models/useHome.ts";
import BusinessUtil from "@/utils/BusinessUtil.ts";

const homeStore = useHome()
const formRef = ref<FormInstance>()
const dynamicValidateForm = reactive<{
  domains: DomainItem[]
}>({
  domains: [
    {
      key: 1,
      value: '',
      label: '',
    },
  ],
})

export interface DomainItem {
  key?: number
  value: string
  label: string
}

const removeDomain = (item: DomainItem) => {
  const index = dynamicValidateForm.domains.indexOf(item)
  if (index !== -1) {
    dynamicValidateForm.domains.splice(index, 1)
  }
}

const addDomain = () => {
  dynamicValidateForm.domains.push({
    key: Date.now(),
    value: '',
    label: '',
  })
}

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate((valid) => {
    if (valid) {
      const sendData = dynamicValidateForm.domains
      logger.debug('提交内容', sendData)
      homeStore.setServerIps(sendData)
      getIps()
      ElMessage.success("保存成功")
      console.log('submit!')
    } else {
      console.log('error submit!')
    }
  })
}

function getIps() {
  const ips = homeStore.getServerIps
  if (ips?.length > 0) {
    dynamicValidateForm.domains = ips;
  }
}

onMounted(() => {
  BusinessUtil.initStorage()
  getIps()
})
</script>
