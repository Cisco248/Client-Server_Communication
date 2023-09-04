"""This Is Group - 14 Mini Project
        Publisher Subscriber
        Group Members - 22UG2 - 0195 Vimukthi Malshan
                        22UG2 - 0120 Nirmal Senevirathna
                        22UG2 - 0004 Lahiru Dilshan
                        22UG2 - 0034 Nethmini Naduni
                        22UG2 - 0200 Imal Lakpriya
                        22UG2 - 0588 Lakshan Janith
                        
                        ********************
                        Server Side Prrogram
                        ********************
                        """

import socket
import csv
import json

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def save_bid(client_id, bid_amount):                                                    # # I use this functions for saving bids
    with open("sym.txt", "a") as file:
        file.write("{}: {}\n".format(client_id, bid_amount))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def server_program():
    host = socket.gethostname()                                                         # get the hostname
    port = 2022                                                                         # initiate port no above 1024

    server_socket = socket.socket()                                                     # get instance look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))                                                    # bind host address and port together
    server_socket.listen(2)                                                             # configure how many client the server can listen simultaneously
    conn, address = server_socket.accept()                                              # accept new connection
    print("Connected Client From: " + str(address))
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    while True:
        client_id = conn.recv(1024).decode()                                            # receive data stream. it won't accept data packet greater than 1024 bytes
        if not client_id:
            break                                                                       # if data is not received break
        print("Successfully Connected Client: " + str(client_id))
        client_id_data = "Successfully Connected..! Client: " + str(client_id)
        conn.send(client_id_data.encode())                                              # send data to the client

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        with open (r'data.csv', mode='r') as file:                                      # you have update your location 
            csv_reader = csv.DictReader(file)
            rows = list(csv_reader)
            selected_rows = rows[:8]
            
            stock_data = []
            
            for row in selected_rows:
                sr1 = "Stock Code : " + row['Stock_Code']
                sr2 = "Base Price : " + row['Base_Price']
                sr3 = "Security : " + row['Security']
                sr4 = "Profit : " + row['Profit']
                stock_data.append([sr1, sr2, sr3, sr4])                                 # Append each row as a list

        stock_data_json = json.dumps(stock_data)                                        # Serialize the stock_data list to a JSON string

        conn.send(stock_data_json.encode())                                             # Now you can send the JSON string to the client
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        stock_code = conn.recv(1024).decode()                                           # receive data stream. it won't accept data packet greater than 1024 bytes
        if not stock_code:
            break                                                                       # if data is not received break
        print("Successfully Entered Stock Code..!" + str(stock_code))
        stock_code_data = ("Successfully..! Your Stock Code : " + str(stock_code))
        conn.send(stock_code_data.encode())                                             # send data to the client

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

        bid_amount = conn.recv(1024).decode()                                           # receive data stream. it won't accept data packet greater than 1024 bytes
        if not bid_amount:
            break                                                                       # if data is not received break
        print("Bid Value..!" + str(bid_amount))
        bid_amount_data = ("Successful..! Your Bid Value : " + str(bid_amount))
        conn.send(bid_amount_data.encode())                                             # send data to the client
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

        
        
        save_bid(str(client_id), bid_amount)
      
    conn.close()                                                                        # close the connection


if __name__ == '__main__':
    server_program()
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
