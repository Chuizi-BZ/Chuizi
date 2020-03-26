
import socket
import queue
import threading
import sys

q=queue.Queue()

class saomiao(threading.Thread):
    def __init__(self,host):
        super().__init__()
        self.host:str = host
    def run(self) -> None:
        while True:
            port=q.get()
            self.scenner(port)
            q.task_done()
    def scenner(self,port):
        conn = socket.socket()
        try:
            conn.connect((self.host,port))
            print(f"锤子跟你说这个/{port}/端口是开着的！！！]")
        except:
            pass
if __name__ == '__main__':
    banner = '''\
        
        //////////               ////////////////
     ////                                    //
    ////                                   //
    ///                                 // 
    ///                              //
       /////////                 ////////////////
                                                        ----"作者彩笔锤子"
                                                        ！！请勿扫描gov,and,edu域名
                                                        请勿用在违法犯罪道路
       '''
    print(banner)
    host = sys.argv[1]
    ip =socket.gethostbyname(host)
    startPort = sys.argv[2]
    endPort = sys.argv[3]
    thredNum = sys.argv[4]

    for i in range(int(thredNum)):
        t=saomiao(ip)
        t.setDaemon(True)
        t.start()
    for i in range(int(startPort),int(endPort)):
        q.put(i)
    q.join()