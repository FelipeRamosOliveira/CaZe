# Mock a SQL data base
import pandas as pd
import sqlite3


def csv_to_sql(file='../volume/db.csv', table_name='houses'):
    ''' 
    Converts a csv file to a SQL data base
    '''
    try:
        table = pd.read_csv(filepath_or_buffer=file, skipinitialspace=True)
        connection = sqlite3.connect('../volume/db.sqlite')
        table.to_sql(table_name, connection)
        return ("converted file")

    except Exception as e:
        return(e)


if __name__ == '__main__':
    response = csv_to_sql()
    print(response)
