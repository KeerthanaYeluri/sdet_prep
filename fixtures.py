import pytest


@pytest.fixture()
def sample_data():
    print("creating test data")
    data = {"name": "abc", "age": 25}
    return data


def test_sample(sample_data):
    assert sample_data["name"] == "abc"
    assert sample_data["age"] == 25
    print("test executed successfully")
