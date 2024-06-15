import argparse
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from rag_get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"
LLM_MODEL = "llama3"

PROMPT_TEMPLATE = """
Contesta la pregunta basándote solo en el siguiente contexto:

{context}

---

Contesta la pregunta en idioma español, basada en el contexto proporcionado arriba: {question}
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)

def query_rag(query_text: str):
    # TODO Redefinir pregunta

    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=10)

    # TODO Evaluar chunks para utilizar los más relevantes

    # Create prompt
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # Send ask to model
    model = Ollama(model="llama3")
    response_text = model.invoke(prompt)

    # Format model response
    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"\n\n##### Respuesta:\n\n{response_text}\n\n##### Documentos fuente:\n\n"
    print(formatted_response)
    
    # Filter results to get the filenames only
    filtered_sources = []
    for it in sources:
       index1 = it.index("/") + 1
       index2 = it[0:it.rindex(":")].rindex(":")
       docName = it[index1:index2]
       if(filtered_sources.count(docName) == 0):
           filtered_sources.append(docName)
           print(docName)
    
    print("\n\n")

    return { 
        "respuesta": response_text,   
        "fuentes": filtered_sources      
    }

if __name__ == "__main__":
    main()