class Logger:
    def setup(self, log_distributors):
        self.__log_distributors = log_distributors

    def log_trace(self, log=""):
        for log_distributor in self.__log_distributors:
            log_distributor.log_trace(log)

    def log_debug(self, log=""):
        for log_distributor in self.__log_distributors:
            log_distributor.log_debug(log)

    def log_info(self, log=""):
        for log_distributor in self.__log_distributors:
            log_distributor.log_info(log)

    def log_warn(self, log=""):
        for log_distributor in self.__log_distributors:
            log_distributor.log_warn(log)

    def log_error(self, log=""):
        for log_distributor in self.__log_distributors:
            log_distributor.log_error(log)

    def log_critical(self, log=""):
        for log_distributor in self.__log_distributors:
            log_distributor.log_critical(log)

    def log_fatal(self, log=""):
        for log_distributor in self.__log_distributors:
            log_distributor.log_fatal(log)
