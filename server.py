from datetime import datetime
from colorama import Fore
import socket

sock = socket.socket()

host = '192.168.0.164'
port = 9999

date = lambda: Fore.YELLOW + f"[{datetime.now().strftime('%x %X')}]: "


def bind_socket():
    msg = Fore.RED + f'Trying to bind the port {port}'
    print(f'{date()} {msg}')
    try:
        sock.bind((host, port))
        print(date(), Fore.GREEN + f'Binding to the port {port} was SUCCESSFUL!')
        sock.listen(5)

    except socket.error as e:
        print(date(), Fore.RED + 'The following error encountered: ', e)
        print(date(), Fore.YELLOW + 'Retrying....')
        bind_socket()


def connect():
    print(date(), f'Listening to the port {port}')
    conn, addr = sock.accept()
    print(date(), Fore.GREEN + f'Connection Established!')
    print(' ' * 22, f'IP: {addr[0]}\n {" " * 22}PORT: {addr[1]}')
    send_data(conn)
    conn.close()


def send_data(conn):
    try:
        while True:
            cmd = bytes(input(f'{date()} {Fore.LIGHTBLUE_EX} Enter a command: '), 'utf-8')
            if cmd:
                try:
                    # print(conn.recv(7))
                    conn.send(cmd)

                except socket.error:
                    main()

    except KeyboardInterrupt:
        print('\n', date(), Fore.YELLOW + 'Exiting....')
        conn.send('exiting123'.encode())

        # while not (out := sock.recv(10000).decode()):
        #     continue
        # print(out)


def main():
    bind_socket()
    connect()


if __name__ == '__main__':
    main()
