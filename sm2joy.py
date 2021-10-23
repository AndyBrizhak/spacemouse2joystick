#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 19:49:51 2021

@author: lpower
"""

from time import sleep
from approxeng.input.selectbinder import ControllerResource
from approxeng.input.spacemousepro import SpaceMousePro
from approxeng.input.controllers import find_matching_controllers, ControllerRequirement
import uinput

# Monkeypatch the library's idea of a spacemouse
def new_registration_ids():
    return [(0x46d, 0xc62b), (0x46d, 0xC626)]

SpaceMousePro.registration_ids = staticmethod(new_registration_ids)

events = (
    uinput.BTN_0,
    uinput.BTN_1,
    uinput.ABS_X + (-350, 350, 0, 0),
    uinput.ABS_Y + (-350, 350, 0, 0),
    uinput.ABS_Z + (-350, 350, 0, 0),
    uinput.ABS_RX + (-350, 350, 0, 0),
    uinput.ABS_RY + (-350, 350, 0, 0),
    uinput.ABS_RZ + (-350, 350, 0, 0),
    uinput.ABS_THROTTLE + (-350, 350, 0, 0),
    )

scale = 350
jiggler = 0

while True:
    try:
        with ControllerResource() as sm:
            with uinput.Device(events, name="sm2joy-device", vendor=0xF00, product=0x0BA5) as device:
                print('Found a SpaceMouse and connected to it.')
                last_z = 0
                while sm.connected:
                    # Do processing
                    # presses = sm.check_presses()
                    # if sm.has_presses:
                    #     if 'fit' in presses:
                    #         device.emit_click(uinput.BTN_0)
                    #         #print("BTN0")
                    #     if 'menu' in presses:
                    #         device.emit_click(uinput.BTN_1)
                    #         #print("BTN1")
                    b1, b0 = sm['fit', 'menu']
                    if b0 is not None:
                        device.emit(uinput.BTN_0, 1)
                    else:
                        device.emit(uinput.BTN_0, 0)
                    if b1 is not None:
                        device.emit(uinput.BTN_1, 1)
                    else:
                        device.emit(uinput.BTN_1, 0)
                    device.emit(uinput.ABS_THROTTLE, jiggler, syn=False)
                    device.emit(uinput.ABS_X, int(sm.lx * scale), syn=False)
                    device.emit(uinput.ABS_Y, int(sm.ly * scale), syn=False)
                    device.emit(uinput.ABS_Z, int(sm.lz * scale), syn=False)
                    # Pretty sure these axes are called something different from what they are
                    device.emit(uinput.ABS_RX, int(sm.roll * scale), syn=False)
                    device.emit(uinput.ABS_RY, int(sm.pitch * scale), syn=False)
                    device.emit(uinput.ABS_RZ, int(sm.yaw * scale), syn=True)
                    jiggler = -jiggler
                    sleep(0.006)
        print('Connection to SpaceMouse lost')
    except IOError:
        print("Unable to find a SpaceMouse yet!")
        sleep(1.0)
