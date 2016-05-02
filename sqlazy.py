'''
Convenience objects when working with SQL databases

Note: Should add methods for inserting rows and adding columns
test:test
'''
import os
import sqlite3
import pandas as pd

class SQLDataBase(object):
    def __init__(self, path2db):
        self.path2db = path2db
        self.database = sqlite3.connect(self.path2db)
        self.dbcursor = self.database.cursor()

    def tables(self):
        '''
        Prints names of tables in database
        '''
        names = self.dbcursor.execute("select name \
                                      from sqlite_master \
                                      where type='table';").fetchall()
        print 'The database "{}" contains the tables:'.format(os.path.basename(self.path2db))
        for name in names:
            print name[0]

    def columns(self, table_name):
        '''
        Prints column names given a table name
        '''
        names = self.dbcursor.execute('select * from ' + table_name).description
        print 'The table "{}" has the following columns:'.format(table_name)
        for name in names:
            print name[0]

    def query2df(self, qry, index_col=None):
        '''
        Given query string and optional index column name (string),
        returns Pandas data frame associated with query
        '''
        return pd.read_sql(qry, self.database, index_col=index_col)

