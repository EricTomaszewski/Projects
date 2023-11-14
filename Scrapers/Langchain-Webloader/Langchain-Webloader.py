# pip install openai langchain

# https://python.langchain.com/docs/integrations/document_loaders/web_base

from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain

url = "https://www.itoma.co.uk/"

# https://python.langchain.com/docs/integrations/document_loaders/web_base
loader = WebBaseLoader(url)
docs = loader.load()

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
chain = load_summarize_chain(llm, chain_type="stuff")

summary = chain.run(docs)

print(summary)