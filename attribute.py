import pydicom
import json
import sys
from pydicom.data import get_testdata_file

exclude_VRs = ["OB", "UN", "SQ", "OD", "OF"]


def map_tags_to_values(file_name, exclude_tags, string_length):
    file_path = get_testdata_file(file_name)

    data_set = pydicom.dcmread(file_path)

    pairing = {}
    non_pairing = {}

    for element in data_set:
        is_included = True
        for tag in exclude_tags:
            if str(element.tag) == tag:
                is_included = False
                break
        for VR in exclude_VRs:
            if str(element.VR) == VR:
                is_included = False
                break

        if is_included:
            pairing[str(element.tag)] = str(element.value)[0:string_length]

    return pairing


if __name__ == "__main__":
    file_name = sys.argv[1]
    exclude_tags = ["(0008, 0008)", "(0008, 0005)", "(0008, 0012)"]
    string_length = 0

    try:
        sys.argv[2]
    except:
        string_length = 50
    else:
        string_length = int(sys.argv[2])

    try:
        sys.argv[3]
    except:
        exclude_tags = ["(0008, 0008)", "(0008, 0005)", "(0008, 0012)"]
    else:
        exclude_tags = [str(sys.argv[3])]

    output = map_tags_to_values(file_name, exclude_tags, string_length)

    with open("out.json", "w") as file:
        json.dump(output, file, indent=2)
