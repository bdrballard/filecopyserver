import socket
import tqdm
import os

def readIncomingMsg():
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 5001
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"

    headerlist = list()
    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(10)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    print("Waiting for the client to connect... ")
    client_socket, address = s.accept()
    print(f"[+] {address} is connected.")
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
            #inputstring = str(bytes_read, 'UTF-8')
            #headerlist.append(inputstring)
            #print(inputstring[0:10])
            progress.update(len(bytes_read))
        #print(headerlist)
    client_socket.close()
    s.close()
