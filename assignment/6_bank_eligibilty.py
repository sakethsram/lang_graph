from langgraph.graph import StateGraph, START, END
from lg_utility import save_graph_as_png
from typing import TypedDict

class State(TypedDict):
    age: int
    sal:int
    cc:int
    path:bool
    res:bool
def inital(state: State):
    state = {
        "age": state.get("age", 0),
        "salary": state.get("sal", 0),
        "cc": state.get("cc", 0),
        "path": state.get("path", True)
    }
    return state

def age(state: State):
    return {**state, "path": False if state["age"] < 22 else True}    

def sal(state: State):
    return {**state, "path": False if state["sal"] < 25000 else True}    


def cc(state: State):
    return {**state, "path": False if state["cc"] < 651 else True}    


def acc(state:State):
    state["res"] =1
    return state

def rej(state:State):
    state["res"] =0
    return state

def age_check(state: State):
     return "REJ" if not state["path"] else "SALARY"

def sal_check(state: State):
     return "REJ" if not state["path"] else "CC"

def cc_check(state: State):
     return "REJ" if not state["path"] else "ACC"

def build_graph():
    builder = StateGraph(State)

    builder.add_node("INITIALISATION", inital)
    
    builder.add_node("AGE", age)
    builder.add_node("SALARY", sal)
    builder.add_node("CC", cc)
    
    builder.add_node("ACC", acc)
    builder.add_node("REJ", rej)

    builder.add_edge(START, "INITIALISATION")
    builder.add_edge("INITIALISATION", "AGE")
    builder.add_edge("REJ", END)
    builder.add_edge("ACC", END)

    builder.add_conditional_edges("AGE", age_check,{"REJ":"REJ","SALARY":"SALARY"})
    builder.add_conditional_edges("SALARY",sal_check,{"REJ": "REJ","CC":"CC"})
    builder.add_conditional_edges("CC", cc_check, {"REJ":"REJ","ACC":"ACC"})
    
    

    
    graph = builder.compile()

    save_graph_as_png(graph, __file__)
    return graph

graph = build_graph()

def main():
    input_state = {
        "age": 25,
        "sal": 30000,
        "cc": 700,
        "path": True,
        "res": False
    }

    response = graph.invoke(input_state)
    print(f"📦 Final State : {response}")

    if response["res"]:
        print("✅ Application Accepted")
    else:
        print("❌ Application Rejected")

if __name__ == "__main__":
    main()
