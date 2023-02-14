distance = 0
led.enable(True)

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    global distance
    pins.digital_write_pin(DigitalPin.P2, 0)
    control.wait_micros(2)
    pins.digital_write_pin(DigitalPin.P2, 1)
    control.wait_micros(10)
    pins.digital_write_pin(DigitalPin.P2, 0)
    distance = pins.pulse_in(DigitalPin.P1, PulseValue.HIGH) / 58
    basic.show_number(distance)
    basic.pause(50)
    serial.write_value("distance", distance)
basic.forever(on_forever2)
