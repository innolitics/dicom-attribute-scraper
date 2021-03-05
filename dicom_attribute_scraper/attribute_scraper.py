import pydicom
import json
import argparse


EXCLUDED_VRS = {"OB", "UN", "SQ", "OD", "OF"}


def map_tags_to_values(file_path, excluded_tags, string_length):

    data_set = pydicom.dcmread(file_path)

    pairing = {}

    for element in data_set:
        is_excluded = (
            element.tag.is_private
            or str(element.tag) in excluded_tags
            or element.VR in EXCLUDED_VRS
        )

        if not is_excluded:
            pairing[str(element.tag).replace(" ", "")] = str(element.value)[0:string_length]

    return pairing


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("dcm_file", help="input DICOM file path")
    parser.add_argument("-o", "--output", help="name of output file")
    parser.add_argument("-l", "--length", help="length of output strings", type=int)
    parser.add_argument(
        "-e",
        "--excluded",
        help="excluded tags, separated by hyphens => for instance: '(0008, 0005)-(0010, 0010)'",
    )
    args = parser.parse_args()

    file_path = args.dcm_file
    if args.output:
        output_name = args.output
    else:
        output_name = "out.json"
    if args.length:
        string_length = args.length
    else:
        string_length = 50
    if args.excluded:
        excluded_tags = str(args.excluded).split(
            "-"
        )  # split by hyphen because commas are present within tags
    else:
        excluded_tags = set()

    output = map_tags_to_values(file_path, excluded_tags, string_length)

    with open(output_name, "w") as file:
        json.dump(output, file, indent=2)
