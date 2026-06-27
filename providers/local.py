import os


class LocalProvider:

    STORAGE_PATH = "storage"

    def save(
        self,
        filename,
        content
    ):

        os.makedirs(
            self.STORAGE_PATH,
            exist_ok=True
        )

        filepath = os.path.join(
            self.STORAGE_PATH,
            filename
        )

        with open(
            filepath,
            "wb"
        ) as file:

            file.write(content)

        return filepath
