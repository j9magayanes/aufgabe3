import json

jsonRequestPath = 'Telegramme/request1.json'
convertedDfqName = 'test.dfq'
outputFile = 'testfile.dfq'

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

def processJsonValue(source, destDict, partNumber = '/1'):
    if source.get('Type') == 'Array' and source.get('ArrayItems'):
        for item in source.get('ArrayItems'):
            processJsonValue(item)
        return
    
    name = source.get('Name').split('.')[-1]
    value = source.get('Value')

    if not name:
        print('! No name found:', source)
        return
    
    if value is None:
        print('! No Value found:', source)
        return
    
    kcode = valueToKCode.get(name)

    if not kcode:
        print('! No K-code found:', source)
        return
    
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

body = getBody(source)
if not body:
    exit(1)

for var in body.get('Variables'):
    processJsonValue(var)

# processJsonValue(json.loads('{"Name": "resHead.batch", "Type": "String", "Value": ""}'))


def writeNewFile(pathInput, filenameInput):
    # reads file
    with open(pathInput) as f:
        source = json.loads(f.read())

    # gets the k number   
    processJsonValue(source, dfqDict)

    

    for var in source[bodyIndex]['Variables']:
        processJsonValue(var)
    

    with open(filenameInput, 'w') as f:
        for key, value in sorted(sourceDict.items(), key=lambda x: 'L' + x[0] if 'K000' in x[0] else x[0]):
            f.write(str(key) +' ' + str(value) + '\n')
            print(key, value)




print('\n\n\nResult is\n')
writeDfqFromDict(dfqDict, outputFile)
# print(source[bodyIndex])