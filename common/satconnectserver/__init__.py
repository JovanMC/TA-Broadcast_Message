import psycopg2

from common.satlogging import Logger


class PostgreDatabase:

    def __init__(self, **kwargs):
        self.__host = kwargs.get('host', None)
        self.__port = kwargs.get('port', None)
        self.__database = kwargs.get('database', None)
        self.__username = kwargs.get('username', None)
        self.__password = kwargs.get('password', None)
        self.__logger = Logger.createLogger(kwargs.get('logName', 'app'))

    def __connect(self):
        connection = psycopg2.connect(
            host=self.__host,
            port=self.__port,
            user=self.__username,
            password=self.__password,
            database=self.__database)
        cursor = connection.cursor()
        cursor.execute("SET TIMEZONE='Asia/Jakarta'")
        return connection, cursor

    def select(self, query, **params):
        connection = None
        cursor = None
        try:
            connection, cursor = self.__connect()
            cursor.execute(query, params)
            status = True
            data = cursor.fetchall()
        except psycopg2.Error as error:
            self.__logger.error(message=str(error))
            status = False
            data = {'error': 'Kesalahan database.'}
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
        return status, data
