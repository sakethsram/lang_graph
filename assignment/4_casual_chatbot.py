from langgraph.graph import StateGraph, START, END
from lg_utility import save_graph_as_png
from typing import TypedDict

class State(TypedDict):
    ans: int
    response:str

def inital(state: State):
    print("enter your ans for the bot")
    print("1. casual 2.Intent_Detection  3.📚 FAQ 4. 😄 Small_Talk")
    return state

def bot_selector(state: State):
    if state["ans"] == 1: return  "casual"
    
    elif state["ans"] == 2:return  "intent_detection"
    
    elif state["ans"] == 3: return  "faq"
    
    elif state["ans"] == 4: return  "small_talk"

def casual(state: State):
   state["response"]="tell me wasssup , you have reached the casual bot "
   return state

def intent_detection(state: State):
   state["response"]="HI HOW MAY I FIGURE OUT UR INTENT , U HAVE REACHED THE INTENTDETECTION "
   return state

def faq(state: State):
   state["response"]="what did u buy and what is ur problem ? "
   return state

def Small_Talk(state: State):
   state["response"]="YP WADDUP , U HAVE REACHED THE Small_Talk "
   return state

    
def build_graph():
    builder = StateGraph(State)

    builder.add_node("INITIALISATION", inital)
    builder.add_node("FAQ", faq)
    builder.add_node("INTENT", intent_detection)
    builder.add_node("CASUAL", casual)
    builder.add_node("SMALL_TALK", Small_Talk)

    builder.add_edge(START, "INITIALISATION")

    builder.add_conditional_edges("INITIALISATION", bot_selector, {"casual": "CASUAL","intent_detection": "INTENT","faq": "FAQ",  "small_talk": "SMALL_TALK"})
    builder.add_edge("CASUAL", END)
    builder.add_edge("INTENT", END)
    builder.add_edge("FAQ", END)
    builder.add_edge("SMALL_TALK", END)


    graph = builder.compile()

    save_graph_as_png(graph, __file__)
    return graph

graph = build_graph()

def main():
    response = graph.invoke({"ans": 3, "response": ""})
    print(f"📦 Response : {response}")
    print()

if __name__ == "__main__":
    main()
