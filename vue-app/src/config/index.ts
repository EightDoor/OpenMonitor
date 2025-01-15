const Config = {
    baseUrl: "/api",
    proUrl: "http://192.168.192.3:8500"
}

const pro = import.meta.env.PROD
if (pro) {
    Config.baseUrl = Config.proUrl
}

export default Config
