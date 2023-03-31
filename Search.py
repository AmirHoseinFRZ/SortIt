from Solution import Solution
from Problem import Problem
from datetime import datetime


class Search:
    @staticmethod
    def bfs(prb: Problem) -> Solution:
        start_time = datetime.now()
        queue = []
        state = prb.initState
        queue.append(state)
        while len(queue) > 0:
            state = queue.pop(0)
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                queue.append(c)
        return None

    # blind searches
    @staticmethod
    def dfs(prb: Problem) -> Solution:
        print("DFS - Depth First Search")
        start_time = datetime.now()
        stack = []
        state = prb.initState
        stack.append(state)
        while len(stack) > 0:
            state = stack.pop(-1)  # index 0 is bottom of stack and index -1 is top of stack
            neighbors = prb.successor(state)
            for neighbor in neighbors[::-1]:  # the rightmost node is add first.
                # the leftmost node is add last.
                # we visited the leftmost node first.
                if prb.is_goal(neighbor):
                    return Solution(neighbor, prb, start_time)
                stack.append(neighbor)
        return None

    @staticmethod
    def modified_dfs(prb: Problem) -> Solution:
        print("modified DFS - modified Depth First Search")
        visited = []
        start_time = datetime.now()
        stack = []
        state = prb.initState
        stack.append(state)
        while len(stack) > 0:
            state = stack[-1]
            visited.append(stack.pop(-1))
            neighbors = prb.successor(state)
            for neighbor in neighbors[::-1]:
                if prb.is_goal(neighbor):
                    return Solution(neighbor, prb, start_time)

                for item in visited:
                    if item.__hash__() == neighbor.__hash__():
                        break
                else:
                    stack.append(neighbor)
        return None

    @staticmethod
    def ids(prb: Problem) -> Solution:
        print("IDS - Iterative Deepening Search")
        start_time = datetime.now()
        cutoff = 0
        while cutoff < 20:
            visited = []
            stack = []
            state = prb.initState
            stack.append(state)
            while len(stack) > 0:
                state = stack[-1]
                if state.g_n <= cutoff - 1:
                    visited.append(stack.pop(-1))
                    neighbors = prb.successor(state)
                    for neighbor in neighbors[::-1]:
                        if prb.is_goal(neighbor):
                            return Solution(neighbor, prb, start_time)
                        for item in visited:
                            if item.__hash__() == neighbor.__hash__():
                                break
                        else:
                            stack.append(neighbor)
                else:
                    stack.pop(-1)
            cutoff += 1
        return None

    @staticmethod
    def ucs(prb: Problem) -> Solution:
        print("UCS - Uniform Cost Search")
        start_time = datetime.now()
        queue = []
        state = prb.initState
        queue.append(state)
        while len(queue) > 0:
            queue.sort(key=lambda st: st.g_n)
            state = queue.pop(0)
            neighbors = prb.successor_ucs(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                queue.append(c)
        return None

    #  Heuristic Methods

    @staticmethod
    def a_star(prb: Problem) -> Solution:
        print("A Star - A*")
        start_time = datetime.now()
        queue = []
        state = prb.initState
        queue.append(state)
        while len(queue) > 0:
            queue.sort(key=lambda st: st.h_n + st.g_n)
            state = queue.pop(0)
            print(f"{state.h_n} + {state.g_n} = {state.h_n + state.g_n}")
            if prb.is_goal(state):
                return Solution(state, prb, start_time)
            neighbors = prb.successor_a_star(state)
            for c in neighbors:
                queue.append(c)
        return None

    @staticmethod
    def ida_star(prb: Problem) -> Solution:
        print("ida_star - Iterative Deepening A*")
        start_time = datetime.now()
        state = prb.initState
        cutoff = state.f_n()

        while state.f_n() <= cutoff:
            min_cutoff = float("inf")
            stack = [state]
            while len(stack) > 0:
                state = stack.pop(-1)
                if prb.is_goal(state):
                    return Solution(state, prb, start_time)
                if state.f_n() <= cutoff:
                    neighbors = prb.successor_a_star(state)
                    for neighbor in neighbors:
                        if neighbor.f_n() <= cutoff:
                            stack.append(neighbor)
                        else:
                            if neighbor.f_n() < min_cutoff:
                                min_cutoff = neighbor.f_n()
                                print(f"{min_cutoff} - {cutoff} - {neighbor.g_n} - {neighbor.h_n}")
            cutoff = min_cutoff
            state = prb.initState
        return None