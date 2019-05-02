import os
from datetime import datetime

from service.logger import _LogLevel
from service.logger.BaseLogger import BaseLogger
from service.file.FileWriteService import FileWriteService


class FolderLogger(BaseLogger):
    def __init__(self, log_level=_LogLevel.INFO, enable_caching=False):
        super(FolderLogger, self).__init__(log_level, enable_caching)
        self.__file = "{}.log".format(datetime.now().replace(microsecond=0)).replace(":", "_")

    def _write_to_destination(self, folder_path, log):
        file_path = os.path.join(folder_path, self.__file)

        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)

        FileWriteService.append(log, file_path)
