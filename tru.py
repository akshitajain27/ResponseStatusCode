import requests
def code():
    for i in range(1,5):
        url="https://neuronme.com/"

        res = requests.get( url)

        #code= str(res.status_code)
        code=100
        #print code
        #ch=code[0]
        ch=1
    #ch=int(cha)
    #print ch
    #ch=2
        if ch=="1":
            return {
                00:"100",
                01:"101",
            }[code]
            """if code[2]=="0":
                print "part of a request has been received without any problems"
            else:
                return " the server is changing to the protocol it defines in the Upgrade header it returns to the client."""""
        elif ch=="2":
            if code[2]<"4":
                if code[2]=="0":
                    return "the request was received and understood and is being processed."
        else:
            print "jk"
for i in range(1,5):
    print code()