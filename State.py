# this class only for the first time setup init state for problem and is given to every search
class State:
    def __init__(self, pipes: list, parent, g_n: int, prev_action: tuple):
        self.pipes = pipes
        self.parent = parent
        self.g_n = g_n
        self.prev_action = prev_action
        self.h_n = self.get_h_n()

    def change_between_two_pipe(self, pipe_src_ind: int, pipe_dest_ind: int):
        self.pipes[pipe_dest_ind].add_ball(self.pipes[pipe_src_ind].remove_ball())

    def __hash__(self):
        hash_strings = []
        for i in self.pipes:
            hash_strings.append(i.__hash__())
        hash_strings = sorted(hash_strings)
        hash_string = ''
        for i in hash_strings:
            hash_string += i + '###'
        return hash_string

    def get_h_n(self):
        h = 0
        is_same = True
        for pipe in self.pipes:
            if len(pipe.stack) >= 2:
                for i in range(len(pipe.stack) - 1):
                    if is_same:
                        if pipe.stack[i] != pipe.stack[i + 1]:
                            is_same = False
                            h += 1
                    else:
                        h += 1
            elif len(pipe.stack) == 1:
                h += 1
        return h
