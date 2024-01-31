import csv

from itertools import islice


class CSVReader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        
    def open_file(self):
        with open(self.file_path, 'r') as file:
            csv_reader = csv.reader(file)
            yield csv_reader
    
    
    def get_headers(self):
        file_generator = self.open_file()
        
        for file in file_generator:
            headers = next(file)
       
        return headers
        

    def get_lenght(self):
        file_generator = self.open_file()
        
        for file in file_generator:
            row_count = sum(1 for line in file)
    
        return row_count
    
    def read(self, chunk_size):
        file_generator = self.open_file()
        
        data = {'headers': self.get_headers()}
        
        if not chunk_size:
            chunk_size = self.get_lenght() - 1
        
             
        for file in file_generator:
            data['data'] = self.iterator(file, chunk_size)
            yield data            
  
    @staticmethod
    def iterator(iterable, chunk_size):
        """Yields chunks of a given size from an iterable."""
        it = iter(iterable)
        while True:
            chunk = list(islice(it, chunk_size))
            if not chunk:
                break
            yield chunk     
    
                    
