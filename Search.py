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

    @staticmethod
    def ucs(prb: Problem) -> Solution:
        start_time = datetime.now()
        queue = []
        state = prb.initState
        queue.append(state)
        while len(queue) > 0:
            # print(list(map(lambda s: s.g_n, queue)), len(queue))
            queue.sort(key=lambda st: st.g_n)
            state = queue.pop(0)
            neighbors = prb.successor_ucs(state)
            for c in neighbors:
                if prb.is_goal(c):
                    print(c.g_n)
                    return Solution(c, prb, start_time)
                queue.append(c)
        return None

    @staticmethod
    def a_star(prb: Problem) -> Solution:
        start_time = datetime.now()
        queue = []
        state = prb.initState
        print(state.h_n)
        for p in state.pipes:
            print(p.color)
            print(p.stack)
        for i in state.pipes:
            i.print_pipe()
        queue.append(state)
        min = 20
        while len(queue) > 0:
            queue.sort(key=lambda st: st.h_n)
            state = queue.pop(0)
            if prb.is_goal(state):
                print(state.g_n)
                return Solution(state, prb, start_time)
            if state.h_n < min:
                min = state.h_n
                print(state.h_n)
                print(state.get_h_n())
                for p in state.pipes:
                    # print(p.color)
                    print(p.stack)
            neighbors = prb.successor(state)
            # for s in neighbors:
            #     print(s.h_n)
            #     for p in s.pipes:
            #         print(p.color)
            #         print(p.stack)
            for c in neighbors:
                if prb.is_goal(c):
                    print(c.g_n)
                    return Solution(c, prb, start_time)
                queue.append(c)
        return None


