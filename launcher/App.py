from config.provider import SettingsKeys
from config.provider.SettingsProvider import SettingsProvider
from launcher import *
from service.logger.LogDistributorBuilder import LogDistributorBuilder
from service.logger.Logger import Logger
from service.selenium.friends_displayer.FriendsDisplayer import FriendsDisplayer


class App:
    @classmethod
    def __init__(cls):
        log_distributor_builder = LogDistributorBuilder()

        if not hasattr(cls, "settings"):
            default_log_distributor = log_distributor_builder.build_default()

            cls.logger = Logger()
            cls.logger.setup([default_log_distributor])

            cls.settings = SettingsProvider(location=settings_location, logger=cls.logger).load()

        if not hasattr(cls, "logger"):
            log_distributor_builder.setup(cls.settings[SettingsKeys.logging][SettingsKeys.loggers])
            log_distributors = log_distributor_builder.build_all()

            cls.logger.setup(log_distributors=log_distributors)

    def run(self):
        self.displayer = FriendsDisplayer(self.settings[SettingsKeys.selenuim][SettingsKeys.driver_location],
                                          self.logger,
                                          self.settings[SettingsKeys.selenuim][SettingsKeys.actions_delay])

        self.displayer.login(self.settings[SettingsKeys.selenuim][SettingsKeys.email],
                             self.settings[SettingsKeys.selenuim][SettingsKeys.password])

        self.displayer.get_friends_dict()

    def finalize(self):
        if hasattr(self, "displayer"):
            self.displayer.finalize()
