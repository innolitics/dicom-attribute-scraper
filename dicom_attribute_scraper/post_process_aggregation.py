"""Cleans up a raw JSON file containing tags and corresponding aggregated examples to reduce file size

Deduplicates the examples for each tag
Limits the number of examples per tag to 6 (default) or a user-input integer
"""

import json
import argparse
from collections import Counter


def clean_aggregated_file(agg_file, number_of_examples):
    for tag in agg_file:
        common_tuples = Counter(agg_file[tag]).most_common(number_of_examples)

        agg_file[tag] = [example_value for example_value, frequency in common_tuples]

    return agg_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="input raw aggregated JSON file")
    parser.add_argument("-n", "--number", help="number of examples to be stored per tag")
    parser.add_argument("-o", "--output", help="name of output file")
    args = parser.parse_args()

    with open(args.file) as f:
        file_to_process = json.load(f)

    if args.number:
        number_of_examples = int(args.number)
    else:
        number_of_examples = 6

    output_name = args.output or "cleaned_aggregation.json"

    output = clean_aggregated_file(file_to_process, number_of_examples)

    with open(output_name, "w") as f:
        json.dump(output, f, indent=2)
