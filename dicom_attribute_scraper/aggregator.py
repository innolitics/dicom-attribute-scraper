import json
import argparse


def aggregate(files):
    tag_set = set()
    mapping = {}

    for file in files:
        for tag in files[file]:
            if tag not in tag_set:
                tag_set.add(tag)

    for tag in tag_set:
        mapping[tag] = []
        for file in files:
            if tag in files[file]:
                mapping[tag].append(files[file][tag])
    return mapping


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="input files")
    parser.add_argument("-o", "--output", help="name of output file")
    args = parser.parse_args()

    file_paths = args.files
    if args.output:
        output_name = args.output
    else:
        output_name = "output.json"

    files = {}

    for path in file_paths:
        with open(path) as f:
            files[path] = json.load(f)

    output = aggregate(files)

    with open(output_name, "w") as f:
        json.dump(output, f, indent=2)
