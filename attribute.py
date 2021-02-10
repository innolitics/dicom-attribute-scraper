import pydicom
import json
import argparse
from pydicom.data import get_testdata_file


EXCLUDED_VRS = {"OB", "UN", "SQ", "OD", "OF"}


def map_tags_to_values(file_name, excluded_tags, string_length):
    file_path = get_testdata_file(file_name)

    data_set = pydicom.dcmread(file_path)

    pairing = {}

    for element in data_set:
        group_tag = int(str(element.tag)[1:5], 16)
        is_excluded = (
            ((group_tag % 2) and (group_tag > 8))
            or str(element.tag) in excluded_tags
            or element.VR in EXCLUDED_VRS
        )

        if not is_excluded:
            pairing[str(element.tag)] = str(element.value)[0:string_length]

    return pairing


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("dcm_file", help="input DICOM file name")
    parser.add_argument("-o", "--output", help="name of output file")
    parser.add_argument("-l", "--length", help="length of output strings", type=int)
    parser.add_argument("-e", "--excluded", help="excluded tag numbers")
    args = parser.parse_args()

    file_name = args.dcm_file
    if args.output:
        output_name = args.output
    else:
        output_name = "out.json"
    if args.length:
        string_length = args.length
    else:
        string_length = 50
    if args.excluded:
        excluded_tags = {str(args.excluded)}
    else:
        excluded_tags = {}

    output = map_tags_to_values(file_name, excluded_tags, string_length)

    with open(output_name, "w") as file:
        json.dump(output, file, indent=2)
