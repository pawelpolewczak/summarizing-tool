from document_loader import DocumentLoader

if __name__ == '__main__':
    path = "long_doc.txt"
    loader = DocumentLoader(path)
    document = loader.load_document()
    print(document)

