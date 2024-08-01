import socket
import datetime 
S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM ) #UDP
ip_address = "127.0.0.1"
port_number = 2525    # 0-65353(somes port numbers are reserved) 

complete_address = (ip_address,port_number)
S.bind(complete_address)

print("Hye! I'm Receiver :) ")
 
current_time = datetime.datetime.now() 
time = str(current_time)

while True:
     message = S.recvfrom(100)

     sender_address = message[1][0]  #127.0.0.1.txt 
     received_message = message[0]
     decrypted_message = received_message.decode('ascii')

     print("Sender : " ,decrypted_message)
     print("Message Received ")
     with open(sender_address +'.txt' , 'a+') as file :    #(127.0.0.1)
          file.write(decrypted_message +'\n')
     
     # // for send a message
     send_address = message[1]
    
     message_to_send = input("Enter to message back :")
    
     encrypt_send_message = message_to_send.encode('ascii')
     S.sendto(encrypt_send_message,send_address)