import pyodbc


class ODBCMS:
    def __init__(self, DRIVER, SERVER, DATABASE, UID, PWD):
        ''' initialization '''

        self.DRIVER = DRIVER
        self.SERVER = SERVER
        self.DATABASE = DATABASE
        self.UID = UID
        self.PWD = PWD

    def __GetConnect(self):
        ''' Connect to the DB '''

        if not self.DATABASE:
            raise(NameError, "no setting db info")

        self.conn = pyodbc.connect(DRIVER=self.DRIVER, SERVER=self.SERVER,
                                   DATABASE=self.DATABASE, UID=self.UID,
                                   PWD=self.PWD, charset="UTF-8")

        cur = self.conn.cursor()
        if not cur:
            raise(NameError, "connected failed!")
        else:
            return cur

    def ExecQuery(self, sql):
        ''' Perform one Sql statement '''

        cur = self.__GetConnect()  # 建立链接并创建数据库操作指针
        cur.execute(sql)           # 通过指针来执行sql指令
        ret = cur.fetchall()       # 通过指针来获取sql指令响应数据
        # ret = cur.fetchone()
        cur.close()                # 游标指标关闭
        self.conn.close()          # 关闭数据库连接

        return ret

    def ExecNoQuery(self, sql):
        ''' SQL like write data, or create table, database and so on'''

        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()    # by connection handle
        cur.close()
        self.conn.close()
