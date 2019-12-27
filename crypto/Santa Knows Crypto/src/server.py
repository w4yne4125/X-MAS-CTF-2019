from Crypto.Util.number import *
import SocketServer
from ElGamal import ElGamal
from secret import flag
from text import *
import os
from hashlib import sha256
prime = 685221181007655969055643176795598500987539499099103356485206001142535588544010199273848305625469714980556215814571531400059127410834556408213573648640620782264547499664798168588595354413552517947288874272302443155003080155578117949303088899418619338227631822471359675459950492254857920916052407700056096582307
PORT = 2000

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def PoW(self):
        s = os.urandom(10)
        h = sha256(s).hexdigest()
        self.request.sendall("Provide a hex string X such that sha256(X)[-6:] = {}\n".format(h[-6:]))
        inp = self.request.recv(2048).strip().lower()
        is_hex = 1
        for c in inp:
            if not c in '0123456789abcdef':
                is_hex = 0

        if is_hex and sha256(inp.decode('hex')).hexdigest()[-6:] == h[-6:]:
            self.request.sendall('Good, you can continue!\n')
            return True
        else:
            self.request.sendall('Oops, your string didn\'t respect the criterion.\n')
            return False

    def handle(self):
        self.request.settimeout(120)
        if not self.PoW():
            return
        self.request.sendall(intro)
        enc = ElGamal(1024, prime)
        print enc.x
        self.request.sendall(details.format(enc.q, enc.g))
        correct = 0
        while correct < 10:
            m = int(os.urandom(32).encode('hex'), 16) % enc.q
            y, c1, c2 = enc.encrypt(m)
            self.request.sendall(challenge.format(c1, c2))
            self.request.sendall(get_input)
            try:
                x = self.request.recv(1024)
                x = int(x)
                if x == m:
                    self.request.sendall(correct_answer)
                    correct += 1
                else:
                    self.request.sendall(wrong_answer.format(m, y))
                    correct = 0                    
            except:
                self.request.sendall(bad_input)
                break
        if correct == 10:
            self.request.sendall(flag+'\n')
                
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == '__main__':
    server = ThreadedTCPServer(('0.0.0.0', PORT), ThreadedTCPRequestHandler)
    server.allow_reuse_address = True
    server.serve_forever()
