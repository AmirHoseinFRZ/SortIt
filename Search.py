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
    def ucs(prb: Problem) -> Solution:
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

    @staticmethod
    def a_star(prb: Problem) -> Solution:
        start_time = datetime.now()
        queue = []
        state = prb.initState
        queue.append(state)
        while len(queue) > 0:
            queue.sort(key=lambda st: st.h_n + st.g_n)
            state = queue.pop(0)
            if prb.is_goal(state):
                return Solution(state, prb, start_time)
            neighbors = prb.successor_a_star(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                queue.append(c)
        return None
