def function1(cod):
    return {
        100:"100: Continue",
        101:"101:Switching Protocols",
    }[cod]


def function2(cod):

    return {
        200: "200:OK",
        201:"201: created",
        202:"202: Accepted",
        203:"203:Non-Authoritative Information",
        204:"204:No content",
        205:"205:Reset content",
        206:"206:Partial content",
    }[cod]


def function3(cod):
    return {
        301:"301: Moved Permanently",
        300:"300:Multiple choices",
        302:"302:Found",
        303:"303: See other",
        304:"304:Not modified",
        305:"305:Use proxy",
        307:"307:Temporary redirect"
    }[cod]


def function4(cod):
    return {
        400:"400:Bad request",
        401:"401: Unauthorized",
        402:"402:Payment required",
        403:"403:forbidden",
        404:"404:Not found",
        405:"405:Methods not allowed",
        406:"406:Not acceptable",
        407:"407:Proxy authentication required",
        408:"408: Request timeout",
        409:"409: conflict",
        410:"410:Gone",
        411:"411:Length required",
        412:"412:Precondition failed ",
        413:"413:Request entity too large",
        414:"414: Request-URI too long",
        415:"415:Unsupported media type",
        416:"416:Request range not satisfiable",
        417:"417:Expectation failed",

    }[cod]


def function5(cod):
    return {
        500:"500:Internal server error",
        501:"501:Not implemented",
        502:"502: Bad gateway",
        503:"503:Service unavailable",
        504:"504:Gateway timeout",
        505:"505:HTTP Version Not Supported",

    }[cod]


import requests,time

def status_code():
    url="https://neuronme.com/"
    res = requests.get( url)

    code= str(res.status_code)
    #print code
    ch=code[0]

    if ch=="1":
        print function1(int(code))
    elif ch=="2":

         return function2(int(code))
    elif ch=="3":
        print  function3(int(code))
    elif ch=="4":
        print function4(int(code))
    elif ch=="5":
        print function5(code)
    else:
        print "no valid response code"



status_code()

