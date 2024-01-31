from infrastructure.presentation.cli.cli import Interface


def main():
    path = 'infrastructure/assets/documents/sample.csv'
    iface = Interface(data_path = path, mode= 'read', db_type= 'csv')
    iface.run()
    
if __name__ == '__main__':
    main()