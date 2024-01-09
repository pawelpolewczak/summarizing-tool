
class DocumentLoader:
    def __init__(self, file_path):
        self.document = self.__load_document(file_path)

    # Create a method that takes file path as parameter and returns the file content
    def __load_document(self, file_path):
        with open(file_path, 'r') as file:
            document = file.read()
        return document



