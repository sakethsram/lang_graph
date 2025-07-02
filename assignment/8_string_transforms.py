from langgraph.graph import StateGraph, START, END
from lg_utility import save_graph_as_png
from typing import TypedDict
import random
from datetime import datetime


class State(TypedDict):
    i:int
    s: str
    

def ini(state: State):
    state = {"s": state.get("s"),"i":state.get("i", 0)}
    return state

def check(State:State):
        if State["i"] == 1: return  "UP"
        
        elif State["i"] == 2:return  "TIME"
        
        elif State["i"] == 3: return  "REV"
        
    

def up(state: State):
    state["s"]=state["s"].upper()
    return state  

def time(state: State):

    state["s"] = datetime.now().strftime("%H:%M:%S")
    return state  

def rev(state: State):
    state["s"] = state["s"][::-1]
    return state


def build_graph():
    builder = StateGraph(State)

    builder.add_node("INI", ini)
    builder.add_node("UP", up)
    builder.add_node("TIME", time)
    builder.add_node("REV", rev)


    builder.add_edge(START, "INI")

    builder.add_conditional_edges("INI", check, {"UP": "UP","REV": "REV",  "TIME": "TIME"})
    builder.add_edge("UP", END)
    builder.add_edge("REV", END)
    builder.add_edge("TIME", END)

    graph = builder.compile()
    save_graph_as_png(graph, __file__)
    return graph

graph = build_graph()

def main():
    t= { "s": "hi how are you","i":random.randint(1,3)}
    result = graph.invoke(t)
    
    print(result)

if __name__ == "__main__":
    main()
