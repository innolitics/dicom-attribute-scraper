import pydicom
import json
import sys
from pydicom.data import get_testdata_file

# # fileName = "CT_small.dcm"
excludeArray = ['OB', 'UN', 'SQ', 'OD', 'OF']


# dict_value = {'thing': [1, 2, 3, 5, 5], "alphabets": True, "last": None }
#
# new_obj = json.dumps(dict_value, indent=2, sort_keys=True)
#
# print(dict_value)
# print(new_obj)
#

def pairTagValue(fileName, excludeTags, stringLength):
    filePath = get_testdata_file(fileName)

    # print(filePath)
    dataset = pydicom.dcmread(filePath)
    print(dataset.__len__(), "\n")
    pairing = {}
    nonPairing = {}

    for m in dataset:
        pairBool = True
        for tag in excludeTags:
            if str(m.tag) == tag:
                pairBool = False
                break
        for VR in excludeArray:
            if str(m.VR) == VR:
                pairBool = False
                break

        if not pairBool:
            nonPairing[str(m.tag)] = str(m.value)[0:stringLength]
        else:
            pairing[str(m.tag)] = str(m.value)[0:stringLength]

    sets = [pairing, nonPairing]

    print(pairing.__len__(), "\n")
    print(nonPairing.__len__(), "\n")

    return sets


def printPairs(fileName):
    pairs = pairTagValue(fileName)

    print(pairs[0].__len__(), pairs[0])
    print(pairs[1].__len__(), pairs[1])


def jsonify(fileName, excludeTags, stringLength):
    set = pairTagValue(fileName, excludeTags, stringLength)
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


    print(fileName, "\n")
    jsonify(fileName, excludeTags, stringLength)
