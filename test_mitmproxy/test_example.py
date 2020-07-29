from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.

    #当我们的返回的url中包含quote.json,就会执行下面的map local
    #雪球的行情返回的url就是quote.json，可以从这方面入手
    if "quote.json" in flow.request.pretty_url :
        #我们通过charles的mirror拿到quote.json，改造成1.json放到项目里面去吧
        #真烦每次我都要UTF-8，歧视windows
        with open("1.json",encoding="UTF-8") as f:
            #这里一个字典
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(), #直接读取我们的json文件，套入到响应，等于响应就是这个1.json
                #由于传的是json，所以content-type改成json的
                {"Content-Type": "application/json"}  # (optional) headers
            )