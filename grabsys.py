import platform
import os
import subprocess
import socket

import psutil
# psutil is the big one.

def process(command: str):
    return subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE
        ).communicate()[0].decode('utf-8')

def grab_res():
    if platform.system() == 'Darwin':
        '''
        Interesting way to get res on macos
        '''
        res = process('system_profiler SPDisplaysDataType | grep Resolution'
        ).split('Resolution: ')[1].strip()

    elif platform.system() == 'Linux':
        '''If this doesn't work on your distro, let me know and i'll fix it.'''
        res = process(
            'xrandr | grep "\*" | cut -d" " -f4'
            ).strip()
    return res

def get_uptime():
    '''u = subprocess.Popen(
        'uptime',
        shell=True,
        stdout=subprocess.PIPE
    ).communicate()[0].decode('utf-8').replace("up ", "")'''
    if platform.system() == 'Linux':
        return process('uptime -p').replace("up ","")
    return ' '.join([i.strip() for i in process(
        'uptime'
        ).replace("up ", "").split(',')[:3]])

def detect_desktop_environment():
    desktop_environment = 'generic'
    if os.environ.get('KDE_FULL_SESSION') == 'true':
        desktop_environment = 'kde'
    elif os.environ.get('GNOME_DESKTOP_SESSION_ID'):
        desktop_environment = 'gnome'
    elif platform.system() == 'Darwin':
        desktop_environment = 'Aqua'
    else:
        try:
            info = subprocess.check_output('xprop -root _DT_SAVE_MODE')
            if ' = "xfce4"' in info:
                desktop_environment = 'xfce'
        except (OSError, RuntimeError):
            pass
    return desktop_environment

def get_user():
    username = environ['USER']
    hostname = process(
            'hostname',
        ).strip().rstrip('\n')
    return f'{username}@{hostname}'

def get_system_info():
    '''
    Layout of get_system_info

    OS: MacOS 11.4
    Host: Macbook10
    Kernel: 20.5
    Uptime ye
    Shell: zsh
    Resolution: 2304x1440
    DE : Aqua
    WM: yabai
    Terminal: Apple terminal
    Terminal font: SFMono Regular
    CPU: intel m3 (speed)
    GPU: intel graphics 616
    Memory: xyz/XYZmb
    '''
    info={}
    # Hacky and could be better
    info['Hostname']=socket.gethostname()
    info['Uptime'] = get_uptime()
    info['OS']=platform.platform(aliased=True).split('-')[0]
    info['Kernel'] = platform.release()
    info['Shell'] = os.environ['SHELL'].split('/')[-1]
    info['Resolution'] = grab_res()
    info['DE']=detect_desktop_environment()
    info['Architecture']=platform.machine()
    info['Terminal']= os.environ['TERM']
    info['Processor']=platform.processor()
    info['RAM']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    return info
