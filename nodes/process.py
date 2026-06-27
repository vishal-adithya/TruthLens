from state import State
from config import llm

def decompose_claim(state: State) -> State:
    claim = state["TheClaim"]
    prompt = f"""You are a research assistant helping verify a scientific claim.

Your job is to generate 1-3 short ArXiv search queries that would find 
papers to verify or refute this claim. Nothing else.

Output format: one search query per line, no bullets, no numbering, 
no explanation, no sub-claims. Just raw search queries.

Good example:
Claim: "Transformers outperform LSTMs on long sequences"
Output:
transformer long sequence performance NLP
LSTM vanishing gradient long range dependencies
transformer LSTM benchmark comparison

Bad example (do NOT do this):
- Sub-claim 1: There is a phenomenon...
- Sub-claim 2: This perceived sky...

Now generate queries for this claim: {claim}
"""
    responses = llm.invoke(prompt)
    response = responses.split("\n")

    return {"DecomposedClaims": response}