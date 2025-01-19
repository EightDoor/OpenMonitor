<template>
  <el-divider content-position="left">服务器地址</el-divider>
  <el-form :model="form.hosts">
    <el-form-item
        v-for="(domain, index) in form.hosts"
        :key="index"
        :label="domain.label + (index + 1)"
        :prop="domain.value"
        :rules="{
          validator: validateHostPath,
          trigger: ['blur', 'change'],
      }"
    >
      <div class="tw-flex tw-flex-row tw-items-center">
        <el-input style="width: 300px" placeholder="服务器地址，前缀是http或者https" v-model="domain.value"/>
        <el-button type="danger" :disabled="index === 0" class="tw-ml-4" @click.prevent="removeDomain(domain)">
          删除
        </el-button>
      </div>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="addDomain">添加</el-button>
    </el-form-item>
  </el-form>
</template>
<script lang="ts" setup>
import {ref} from "vue";
import {IOptions} from "@/interface/IOptions.ts";
import {cloneDeep} from "lodash";

interface IHost {
  hosts: IOptions[];
}

const defaultHost: IOptions = {
  label: '地址',
  value: ''
}

const form = ref<IHost>({
  hosts: [cloneDeep(defaultHost)]
})

function removeDomain(item: IHost) {
  const index = form.value.hosts.indexOf(item)
  if (index !== -1) {
    form.value.hosts.splice(index, 1)
  }
}

function addDomain() {
  const obj = cloneDeep(defaultHost);
  form.value.hosts.push(obj);
}


const validateHostPath = (rule: any, value: any, callback: any) => {
  const urlRegex = /^(https?:\/\/)([^\s:@\/?#]+(:[^\s:@\/?#]*)?@)?((([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})|(\d{1,3}(\.\d{1,3}){3})|(\[[^\]]+\]))(:\d+)?(\/[^\s?#]*)?(\?[^\s#]*)?(#[^\s]*)?$/;
  if (value === '') {
    callback(new Error('请输入服务器地址'))
  } else if (!urlRegex.test(value)) {
    callback(new Error("请输入正确的URL地址"))
  } else {
    callback()
  }
}


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
