from langgraph.graph import StateGraph, START, END
from lg_utility import save_graph_as_png
from typing import TypedDict
import random

class State(TypedDict):
    i: int
    cc: int

def inital(state: State):
    state = {
        "cc": state.get("cc", 0),
        "i": 0,
    }
    return state

def load(state: State):
    print("\nFINISHED LOADING THE FILES\n")
    return state  

def clean_up(state: State):
    r1 = random.randint(0, 1) 
    if r1:
        print("CLEAN IS SUCCESSFUL")
        state["cc"] = 1
    else:
        print("CLEANUP FAILED")
        state["cc"] = 0 
    return state  

def clean_check(state: State):
    if state["cc"] == 1:
        return "TRANSFORM"
    return "LOG"

def transform(state: State):
    print("\nFINISHED TRANSFORMING THE FILES\n")   
    return state  

def db(state: State):
    print("\nFINISHED SAVING TO THE DB\n")   
    return state

def log(state: State):
    print("\nSINCE THE CLEANING FAILED, LOGGING IS DONE\n")   
    return state 

def build_graph():
    builder = StateGraph(State)

    builder.add_node("INITIALISATION", inital)
    builder.add_node("LOAD", load)
    builder.add_node("CLEANUP", clean_up)
    builder.add_node("TRANSFORM", transform)
    builder.add_node("DB", db)
    builder.add_node("LOG", log)

    builder.add_edge(START, "INITIALISATION")
    builder.add_edge("INITIALISATION", "LOAD")
    builder.add_edge("LOAD", "CLEANUP")

    builder.add_conditional_edges("CLEANUP", clean_check, {
        "LOG": "LOG",
        "TRANSFORM": "TRANSFORM"
    })

    builder.add_edge("LOG", "DB")
    builder.add_edge("TRANSFORM", "DB")
    builder.add_edge("DB", END)

    graph = builder.compile()
    save_graph_as_png(graph, __file__)
    return graph

graph = build_graph()

def main():
    initial_state = {"i": 0, "cc": 0}
    
    result = graph.invoke(initial_state)
    
    print(result)

if __name__ == "__main__":
    main()
