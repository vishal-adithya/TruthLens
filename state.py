from langgraph.graph import StateGraph
from typing import Annotated,TypedDict

class State(TypedDict):
    TheClaim: str
    DecomposedClaims: list[str]
    FetchedPapers: list[dict]