# this class only for the first time setup init state for problem and is given to every search
class State:
    def __init__(self, pipes: list, parent, g_n: int, prev_action: tuple):
        self.pipes = pipes
        self.pipes.sort(key=lambda pipe: pipe.maximum_same_ball_color)
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
        # for i in range(number_of_balls / self.pipes[0].limit):
        for color in colors:
            for pipe in self.pipes:
                if pipe.color == color:
                    colors[color] -= pipe.maximum_same_ball_color
                    if colors[color] == 0:
                        break
                else:
                    for ball in range(len(pipe.stack)):
                        if pipe.stack[ball] == color:
                            colors[color] -= 1
                            h += len(pipe.stack) - ball
        return h

