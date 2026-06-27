from state import State
from config import llm


import arxiv

def fetch_papers(state: State) -> State:
    queries = state["DecomposedClaims"]
    client = arxiv.Client()
    docs = []

    for query in queries:

        search = arxiv.Search(
            query=queries,
            max_results=2,
            sort_by=arxiv.SortCriterion.Relevance,
            sort_order=arxiv.SortOrder.Descending
        )
        for result in client.results(search):
            docs.append({"abstract": result.summary, "source": result.entry_id})
    return {"FetchedPapers": docs}
        