import json

jsonRequestPath = 'Telegramme/request1.json'
convertedDfqName = 'test.dfq'

valueToKCode = {
    'batch': 'K0006',
    'RTNest': 'K0007',
}

dfqDict = dict({
    'K0100': 1,
    'K0101': 2,
})

def processJsonValue(source, partNumber = '/1'):
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
    
    dfqDict[kcode + partNumber] = value


def writeDfqFromDict(sourceDict):
    for key, value in sourceDict.items():
        print(key, value)


with open(jsonRequestPath) as f:
    source = json.loads(f.read())

# with open(convertedDfqName, 'w') as dfq:

bodyIndex = -1

for index, item in enumerate(source):
    if item.get("Name") == "Body":
        bodyIndex = index
        break

if bodyIndex == -1:
    exit(-1)


for var in source[bodyIndex]['Variables']:
    processJsonValue(var)

# processJsonValue(json.loads('{"Name": "resHead.batch", "Type": "String", "Value": ""}'))

print('\n\n\nResult is\n')
print(dfqDict)
writeDfqFromDict(dfqDict)
# print(source[bodyIndex])