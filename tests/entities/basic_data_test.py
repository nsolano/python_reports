import uuid

from entities.basic_data import BasicData


def test_basic_data():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "headers": ["header1", "header2", "header3"],
        "data": ["data1", "data2", "data3"],
    }

    data = BasicData.from_dict(init_dict)

    assert data.to_dict() == init_dict


def test_basic_data_comparisson():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "headers": ["header1", "header2", "header3"],
        "data": ["data1", "data2", "data3"],
    }

    data_1 = BasicData.from_dict(init_dict)
    data_2 = BasicData.from_dict(init_dict)

    assert data_1 == data_2
