from langgraph.graph import StateGraph, START, END
from lg_utility import save_graph_as_png
from typing import TypedDict

class State(TypedDict):
    val=int
    is_even=bool
    is_odd=bool
    is_prime=bool

def inital(state: State):
    return {"value": state.get("value", 0),"is_even": 0,"is_odd": 0,"is_prime": 0}

def is_even(state: State):
    if state["val"]%2==0:state["is_even"]=1
    else:state["is_even"]= 0
    return state
def is_odd(state: State):
    if state["val"]%2==1:state["is_odd"]=1
    else:state["is_odd"]= 0
    return state

def is_prime(state:State):
    n= state["val"]
    t=0
    for i in range(1,n+1):
        if n%i==0:t=t+1
    
    if(t>2): state["is_prime"]=0
    else:state["is_prime"]=1
    return state

def build_graph():
    builder = StateGraph(State)
    
    builder.add_node("intialisation", inital)
    builder.add_node("even?", is_even)
    builder.add_node("odd?", is_odd)
    builder.add_node("prime?", is_prime)


    builder.add_edge(START, "intialisation")
    builder.add_edge("prime", END)

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
