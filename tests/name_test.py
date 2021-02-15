import pytest
from dicom_attribute_scraper.attribute_scraper import map_tags_to_values


# file-path:/home/arjun/.pyenv/versions/3.7.0/envs/scraper/lib/python3.7/site-packages/pydicom/data/test_files/CT_small.dcm
file_name = "./example_dicom_files/1-15.dcm"

# print(map_tags_to_values('1-15.dcm', {}, 100)['(0010, 0010)'])
def test_patient_name():
    patient_name = map_tags_to_values(file_name, {}, 100)["(0010, 0010)"]
    assert patient_name == "833975-119-R-1565"


# test_patient_name()


def test_string_length():
    string_attribute = map_tags_to_values(file_name, {}, 24)["(7fe0, 0010)"]
    # print(string_attribute)
    assert string_attribute.__len__() == 24


# test_string_length()


def test_excluded_tags():
    dataset = map_tags_to_values(file_name, ["(0010, 0010)", "(0008, 0005)"], 24)
    assert "(0010, 0010)" not in dataset.keys() and "(0008, 0005)" not in dataset.keys()


# test_excluded_tags()
