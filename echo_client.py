import socket
import sys
import traceback


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    print(
        'connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    received_message = ''
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        sock.sendall(msg.encode('utf8'))
        chunk = ''
        while True:
            chunk = sock.recv(16)
            print(
                'received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
            received_message = received_message + chunk.decode('utf8')
            if len(chunk) < 16:
                break
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    finally:
        print('closing socket', file=log_buffer)
        sock.close()
        return (received_message)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
