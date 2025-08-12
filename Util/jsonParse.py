import json
def parseJsonFile(filePath):
    try:
        with open(filePath, 'r') as jsonFile:
            data = json.load(jsonFile)
            return data
    except json.JSONDecodeError as e:
        return {}