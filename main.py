#! /usr/bin/env pybricks-micropython

from micropython import const
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Button
from pybricks.tools import wait

motor_l = Motor(Port.A)
motor_r = Motor(Port.D)

brick = EV3Brick()


def drive_one_meter_with(wheel_diameter, axle_track):
    robo = DriveBase(motor_l, motor_r, wheel_diameter, axle_track)
    robo.straight(1000)
    robo.stop()


def turn_360_degrees_with(wheel_diameter, axle_track):
    robo = DriveBase(motor_l, motor_r, wheel_diameter, axle_track)
    robo.turn(360)
    robo.stop()


_CALIB_WHEEL_DIAMETER = const(1)
_CALIB_AXLE_TRACK = const(2)


def main():
    wheel_diameter = 69
    axle_track = 123
    mode = _CALIB_WHEEL_DIAMETER

    while True:
        brick.screen.clear()
        if mode == _CALIB_WHEEL_DIAMETER:
            brick.screen.print("Wheel diameter\nSetting: %d" % (wheel_diameter,))
        if mode == _CALIB_AXLE_TRACK:
            brick.screen.print("Axle track\nSetting: %d" % (axle_track,))

        # Wait for a button to be pressed. Up button increments the setting to be
        # calibrated. Down button decrements. Center button causes a run of
        # the calibration mode.
        while True:
            pressed = brick.buttons.pressed()
            if Button.UP in pressed:
                if mode == _CALIB_WHEEL_DIAMETER:
                    wheel_diameter += 1
                if mode == _CALIB_AXLE_TRACK:
                    axle_track += 1
                break
            if Button.DOWN in pressed:
                if mode == _CALIB_WHEEL_DIAMETER:
                    wheel_diameter -= 1
                if mode == _CALIB_AXLE_TRACK:
                    axle_track -= 1
                break
            if Button.CENTER in pressed:
                brick.speaker.beep()
                wait(1000)
                if mode == _CALIB_WHEEL_DIAMETER:
                    drive_one_meter_with(wheel_diameter, axle_track)
                else:
                    turn_360_degrees_with(wheel_diameter, axle_track)
                break
            if Button.LEFT in pressed or Button.RIGHT in pressed:
                if mode == _CALIB_WHEEL_DIAMETER:
                    mode = _CALIB_AXLE_TRACK
                elif mode == _CALIB_AXLE_TRACK:
                    mode = _CALIB_WHEEL_DIAMETER
                break
            wait(10)

        while len(brick.buttons.pressed()) > 0:
            wait(10)


if __name__ == "__main__":
    main()
