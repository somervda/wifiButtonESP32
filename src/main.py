import util
from machine import Pin
import network
from microWebCli import MicroWebCli
import utime
import config


def buttonPress(p):
    global last_press
    # Simple debounce - make sure at least 200ms has passed
    #  since last time a button press action is performed
    if utime.ticks_ms() - last_press > 200:
        print('pin change', p, str(last_press))
        contentBytes = MicroWebCli.GETRequest(
            'http://192.168.1.115:1880/red/', {'button': 'red'})
        print(contentBytes)
        last_press = utime.ticks_ms()


def connect():
    if not net_if.isconnected():
        print('connecting to network...')
        net_if.active(True)
        net_if.connect(config.wifi_config['ssid'],
                       config.wifi_config['password'])
        while not net_if.isconnected():
            print('.', end='')
            utime.sleep_ms(500)
        print('network config: {}'.format(net_if.ifconfig()))


net_if = network.WLAN(network.STA_IF)
connect()

last_press = utime.ticks_ms()
p16 = Pin(16, Pin.IN, Pin.PULL_UP)
p16.irq(trigger=Pin.IRQ_FALLING, handler=buttonPress)
