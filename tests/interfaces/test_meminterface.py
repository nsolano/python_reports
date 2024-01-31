import pytest

from entities.basic_data import BasicData
from interfaces.meminterface import MemInterface


@pytest.fixture
def basic_data_dict():
    return [
        {
            "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e1a",
            "headers": ["header1", "header2", "header3"],
            "data": ["data1", "data2", "data3"],
        },
        {
            "code": "ge2c3195-aeff-487a-a08f-e0bdc0ec6e2b",
            "headers": ["header4", "header5", "header6"],
            "data": ["data4", "data5", "data6"],
        },
        {
            "code": "ae2c3195-aeff-487a-a08f-e0bdc0ec6e3c",
            "headers": ["header7", "header8", "header9"],
            "data": ["data7", "data8", "data9"],
        },
        {
            "code": "be2c3195-aeff-487a-a08f-e0bdc0ec6e4d",
            "headers": ["header7", "header8", "header9"],
            "data": ["data7", "data8", "data9"],
        },
    ]


def test_basic_data_list_no_params(basic_data_dict):
    inter = MemInterface(basic_data_dict)
    data = basic_data_dict

    basic_data_list = [BasicData.from_dict(i) for i in data]

    assert inter.list() == basic_data_list
