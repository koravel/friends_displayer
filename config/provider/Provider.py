import abc
import util.TextConstants as tconst


class Provider:
    def __init__(self, location="", default_location="", logger=None):
        self.location = location
        self.default_location = default_location
        self.logger = logger

    @staticmethod
    @abc.abstractmethod
    def load(read_method, load_default=False):
        raise NotImplementedError(tconst.not_implemented_text.format("load"))

    @staticmethod
    @abc.abstractmethod
    def save(write_method):
        raise NotImplementedError(tconst.not_implemented_text.format("save"))
