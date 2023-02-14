let distance = 0
led.enable(true)
basic.forever(function on_forever() {
    
})
basic.forever(function on_forever2() {
    
    pins.digitalWritePin(DigitalPin.P2, 0)
    control.waitMicros(2)
    pins.digitalWritePin(DigitalPin.P2, 1)
    control.waitMicros(10)
    pins.digitalWritePin(DigitalPin.P2, 0)
    distance = pins.pulseIn(DigitalPin.P1, PulseValue.High) / 58
    basic.showNumber(distance)
    basic.pause(50)
    serial.writeValue("distance", distance)
})
