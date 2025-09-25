from .rest import create_rest_app


class Ventricle:

    def __init__(self):
        self.rest = create_rest_app()
        pass

    def start(self):
        pass

