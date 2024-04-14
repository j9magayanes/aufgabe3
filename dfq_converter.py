import json
from pathlib import Path

jsonRequestPath = 'Telegramme/request1.json'
convertedDfqName = 'test.dfq'
outputFile = 'testfile.dfq'
skipAll = False

valueToKCode = {
    'batch': 'K0006',
    'RTNest': 'K0007',
    'PartId': 'K1001',
    'machineId': 'K1081',
    'SpecPartNo': 'K2110',
    'locationId': 'K2410',
    'OrderNoCur': 'K4032',
    'eventId': 'K4222',
}

dfqDict = dict({
    'K0100': 1,
    'K0101': 2,
})


def processJson(source, destDict, partNumber = '/1'):
    global skipAll
    if source.get('Type') == 'Array' and source.get('ArrayItems'):
        for item in source.get('ArrayItems'):
            processJson(item, destDict)
        return
    
    name = source.get('Name').split('.')[-1]
    value = source.get('Value')

    if not name:
        # print('! No name found:', source)
        return
    
    if value is None:
        # print('! No Value found:', source)
        return
    
    kcode = valueToKCode.get(name)

    if not kcode:
        if skipAll:
            return
        
        userChoise = input('Which K-code would you like to give to the "{}" JSON name?\nIts value is "{}"\nOptions are:\n1. [s]kip to skip\n2. [S]kip for skip all\n3. Type the K<xxxx> code and enter\nYour choise: '.format(name, value))
        print('\n---------------------------------------------------\n')
        if userChoise == 's':
            return
        
        if userChoise == 'S':
            skipAll = True
            return
        
        kcode = userChoise
        # print('! No K-code found:', source)
    
    destDict[kcode + partNumber] = value


def writeDfqFromDict(sourceDict: dict, filename):

    with open(filename, 'w') as f:
        for key, value in sorted(sourceDict.items(), key=lambda x: 'L' + x[0] if 'K000' in x[0] else x[0]):
            f.write(str(key) +' ' + str(value) + '\n')
            print(key, value)


with open(jsonRequestPath) as f:
    source = json.loads(f.read())

# with open(convertedDfqName, 'w') as dfq:

def getBody(jsonString):
    for item in jsonString:
        if item.get("Name") == "Body":
            return item
    return None


def getInpulFilePath():
    filePath = Path()
    while not filePath.is_file():
        filePath = Path(input('Telegramme file: '))

    return filePath


def getOutputFilePath():
    return Path(input('Output file: '))


def extractJsonFromTelegramme(telegramme):
    telegramme = telegramme[telegramme.find('['):]
    telegramme = telegramme[:telegramme.find(';')]
    return telegramme


def main():
    # inputFilePath = getInpulFilePath()
    # outputFilePath = getOutputFilePath()
    inputFilePath = 'Telegramme/0600_1201_0140_1234_240409_0001_091718.txt'
    outputFilePath = 'e.dfq'


    # reads file
    with open(inputFilePath) as f:
        source = json.loads(extractJsonFromTelegramme(f.read()))


    body = getBody(source)
    if not body:
        print('! No body is found')
        return

    # json to k-code dict
    for var in body.get('Variables'):
        processJson(var, dfqDict)
    

    with open(outputFilePath, 'w') as f:
        for key, value in sorted(dfqDict.items(), key=lambda x: 'L' + x[0] if 'K000' in x[0] else x[0]):
            f.write(str(key) +' ' + str(value) + '\n')
            # print(key, value)




# print('\n\n\nResult is\n')
# writeDfqFromDict(dfqDict, outputFile)
# # print(source[bodyIndex])

main()