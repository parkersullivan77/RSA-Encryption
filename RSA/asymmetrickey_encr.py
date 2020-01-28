import math
import sys
def main():
    text=sys.argv[1]
    keys = sys.argv[2]
    key = grabKeys(keys)
    key1 = key[0][:10]
    key2 = key[1][:10]
    values =wrapPublicKey(key1)
    values1= wrapPublicKey(key2)
    writeKeys("wrappedKeys.txt",values,values1)

    
    
    
def wrapPublicKey(key):
    values = []
    for i in key:
        values.append(pow(ord(i),14567)%659369)
    return values

def writeKeys(fileName,values, values1):
    file = open(fileName,"w")
    for i in values:
        file.write("%s" % i + " ")
    file.write('\n')
    for i in values1:
        file.write("%s" % i + " ")
    
        
def grabKeys(fileName):
    file = open(fileName, "r")
    keys = file.readline()
    splitBoy = keys.split(" ")
    return splitBoy
    
        
    


main()
