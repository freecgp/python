import optparse
import socket
from socket import *
from threading import Thread, Semaphore


def main ():
    parser = optparse.OptionParser('usage %prog -H'+\
                               '<target host> -P <target port>')
    parser.add_option('-H',dest='tgtHost',type='string',\
                      help='specify target host')
    parser.add_option('-P', dest='tgtPort', type='string', \
                      help='specify target ports[s] separated by comma')
    (options,args)= parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts == None):
        print 'you must input host and ports'
        exit(0)
    portScan(tgtHost,tgtPorts)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print 'can not resolve'
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] scan result for:'+tgtName[0]
    except:
        print '\n[+] scan reslts for:'+tgtIP
    for tgtPort in tgtPorts:
        print 'scannning port'+tgtPort
        t =Thread(target=connScan,args=(tgtHost,int(tgtPort)))
        t.start()

screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print '[+]%d/tcp open'%tgtPort
        print '[+]'+str(results)
    except Exception ,e:
        screenLock.acquire()
        print '[-]%d/tcp closed'%tgtPort
    finally:
        screenLock.release()
        connSkt.close()

if __name__ == '__main__':
    main()
