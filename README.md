## OpenRazer_GameOflife
### Run Game of Life on your favourite Razer Keyboard!

#### Requirements:

- python-notify2, available on AUR
- openrazer-meta, available on AUR
- Python 3.x
- NumPy library, available via pip
- linux-headers, available on pacman repository

After setting all this up, if you didn't do it already, run this command:

``sudo gpasswd -a <YOURUSERNAME> plugdev``

and reboot your system in order to let the OpenRazer Driver to run properly.

> All this code is tested under Arch Linux, it should also work in other distros!


### Usage:

Run the game:

``python main.py``

Restore keyboard after usage:

``python main.py reset``

##### This project is based on OpenRazer drivers

[OpenRazer Website](https://openrazer.github.io/)
