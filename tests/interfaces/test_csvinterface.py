from interfaces.csvinterface import CSVInterface


def test_data_list():

    data_generator = iter(
        [
            {"headers": ["header1", "header2"], "data": [[1, 2], [3, 4]]},
            {"headers": ["header3", "header4"], "data": [[5, 6], [7, 8]]},
        ]
    )

    csv_interface = CSVInterface(data_generator)

    result = csv_interface.data_dict_in_list()

    assert isinstance(result, list)

    for dictionary in result:
        assert "code", "headers" in dictionary.keys()

    assert result[0]["data"] == [1, 2]
