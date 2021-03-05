from dicom_attribute_scraper.aggregator import aggregate

FILE_1 = "./tests/fixtures/parsed_1.json"
FILE_2 = "./tests/fixtures/parsed_2.json"
FILE_3 = "./tests/fixtures/parsed_3.json"

file_paths = [FILE_1, FILE_2, FILE_3]


def test_tag_aggregation():
    attr = aggregate(file_paths)["(0008,0070)"]
    assert set(attr) == set(
        ["GE MEDICAL SYSTEMS", "Stanford University", "Philips Medical Systems"]
    )
