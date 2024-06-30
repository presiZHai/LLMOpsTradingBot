from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

def load_file():
    pdf_files = [
        "C:\\iNeuron\\LLMTradingBot\\data\\cryptotrading.pdf",
        "C:\\iNeuron\\LLMTradingBot\\data\\finance_data.pdf"
    ]

    raw_text = ''

    for pdf_file in pdf_files:
        loader = PyPDFLoader(pdf_file)
        pages = loader.load()

        for i, doc in enumerate(pages):
            text = doc.page_content
            if text:
                raw_text += text

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    docs = text_splitter.split_text(raw_text)

    return docs
