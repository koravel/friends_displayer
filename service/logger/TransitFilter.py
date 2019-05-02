class TransitFilter:
    def __init__(self, destination, is_enabled=True):
        """
        :param destination: Abstract object: path, connection_params etc.
        :param is_enabled: is transport to destination enabled
        """
        self.destination = destination
        self.is_enabled = is_enabled
