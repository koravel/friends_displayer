from service.file.FileWriteService import FileWriteService
from service.json.JSONCoder import JSONCoder


class JSONWriteService(FileWriteService):
    @staticmethod
    def write(obj, obj_location, extended_encoder=None):
        super(JSONWriteService, JSONWriteService).write(JSONCoder.encode(obj, extended_encoder), obj_location)
