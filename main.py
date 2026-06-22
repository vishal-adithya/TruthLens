from state import State
from langgraph.graph import START, END,StateGraph
from nodes.process import decompose_claim


if __name__ == "__main__":
    
    graph_builder = StateGraph(State)
    graph_builder.add_node("decompose_claim", decompose_claim)
    graph_builder.add_edge(START, "decompose_claim")
    graph_builder.add_edge("decompose_claim", END)
    graph = graph_builder.compile()

    final_state = graph.invoke({"TheClaim": "Transformers outperform RNNs on long sequence tasks"})
    print(final_state["DecomposedClaims"])
