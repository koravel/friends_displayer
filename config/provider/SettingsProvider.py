from service.json.JSONWriteService import JSONWriteService
from service.json.JSONReadService import JSONReadService
from config.provider.Provider import Provider


class SettingsProvider(Provider):
    def save(self, settings, write_method=JSONWriteService.write):
        try:
            write_method(settings, self.location)
        except:
            self.__log_error("Cannot save settings to {}. Any changes were lost".format(self.location))
        else:
            self.__log_info("Successfully saved settings to {}".format(self.location))

    def load(self, read_method=JSONReadService.read, load_default=False):
        settings = dict()
        try:
            settings = read_method(self.location)
        except:
            if self.default_location is not None and load_default:
                self.__log_error("Cannot load settings from {}. Try to load default file...".format(self.location))
                settings = self.__load_defaults(read_method)
        else:
            self.__log_info("Successfully loaded settings from {}".format(self.location))
        return settings

    def __load_defaults(self, read_method=JSONReadService.read):
        defaults = None
        try:
            defaults = read_method(self.default_location)
        except:
            self.__log_error("Unable to load default settings from {}".format(self.default_location))
        else:
            self.__log_info("Successfully load default settings".format(self.default_location))
        return defaults

    def __log_error(self, text):
        if self.logger is not None:
            self.logger.log_critical(text)

    def __log_info(self, text):
        if self.logger is not None:
            self.logger.log_info(text)
