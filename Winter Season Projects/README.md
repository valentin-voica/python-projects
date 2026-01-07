## 3D Xmas Tree

[3D Xmas Tree for Raspberry Pi](https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi)

This example sets all the red LEDs to flicker randomly.

## SnowPi

[Ryanteck SnowPi - GPIO Zero Guide](https://thepihut.com/blogs/raspberry-pi-tutorials/ryanteck-snowpi-gpio-zero-guide)

This example sets separate patterns for the nose, eyes and body LEDs.

## Run the programs at boot

To run the scripts automatically, every time after a reboot, create a `systemd` service (the example below was created for the Xmas tree; adjust it accordingly for the snowman):

`sudo nano /etc/systemd/system/xmas-tree.service`

And add at the following:

```
[Unit]
Description=Switch the Christmass Tree lights on.

[Service]
Type=simple
ExecStart=python3 /home/valentin/xmas-tree.py

[Install]
WantedBy=multi-user.target

```

Set the correct permissions:

`sudo chmod 644 /etc/systemd/system/xmas-tree.service`

Enable the service to run at boot:

`sudo systemctl enable xmastree.service`

Reboot the Raspberry Pi and check if the script runs automatically:

`sudo reboot`
