from websocket import create_connection
from datetime import datetime

def init_ws(ip, port):
     ws_url = "ws://" + str(ip) +":"+ str(port)
     ws = create_connection(ws_url)
     return ws

def close_ws(ws):
     ws.close()

def send_data(ws, bin_id, bin_level, last_emptied, contains_meat, contains_danger):
     current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     data = str(bin_id)+","+str(current_timestamp)+","+str(bin_level)+","+str(last_emptied)+","+str(contains_meat)+","+str(contains_danger)
     ws.send(data)

def recieve_data(ws):
     return ws.recv()