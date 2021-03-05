from dicom_attribute_scraper.attribute_scraper import map_tags_to_values

FILE_NAME = "./example_dicom_files/egfile3.dcm"


def test_patient_name():
    patient_name = map_tags_to_values(FILE_NAME, {}, 100)["(0010,0010)"]
    assert patient_name == "833975-119-R-1565"


def test_string_length():
    string_attribute = map_tags_to_values(FILE_NAME, {}, 24)["(7fe0,0010)"]
    assert len(string_attribute) == 24


def test_excluded_tags():
    dataset = map_tags_to_values(FILE_NAME, ["(0010, 0010)", "(0008, 0005)"], 24)
    assert "(0010,0010)" not in dataset.keys() and "(0008,0005)" not in dataset.keys()
