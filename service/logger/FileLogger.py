import os

from service.logger.BaseLogger import BaseLogger
from service.file.FileWriteService import FileWriteService


class FileLogger(BaseLogger):
    def _write_to_destination(self, file_path, log):
        folder_path = os.path.dirname(file_path)

        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)

        FileWriteService.append(log, file_path)
