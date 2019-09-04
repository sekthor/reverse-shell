# python reverse shell

This is a reverse shell written in python3. It allows an attacker to remotely send commands to the victims command promt and steal and place files. 

## Description

The listener.py is listening on the attacker machine and the reverse-shell.py is planted on target. Listener has to be running when reverse-shell is executed.
The reverse-shell will call it's master and establish a connection. 

## Usage

### Running the listener

'''
python3 listener.py
'''

### Running the reverse shell

'''
python3 reverse-shell.py
'''