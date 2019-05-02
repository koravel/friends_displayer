import json


class JSONCoder:
    @staticmethod
    def encode(obj, extended_encoder=None):
        try:
            result = json.dumps(obj=obj, sort_keys=True, indent=4, cls=extended_encoder)
        except Exception as ex:
            return ex
        else:
            return result

    @staticmethod
    def decode(obj, extended_decoder=None):
        try:
            result = json.loads(s=obj, cls=extended_decoder)

        except json.JSONDecodeError:
            raise json.JSONDecodeError
        else:
            return result
