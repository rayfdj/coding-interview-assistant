from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

SYSTEM_TEMPLATE = "You're a competent and experienced {programming_language} programmer who is working on coding " \
                  "interview challenges. You'll be asked to solve a coding challenge in idiomatic {" \
                  "programming_language}, and where applicable, you need to provide a few alternatives, " \
                  "e.g.: iterative/recursive, complete with the space and time complexity analysis, as appropriate. " \
                  "Also provide ideas on how the solution can be optimized further."
HUMAN_TEMPLATE = "{text}"


def generate_solution(language: str, transcript: str) -> str:
    chat_open_ai = ChatOpenAI(temperature=0)
    system_message_prompt = SystemMessagePromptTemplate.from_template(SYSTEM_TEMPLATE)
    human_message_prompt = HumanMessagePromptTemplate.from_template(HUMAN_TEMPLATE)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    chain = LLMChain(llm=chat_open_ai, prompt=chat_prompt)
    result = chain.run(programming_language=language, text=transcript)
    print(result)
    return result
