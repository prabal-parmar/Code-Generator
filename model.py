from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def generate_response(question: str, language: str):
    load_dotenv()
    llm = ChatGroq(model="llama3-8b-8192", temperature=0)

    system_prompt = SystemMessagePromptTemplate.from_template("""
                                                            You are a helpful AI agent who anwer only coding questions.
                                                            You help user by answering code for the question which user ask you.
                                                            User has asked you to answer the question in {language} language only.
                                                            If question is not about code then don't interact just answer in code.
                                                            """)

    human_prompt = HumanMessagePromptTemplate.from_template("""Give well structured code for {question}""")

    prompt = ChatPromptTemplate.from_messages([
        (system_prompt),
        (human_prompt)
    ])

    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"question": question, "language": language})

    return response