import sys

def main():
    cipherfile = sys.argv[1]
    keys = sys.argv[2]
    key = grabKeys(keys)
    key1 = key[0][:10]
    key2 = key[1][:10]
    key1Numbers = assignUpperValues(key1)
    key2Numbers = assignUpperValues(key2)
    ciphertext = read(cipherfile)
    rows=getNumbRows(ciphertext)
    allGroups = decode(ciphertext,rows,key2)
    booy = makeText(allGroups)
    finish = decode(booy,rows,key1)
    finish = makeText(finish)
    writeFile("BobsPlainText.txt",finish)


   

def split(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]



def decode(ciphertext,rows,key1):
    keyOrder = [''.join(sorted(key1)).find(x) for x in key1]
    str1 = ''.join(map(str,keyOrder))
    order ={int(val): num for num ,val in enumerate(str1)}
    
    splits = split(ciphertext,rows)
    
    grid = []
    
    for i in range(rows):
        row = ['x'] *10
        grid.append(row)
    
    
    for index in sorted(order.keys()):
        for j in range(rows):
            grid[j][order[index]] = splits[index][j]
    
    return grid
            
        
    
    

def read(fileName):
    file  = open(fileName, "r")
    message = file.read()
    return message

def grabKeys(fileName):
    file = open(fileName, "r")
    keys = file.readline()
    splitBoy = keys.split(" ")
    return splitBoy
    
def assignUpperValues(key):
    sortedKey = sorted(key)
    numbers = [0] *10
    for i in range (0,10):
        index = key.index(sortedKey[i])
        numbers[index] = i
        
    return numbers

def writeGrid(fileName, plaintext):
    file = open(fileName,"w")
    for i in range(len(plaintext)):
        for j in range(len(plaintext)):
            file.write(plaintext[i][j]);
            
def getNumbRows(cleanText):
    rows = len(cleanText)//10
    if(len(cleanText)% 10 != 0):
        rows +=1 
    return rows



def makeText(groups):
    text = ""
    for i in groups:
        text += ''.join(i)
    
    return text

def writeFile(fileName,message):
    files = open(fileName,"w")
    files.write(message)
    
main()


   
    


    
