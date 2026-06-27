import os
import uuid

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

        unique_name = f"{uuid.uuid4()}_{filename}"

        filepath = os.path.join(
            self.STORAGE_PATH,
            unique_name
        )
        )

        with open(
            filepath,
            "wb"
        ) as file:

            file.write(content)

       return {

            "filename": unique_name,
        
            "path": filepath
        
        }
