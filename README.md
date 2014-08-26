steamMetroTiles
===============
Creates Metro Tiles for Windows 8/8.1 for your Non-Steam games (from the steam library)
Only works if you set a custom image for them (else it's useless because it will look ugly)
(Tutorial here: http://www.howtogeek.com/179370/how-to-add-non-steam-games-to-steam-and-apply-custom-icons/) - Not my contribution
Usage:

python testgrid.py "C:\Program Files (x86)\Steam\userdata\12345678" (Replace 12345678 with your ID you can find in that folder)

or if you don't have Python

dist\windows_steamgrid.exe "C:\Program Files (x86)\Steam\userdata\12345678" (Replace 12345678 with your ID you can find in that folder)

Thanks to Argony-OT on XDA for creating this tool: http://forum.xda-developers.com/showthread.php?t=1899865 (core of the whole script)
And also thanks to https://github.com/scottrice for providing the parser for the steam config file.
