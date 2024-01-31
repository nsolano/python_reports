import uuid
from unittest import mock

import pytest

from entities.basic_data import BasicData
from logic.basic_data_list import get_list


@pytest.fixture
def basic_data_list():
    data_1 = BasicData(
        code=uuid.uuid4(),
        headers=["header1", "header2", "header3"],
        data=["data1", "data2", "data3"],
    )

    data_2 = BasicData(
        code=uuid.uuid4(),
        headers=["header4", "header5", "header6"],
        data=["data4", "data5", "data6"],
    )

    data_3 = BasicData(
        code=uuid.uuid4(),
        headers=["header7", "header8", "header9"],
        data=["data7", "data8", "data9"],
    )

    return [data_1, data_2, data_3]


def test_basic_data_list_no_params(basic_data_list):
    inter = mock.Mock()
    inter.list.return_value = basic_data_list

    result = get_list(inter)

    assert result == basic_data_list
