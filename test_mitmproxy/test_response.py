import json
from pprint import pprint

def response(flow):
    # 雪球的行情返回的url就是quote.json，可以从这方面入手
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:

        #只要有pprint，还有flow.response，mitmdump肯定打印出所有响应的内容
        # pprint(flow.response)
        #只要有pprint，还有flow.response.content,mitmdump肯定打印出所有响应的内容
        # pprint(flow.response.content)

        #把content的json内容转化成python变量
        data=json.loads(flow.response.content)
        #提取出第一个股票的名字，并在股票后面加一个字符串通通
        data["data"]["items"][0]["quote"]["name"]=data["data"]["items"][0]["quote"]["name"]+"tongtong"
        #response.text 返回的是一个 unicode 型的文本数据
        #response.content 返回的是 bytes 型的二进制数据

        #让最终的输出的text修改成我们定义的data数据
        flow.response.text=json.dumps(data)



