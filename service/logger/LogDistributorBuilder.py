from service.logger import _LogLevel
from service.logger.BaseLogger import BaseLogger
from service.logger.FileLogger import FileLogger
from service.logger.FolderLogger import FolderLogger
from service.logger.LogDistributor import LogDistributor
from service.logger.TransitFilter import TransitFilter
from config.provider import SettingsKeys
from config.provider.SettingsProvider import SettingsProvider


class _LoggerSettingOptions:
    type = "type"
    log_level = "log_level"
    destination = "destination"
    is_enabled = "is_enabled"


class _LoggerTypes:
    console = "console"
    folder = "folder"
    file = "file"


class LogDistributorBuilder:
    def setup(self, settings):
        self.__loggers_settings = settings

    def build_all(self):
        log_distributors = []
        for logger_setting in self.__loggers_settings:
            if logger_setting[_LoggerSettingOptions.type] == _LoggerTypes.console:
                log_distributors.append(self.__build(logger_setting=logger_setting, distr_type=BaseLogger))
            elif logger_setting[_LoggerSettingOptions.type] == _LoggerTypes.folder:
                log_distributors.append(self.__build(logger_setting=logger_setting, distr_type=FolderLogger))
            elif logger_setting[_LoggerSettingOptions.type] == _LoggerTypes.file:
                log_distributors.append(self.__build(logger_setting=logger_setting, distr_type=FileLogger))
        return log_distributors

    @staticmethod
    def __build(distr_type, logger_setting):
        distributor = LogDistributor(
            logger=distr_type(
                log_level=logger_setting[_LoggerSettingOptions.log_level]
            ),
            transit_filter=TransitFilter(
                destination=logger_setting[_LoggerSettingOptions.destination],
                is_enabled=logger_setting[_LoggerSettingOptions.is_enabled]

            ))

        return distributor

    @staticmethod
    def build(log_level, destination, is_enabled, distr_type):
        distributor = LogDistributor(
            logger=distr_type(
                log_level=log_level
            ),
            transit_filter=TransitFilter(
                destination=destination,
                is_enabled=is_enabled

            ))

        return distributor

    @staticmethod
    def build_default():
        return LogDistributorBuilder.build(_LogLevel.TRACE, "", True, BaseLogger)
