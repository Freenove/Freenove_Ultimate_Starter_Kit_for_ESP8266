from machine import Pin
import time
import socket
import network

# set led pin
led = Pin(2, Pin.OUT)

ssid = '********'          #Enter the router name
password = '********'      #Enter the router password

wifi_status = network.WLAN(network.STA_IF)
wifi_status.active(True)
wifi_status.connect(ssid, password)
# check wifi connected
while wifi_status.isconnected() == False:
    print('Wifi lost connect...')
# if connected
print('Wifi connect successful')
print(wifi_status.ifconfig())

def WebPage():
    if led.value() == 1:
        gpio_state = 'OFF'
    else:
        gpio_state = 'ON'
    
    # html code ...
    html = """
    <html>
        <head>
            <title>ESP8266 Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="icon" href="data:,">
            <style>
                html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
                h1{color: #0F3376; padding: 2vh;}
                p{font-size: 1.5rem;}
                button{display: inline-block; background-color: #4286f4; border: none;border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
                button2{background-color: #4286f4;}
            </style>
        </head>
        <body> <h1>ESP8266 Web Server</h1> 
          <p>GPIO state: <strong>""" + gpio_state + """</strong></p>
          <p><a href="/?led=on"><button class="button">ON</button></a></p>
          <p><a href="/?led=off"><button class="button button2">OFF</button></a></p>
        </body>
    </html>
    """
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
try:
    while True:
        conn, addr = s.accept()
        print('Connection: %s' % str(addr))
        req = conn.recv(1024)
        req = str(req)
        print('Connect = %s' % req)
        led_on = req.find('/?led=on')
        led_off = req.find('/?led=off')
        if led_on == 6:
            print('LED ON')
            led.value(0)
        else:
            print('LED OFF')
            led.value(1)
        if led.value() == 1:
            gpio_state = 'OFF'
        else:
            gpio_state = 'ON'
        response = WebPage()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
except:
    pass
