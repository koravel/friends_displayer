from service.file.FileService import FileService
from service.file import OpenModes


class FileReadService(FileService):
    @staticmethod
    def _open(obj_location, mode=OpenModes.READ):
        return super(FileReadService, FileReadService)._open(obj_location, OpenModes.READ)

    @staticmethod
    def read_yield(obj_location):
        try:
            with FileReadService._open(obj_location) as file_stream:
                for line in file_stream:
                    yield line
        except Exception as ex:
            raise ex

    @staticmethod
    def read_all(obj_location):
        try:
            with FileReadService._open(obj_location) as file_stream:
                return file_stream.read()
        except Exception as ex:
            raise ex
