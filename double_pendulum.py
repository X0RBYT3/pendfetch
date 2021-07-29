from math import pi, sin, cos, floor, copysign
from time import sleep
from datetime import datetime, timedelta
import curses
import sys, argparse, textwrap

# Not clean, but it works
# Board drawing functions


def draw_point(scr: curses.window, A: int, B: int, c: str):
    if A < 0 or B < 0 or A >= WIDTH / dW or B >= HEIGHT / dH:
        scr.addstr(6, 0, "Hello.")
        return
    scr.addstr(int(B), int(A), c)


def draw_line(scr: curses.window, A: float, B: float, C: float, D: float, c: str):

    if A > C:
        C, A = A, C
        D, B = B, D
    if B == D:
        for i in range(int(A), int(C) + 1):
            draw_point(scr, i, B, c)

    if A == C:
        mi = B
        ma = D
        if D < B:
            mi = D
            ma = B
        for i in range(int(mi), int(ma) + 1):
            draw_point(scr, A, i, c)
    if abs(D - B) < abs(C - A):
        plot_line_low(scr, A, B, C, D, c)
    else:
        if B > D:
            plot_line_high(scr, C, D, A, B, c)
        else:
            plot_line_high(scr, A, B, C, D, c)


def plot_line_low(
    scr: curses.window, x0: float, y0: float, x1: float, y1: float, c: str
):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1

    yi = copysign(1, dy)
    dy = abs(dy)
    D = 2 * dy - dx
    y = y0
    for x in range(int(x0), int(x1) + 1):
        draw_point(scr, x, y, c)
        if D > 0:
            y += yi
            D -= 2 * dx
        D += 2 * dy
        # scr.addstr(0,0,'f1')


def plot_line_high(
    scr: curses.window, x0: float, y0: float, x1: float, y1: float, c: str
):

    dx = x1 - x0
    dy = y1 - y0
    xi = 1

    xi = copysign(1, dx)
    dx = abs(dx)

    D = 2 * dx - dy
    x = x0

    for y in range(int(y0), int(y1) + 1):
        draw_point(scr, x, y, c)
        if D > 0:
            x += xi
            D -= 2 * dy
        D += 2 * dx


# Number of Pendulums to Simulate.
epsilon = 0.00001
g = 9.81  # Pfft, screw gravity.
l1, l2 = {}, {}  # Lengths
m1, m2 = {}, {}  # Masses
O1, O2 = {}, {}  # Angles
w1, w2 = {}, {}  # Angular Velocities

# Screen parameters
WIDTH = 1440
HEIGHT = 1200
dW = 14
dH = 40


def sim(n: int, trace: bool, length: float, mass: float):
    for i in range(n):
        # Define them all manually for that sweet chaos
        # Length
        l1[i] = length
        l2[i] = length
        # Mass
        m1[i] = mass
        m2[i] = mass
        # Original angle to be offset slightly

        O1[i] = 2.0 * pi / 2.0 + epsilon * (float(2 * i - n + 4))
        O2[i] = 2.0 * pi / 2.0
        ## Angular Velocity
        w1[i] = 0.0
        w2[i] = 0.0

    fps = 300.0
    dt = 1.0 / fps
    acc = 0.0
    frame_start = datetime.now()
    # Actually initialise window Now
    stdscr = curses.initscr()
    curses.resizeterm(HEIGHT, WIDTH)
    stdscr.clear()

    # Initialise board
    if trace:
        trace = [[0] * int(WIDTH / dW) for x in range(int(HEIGHT / dH))]
    # stdscr.addstr(floor(HEIGHT/dH)-1,floor(WIDTH/dW),'\0')
    # for x in range(floor(HEIGHT/dH)-1):
    #    stdscr.addstr(i,floor(WIDTH/dW),'\n')
    f = 0

    while True:
        f += 1
        current = datetime.now()
        acc += (current - frame_start) / timedelta(microseconds=1)
        frame_start = current
        if acc >= 1.0 / 30.0:
            acc = 1.0 / 30.0
        while acc > dt:
            for i in range(n):
                a1 = (
                    -g * (2 * m1[i] + m2[i]) * sin(O1[i])
                    - g * m2[i] * sin(O1[i] - 2 * O2[i])
                    - 2
                    * m2[i]
                    * sin(O1[i] - O2[i])
                    * (
                        w2[i] * w2[i] * l2[i]
                        + w1[i] * w1[i] * l1[i] * cos(O1[i] - O2[i])
                    )
                ) / (l1[i] * (2 * m1[i] + m2[i] - m2[i] * cos(2 * O1[i] - 2 * O2[i])))
                a2 = (
                    (2 * sin(O1[i] - O2[i]))
                    * (
                        w1[i] * w1[i] * l1[i] * (m1[i] + m2[i])
                        + g * (m1[i] + m2[i]) * cos(O1[i])
                        + w2[i] * w2[i] * l2[i] * m2[i] * cos(O1[i] - O2[i])
                    )
                    / l2[i]
                    / (2 * m1[i] + m2[i] - m2[i] * cos(2 * O1[i] - 2 * O2[i]))
                )
                ## Just trust them.
                w1[i] += 15 * dt * a1
                w2[i] += 15 * dt * a2
                O1[i] += 15 * w1[i] * dt
                O2[i] += 15 * w2[i] * dt
            acc -= dt
            if trace:
                for i in range(int(HEIGHT / dH)):
                    for j in range(int(WIDTH / dW)):
                        if trace[i][j] > 0:
                            trace[i][j] -= 1
        if not trace:
            stdscr.clear()
        for i in range(floor(HEIGHT / dH)):
            # for j in range(floor(WIDTH/dW)):
            #        stdscr.addstr(i,j,' ')
            for j in range(floor(WIDTH / dW)):
                if trace:
                    if stdscr.inch(i, j) == ord("@"):
                        #stdscr.addstr(6, 0, "Tracing")
                        trace[i][j] = fps
                    if trace[i][j] >= 3 * int(fps / 4):
                        stdscr.addstr(i, j, ":")
                    elif trace[i][j] >= 2 * int(fps / 4):
                        stdscr.addstr(i, j, ".")
                    elif trace[i][j] >= int(fps / 4):
                        if (i + j) % 2:
                            stdscr.addstr(i, j, ".")
                        else:
                            stdscr.addstr(i, j, " ")
                    else:
                        stdscr.addstr(i, j, " ")
                if i < int(HEIGHT / dH / 2):
                    draw_point(stdscr, WIDTH / 2 / dW, i, "|")
        for i in range(n):
            x1 = (WIDTH / 2 + sin(O1[i]) * l1[i] + dW * 0.5) / dW
            y1 = (cos(O1[i]) * l1[i] + dH * 0.5) / dH + HEIGHT / dH / 2
            x2 = x1 + (sin(O2[i]) * l2[i] + dW * 0.5) / dW
            y2 = y1 + (cos(O2[i]) * l2[i] + dH * 0.5) / dH
            if i % 2 == 0:
                draw_line(stdscr, WIDTH / 2 / dW, HEIGHT / dH / 2, x1, y1, "*")
                draw_line(stdscr, x1, y1, x2, y2, "*")
                # stdscr.addstr(0,0,'{} {} {} {}'.format(x1,y1,x2,y2))
                draw_point(stdscr, WIDTH / 2 / dW, HEIGHT / dH / 2, "O")
                draw_point(stdscr, x1, y1, "@")
                draw_point(stdscr, x2, y2, "@")
            else:
                draw_line(stdscr, WIDTH / 2 / dW, HEIGHT / dH / 2, x1, y1, ".")
                draw_line(stdscr, x1, y1, x2, y2, ".")
                draw_point(stdscr, WIDTH / 2 / dW, HEIGHT / dH / 2, "O")
                draw_point(stdscr, x1, y1, "@")
                draw_point(stdscr, x2, y2, "@")
        stdscr.addstr(
            0,
            0,
            "Flo's Double Pendulum. Number of Pendulums: {0},Time:{1}.".format(
                n, floor(f / 30)
            ),
        )
        stdscr.refresh()


def main(argv):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            """\
           Flo's Glorious Pendulum!
        --------------------------------
           Good luck solving this code
       Not even I know what half of it does
              Enjoy either way <3
                       """
        ),
    )
    parser.add_argument(
        "-t", "--trace", help="Enables tracing on pendulums", action="store_true"
    )
    parser.add_argument(
        "-p",
        "--pendulums",
        help="Number of Pendulums",
        action="store",
        type=int,
        default=1,
    )
    parser.add_argument(
        "-l",
        "--length",
        help="Length of arms",
        action="store",
        type=float,
        default=250.0,
    )
    parser.add_argument(
        "-m",
        "--mass",
        help="Mass of pendulums",
        action="store",
        type=float,
        default=100.0,
    )
    # parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,help=help_str)
    parser.print_help()
    args = parser.parse_args()
    # Because I'm an idiot and I made order matter (groan)
    v = vars(args)
    OPTIONS = [v["pendulums"], v["trace"], v["length"], v["mass"]]
    print(
        "Running with {0} Pendulums, Trace set to {1}, Length of {2} and Mass of {3} ".format(
            *OPTIONS
        )
    )
    sleep(2)
    sim(*OPTIONS)


if __name__ == "__main__":
    main(sys.argv[1:])
