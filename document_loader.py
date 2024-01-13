class DocumentLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_document(self):
        with open(self.file_path, 'r') as file:
            document = file.read()
        return document
