#coding:gbk
import pymysql
class DataOutput(object):
    def __init__(self):
        self.con = pymysql.connect(host='localhost',user='root',
        passwd='',db='test',port=3306,charset='gbk')
        self.cur=self.con.cursor()
        self.create_table('person')
        self.datas=[]

    def create_table(self,table_name):

        values = '''
        id integer primary key,
        MovieId integer,
        MovieTitle varchar(40) NOT NULL,
        RatingFinal REAL NOT NULL DEFAULT 0.0,
        ROtherFinal REAL NOT NULL DEFAULT 0.0,
        RPictureFinal REAL NOT NULL DEFAULT 0.0,
        RDirectorFinal REAL NOT NULL DEFAULT 0.0,
        RStoryFinal REAL NOT NULL DEFAULT 0.0,
        Usercount integer NOT NULL DEFAULT 0,
        AttitudeCount integer NOT NULL DEFAULT 0,
        TotalBoxOffice varchar(20) NOT NULL,
        TodayBoxOffice varchar(20) NOT NULL,
        Ran integer NOT NULL DEFAULT 0,
        ShowDays integer NOT NULL DEFAULT 0,
        isRelease integer NOT NULL
        '''
        self.cur.execute('CREATE TABLE IF NOT EXISTS %s( %s ) '%(table_name,values))


    def store_data(self,data):
        '''
        数据存储
        :param data:
        :return:
        '''
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas)>10:
            self.output_db('person')

    def output_db(self,table_name):
        '''
        将数据存储到sqlite
        :return:
        '''
        for data in self.datas:
            print(data)
            self.cur.execute("INSERT INTO %s (MovieId,MovieTitle,"
                            "RatingFinal,ROtherFinal,RPictureFinal,"
                            "RDirectorFinal,RStoryFinal,Usercount,"
                            "AttitudeCount,TotalBoxOffice,TodayBoxOffice,"
                            "Ran,ShowDays,isRelease) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?) "
                            ""%table_name,data)
            self.datas.remove(data)
        self.con.commit()

    def output_end(self):
        '''
        关闭数据库
        :return:
        '''
        if len(self.datas)>0:
            self.output_db('person')
        self.con.close()
