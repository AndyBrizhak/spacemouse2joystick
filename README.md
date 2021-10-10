# spacemouse2joystick
This Python script reads data in from a 3DConnexion SpaceNavigator and creates a virtual joystick device through uinput.
As it uses uinput to create the virtual device, this script is only compatible with Linux.

## Dependencies
* python-uinput
* approxeng.input

Both of these can be installed through pip.

## Setup
You must first ensure that the uinput kernel module is loaded:
```
modprobe uinput
```
In order to be able to run this script as anything other than the root user, you will need to additionally do the following things:
1. Determine which group owns the `eventx` files located in `/dev/input`.
2. Add yourself to that group: `sudo usermod -aG group username`
3. Create a group "uinput": `sudo groupadd uinput`
3. Add [this udev rule](https://github.com/tuomasjjrasanen/python-uinput/blob/master/udev-rules/40-uinput.rules) to your udev rules.
4. Add yourself to the uinput group: `sudo usermod -aG uinput username`
5. Reboot.

After rebooting, you should be able to run this script as a normal user/without sudo.

## Usage
This script takes no arguments.  You can run it in the background of a terminal window using any method you like.  I prefer using good ol' `nohup` to run mine in the background and allow me to close the terminal window.

Have fun gaming!
