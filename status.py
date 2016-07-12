import requests,time
def code():

    url="https://neuronme.com/"

    res = requests.get( url)

    code= str(res.status_code)
    print code
#code=str(201)
    ch=code[0]
    #ch=int(cha)
    #print ch
    #ch=2
    if ch=="1":
        if code[2]=="0":
            return "part of a request has been received without any problems"
        else:
            return " the server is changing to the protocol it defines in the Upgrade header it returns to the client."
    elif ch=="2":
        if code[2]<"4":
            if code[2]=="0":
                return "the request was received and understood and is being processed."
            elif code[2]=="1":
                return "A 201 status code indicates that a request was successful and as a result, a resource has been created"
            elif code[2]=="2":
                return "server has received and understood the request, and that it has been accepted for processing, although it may not be processed immediately."
            elif code[2]=="3":
                return "the request was received and understood, and that information sent back about the response is from a third party, rather than the original server."
        elif code[2]>"3":
            if code[2]=="4":
                return "the request was received and understood, but that there is no need to send any data back."
            elif code[2]=="5":
                return "request from the server to the client to reset the document from which the original request was sent."
            elif code[2]=="6":
                return " response to a request for part of a document."
    elif ch=="3":
        if code[2]<"4":
            if code[2]=="0":
                return "300"
            elif code[2]=="1":
                return "301"
            elif code[2]=="2":
                return "302"
            elif code[2]=="3":
                return "303"
        elif code[2]>"3":
            if code[2]=="4":
                return "304"
            elif code[2]=="5":
                return "305"
            elif code[2]=="7":
                return "307"
    elif ch=="4":
        if code[1] != "1":

            if code[2]<"5":

                if code[2]=="0":
                    return "400"
                elif code[2]=="1":
                    return "401"
                elif code[2]=="2":
                    return "402"
                elif code[2]=="3":
                    return "403"
                elif code[2]=="4":
                    return "404"

            elif code[2]>"4":
                if code[2]=="5":
                    return "405"
                elif code[2]=="6":
                    return "406"
                elif code[2]=="7":
                    return "407"
                elif code[2]=="8":
                    return "408"
                elif code[2]=="9":
                    return "409"
        else:
            if code[2]<"4":

                if code[2]=="0":
                    return "410"
                elif code[2]=="1":
                    return "411"
                elif code[2]=="2":
                    return "412"
                elif code[2]=="3":
                    return "413"


            elif code[2]>"3":

                if code[2]=="4":
                    return "414"
                elif code[2]=="5":
                    return "415"
                elif code[2]=="6":
                    return "416"
                elif code[2]=="7":
                    return "417"

    elif ch == "5":

            if code[2]=="0":
                return "500"
            elif code[2]=="1":
                return "501"
            elif code[2]=="2":
                return "502"
            elif code[2]=="3":
                return "503"
            elif code[2]=="5":
                return "505"
    else:

        print "response not found"
    time.sleep(5)
for i  in range(1,5):
    print code()















