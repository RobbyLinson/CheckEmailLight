from langchain_anthropic import ChatAnthropic
from src.schema import InboxDigest
from langchain_core.prompts import ChatPromptTemplate

model = ChatAnthropic(model_name="claude-haiku-4-5-20251001", timeout=None, stop=None)
structured_model = model.with_structured_output(InboxDigest)

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You catch someone up on their inbox after time away. "
     "Given a list of emails, each with a sentiment signal, produce a single "
     "digest: an overall summary of what happened, which emails need attention "
     "and why, and a consolidated to-do list."),
    ("human", "Here are the emails with sentiment signals:\n\n{emails}")
])
chain = prompt | structured_model

def generate_briefing(analyzed_emails: list):
    result = chain.invoke({"emails": analyzed_emails})
    return result
