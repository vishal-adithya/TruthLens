from langgraph.graph import StateGraph
from typing import Annotated,TypedDict

class State(TypedDict):
    query: str