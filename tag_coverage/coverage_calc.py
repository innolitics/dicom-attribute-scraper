"""Calculates the percentage of included tags in an aggregated file out of the total possible tags

Input:
JSON file with aggregated examples for each tag
JSON file with all possible tags, with two keys each: 'tag' and 'name'

Output:
Percentage covered out of total number of tags possible
"""
import argparse
import json


def calculate_coverage(input_tag_map, reference_file):

    filtered_reference_tags = [
        data_element["tag"]
        for data_element in reference_file
        if data_element["tag"][3:5] != "XX"  # excludes non-specific tags
        and int(data_element["tag"][1:5], 16) % 2 == 0  # excludes private tags
        and "Sequence" not in data_element["name"]
    ]

    return len(input_tag_map) * 100 / len(filtered_reference_tags)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="JSON file for which to calculate tag coverage")
    parser.add_argument(
        "reference_file",
        help="JSON file containing all possible tags with 'tag' and 'name' keys and string values",
    )
    args = parser.parse_args()

    with open(args.input_file) as f:
        input_tag_map = json.load(f)

    with open(args.reference_file) as f:
        reference_file = json.load(f)

    print("{:.2f}%".format(calculate_coverage(input_tag_map, reference_file)))
