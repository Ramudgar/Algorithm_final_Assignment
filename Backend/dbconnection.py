import mysql.connector

class DBConnect:
    def __init__(self):

        self.con=mysql.connector.connect(host='localhost',user='root',password='Softco@123',
                                         database='Algorithm_final')
        self.cur=self.con.cursor()


    def insert(self,query,values):
        '''
        this function will insert the data into database
        :param query: query should be str type
        :param values: values should be tuple
        :return: None
        '''
        self.cur.execute(query,values)
        self.con.commit()

    def select(self,query,values):
        '''
        this function will inser the data in to database
        :param query: query should be string type
        :param values: values should tuple
        :return: rows
        '''
        self.cur.execute(query,values)
        rows=self.cur.fetchall()
        return rows

    def selectall(self,query):
        '''
        this function fetch all values from database to tree view
        :param query:
        :return:value from database
        '''
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def create(self, query):
        self.cur.execute(query)
        self.con.commit()








