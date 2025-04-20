import streamlit as st
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI
import tempfile
import os
from dotenv import load_dotenv
load_dotenv()




def load_document(file):
    if file.type == "application/pdf":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name
        loader = PyPDFLoader(tmp_path)
    elif file.type == "text/plain":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name
        loader = TextLoader(tmp_path)
    else:
        return None

    documents = loader.load()
    os.remove(tmp_path)
    return documents

def main():
    st.set_page_config(page_title="IndianExamGPT", page_icon="🎓")
    st.title("📘 IndianExamGPT")
    st.write("Ask questions from Indian exam PDFs or text files using OpenAI + LangChain.")

    file = st.file_uploader("📂 Upload a PDF or TXT file", type=["pdf", "txt"])
    if file is not None:
        with st.spinner("Processing document..."):
            documents = load_document(file)
            if not documents:
                st.error("Unsupported file format.")
                return

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            texts = text_splitter.split_documents(documents)

            embeddings = OpenAIEmbeddings()
            vectorstore = FAISS.from_documents(texts, embeddings)

            st.success("✅ Document indexed! Ask your questions below.")
            query = st.text_input("❓ Ask a question:")
            if query:
                docs = vectorstore.similarity_search(query)
                llm = ChatOpenAI(model_name="gpt-3.5-turbo")
                chain = load_qa_chain(llm, chain_type="stuff")
                response = chain.run(input_documents=docs, question=query)
                st.markdown("### 📄 Answer:")
                st.write(response)

if __name__ == "__main__":
    main()
