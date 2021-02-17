import json
import argparse
from collections import defaultdict


def aggregate(file_paths):
    parsed_files = []

    for path in file_paths:
        with open(path) as f:
            parsed_files.append(json.load(f))

    tag_to_values = defaultdict(list)
    for file in parsed_files:
        for tag, value in file.items():
            tag_to_values[tag].append(value)

    return tag_to_values


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="input files")
    parser.add_argument("-o", "--output", help="name of output file")
    args = parser.parse_args()

    file_paths = args.files

    output_name = args.output if args.output else "output.json"

    output = aggregate(file_paths)

    with open(output_name, "w") as f:
        json.dump(output, f, indent=2)
