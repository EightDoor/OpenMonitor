const Config = {
    baseUrl: "/api",
    proUrl: "http://192.168.192.3:8500",
    serverIps: [
        {
            label: "(thinkpad-笔记本) 192.168.192.3",
            value: "http://192.168.192.3:8500"
        },
        {
            label: "(e5-台式) 192.168.192.4",
            value: "http://192.168.192.4:8500"
        }
    ]
}

const pro = import.meta.env.PROD
if (pro) {
    Config.baseUrl = Config.proUrl
}

export default Config
