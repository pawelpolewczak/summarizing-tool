import dotenv
import datetime

from document_loader import DocumentLoader
from text_summarizer import TextSummarizer


def process_document(path):
    loader = DocumentLoader(path)
    document = loader.load_document()
    text_summarizer = TextSummarizer(document)
    summary = text_summarizer.summarize()

    save_to_file(path, summary)


def save_to_file(path, summary):
    now = datetime.datetime.now()
    date_suffix = now.strftime("%Y%m%d%H%M%S")
    summary_path = path.replace(".md", "") + "_summary_" + date_suffix + ".md"
    with open(summary_path, 'w') as file:
        file.write(summary.get('output_text'))


if __name__ == '__main__':
    dotenv.load_dotenv()
    process_document("long_doc.md")
