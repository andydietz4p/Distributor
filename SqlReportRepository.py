from ReportRepository import ReportRepository
import pymssql
import os


class SqlReportRepository(ReportRepository):
    def __init__(self):
        # build the connection to the sql server
        self.__server = os.environ['DBSERVER']
        self.__user = os.environ['DBUSER']
        self.__password = os.environ['DBPASSWORD']
        self.__allReportsSql = os.environ['DBALLREPORTSSQL']
        self.__conn = pymssql.connect(self.__server, self.__user, self.__password)
        self.__cursor = self.__conn.cursor(as_dict=True)

    def __delete__(self):
        # kill the connection to the sql server
        self.__conn.close()

    def getAllReports(self):
        # get all reports.
        self.__cursor.execute(self.__allReportsSql)
        reports = self.__cursor.fetchall()
        return reports

    def getSomeReports(self, filter):
        return None
