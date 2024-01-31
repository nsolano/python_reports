import uuid

class CSVInterface:
    def __init__(self, data_generator):
        self.data_generator = data_generator


    def data_dict_in_list(self):
        code = uuid.uuid4()
        data_list = []
        for data_dict in self.data_generator:
            for data in data_dict['data']:
                data_list.append({
                    'code': code,
                    'headers': data_dict['headers'],
                    'data': data
                })
        return data_list