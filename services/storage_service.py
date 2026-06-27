from providers.local import LocalProvider


class StorageService:

    def __init__(self):

        self.provider = LocalProvider()

    def upload(
        self,
        filename,
        content
    ):

        return self.provider.save(
            filename,
            content
        )
