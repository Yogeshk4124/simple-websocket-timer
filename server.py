# websocket_server.py

import asyncio
import websockets
import json

TIMER_INTERVAL = 1  # Update interval in seconds

async def timer_handler(websocket, path):
    seconds = 100  # Initial timer value
    try:
        while seconds >= 0:
            await websocket.send(json.dumps({'seconds': seconds}))
            seconds -= 1
            await asyncio.sleep(TIMER_INTERVAL)
    except websockets.exceptions.ConnectionClosed:
        pass

if __name__ == "__main__":
    start_server = websockets.serve(timer_handler, "localhost", 8080)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
