import socket 
S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM ) #UDP

target_ip_address = "127.0.0.1"
# target_ip_address ="xyz "
port_number = 2525    # 0-65353(somes port numbers are reserved) 

target_complete_address = (target_ip_address,port_number)

while True:
      message = input("write your message here : ")
      encrypt_message = message.encode('ascii')#Encrypting the message
      S.sendto(encrypt_message,target_complete_address)
      print("Message Sent")

      # FOR RECEIVE A MESSAGE 

      rec_message = S.recvfrom(100)# We are giving a buffer size that at a time 100 char message
      
      received_message = rec_message[0]
      decrypted_message = received_message.decode('ascii')
      print("Receiver :",decrypted_message)

      