'''
processdatafiles.py

This method processes the incoming datafile from the
Flacktek Mixer.  The method first determines if this
a mixer file and if so stores it in the appropriate location.

Developer:  Dan Ballard
Creation Date:  January 30, 2022
Revision Date: May 8, 2022

TODO:  remove the tqdm calls since there will be no
user watching the process of loading incoming files.

'''


import socket
import tqdm
import os

def readIncomingMsg():
    SERVER_HOST = "10.0.0.119"          #  The server address
                                        # The apollo server is
                                        # 192.168.10.117
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

    directory_path = os.getcwd()
    print("My current directory is : " + directory_path)
    folder_name = os.path.basename(directory_path)
    print("My directory name is : " + folder_name)

    filename = os.path.basename(filename)
    print("My filename is : " + filename)
    filesize = int(filesize)
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))
    client_socket.close()
    s.close()
    return filename
