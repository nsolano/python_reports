from infrastructure.repositories.csv.reader import CSVReader
from interfaces.csvinterface import CSVInterface
from interfaces.meminterface import MemInterface
from logic.basic_data_list import get_list

class Interface:
    def __init__(self, data_path: str, mode: str, db_type: str):
        self.data_path = data_path
        self.mode = mode
        self.db_type = db_type

    def read_data_from_path(self):
        print(f'Opening {self.db_type} data in: {self.data_path} \n')

        if self.db_type.lower() == 'csv':
            reader = CSVReader(self.data_path)
            lenght_csv = reader.get_lenght() - 1
            
            print(f'There are {lenght_csv} number of rows')
            
            while True:
                chunk_size = input("Please enter the chunk size: ")
                
                if chunk_size.isdecimal():
                    chunk_size = int(chunk_size)
                    break   
            
            if chunk_size > lenght_csv:
                chunk_size = None

            try:
                content = reader.read(chunk_size=chunk_size)
                return content
            except Exception as ex:
                print(ex)
        else:
            raise ValueError('DB type is not CSV or SQL')
    
    @staticmethod
    def show_list(data):
        data_generator = CSVInterface(data)        
        interface = MemInterface(data_generator.data_dict_in_list())
        return get_list(interface)
    
    def run(self):
        print('Welcome \n')
        data = self.read_data_from_path()
        print(data)        
        
        result = self.show_list(data)
        print(result)
        print('\nExiting...')
            
        
        