# python reverse shell

This is a reverse shell written in python3. It allows an attacker to remotely send commands to the victims command promt and steal and place files. As of right now it is still pretty buggy. Will fix some time in the future.

## Description

The listener.py is listening on the attacker machine and the reverse-shell.py is planted on target. Listener has to be running when reverse-shell is executed.
The reverse-shell will call it's master and establish a connection. 

## Usage

### Running the listener

```
python3 listener.py
```

### Running the reverse shell

```
python3 reverse-shell.py
```

### Valid commands

Once the reverse-shell has connected to the listener, you will be prompted to enter a command. Valid commands are:

```
system <command>
```
The system-command will send whatever command you give it as a parameter to the of the victim's machine, execute it, and send back the response.

```
steal /path/on/vitctim /path/on/attacker
```
The steal-command will send any file from the victims computer to the attacker and save it to the specified location.

```
place /path/on/vitctim /path/on/attacker
```
Place will let you place any file from the attacking machine on the target-system.
