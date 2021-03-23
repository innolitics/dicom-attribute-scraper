"""Calculates the percentage of included tags in an aggregated file out of the total possible tags

Input:
JSON file with aggregated examples for each tag

Output:
Percentage covered out of total number of tags possible
"""
import argparse
import json

TAG_FILE = "./attributes.json"


def calculate_coverage(in_file):

    with open(TAG_FILE) as f:
        ref_file = json.load(f)

    ref_tags = [
        x["tag"]
        for x in ref_file
        if x["tag"][3:5] != "XX"
        and int(x["tag"][1:5], 16) % 2 == 0
        and "Sequence" not in x["name"]
    ]

    your_tags = [x.upper() for x in in_file]

    return len(your_tags) * 100 / len(ref_tags)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="JSON file for which to calculate tag coverage")
    args = parser.parse_args()

    with open(args.input_file) as f:
        in_file = json.load(f)

    print("{}%".format(calculate_coverage(in_file)))
