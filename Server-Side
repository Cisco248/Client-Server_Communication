import socket
import pandas as pd

def save_bid(client_id, bid_amount):
    with open("sym.txt", "a") as file:
        file.write("{}: {}\n".format(client_id, bid_amount))

def server_program():
    host = socket.gethostname()                                                 # get the hostname
    port = 2022                                                                 # initiate port no above 1024

    server_socket = socket.socket()                                             # get instance look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))                                            # bind host address and port together
    server_socket.listen(2)                                                     # configure how many client the server can listen simultaneously
    conn, address = server_socket.accept()                                      # accept new connection
    print("Connected Client From: " + str(address))
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    while True:
        client_id = conn.recv(1024).decode()                                    # receive data stream. it won't accept data packet greater than 1024 bytes
        if not client_id:
            break                                                               # if data is not received break
        print("Successfully Connected Client: " + str(client_id))
        client_id_data = "Successfully Connected..! Client: " + str(client_id)
        conn.send(client_id_data.encode())                                      # send data to the client

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        stock_data = "C:\\Users\\Lahiru\\Desktop\\Current Sources\\data.csv"    # pd.read_csv('data.csv') 'C:\Users\Lahiru\Desktop\Current Sources'
        conn.send(stock_data.encode())                                          # csv file transfer the client side file

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        stock_code = conn.recv(1024).decode()                                   # receive data stream. it won't accept data packet greater than 1024 bytes
        if not stock_code:
            break                                                               # if data is not received break
        print("Successfully Entered Stock Code..!" + str(stock_code))
        stock_code_data = ("Successfully..! Your Stock Code : " + str(stock_code))
        conn.send(stock_code_data.encode())                                     # send data to the client

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

        bid_amount = conn.recv(1024).decode()                                   # receive data stream. it won't accept data packet greater than 1024 bytes
        if not bid_amount:
            break                                                               # if data is not received break
        print("Bid Value..!" + str(bid_amount))
        bid_amount_data = ("Successful..! Your Bid Value : " + str(bid_amount))
        conn.send(bid_amount_data.encode())                                     # send data to the client
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

        save_bid(str(client_id), bid_amount)
      
    conn.close()                                                                # close the connection


if __name__ == '__main__':
    server_program()
