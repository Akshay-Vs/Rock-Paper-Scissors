import base64
import hashlib
import os
from Crypto import Random
from Crypto.Cipher import AES

key="key"

class AESCipher(object):
    #Encrypt using AES Standard

    def __init__(self, key): 
        #fetch key for encryption
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        #fetch raw string data
        #Return 16-bit ASCII encoded data
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b16encode(iv + cipher.encrypt(raw.encode())) 

    def decrypt(self, enc):
        #fetch encoded data
        #Return 16-bit ASCII decrypted data
        enc = base64.b16decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s): #padding enc
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s): #unpading enc
        return s[:-ord(s[len(s)-1:])]


class io:

    def __init__(self,path)->None:

        self.path = f'{path}.RPS'
        #creating initial files
        try:open(f"{self.path}/.nomedia",'r')

        except Exception:
            # mkdirs first
            os.mkdir(f"{self.path}")
            os.mkdir(f"{self.path}\\Version")
            os.mkdir(f"{self.path}\\data")
            os.mkdir(f"{self.path}\\data/score")

            # Writing files
            open(f'{self.path}/.nomedia','w+')
            open(f'{self.path}/Version/.version','w+')
            open(f'{self.path}/data/score/highscore.psl','w+')
            open(f'{self.path}/data/score/scoreboard.psl','w+')
            open(f"{self.path}/data/lastplay.psl",'w+')

    def read_file(self,type)->str:
        #reading and decoding
        #fetch file type (str) ie: version, highscore
        #read raw data
        #return str type decrypted data

        if type=="version":
            self.version=open(f'{self.path}/Version/.version','rb+')
            version=AESCipher(key).decrypt(self.version.read())
            return version

        elif type=="highscore":
            self.highscore=open(f'{self.path}/data/score/highscore.psl','rb+')
            highscore=self.highscore.read()
            highscore=AESCipher(key).decrypt(highscore)
            return highscore

        elif type=="scoreboard":
            self.scoreboard= open(f'{self.path}/data/score/scoreboard.psl','rb+')
            scoreboard= self.scoreboard.read()
            scoreboard= AESCipher(key).decrypt(scoreboard)
            return scoreboard

        elif type=="lastplay":
            self.lastplay=open(f"{self.path}/data/lastplay.psl",'rb+')
            lastplay=self.lastplay.read()
            lastplay=AESCipher(key).decrypt(lastplay)
            return lastplay

    def write_file(self,type,content)->None: 
        #fetch UTF-8 str
        #write encoded ASCII-16 byte

        if type=="version":
            content=AESCipher(key).encrypt(content)
            self.version=open(f'{self.path}/Version/.version','rb+')
            self.version.write(content)

        elif type=="highscore":
            self.highscore=open(f'{self.path}/data/score/highscore.psl','rb+')
            content=AESCipher(key).encrypt(content)
            self.highscore.write(content)

        elif type=="scoreboard":
            self.scoreboard= open(f'{self.path}/data/score/scoreboard.psl','rb+')
            content=AESCipher(key).encrypt(content)
            self.scoreboard.write(content)

        elif type=="lastplay":
            content=AESCipher(key).encrypt(content)
            self.lastplay=open(f"{self.path}/data/lastplay.psl",'rb+')
            self.lastplay.write(content)

if __name__=="__main__": #testing

    file=io("path\\")
    file.write_file("version","1.0")
    print(file.read_file("version"))
    
    file.write_file("highscore","100")
    print(file.read_file("highscore"))

    file.write_file("lastplay","12:37")
    print(file.read_file("lastplay"))

    file.write_file("scoreboard",'2,34,45,67,87')
    print(file.read_file("scoreboard"))
    
