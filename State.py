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
        colors = {'red': 0, 'blue': 0, 'green': 0, 'yellow': 0}
        for pipe in self.pipes:
            for ball in pipe.stack:
                colors[ball] += 1
        number_of_balls = sum(colors.values())
        for color in colors:
            n = colors[color] / self.pipes[0].limit
            for pipe in self.pipes:
                if n == 0 and color == pipe.color:
                    pipe.color = None
                if color == pipe.color:
                    n -= 1
        for pipe in self.pipes:
            if pipe.color is not None:
                for ball in range(len(pipe.stack)):
                    if pipe.stack[ball] != pipe.color:
                        h += len(pipe.stack) - ball
            elif pipe.color is None:
                h += len(pipe.stack)
        return h

    def f_n(self):
        return self.g_n + self.h_n
