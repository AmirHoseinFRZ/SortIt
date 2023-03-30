import copy

from State import State


class Problem:
    def __init__(self, *args):
        self.path_cost = [1, 1, 1, 1]
        if type(args[0]) == State:
            self.initState = args[0]
        else:
            self.initState = State(args[0], args[1])
        if type(args[-1]) == list:
            self.set_path_cost(args[-1])

    @staticmethod
    def is_goal(state: State) -> bool:  # this method check this state is goal or not
        for i in state.pipes:
            if not i.is_one_color() or (not (i.is_full() or i.is_empty())):
                return False
        return True

    # this method for every state gives every possible states form this self and return it
    def successor(self, state: State) -> list:
        child = []
        for i in range(len(state.pipes)):
            for j in range(len(state.pipes)):
                if i == j:
                    continue
                if not state.pipes[j].is_full() and not state.pipes[i].is_empty():
                    s = State(copy.deepcopy(state.pipes), state, self.get_cost_from_change(state, i), (i, j))
                    s.change_between_two_pipe(i, j)
                    child.append(State(copy.deepcopy(s.pipes), state, self.get_cost_from_change(state, i), (i, j)))
        return child

    def successor_ucs(self, state: State) -> list:
        child = []
        for i in range(len(state.pipes)):
            for j in range(len(state.pipes)):
                if i == j:
                    continue
                if not state.pipes[j].is_full() and not state.pipes[i].is_empty():
                    s = State(copy.deepcopy(state.pipes), state, self.get_cost_from_change_ucs(state, i, j), (i, j))
                    s.change_between_two_pipe(i, j)
                    child.append(s)
        return child

    def successor_a_star(self, state: State) -> list:
        child = []
        for i in range(len(state.pipes)):
            for j in range(len(state.pipes)):
                if i == j:
                    continue
                if not state.pipes[j].is_full() and not state.pipes[i].is_empty():
                    s = State(copy.deepcopy(state.pipes), state, self.get_cost_from_change_a_star(state, i, j), (i, j))
                    s.change_between_two_pipe(i, j)
                    child.append(s)
        return child
    @staticmethod
    def print_state(state: State):
        for i in state.pipes:
            i.print_pipe()

    @staticmethod
    def get_state_for_gui(state: State):
        out = ""
        for i in range(len(state.pipes)):
            out += 'p' + str(i + 1) + '=' + state.pipes[i].get_pipe_for_gui() + ','
        out = out[:len(out) - 1] + '\n'
        return out

    def get_cost_from_change(self, state: State, pipe_src_ind: int) -> int:
        if state.pipes[pipe_src_ind].stack[-1] == 'red':
            return state.g_n + self.path_cost[0]
        elif state.pipes[pipe_src_ind].stack[-1] == 'blue':
            return state.g_n + self.path_cost[1]
        elif state.pipes[pipe_src_ind].stack[-1] == 'green':
            return state.g_n + self.path_cost[2]
        elif state.pipes[pipe_src_ind].stack[-1] == 'yellow':
            return state.g_n + self.path_cost[3]

    @staticmethod
    def get_cost_from_change_ucs(state: State, pipe_src_ind: int, pipe_dest_ind: int) -> int:
        cost = abs(pipe_dest_ind - pipe_src_ind)
        return state.g_n + cost

    @staticmethod
    def get_cost_from_change_a_star(state: State, pipe_src_ind: int, pipe_dest_ind: int):
        src_pipe = state.pipes[pipe_src_ind]
        des_pipe = state.pipes[pipe_dest_ind]
        if src_pipe.color is None:
            if src_pipe.stack[-1] == des_pipe.color:
                if des_pipe.is_one_color():
                    return state.g_n - 2
                else:
                    for ball_ind in range(len(des_pipe.stack) - 1, -1, -1):
                        if des_pipe.stack[ball_ind] != des_pipe.color:
                            return state.g_n + len(des_pipe.stack) - ball_ind + 1
            else:
                return state.g_n + 1
        else:
            if src_pipe.is_one_color():
                return state.g_n + float('+inf')
            else:
                if src_pipe.stack[-1] == des_pipe.color:
                    if des_pipe.is_one_color():
                        return state.g_n - 2
                    else:
                        for ball_ind in range(len(des_pipe.stack) - 1, -1, -1):
                            if des_pipe.stack[ball_ind] != des_pipe.color:
                                return state.g_n + len(des_pipe.stack) - ball_ind + 1
                else:
                    return state.g_n + 1

    def set_path_cost(self, cost: list):
        self.path_cost = cost
