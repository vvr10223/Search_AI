from langgraph.graph import StateGraph, START, END
from .websearch import websearch
from .webstate import webstate
from .planner_chain import planner_chain
from .replanner_chain import replanner_chain
def plan_step(state: webstate):
    input = state.input
    plan = planner_chain.invoke(input)['plan']
    #print(plan)
    state.plan = plan
    #print("planner\n", state)
    #print()
    return state

def replan_step(state:webstate):
    result = replanner_chain.invoke({
        "input": state.input,
        "plan": state.plan,
        "past_steps": state.past_steps
    })

    if result['action_type'] == "response":
        # Complete - set final response
        final_answer=result['response']
        state.response = final_answer
        #print("replanner\n",state)
        #print()
    else:  # action_type == "plan"
        # Continue - update plan
        #print(result['plan'])
        state.plan = result['plan']
        #print("replanner\n",state)
        #print()

    return state

def execute_plan(state:webstate):
    plan = state.plan
    task = plan[0]
    web_response = websearch(task)
    state.past_steps.append((task, web_response))
    #print("execute\n",state)
    #print()
    return state

def should_end(state: webstate):
    if state.response:
        return END
    else:
        return "websearch"

workflow = StateGraph(webstate)
workflow.add_node("planner", plan_step)
workflow.add_node("websearch", execute_plan)
workflow.add_node("replan", replan_step)

workflow.add_edge(START, "planner")
workflow.add_edge("planner", "websearch")
workflow.add_edge("websearch", "replan")
workflow.add_conditional_edges("replan", should_end, ["websearch", END])

graph = workflow.compile()

def webagent(query:str):
    output=graph.invoke({'input': query, 'response': ""})
    #print(output['response'])
    return output['response']
if __name__ == "__main__":
    output=webagent('latest ai news')
    print(output)
