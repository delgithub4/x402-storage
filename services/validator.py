class FileValidator:

    MAX_SIZE = 10 * 1024 * 1024

    ALLOWED_TYPES = [

        "application/pdf",

        "image/png",

        "image/jpeg"

    ]

    def validate(
        self,
        file,
        size
    ):

        if size > self.MAX_SIZE:

            return False, "File too large."

        if file.content_type not in self.ALLOWED_TYPES:

            return False, "Unsupported file."

        return True, "OK"
