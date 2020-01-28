import sys

def main():
    
    text=sys.argv[1]
    keys = sys.argv[2]
    key = grabKeys(keys)
    key1 = key[0][:10]
    key2 = key[1][:10]
    key1Numbers = assignUpperValues(key1)
    key2Numbers = assignUpperValues(key2)
    cleanText = readandClean(text)
    rows=getNumbRows(cleanText)
    messageGrid = buildMessagegrid(cleanText,rows)
    groups = encode(messageGrid,key1Numbers)
    newGrid = buildGroupGrid(groups)
    groups2 = encode(newGrid,key2Numbers)
    
    
    
    print("Encrypting")
    encodedGrid = buildGroupGrid(groups2)
    writeGrid("plain-text.cipher",encodedGrid)
    print("Done")
    


    
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


def readandClean(fileName):
    file  = open(fileName, "r")
    message = file.read()
    message =message.strip()
    message = message.replace(" ","")
    return message

def getNumbRows(cleanText):
    rows = len(cleanText)//10
    if(len(cleanText)% 10 != 0):
        rows +=1 
    return rows

def buildMessagegrid(cleanText,rows):
    messageGrid = []
    for i in range(rows):
        row = ['x'] *10
        messageGrid.append(row)
        for j in range(0,10):
            if(i*10) + j > len(cleanText)-1 :
                continue
            else:
                messageGrid[i][j] = cleanText[(i*10) + j]
        
    return messageGrid


def buildGroupGrid(groups):
    grid = []
    row = []
    for i in range(len(groups)):
        for j in range(len(groups[i])):
            row.append(groups[i][j])
        if (i % 2) != 0:
            grid.append(row)
            row = []
    return grid

def encode(messageGrid,keyNumbers):
    
    allGroups = []
    group = []
    
    for i in range(10):
        index = keyNumbers.index(i)
        count = 0
        if (count != len(messageGrid)):
            for j in range(len(messageGrid)):
                group.append(messageGrid[count][index])
                count +=1
                if(len(group) == 5):
                    allGroups.append(group)
                    group = []
    return allGroups

def writeGrid(fileName, ciphertext):
    file = open(fileName,"w")
    for i in range(len(ciphertext)):
        for j in range(len(ciphertext[i])):
            file.write(ciphertext[i][j]);

            
                
    
    
main()
