from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains.combine_documents.reduce import ReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


class TextSummarizer:
    def __init__(self, documents):
        self.documents = documents
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")

    def summarize(self):
        return self.__summarize_documents()

    def __summarize_documents(self):
        map_chain = self.__create_map_chain()
        reduce_chain = self.__create_reduce_chain()

        map_reduce_chain = MapReduceDocumentsChain(
            llm_chain=map_chain,
            reduce_documents_chain=reduce_chain,
            document_variable_name="docs"
        )

        return map_reduce_chain.invoke(self.documents)

    def __create_map_chain(self):
        map_template = """In order to break down the given article into easily understandable bullet points, read each section carefully. 
        As a software engineer looking to learn, extract the most useful and relevant information, ignoring what you already know. 
        Write your notes in the form of concise bullet points, making sure to keep it simple and in English.
        Follow only the topic that is presented in the article.
        ###Document
        {docs}
        """
        map_prompt = PromptTemplate.from_template(map_template)
        map_chain = LLMChain(llm=self.llm, prompt=map_prompt)
        return map_chain

    def __create_reduce_chain(self):
        reduce_template = """
        Given the set of notes on a specific topic, could you please review and consolidate them into a single, well-structured document? 
        Feel free to group related bullet points into comprehensive sentences, ensuring to maintain a clear flow. 
        Please format final document in Markdown language and make sure it is in English.
        You should use formatting for better redability like bold, italic, underline or making list with bullet points.
        ###Document
        {docs}
        """
        reduce_prompt = PromptTemplate.from_template(reduce_template)
        reduce_chain = LLMChain(llm=self.llm, prompt=reduce_prompt)
        combine_documents_chain = StuffDocumentsChain(llm_chain=reduce_chain, document_variable_name="docs")
        return ReduceDocumentsChain(combine_documents_chain=combine_documents_chain,
                                    collapse_documents_chain=combine_documents_chain, token_max=4000)
