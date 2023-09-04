"""This Is Group - 14 Mini Project
        Client Server
        Group Members - 22UG2 - 0195 Vimukthi Malshan
                        22UG2 - 0120 Nirmal Senevirathna
                        22UG2 - 0004 Lahiru Dilshan
                        22UG2 - 0034 Nethmini Naduni
                        22UG2 - 0200 Imal Lakpriya
                        22UG2 - 0588 Lakshan Janith
                        
                        ********************
                        Client Side Prrogram
                        ********************
                        """

import socket
import pandas as pd
import json

#----------------------------------------------------------------------------------

def save_bid(client_id, bid_amount):                                                                # i use this functions for saving bids
    with open("sym.txt", "a") as file:
        file.write("Client ID : {} - Bid Amount : {}\n".format(client_id, bid_amount))

#----------------------------------------------------------------------------------

def client_program():
    host = socket.gethostname()                                                                      # as both code is running on same pc
    port = 2022                                                                                      # socket server port number

    client_socket = socket.socket()                                                                  # instantiate
    client_socket.connect((host, port))                                                              # connect to the server

#----------------------------------------------------------------------------------
    
    client_id = input(" ---> Input The Client ID: ")                                                 # take input

    client_socket.send(client_id.encode())                                                           # send message
    client_data = client_socket.recv(1024).decode()                                                  # receive response
    print(" <--- " + client_data)                                                                    # show in terminal
    pass

#----------------------------------------------------------------------------------
    
    print("")
    rec_data = client_socket.recv(4096).decode()                                                     # Receive the JSON string from the server
    stock_data = json.loads(rec_data)                                                                # Deserialize the JSON string back into a list

    for row in stock_data:                                                                           # Now 'stock_data' contains the data received as a list of lists
        print(f"{row}\n")
        #for item in row:
            
    print("")

#----------------------------------------------------------------------------------
    
    stock_code = input(" ---> Enter the Stock Code: ")                                               # again take input
    
    client_socket.send(stock_code.encode())
    stock_code_data = client_socket.recv(1024).decode()
    print(" <--- " + stock_code_data)
    pass
    stock_code_to_update = stock_code
#----------------------------------------------------------------------------------     
    
    print("")
    bid_amount = input(" ---> Enter the Bid Amount: ")                                               # again take input
    
    client_socket.send(bid_amount.encode())
    bid_amount_data = client_socket.recv(1024).decode()
    print(" <--- " + bid_amount_data)
    pass
    new_base_price = bid_amount
#----------------------------------------------------------------------------------

    csv_file_path = 'Desktop\\Client - Server Mini Project\\data.csv'
    data_file = pd.read_csv(csv_file_path)
    data_file.loc[data_file['Stock_Code'] == stock_code_to_update, 'Base_Price'] = new_base_price
    data_file.to_csv(csv_file_path, index=False)                                                    # Write the updated DataFrame back to the CSV file

    client_socket.close()                                                                           # close the connection
    print("")
    print("<--> Wish Your Lucky Day !!!...")
    print("")

#---------------------------------------------------------------------------------

if __name__ == '__main__':                                                                          # Start the main function tasks
    client_program()