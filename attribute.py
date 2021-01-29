import pydicom
import json
import sys
from pydicom.data import get_testdata_file

excludeVRs = ['OB', 'UN', 'SQ', 'OD', 'OF']

def mapTagsToValues(fileName, excludeTags, stringLength):
    filePath = get_testdata_file(fileName)

    dataset = pydicom.dcmread(filePath)
    # print(dataset.__len__(), "\n")

    pairing = {}
    nonPairing = {}

    for element in dataset:
        isIncluded = True
        for tag in excludeTags:
            if str(element.tag) == tag:
                isIncluded = False
                break
        for VR in excludeVRs:
            if str(element.VR) == VR:
                isIncluded = False
                break

        if not isIncluded:
            nonPairing[str(element.tag)] = str(element.value)[0:stringLength]
        else:
            pairing[str(element.tag)] = str(element.value)[0:stringLength]

    sets = [pairing, nonPairing]

    # print(pairing.__len__(), "\n")
    # print(nonPairing.__len__(), "\n")

    return sets

def jsonify(fileName, excludeTags, stringLength):
    set = mapTagsToValues(fileName, excludeTags, stringLength)
    new_set = json.dumps(set, indent=2)
    print(new_set)


if __name__ == '__main__':
    fileName = sys.argv[1]
    excludeTags = ['(0008, 0008)', '(0008, 0005)', '(0008, 0012)']
    stringLength = 0

    try:
        sys.argv[2]
    except:
        stringLength = 50
    else:
        stringLength = int(sys.argv[2])

    try:
        sys.argv[3]
    except:
        excludeTags = ['(0008, 0008)', '(0008, 0005)', '(0008, 0012)']
    else:
        excludeTags = [str(sys.argv[3])]

    # print(get_testdata_file(fileName), "\n")
    jsonify(fileName, excludeTags, stringLength)
