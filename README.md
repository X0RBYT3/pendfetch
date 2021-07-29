# Double Pendulum Using Curses in Python.

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>


**Does NOT work on Windows, UNIX only.**

Uses equations from [here.](https://www.myphysicslab.com/pendulum/double-pendulum-en.html), obviously a lot could be done to it (see below the Args), Any contributions are appreciated)

### Demo: 
https://user-images.githubusercontent.com/11583852/127576299-a97625a4-69bc-4887-8793-972192db6086.mov

## Args
|short|long|help|default
|--|---|--|--|
|-h| --help | shows help message |N/A|
|-t| --trace | enables the trace functionality | off|
|-p| --pendulums |  Number of pendulums | 1|
|-m| --mass | Starting mass of pendulums | 100.0|
|-l| --length | Starting length of the arms | 250.0|
---------------------------------------------------

# TODO
- add windows functionality
- add more functionality to arguments (epsilon, weight1, weight2)
- general cleanup of variable names 
- improve efficiency (esp in lists)
- add colors :)
