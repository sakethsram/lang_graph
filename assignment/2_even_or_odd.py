from langgraph.graph import StateGraph, START, END
from lg_utility import save_graph_as_png
from typing import TypedDict

class State(TypedDict):
    val: int
    is_even: bool
    is_odd: bool
    is_prime: bool

def inital(state: State):
    return {"val": state.get("val", 0), "is_even": False, "is_odd": False, "is_prime": False}

def is_even(state: State):
    state["is_even"] = state["val"] % 2 == 0
    return state

def is_odd(state: State):
    state["is_odd"] = state["val"] % 2 == 1
    return state

def is_prime(state: State):
    n = state["val"]
    if n <= 1:state["is_prime"] = False
    else:state["is_prime"] = all(n % i != 0 for i in range(2, int(n**0.5)+1))
    return state

def build_graph():
    builder = StateGraph(State)

    builder.add_node("INITIALISATION", inital)
    builder.add_node("EVEN", is_even)
    builder.add_node("ODD", is_odd)
    builder.add_node("PRIME", is_prime)

    builder.add_edge(START, "INITIALISATION")
    builder.add_edge("INITIALISATION", "EVEN")
    builder.add_edge("EVEN", "ODD")
    builder.add_edge("ODD", "PRIME")
    builder.add_edge("PRIME", END)

    graph = builder.compile()

    save_graph_as_png(graph, __file__)
    return graph

graph = build_graph()

def main():
    response = graph.invoke({"val": 35})
    print(f"📦 Response : {response}")
    print()

if __name__ == "__main__":
    main()
