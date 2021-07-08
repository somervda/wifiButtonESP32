import util
from machine import Pin
import network
from microWebCli import MicroWebCli
import utime
import config


def buttonPress(p):
    print('pin change', p)
    contentBytes = MicroWebCli.GETRequest(
        'http://192.168.1.115:1880/red/', {'button': 'red'})
    print(contentBytes)


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

p16 = Pin(16, Pin.IN)
p16.irq(trigger=Pin.IRQ_FALLING, handler=buttonPress)
