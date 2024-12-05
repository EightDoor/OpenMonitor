import httpx

client = httpx.AsyncClient()

async def address_information(ip: str | None = None, *, type: int = 1):
    """
    查看ip地址信息
    """
    if type == 1:
        #  ip.cn
        url = "https://www.ip.cn/api/index?type=0"
        if ip is not None:
            url += f'&ip={ip}'
        req = client.build_request('GET', url)
        res_ipcn = await client.send(req)
        return res_ipcn.json()
    elif type == 2:
        # ipchaxun
        req = client.build_request('GET', "https://2024.ipchaxun.com/", headers= {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:132.0) Gecko/20100101 Firefox/132.0'
        })
        res_ipchaxun = await client.send(req)
        return res_ipchaxun.json()
    else:
        # csdn
        url = "https://searchplugin.csdn.net/api/v1/ip/get"
        if ip is not None:
            url += f"?ip={ip}"
        req = client.build_request('GET', url)
        res_csdn = await client.send(req)
        return res_csdn.json()