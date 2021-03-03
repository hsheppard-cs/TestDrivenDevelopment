import pytest
from NameFrequency import NameFrequency

@pytest.fixture()
def name_frequency():
    name_frequency = NameFrequency()
    return name_frequency


def test_CanReadCsvInDataframe(name_frequency):
    name_frequency.preparingData('users.csv', 'name')
    assert name_frequency.preparingData('users.csv', 'name') == True
    # assert keyword is used to test if a condition returns True, if not,
    # the program will raise an AssertionError

