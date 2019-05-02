import abc
import traceback
from datetime import datetime

from service.logger import _LogLevel
import util.TextConstants as tconst


class BaseLogger:
    def __init__(self, log_level=_LogLevel.INFO, enable_caching=False):
        self.__log_level = log_level
        self.__enable_caching = enable_caching
        if not hasattr(self, "journal"):
            self.journal = []

    @staticmethod
    def _get_formatted_message(log, log_level):
        """
                Format: [current_time][log_level]: log_text
                """
        return "[{}][{}]: {}".format(datetime.now().replace(microsecond=0), _LogLevel.title[log_level], log)

    @abc.abstractmethod
    def _write_to_destination(self, destination, log):
        raise NotImplementedError(tconst.not_implemented_text.format("__write_to_destination"))

    def __log(self, log_level, log, destination=""):
        if self.__log_level >= log_level:
            formatted_log = self._get_formatted_message(log, log_level)

            traceback_log = traceback.format_exc()
            if len(traceback_log) > 15:
                formatted_log = "\n{}\n{}".format(formatted_log, traceback_log)

            if destination == "":
                if self.__enable_caching:
                    self.__write_to_journal(formatted_log)
                else:
                    self.__write_to_console(formatted_log)
            else:
                self.__clear_cache(destination)
                self._write_to_destination(destination, formatted_log)

    def __clear_cache(self, destination):
        while len(self.journal) > 0:
            self._write_to_destination(destination, self.journal.pop())

    def __write_to_journal(self, log):
        self.journal.append(log)

    @staticmethod
    def __write_to_console(log):
        print(log)

    def log_trace(self, log, destination):
        self.__log(_LogLevel.TRACE, log, destination)

    def log_debug(self, log, destination):
        self.__log(_LogLevel.DEBUG, log, destination)

    def log_info(self, log, destination):
        self.__log(_LogLevel.INFO, log, destination)

    def log_warn(self, log, destination):
        self.__log(_LogLevel.WARN, log, destination)

    def log_error(self, log, destination):
        self.__log(_LogLevel.ERROR, log, destination)

    def log_critical(self, log, destination):
        self.__log(_LogLevel.CRITICAL, log, destination)

    def log_fatal(self, log, destination):
        self.__log(_LogLevel.FATAL, log, destination)
