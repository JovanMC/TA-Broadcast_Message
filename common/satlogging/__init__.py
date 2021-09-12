import datetime
import logging
import os
import pathlib


class Logger(logging.Logger):

    @staticmethod
    def createLogger(name):
        if os.environ.get('GAE_INSTANCE') is not None:
            return AppEngineLogger(name)
        else:
            return StorageLogger(name)


class StorageLogger(Logger):

    def __init__(self, name):
        super().__init__(name)

        self.__path = pathlib.Path(f'logs/{name}')
        self.__logger = logging.Logger(name)
        self.__formatter = logging.Formatter(
            fmt='%(asctime)s %(levelname)s %(message)s',
            datefmt='%H:%M:%S')
        self.__path.mkdir(parents=True, exist_ok=True)

    def __createHandler(self):
        if self.__logger.hasHandlers():
            self.__logger.removeHandler(self.__logger.handlers[0])

        date = datetime.date.today().strftime('%Y-%m-%d')
        handler = logging.FileHandler(
            mode='a',
            filename=f'{self.__path}/{date}.log')
        handler.setFormatter(self.__formatter)
        self.__logger.addHandler(handler)

    def debug(self, message, *args, **kwargs):
        self.__createHandler()
        self.__logger.debug(message)

    def info(self, message, *args, **kwargs):
        self.__createHandler()
        self.__logger.info(message)

    def warning(self, message, *args, **kwargs):
        self.__createHandler()
        self.__logger.warning(message)

    def error(self, message, *args, **kwargs):
        self.__createHandler()
        self.__logger.error(message)

    def critical(self, message, *args, **kwargs):
        self.__createHandler()
        self.__logger.critical(message)


class AppEngineLogger(Logger):

    def __init__(self, name):
        from google.cloud import logging_v2
        from google.cloud.logging_v2.resource import Resource

        super().__init__(name)

        self.__client = logging_v2.Client()
        self.__logger = self.__client.logger(name)
        self.__resource = Resource(
            type='gae_app',
            labels={
                'module_id': os.environ.get('GAE_SERVICE'),
                'project_id': os.environ.get('GOOGLE_CLOUD_PROJECT'),
                'version_id': os.environ.get('GAE_VERSION')})

    def __log(self, severity, **kwargs):
        self.__logger.log_struct(
            resource=self.__resource,
            severity=severity,
            info=kwargs)

    def debug(self, message, *args, **kwargs):
        self.__log(
            severity='DEBUG',
            message=message,
            **kwargs)

    def info(self, message, *args, **kwargs):
        self.__log(
            severity='INFO',
            message=message,
            **kwargs)

    def warning(self, message, *args, **kwargs):
        self.__log(
            severity='WARNING',
            message=message,
            **kwargs)

    def error(self, message, *args, **kwargs):
        self.__log(
            severity='ERROR',
            message=message,
            **kwargs)

    def critical(self, message, *args, **kwargs):
        self.__log(
            severity='CRITICAL',
            message=message,
            **kwargs)
