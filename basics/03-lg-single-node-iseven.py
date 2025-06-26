from langgraph.graph import StateGraph, START, END
from lg_utility import save_graph_as_png
from typing import TypedDict

class State(TypedDict):
    value: int
    is_even: bool
    output: str

def initialize_state_defaults(state: dict):
    return {
        "value": state.get("value", 0),
        "is_even": False,
        "output": None
    }

def is_even(state: State):
    if state["value"] % 2 == 0:
        state["is_even"] = True
    else:
        state["is_even"] = False
        
    return state

def build_output(state: State):
    if state['is_even']:
        tstr = f"{state['value']} is Even number"
    else:
        tstr = f"{state['value']} is Odd number"
        
    state["output"] = tstr
    return state

def build_graph():
    builder = StateGraph(State)
    
    builder.add_node("INITIALIZER", initialize_state_defaults)
    builder.add_node("EVEN_ODD", is_even)
    builder.add_node("OUTPUT", build_output)

    builder.add_edge(START, "INITIALIZER")
    builder.add_edge("INITIALIZER", "EVEN_ODD")
    builder.add_edge("EVEN_ODD", "OUTPUT")
    builder.add_edge("OUTPUT", END)

    graph = builder.compile()

    save_graph_as_png(graph, __file__)

    return graph


graph = build_graph()
    

def main():
    response = graph.invoke({"value": 10})
    print(f"Response :{response}")
    print(f"Output   :{response['output']}")
    print()
    
if __name__ == "__main__":
    main()
