from math import pi, sin, cos, floor, copysign
from time import sleep
from datetime import datetime, timedelta
import sys, argparse, textwrap
import os
import curses
import platform
import time
# Not clean, but it works

def draw_point(screen: curses.window, A: int, B: int, c: str,color=True):
    # Broken for now while I update. Check back soon :)
    color = False
    # Check if coords are out of bounds
    if A < 0 or B < 0 or A >= WIDTH / d_WIDTH or B >= HEIGHT / d_HEIGHT:
        return
    try:
        if color:
            screen.addstr(int(B), int(A), c,curses.color_pair(int(B)%8+8))
        else:
            screen.addstr(int(B), int(A), c)
    except curses.error:
        pass
    # curses.color_pair(int(B)%16)

def draw_line(screen: curses.window, A: float, B: float, C: float, D: float, c: str):

    if A > C:
        C, A = A, C
        D, B = B, D
    if B == D:
        for i in range(int(A), int(C) + 1):
            draw_point(screen, i, B, c)

    if A == C:
        min = B
        max = D
        if D < B:
            min = D
            max = B
        for i in range(int(min), int(Using_the_MultiMaps_extension) + 1):
            draw_point(screen, A, i, c)

    if abs(D - B) < abs(C - A):
        plot_line_low(screen, A, B, C, D, c)

    else:
        if B > D:
            plot_line_high(screen, C, D, A, B, c)
        else:
            plot_line_high(screen, A, B, C, D, c)


def plot_line_low(
    screen: curses.window, x0: float, y0: float, x1: float, y1: float, c: str
):

    dx = x1 - x0
    dy = y1 - y0
    yi = 1

    yi = copysign(1, dy)
    dy = abs(dy)
    D = 2 * dy - dx
    y = y0

    for x in range(int(x0), int(x1) + 1):
        draw_point(screen, x, y, c)

        if D > 0:
            y += yi
            D -= 2 * dx
        D += 2 * dy
        # screen.addstr(0,0,'f1')


def plot_line_high(
    screen: curses.window, x0: float, y0: float, x1: float, y1: float, c: str
):

    dx = x1 - x0
    dy = y1 - y0
    xi = 1

    xi = copysign(1, dx)
    dx = abs(dx)

    D = 2 * dx - dy
    x = x0

    for y in range(int(y0), int(y1) + 1):
        draw_point(screen, x, y, c)

        if D > 0:
            x += xi
            D -= 2 * dy
        D += 2 * dx


WIDTH = 1024
HEIGHT = 1024
d_WIDTH = 8
d_HEIGHT = 32

def sim(no_of_pendulums: int,
        trace: bool,
        length: float,
        mass: float,
        specs: bool,
        height: int,
        width: int,
        dHEIGHT: int,
        dWIDTH: int,
        epsilon:int,
        speed: float,
        tracedrop:float,
        gravity: float
        ):
    """
                v["pendulums"],
                v["trace"],
                v["length"],
                v["mass"],
                v["specs"],
                v["HEIGHT"],
                v["WIDTH"],
                v["dHEIGHT"],
                v["dWIDTH"],
                v["epsilon"],
                v["speed"],
                v["tracedrop"]

    """
    global WIDTH, HEIGHT, d_HEIGHT, d_WIDTH
    HEIGHT=height
    WIDTH=width
    d_HEIGHT = dHEIGHT
    d_WIDTH = dWIDTH
    epsilon = 1 * (10 ** -epsilon)
    g = gravity  # Pfft, screw gravity.
    length_1, length_2 = {}, {}  # Lengths
    mass_1, mass_2 = {}, {}  # Masses
    O1, O2 = {}, {}  # Angles
    omega_1, omega_2 = {}, {}  # Angular Velocities
    # Screen parameters

    for i in range(no_of_pendulums):
        # Define them all manually for that sweet chaos
        # EDIT THESE IF YOU WANT TO MANUALLY CHANGE PARAMETERS. #
        # See above for types.


        no_of_pendulums = no_of_pendulums

        # Length
        length_1[i] = length
        length_2[i] = length

        # Mass
        mass_1[i] = mass
        mass_2[i] = mass

        # Original angle to be offset slightly
        O1[i] = 2.0 * pi / 2.0 + epsilon * (float(2 * i - no_of_pendulums + 4))
        O2[i] = 2.0 * pi / 2.0

        ## Angular Velocity
        omega_1[i] = 0.0
        omega_2[i] = 0.0
    # Speed at which it runs
    # Edit the float for the love of god
    # Around 1-1.5 is good.
    speed = speed * 1.5
    # Rate at which the trails fades, higher = faster fade.
    trace_drop_off = tracedrop
    trace_color = 0 # 0-8
    fps = 300.0
    dt = 1.0 / fps
    accumulator = 0.0
    frame_start = datetime.now()
    # Actually initialise window Now
    stdscr = curses.initscr()
    stdscr.resize(WIDTH,HEIGHT)
    stdscr.clear()
    # Init colours
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    # Specs Stuff
    if specs:
        if platform.os == 'Windows':
            print('Unfortunately -s --specs isn\'t available for windows right now.')
            specs = False
        else:
            import grabsys
            sys_specs = grabsys.get_system_info()
    # Initialise board
    if trace:
        trace = [[0] * int(WIDTH / d_WIDTH) for x in range(int(HEIGHT / d_HEIGHT))]
    [[0] * int(WIDTH / d_WIDTH) for x in range(int(HEIGHT / d_HEIGHT))]

    # The main loop.
    while True:
        current = datetime.now()

        # Divide by timedelta to acheive float.
        accumulator += (current - frame_start) / timedelta(microseconds=1)
        frame_start = current
        if accumulator >= 1.0 / 30.0:
            accumulator = 1.0 / 30.0
        # Prepare for a calculations headache.
        while accumulator > dt:
            for i in range(no_of_pendulums):

                a1 = (
                    -g * (2 * mass_1[i] + mass_2[i]) * sin(O1[i])
                    - g * mass_2[i] * sin(O1[i] - 2 * O2[i])
                    - 2
                    * mass_2[i]
                    * sin(O1[i] - O2[i])
                    * (
                        omega_2[i] ** 2 * length_2[i]
                        + omega_1[i] * omega_1[i] * length_1[i] * cos(O1[i] - O2[i])
                    )
                ) / (
                    length_1[i]
                    * (
                        2 * mass_1[i]
                        + mass_2[i]
                        - mass_2[i] * cos(2 * O1[i] - 2 * O2[i])
                    )
                )

                a2 = (
                    (2 * sin(O1[i] - O2[i]))
                    * (
                        omega_1[i] * omega_1[i] * length_1[i] * (mass_1[i] + mass_2[i])
                        + g * (mass_1[i] + mass_2[i]) * cos(O1[i])
                        + omega_2[i]
                        * omega_2[i]
                        * length_2[i]
                        * mass_2[i]
                        * cos(O1[i] - O2[i])
                    )
                    / length_2[i]
                    / (
                        2 * mass_1[i]
                        + mass_2[i]
                        - mass_2[i] * cos(2 * O1[i] - 2 * O2[i])
                    )
                )
                ## Just trust them.
                omega_1[i] += speed * dt * a1
                omega_2[i] += speed * dt * a2
                O1[i] += speed * omega_1[i] * dt
                O2[i] += speed * omega_2[i] * dt
            accumulator -= dt
            if trace:
                for i in range(int(HEIGHT / d_HEIGHT)):
                    for j in range(int(WIDTH / d_WIDTH)):
                        if trace[i][j] > 0:
                            trace[i][j] -= trace_drop_off
        try:
            for i in range(floor(HEIGHT / d_HEIGHT)):
                # for j in range(floor(WIDTH/d_WIDTH)):
                #        stdscr.addstr(i,j,' ')
                for j in range(floor(WIDTH / d_WIDTH)):
                    if trace:
                        if stdscr.inch(i, j) == ord("@"):
                            # stdscr.addstr(6, 0, "Tracing")
                            trace[i][j] = fps

                        if trace[i][j] >= 3 * int(fps / 4):
                            stdscr.addstr(i,j, ":",curses.color_pair(trace_color+8))
                        elif trace[i][j] >= 2 * int(fps / 4):
                            stdscr.addstr(i,j, ".",curses.color_pair(trace_color+9))

                        elif trace[i][j] >= int(fps / 4):
                            if (i + j) % 2:
                                stdscr.addstr(i,j, ".",curses.color_pair(trace_color+11))
                            else:
                                stdscr.addstr(i,j, " ")
                        else:
                            stdscr.addstr(i,j, " ")
                    else:
                        stdscr.addstr(i,j, " ")
                    if i < int(HEIGHT / d_HEIGHT / 2):
                        stdscr.addstr(int(i),int(WIDTH / 2 / d_WIDTH), "|",curses.color_pair(i%8+8))
        except curses.error as e:
            pass


        for i in range(no_of_pendulums):
            x1 = (WIDTH / 2 + sin(O1[i]) * length_1[i] + d_WIDTH * 0.5) / d_WIDTH
            y1 = (
                cos(O1[i]) * length_1[i] + d_HEIGHT * 0.5
            ) / d_HEIGHT + HEIGHT / d_HEIGHT / 2
            x2 = x1 + (sin(O2[i]) * length_2[i] + d_WIDTH * 0.5) / d_WIDTH
            y2 = y1 + (cos(O2[i]) * length_2[i] + d_HEIGHT * 0.5) / d_HEIGHT
            if i % 2 == 0:
                draw_line(
                    stdscr, WIDTH / 2 / d_WIDTH, HEIGHT / d_HEIGHT / 2, x1, y1, "*"
                )
                draw_line(stdscr, x1, y1, x2, y2, "*")
                # stdscr.addstr(0,0,'{} {} {} {}'.format(x1,y1,x2,y2))
                draw_point(stdscr, WIDTH / 2 / d_WIDTH, HEIGHT / d_HEIGHT / 2, "@")
                draw_point(stdscr, x1, y1, "@",color=False)
                draw_point(stdscr, x2, y2, "@",color=False)
            else:
                draw_line(
                    stdscr, WIDTH / 2 / d_WIDTH, HEIGHT / d_HEIGHT / 2, x1, y1, "#"
                )
                draw_line(stdscr, x1, y1, x2, y2, "#")
                draw_point( stdscr, WIDTH / 2 / d_WIDTH, HEIGHT / d_HEIGHT / 2, "@")
                draw_point(stdscr, x1, y1, "@",color=False)
                draw_point(stdscr, x2, y2, "@",color=False)


        if specs:
            stdscr.addstr(2,0,'-'*30,curses.color_pair(2))
            i = 0
            for x in sys_specs.keys():
                if sys_specs[x] == '':
                    pass
                i+=1
                stdscr.addstr(i+3,0,str(x),curses.color_pair(4))

                stdscr.addstr(i+3,(len(x)+1),': {0}'.format(sys_specs[x].title()))

            # Add the colours
            for y in range(0,2): ##For a 2x8 Grid
                for x in range(0,8):
                    i = y*4+x
                    stdscr.addstr(y+20,2*x,'██',curses.color_pair(i))
        stdscr.addstr(
            0,
            0,
            "Flo's Double Pendulum. Number of Pendulums: {0}.".format(
                no_of_pendulums
            ),
            curses.color_pair(5)
        )
        stdscr.refresh()


def main():
    parser = argparse.ArgumentParser(
        add_help=False,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
    """
             Flo's Glorious Pendulum!
         --------------------------------
           Good luck solving this code
       Not even I know what half of it does
              Enjoy either way <3"""))
    parser.add_argument(
        "-t", "--trace", help="Enables tracing on pendulums", action="store_true"
    )
    parser.add_argument(
        "-tD",
        "--tracedrop",
        help="Speed at which trace fades",
        action="store",
        type=float,
        default=1.0,
    )
    parser.add_argument(
        "-s", "--specs", help="Enables displaying specs down the side. REQUIRES PSUTIL", action="store_true"
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
        default=150.0,
    )
    parser.add_argument(
        "-g",
        "--gravity",
        help="Force of gravity",
        action="store",
        type=float,
        default=9.81,
    )
    parser.add_argument(
        "-sP",
        "--speed",
        help="Speed at which pendulum runs",
        action="store",
        type=float,
        default=1.0,
    )
    parser.add_argument(
        "-H",
        "--HEIGHT",
        help="Height of screen.",
        action="store",
        type=int,
        default=1024,
    )
    parser.add_argument(
        "-W",
        "--WIDTH",
        help="Width of screen.",
        action="store",
        type=int,
        default=1024,
    )
    parser.add_argument(
        "-dH",
        "--dHEIGHT",
        help="Value HEIGHT is divided by.",
        action="store",
        type=int,
        default=32,
    )
    parser.add_argument(
        "-dW",
        "--dWIDTH",
        help="Value WIDTH is divided by",
        action="store",
        type=int,
        default=8,
    )
    parser.add_argument(
        "-e",
        "--epsilon",
        help="1e-Value",
        action="store",
        type=int,
        default=5,
    )


    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS)
    args = parser.parse_args()
    parser.print_help()
    # Because I'm an idiot and I made order matter (groan)
    v = vars(args)
    # Needed for 'global' values
    h, w = v["HEIGHT"],v["WIDTH"]
    OPTIONS = [
            v["pendulums"],
            v["trace"],
            v["length"],
            v["mass"],
            v["specs"],
            h,
            w,
            v["dHEIGHT"],
            v["dWIDTH"],
            v["epsilon"],
            v["speed"],
            v["tracedrop"],
            v["gravity"]

            ]
    print('')
    for k, va in v.items():
        print('{0}: {1}'.format(k,va))
    sleep(3)
    sim(*OPTIONS)


if __name__ == "__main__":
    main()
