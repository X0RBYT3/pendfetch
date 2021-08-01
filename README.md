<h1 align="center">Double Pendulum Using Curses in Python.</h1>

<p align="center"><a href="https://forthebadge.com" target="_blank"><img src="https://forthebadge.com/images/badges/built-with-love.svg" alt="Build with <3" /></a>&nbsp;<a href="https://forthebadge.com" target="_blank"><img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="Made with python" /></a>&nbsp;<a href="https://forthebadge.com" target="_blank"><img src="https://forthebadge.com/images/badges/powered-by-coffee.svg"/></p>


<p align="center"><a href="https://github.com/psf/black" target="_blank"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black" height="18" /></a>&nbsp;
<a href="https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fpypi.org%2Fproject%2Fdouble-pendulum%2F1.0.4%2F"><img alt="Twitter" src="https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fpypi.org%2Fproject%2Fdouble-pendulum%2F1.0.4%2F" height="18"></a>
<a href="http://makeapullrequest.com" target="_blank"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=shields" height="18"/>&nbsp;
<a href="https://badge.fury.io/py/double-pendulum"><img src="https://badge.fury.io/py/double-pendulum.svg" alt="PyPI version" height="18"></a>


</p>
<p align="center">A nice relaxing double pendulum simulation using ASCII, able to simulate multiple pendulums at once, and provide tracing of pendulums.</p>

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Quickstart](#demo)
- [Args](#args)
- [TODO](#todo)

## Features
- As mentioned, able to simulate multiple pendulums at once.
- Able to specify the weight and mass of pendulums to create different butterfly effects.
- Uses equations from [here.](https://www.myphysicslab.com/pendulum/double-pendulum-en.html)
- If -s is used, it grabs system specs and displays them (hi r/unixporn)
- Obviously a lot could be done to it (see below the Args), Any contributions are appreciated)

## Demo:


https://user-images.githubusercontent.com/11583852/127770473-25e63061-cca6-4ca3-997f-d3d1b1469652.mov



## Quickstart:

__Dependencies:__ Python 3.2+,curses (standard on UNIX), psutils if you want to use -s

### Github
- Clone using `https://github.com/Nekurone/double-pendulum-ascii.git` or download the zip.
- Extract if necessary and head inside the folder `double-pendulum`
- ```python3 pendulum.py [args]```

### Pip
- `python3 -m pip install double-pendulum-ascii`
- `python3 -m double-pendulum [args]`

## Args
|short|long|help|default
|--|---|--|--|
|-h| --help | shows help message |N/A|
|-t| --trace | enables the trace functionality | off|
|-p| --pendulums |  Number of pendulums | 1|
|-m| --mass | Starting mass of pendulums | 100.0|
|-l| --length | Starting length of the arms | 250.0|
|-s| --specs | Enables Specs Mode | off |
---------------------------------------------------

## TODO

Note I will not be updating the words on this TODO, but rather just checking them off, as a nice front page reminder of the work done :)

- [x] Add windows functionality
- [ ] Add more functionality to arguments (epsilon, weight1, weight2)
- [ ] General cleanup of variable names
- [ ] Improve efficiency (esp in lists)
- [ ] Add colors :)

<h3 align="center">If you have any suggestions, or anything you'd like to add, just open a PR :)</h3>
