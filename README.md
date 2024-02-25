# WebSocket Timer

WebSocket Timer is a simple project that demonstrates how to use WebSockets to create a timer that updates in real-time. The project consists of a WebSocket server written in Python using the `websockets` library and a simple HTML client.

## What is WebSocket?
WebSocket is a communication protocol that provides full-duplex communication channels over a single, long-lived connection. It is designed to be lightweight, efficient, and ideal for real-time applications. Unlike traditional request-response-based communication, where the client sends a request and waits for the server to respond, WebSockets enable bidirectional communication, allowing both the client and server to send messages to each other at any time.

## How WebSockets Work
- Handshake: The WebSocket connection starts with a handshake initiated by the client through an HTTP request. If the server supports WebSocket, it responds with a specific header indicating a successful handshake.
- Full-Duplex Communication: Once the handshake is complete, both the client and server can send messages to each other independently. This enables real-time updates without the need for continuous polling.

## Technologies Used

- Python
- WebSockets
- HTML
- JavaScript

## Features

- **Real-time updates:** The timer on the HTML page updates in real-time as the server sends continuous messages.
- **Simple setup:** Easy-to-understand code and setup for learning purposes.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/websocket-timer.git
    cd websocket-timer
    ```

2. **Install dependencies:**

    ```bash
    pip install websockets
    ```

## Usage

1. **Run the WebSocket Server:**

    ```bash
    python websocket_server.py
    ```

    The server will start and listen on `localhost:8080`.

2. **Open the HTML Page:**

    Open the `index.html` file in your browser:

    ```bash
    # If using Linux or macOS
    xdg-open index.html

    # If using Windows
    start index.html
    ```

    The HTML page will connect to the WebSocket server and display the timer.

## Customization

- **Timer Interval:** You can customize the timer interval by modifying the `TIMER_INTERVAL` variable in the `websocket_server.py` file.
  
- **Initial Timer Value:** The initial timer value is set in the `start_timer` method in `websocket_server.py`.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

## Acknowledgments

- [websockets](https://websockets.readthedocs.io/en/stable/) - A Python library for building WebSocket servers and clients.

## Support

If you have any questions or issues, please [open an issue](https://github.com/yourusername/websocket-timer/issues).
