class FileService:
    @staticmethod
    def _open(obj_location, mode):
        return open(obj_location, mode)
