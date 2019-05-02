class LogDistributor:
    def __init__(self, logger, transit_filter):
        self.__logger = logger
        self.__transit_filter = transit_filter

    def log_trace(self, log=""):
        if self.__transit_filter.is_enabled:
            self.__logger.log_trace(log, self.__transit_filter.destination)

    def log_debug(self, log=""):
        if self.__transit_filter.is_enabled:
            self.__logger.log_debug(log, self.__transit_filter.destination)

    def log_info(self, log=""):
        if self.__transit_filter.is_enabled:
            self.__logger.log_info(log, self.__transit_filter.destination)

    def log_warn(self, log=""):
        if self.__transit_filter.is_enabled:
            self.__logger.log_warn(log, self.__transit_filter.destination)

    def log_error(self, log=""):
        if self.__transit_filter.is_enabled:
            self.__logger.log_error(log, self.__transit_filter.destination)

    def log_critical(self, log=""):
        if self.__transit_filter.is_enabled:
            self.__logger.log_critical(log, self.__transit_filter.destination)

    def log_fatal(self, log=""):
        if self.__transit_filter.is_enabled:
            self.__logger.log_fatal(log, self.__transit_filter.destination)

