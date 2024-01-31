from entities.basic_data import BasicData

class MemInterface:
    def __init__(self, data_dict):
        self.data_dict = data_dict
    
    def list(self):
        return [BasicData.from_dict(i) for i in self.data_dict]