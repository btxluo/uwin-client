import json
import time

import websocket


def on_message(ws, message):
    print(ws)
    print(message)
    time.sleep(2)
    ws.send("ping")

def on_error(ws, error):
    print(ws)
    print(error)


def on_close(ws):
    print(ws)
    print("### closed ###")

def on_open(ws):
    ws.send("ping")

    # ws.send(json.dumps({"reqType": "scada", "id": "01FPWJ6GAD44WCBVF0DGGABE7S"}))
    # ws.send(json.dumps({"reqType": "realtimeView", "id": "01FPWJ6GAD44WCBVF0DGGABE7S", "level": 2, "chnName": "用能分析"}))

websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws://grid.sxhmzc.cn:8103/notifies/4f51e5f64d071c107431d923df331764",
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()