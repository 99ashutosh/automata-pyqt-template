import graphviz
import pydot
import os

states=[]
def state_initial(c):
    if (c == ' '):
        dfa = 0
        states.append("q0");
    elif (c == 'a'):
        dfa = 1
        states.append("q0")
        states.append("q1")
    elif (c == 'b'):
        dfa = 4
        states.append("q0")
        states.append("q4")
    else:
        dfa = -1
        states.append("D")
    return dfa

def state1(c):
    if (c == 'a'):
        dfa = 2
        states.append("q2")
    elif (c == 'b'):
        dfa = 3
        states.append("q3")
    else:
        dfa = -1
        states.append("D")
    return dfa

def state2(c):
    if (c == 'a'):
        dfa = 1
        states.append("q1")
    elif (c == 'b'):
        dfa = 4
        states.append("q4")
    else:
        dfa = -1
        states.append("D")
    return dfa

def state3(c):
    if (c == 'a'):
        dfa = -1
        states.append("D")
    elif (c == 'b'):
        dfa = 4
        states.append("q4")
    else:
        dfa = -1
        states.append("D")
    return dfa

def state4(c):
    if (c == 'a'):
        dfa = -1
        states.append("D")
    elif (c == 'b'):
        dfa = 3
        states.append("q3")
    else:
        dfa = -1
        states.append("D")
    return dfa


class automata():
    def check_string(string):
        current_state=0
        l = len(string)
        for i in range(l):
            if (current_state==0):
                current_state = state_initial(string[i])
            elif (current_state==1):
                current_state = state1(string[i])
            elif (current_state==2):
                current_state = state2(string[i])
            elif (current_state==3):
                current_state = state3(string[i])
            elif (current_state==4):
                current_state = state4(string[i])
            else:
                return 0
        if (current_state == 0):
            return 1
        elif (current_state == 2):
            return 1
        elif (current_state == 3):
            return 1
        else:
            return 0

    def reset_states():
        states.clear()

    def get_last_transition():
        return states[-1]

    def gen_transition_png():
        d=0
        d = graphviz.Digraph()
        d.graph_attr['rankdir'] = 'LR'
        for i in states:
            d.node(i)

        for i in range(len(states)-1):
            if (i != len(states)):
                d.edge(states[i], states[i+1])
        d.render()
    
        (graph,) = pydot.graph_from_dot_file('Digraph.gv')
        os.remove('transition_history.png')
        graph.write_png('transition_history.png')
