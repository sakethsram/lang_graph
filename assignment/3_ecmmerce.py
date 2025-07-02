from langgraph.graph import StateGraph, START, END
from lg_utility import save_graph_as_png
from typing import TypedDict
from random import randint

class State(TypedDict):
    stock: int
    payment:bool
    
def stock(state: State):
    print("tell me how much stock u need ?")
    state["stock"]=randint(0,1)
    return state

def stock_checker(state: State):
    if state["stock"]: return 1
    return 0

def add_to_cart(state:State):
    print("the stock item  has been added to the cart ")
    return state

def payment(state:State):
    t=randint(0,1)
    state['payment']=t

    return state

def payment_checker(state:State):
    if state['payment'] :return 1
    return 0

def confirmation(state:State):
    print("the order has been confirmed")
    return state

def order_placed(state:State):
    print("the order has been placed")
    return state

def order_cancelled(state:State):
    print("the order has been cancelled ")
    return state

def build_graph():
    builder = StateGraph(State)
    
    
    builder.add_node("STOCK", stock)
    builder.add_node("CART", add_to_cart)
    builder.add_node("PAY", payment)
    builder.add_node("CONF", confirmation)
    builder.add_node("PLACED", order_placed)
    builder.add_node("FAILED", order_cancelled)


    
    builder.add_edge(START, "STOCK")
    builder.add_conditional_edges("STOCK", stock_checker, {1: "CART", 0: "FAILED"})

    builder.add_edge("CART", "PAY")
    builder.add_conditional_edges("PAY", payment_checker, {1: "CONF", 0: "FAILED"})
    builder.add_edge("CONF", "PLACED")
    builder.add_edge("PLACED", END)
    builder.add_edge("FAILED", END)


    graph = builder.compile()

    save_graph_as_png(graph, __file__)
    return graph

graph = build_graph()

def main():
    response = graph.invoke({"stock": 0, "payment": False})
    print(f"📦 Response : {response}")

if __name__ == "__main__":
    main()
