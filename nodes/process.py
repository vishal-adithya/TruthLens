from state import State
from config import llm

def decompose_claim(state: State) -> State:
    claim = state["TheClaim"]

