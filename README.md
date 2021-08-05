<p align="center"><img src="https://user-images.githubusercontent.com/11583852/128283452-314f3aca-d095-4d2b-9cf9-4e7afaf8c404.png" alt="Header image: Pendfetch"></img></p>

<h1 align="center">Show off your terminal, in style.</h1>

<p align="center"><a href="https://forthebadge.com" target="_blank"><img src="https://forthebadge.com/images/badges/built-with-love.svg" alt="Build with <3" height="35"/></a>&nbsp;<a href="https://forthebadge.com" target="_blank"><img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="Made with python" height="35" /></a>&nbsp;<a href="https://forthebadge.com" target="_blank"><img src="https://forthebadge.com/images/badges/powered-by-coffee.svg" height="35"/></p>


<p align="center">
  <a
  href="https://github.com/psf/black"
   target="_blank">
      <img 
        src="https://img.shields.io/badge/code%20style-black-000000.svg" 
        alt="Code style: black" height="20" />
  </a>&nbsp;
  <a 
    href="https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fpypi.org%2Fproject%2Fdouble-pendulum%2F"><img alt="Twitter" src="https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fpypi.org%2Fproject%2Fdouble-pendulum%2F1.0.12%2F" height="20"></a>
<a href="http://makeapullrequest.com" target="_blank"><img src="https://img.shields.io/badge/PRs-welcome-bcentergreen.svg?style=shields" height="20"/>&nbsp;
<a href="https://badge.fury.io/py/double-pendulum"><img src="https://badge.fury.io/py/double-pendulum.svg" alt="PyPI version" height="20"></a>


</p>
<p align="center">A nice relaxing double pendulum simulation using ASCII, able to simulate multiple pendulums at once, and provide tracing of pendulums as well as providing some system information. 
  If you spot any bugs or features that need adding (especially with the specs), just open an issue :)</p>
<p align="center">
  <!--<h2>Demo</h2>&nbsp;-->
  <img src="https://i.imgur.com/37vz3rc.gif", alt="Demo Gif"></p>

    

## Features
- As mentioned, able to simulate multiple pendulums at once.
- Able to specify the weight and mass of pendulums to create different butterfly effects.
- Uses equations from [here.](https://www.myphysicslab.com/pendulum/double-pendulum-en.html)
- If -s is used, it grabs system specs and displays them.(hi r/unixporn)
- Obviously a lot could be done to it (see below the Args), Any contributions are appreciated)
## Quickstart:
__Dependencies:__ Python 3.2+,curses (standard on UNIX) or relevent windows port, psutils if you want to use -s

### Github
- Clone using `https://github.com/Nekurone/pendfetch.git` or download the zip.
- Extract if necessary and head inside the folder.
- ```python3 pendulum.py [args]```

### Pip
- `python3 -m pip install pendfetch` (or `pip install pendfetch`)
- `pendfetch [args]`

#### Don't forget to include `-s` for neofetch feature :) 
## **__Args__**

Visuals
- [help (-h)](#help)
- [trace (-t)](#trace)
- [tracedrop (-tD)](#tracedrop)
- [specs (-s)](#specs)

Maths and Pendulum settings
- [pendulum (-p)](#pendulum)
- [speed (-sP)](#speed)
- [gravity (-g)](#gravity)
- [mass (-m)](#mass)
- [length (-l)](#length)

Window settings
- [HEIGHT (-H)](#height)
- [WIDTH (-W)](#width)
- [dHEIGHT (-dH)](#dheight)
- [dWIDTH (-dW)](#dwidth)

<h1 align="center"> Visuals </h1>
<h2 align="center">--help (-h)</h2>
<h5 align="center">Spits out a fairly standard argparse help message. Note this is printed out when the program is run anyway. <img src="https://i.imgur.com/bIgrjqa.png"></img></h5>

<h5 align="center">
 type: None, default: None
 setting in example: -h 
 </h5>
 
 
 <h2 align="center">--trace (-t)</h2>
<h5 align="center"> Enables 'tracing', a faint line behind the pendulums that fades. <img src="https://i.imgur.com/UCp4pGL.gif"></img></h5>
<h5 align="center">type: bool, default: off,
 setting in example: -t
 </h5>
 

 
 <h2 align="center">--traceDrop (-tD)</h2>
<h5 align="center"> Controls the rate at which the trace from -t fades. Higher is faster fading. <img src="https://i.imgur.com/MGsazE3.gif"></img></h5>
<h5 align="center">type: float, default: 1.0,
 setting in example: -t -tD 0.5
 </h5>
 
 
 <h2 align="center">--specs (-t)</h2>
<h5 align="center"> Enables showing system info, note this feature is still a WIP, any bugs or issues just let me know. <img src="https://i.imgur.com/bPEBhst.png"></img></h5>
<h5 align="center">
 type: bool, default: off,
 setting in example: -s
 </h5>
 
 <h1 align="center"> Maths and Pendulum Settings </h1>
 
   <h2 align="center">--pendulum (-p)</h2>
<h5 align="center"> Number of pendulums to simulate at once. Combine with the gravity settings and some speed settings for some really pretty visuals. <img src="https://i.imgur.com/hAcvr2T.gif"></img></h5>
<h5 align="center">
 type: int, default: 1,
 setting in example: -p 300 
 </h5>
 
 <h2 align="center">--speed (-sP)</h2>
<h5 align="center"> Multiplier for speed of simulation. Around 0.5-1.5 is a good range <img src="https://i.imgur.com/Yl9BiRP.gif">
</img></h5>
<h5 align="center">
 type: float, default: 1.0,
 setting in example: -sP 3.0
 </h5>
 
 <h2 align="center">--gravity(-g)</h2>
<h5 align="center"> Controls the strength of gravity, note, this directly affects the speed of the simulation. So slowing down is recommended.<img src="https://i.imgur.com/zi5yh8V.gif"></img></h5>
<h5 align="center">
 type: float, default: 9.81,
 setting in example: -g 1
 </h5>
 
  <h2 align="center">--mass (-m)</h2>
<h5 align="center"> Controls the mass of the pendulums, useful mostly for butterfly effects <img src="https://i.imgur.com/1d9BSK0.gif">
</img></h5>
<h5 align="center">
 type: float, default: 100.0,
 setting in example: -m 300 -sP 0.2
 </h5>
 
  <h2 align="center">--length (-l)</h2>
<h5 align="center"> Controls the length of the arms of the pendulums, useful mostly for butterfly effects <img src="https://i.imgur.com/zSXYn3K.gif">
</img></h5>
<h5 align="center">type: float, default: 250.0, setting in example: -l 150 -sP 0.3
 </h5>

<h1 align="center">todo: Window settings</h1>
<h3 align="center">If you have any suggestions, or anything you'd like to add (or, more likely you found a bug) just open a PR :)</h3>

