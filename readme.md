# Pico Turntable

The purpose of this project is to create a turntable which can be used with any camera which
accepts a 2.5mm remote input. The idea is the pico will drive the turntable to rotate x degrees
and take a photo using the remote input. This will require a few components:

- A turn table surface (stls included for a nemo 17 stepper motor connection)
- A nemo 17 stepper motor
- A Pi Pico
- A motor controller
- 2.5mm jack

the code for the stepper motor was taken from [here](https://github.com/sbcshop/Pico-Motor-Driver/tree/main) and adapted
