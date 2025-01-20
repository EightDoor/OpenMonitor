import axios from 'axios';
import Config from "@/config";
import {useHome} from "@/store/models/useHome.ts";
import store from '@/store/index.ts';
import logger from "@/utils/logger.ts";

const homeStore = useHome(store)

const request = axios.create({
    baseURL: Config.baseUrl,
})

request.interceptors.request.use(function (request) {
    let selectIp = homeStore.getSelectIP;
    if (!selectIp && homeStore.getServerIps?.length > 0) {
        const configIP = homeStore.getServerIps[0].value
        homeStore.setSelectIP(configIP)
        selectIp = configIP
    }
    logger.debug('request请求ip', selectIp)
    request.baseURL = selectIp;
    return request
}, function (error) {
    return Promise.reject(error)
})

// 添加响应拦截器
request.interceptors.response.use(function (response) {
    // 2xx 范围内的状态码都会触发该函数。
    // 对响应数据做点什么
    return response.data;
}, function (error) {
    // 超出 2xx 范围的状态码都会触发该函数。
    // 对响应错误做点什么
    return Promise.reject(error);
});

export default request
