from langgraph.graph import StateGraph, START, END
from lg_utility import save_graph_as_png
from typing import TypedDict

class State(TypedDict):
    name:str
    marks:int
    output:bool

def pass_or_fail(state: State):
    print("📘 Checking pass or fail status")
    print(f"👤 Name  : {state['name']}")
    print(f"📝 Marks : {state['marks']}")

    if state["marks"] > 34:
        state["output"] = True
        print("✅ Result: Passed")
    else:
        state["output"] = False
        print("❌ Result: Failed")

    return state

def build_graph():
    builder = StateGraph(State)
    
    builder.add_node("passorfail", pass_or_fail)

    builder.add_edge(START, "passorfail")
    builder.add_edge("passorfail", END)

    graph = builder.compile()

    save_graph_as_png(graph, __file__)

    return graph


graph = build_graph()
    

def main():
    response = graph.invoke({"name": "Saketh", "marks": 35})
    print(f"📦 Response : {response}")
    print(f"🎯 Output   : {response['output']}")
    print()
if __name__ == "__main__":
    main()
