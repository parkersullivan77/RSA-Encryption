import sys
import math
def main():
        
    privateKeys = sys.argv[1]
    wrappedKeys = sys.argv[2]
    key1,key2 = readWrappedkeys(wrappedKeys)
    private,n=grabPrivate(privateKeys)
    ukey1 = decryptFile(private,key1,n)
    ukey2 = decryptFile(private,key2,n)
    writeFile("keys.txt",ukey1,ukey2)

    





def readWrappedkeys(fileName):
    files = open(fileName, "r")
    key1 = files.readline()
    #key3 =files.readLine()
    key2 = files.readline()
    
    return key1,key2
    
    
def grabPrivate(fileName):
    files = open(fileName,"r")
    key = files.readline();
    key = key.split(", ")
    return key[0],key[1]

def decryptFile(private, wrappedKey, n):
    num = wrappedKey.split(" ")
    key = ""
    num = num[:-1]
    for i in num:
        char =pow(int(i),int(private)) % int(n)
        key += chr(char)
    return key


def writeFile(filename, key1,key2):
    files = open(filename, "w")
    files.write(key1 + " "+ key2)
    
    
main()
