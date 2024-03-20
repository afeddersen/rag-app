import os
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import bs4
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from pathlib import Path
from langchain_community.document_loaders import UnstructuredMarkdownLoader

#### INDEXING ####

# Assuming markdown_dir is a Path object pointing to the directory
markdown_dir = Path("/Users/afeddersen/github/rag-app/artifacts")
markdown_files = list(markdown_dir.glob("*.md"))  # This will get all markdown files in the directory

docs = []
for markdown_file in markdown_files:
    loader = UnstructuredMarkdownLoader(str(markdown_file))
    docs.extend(loader.load())

os.environ["OPENAI_API_KEY"] = ""

text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
texts = text_splitter.split_documents(docs)

# After loading the documents, check if docs is not empty
if not docs:
    raise ValueError(
        "No documents were loaded. Please check the loader configuration and the URLs."
    )

# Debug: Print the first 500 characters of each document to verify content
for doc in docs:
    text_content = doc.text if hasattr(doc, "text") else str(doc)
    print(text_content[:500], "\n\n---\n\n")

# Check if texts is not empty after splitting
if not texts:
    raise ValueError(
        "Text splitting resulted in an empty list. Please check the text splitter configuration."
    )

embeddings = OpenAIEmbeddings()
# Set the persist directory to the current working directory
persist_directory = os.getcwd()
vectordb = Chroma.from_documents(
    documents=texts, embedding=embeddings, persist_directory=persist_directory
)
vectordb.persist()

retriever = vectordb.as_retriever(search_kwargs={"k": 3})
llm = ChatOpenAI(model_name="gpt-4")

qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

query = """I'm working on STIGs for Wolfi OS and Chainguard Images.  Can you confirm that I'm compliant based on what you know.  If so, can you provide a shell script to help me validate the configuration is correct?
The operating system must provide automated mechanisms for supporting account management functions.	"Enterprise environments make account management challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other errors.

A comprehensive account management process that includes automation helps to ensure accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended or terminated, or by disabling accounts located in non-centralized account stores such as multiple servers. This requirement applies to all account types, including individual/user, shared, group, system, guest/anonymous, emergency, developer/manufacturer/vendor, temporary, and service.

The automated mechanisms may reside within the operating system itself or may be offered by other infrastructure providing automated account management capabilities. Automated mechanisms may be composed of differing technologies that, when placed together, contain an overall automated mechanism supporting an organization's automated account management requirements.

Account management functions include: assigning group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to automatically notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephonic notification to report atypical system account usage."""

llm_response = qa(query)
print(llm_response["result"])



