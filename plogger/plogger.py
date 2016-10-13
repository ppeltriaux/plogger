#!/usr/bin/env python

#logging
import logging
import logging.config

class plogger():

    def __init__(self,loglevel=logging.INFO,name='plogger'):
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(loglevel)
        self.__formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def fileHandler(self,logfile,loglevel=logging.INFO):
        fh = logging.FileHandler(logfile)
        fh.setLevel(loglevel)
        fh.setFormatter(self.__formatter)
        self.__logger.addHandler(fh)

    def consoleHandler(self,loglevel=logging.INFO):
        ch = logging.StreamHandler()
        ch.setLevel(loglevel)
        ch.setFormatter(self.__formatter)
        self.__logger.addHandler(ch)

    def debug(self,txt):
        self.__logger.debug(txt)

    def warning(self,txt):
        self.__logger.warning(txt)

    def info(self,txt):
        self.__logger.info(txt)

    def critical(self,txt):
        self.__logger.critical(txt)

    def error(self,txt):
        self.__logger.error(txt)

    def exception(self,txt):
        self.__logger.exception(txt)


if __name__ == '__main__':
    FILE = 'example.log'
    mylogger = plogger(logging.DEBUG)
    mylogger.fileHandler(FILE)
    mylogger.consoleHandler(logging.ERROR)
    mylogger.info("test1234")
