const Config = {
    baseUrl: "",
    proUrl: "/api",
}

const pro = import.meta.env.PROD
if (pro) {
    Config.baseUrl = Config.proUrl
}

export default Config
