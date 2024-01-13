from langchain.text_splitter import MarkdownHeaderTextSplitter


class DocumentLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_document(self):
        with open(self.file_path, 'r') as file:
            document = file.read()
        return self.__split_markdown(document)

    @staticmethod
    def __split_markdown(document):
        headers_to_split = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
        markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split)
        return markdown_splitter.split_text(document)
