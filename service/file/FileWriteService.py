from service.file.FileService import FileService
from service.file import OpenModes


class FileWriteService(FileService):
    @staticmethod
    def _open(obj_location, mode=OpenModes.WRITE):
        if mode == OpenModes.WRITE or mode == OpenModes.APPEND:
            return super(FileWriteService, FileWriteService)._open(obj_location, mode)
        raise ValueError

    @staticmethod
    def write(obj, obj_location):
        FileWriteService._write(obj, obj_location, OpenModes.WRITE)

    @staticmethod
    def write_array(obj, obj_location):
        return FileWriteService._write_array(obj, obj_location, OpenModes.WRITE)

    @staticmethod
    def append(obj, obj_location):
        FileWriteService._write(obj, obj_location, OpenModes.APPEND)

    @staticmethod
    def append_array(obj, obj_location):
        return FileWriteService._write_array(obj, obj_location, OpenModes.APPEND)

    @staticmethod
    def _write(obj, obj_location, mode):
        try:
            with FileWriteService._open(obj_location, mode) as file_stream:
                file_stream.write("{}\n".format(str(obj)))
        except Exception as ex:
            raise ex

    @staticmethod
    def _write_array(obj, obj_location, mode):
        try:
            counter = 0
            with FileWriteService._open(obj_location, mode) as file_stream:
                for item in obj:
                    file_stream.write("{}\n".format(str(item)))
                    counter += 1
            return counter
        except Exception as ex:
            raise ex
