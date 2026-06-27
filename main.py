from state import State
from langgraph.graph import START, END,StateGraph
from nodes.process import decompose_claim
from nodes.rag import fetch_papers

if __name__ == "__main__":
    
    graph_builder = StateGraph(State)
    graph_builder.add_node("decompose_claim", decompose_claim)
    graph_builder.add_node("fetch_papers", fetch_papers)

    graph_builder.add_edge(START, "decompose_claim")
    graph_builder.add_edge("decompose_claim", "fetch_papers")
    graph_builder.add_edge("fetch_papers", END)
    
    graph = graph_builder.compile()

    final_state = graph.invoke({"TheClaim": "The Sky is blue"})
    print(final_state["DecomposedClaims"])
    print("================================================")
    print(final_state["FetchedPapers"])
    print("================================================")
