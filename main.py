# Author: Om Shingare
# Language: MicroPython
# Project Name: ESP32 Simple Web Server

import socket
import network
import machine
import networkcredentials
import time

led = machine.Pin(2, machine.Pin.OUT)
led.off()

sta = network.WLAN(network.STA_IF)
if not sta.isconnected():
    print('Connecting to the network...')
    sta.active(True)
    sta.connect('try', None)
    while not sta.isconnected():
        pass
    print('Network config:', sta.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))  # Specify the port number (80 for HTTP)
s.listen(50)


def web_page():
    led_state = get_led_state()

    html_page = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="Control your ESP32 using a web interface.">
        <title>ESP32 Web Server</title>
        <meta name="favicon" href="https://omshingare.me/assets/logo-12777f7b.svg">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
        <style>
            body {{
                background-color: #121212;
                color: #ffffff;
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }}

            .container {{
                background-color: #1e1e1e;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
                padding: 20px;
                text-align: center;
            }}

            h2 {{
                color: #03a9f4;
            }}

            button {{
                font-size: 18px;
                padding: 12px 24px;
                margin: 5px;
            }}

            button.btn-success {{
                background-color: #4caf50;
            }}

            button.btn-danger {{
                background-color: #f44336;
            }}

            button.btn-warning {{
                background-color: #ff9800;
            }}

            p {{
                font-size: 20px;
                color: #ccc;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2 class="mt-4">ESP32 Web Server</h2>
            <p>This web interface allows you to control your ESP32 remotely.</p>
            <form class="mt-4">
                <button class="btn btn-success" name="LED" type="submit" value="1">LED ON</button>
                <button class="btn btn-danger" name="LED" type="submit" value="0">LED OFF</button>
                <button class="btn btn-warning" name="LED" type="submit" value="2">LED BLINK</button>
            </form>
            <p class="mt-4">LED is currently <strong>{led_state}</strong>.</p>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>"""

    return html_page




def get_led_state():
    if isLedBlinking:
        return 'Blinking'
    elif led.value() == 1:
        return 'ON'
    elif led.value() == 0:
        return 'OFF'


tim0 = machine.Timer(0)


def handle_callback(timer):
    led.value(not led.value())


isLedBlinking = False

while True:
    # Socket accept()
    conn, addr = s.accept()
    print("Got connection from %s" % str(addr))

    # Socket receive()
    request = conn.recv(1024)
    print("")
    print("")
    print("Content %s" % str(request))

    # Socket send()
    request = str(request)
    led_on = request.find('/?LED=1')
    led_off = request.find('/?LED=0')
    led_blink = request.find('/?LED=2')
    if led_on == 6:
        print('LED ON')
        print(str(led_on))
        led.value(1)
        if isLedBlinking:
            tim0.deinit()
            isLedBlinking = False

    elif led_off == 6:
        print('LED OFF')
        print(str(led_off))
        led.value(0)
        if isLedBlinking:
            tim0.deinit()
            isLedBlinking = False

    elif led_blink == 6:
        print('LED Blinking')
        print(str(led_blink))
        isLedBlinking = True
        tim0.init(period=500, mode=machine.Timer.PERIODIC, callback=handle_callback)

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)

    conn.close()

