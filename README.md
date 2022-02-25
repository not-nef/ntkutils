# ntkutils

**n**efs **tk**inter **util**itie**s**

These are some useful tkinter utilities that i like to personally use.
I upload this here because someone might wants to use it.
Someone probably made something similar (and better) to this but idrc.

## Installation:

```
py -m pip install ntkutils
```

## Features:

- `ntkutils.placeappincenter(window)`: Place a tkinter window in the center of your screen. Specify the window with the `window` parameter.
- `ntkutils.ttktheme(window, source_file, theme)`: A simpler way of loading ttk themes. Parameters: `window` for the tkinter window, `source_file` for the .tcl theme file and `theme` for the theme (dark or light)
- `ntkutils.windowsetup(window, title, icon, resizeable, size)`: A simpler way of configuring your tkinter window. If you want to skip any parameters, just specify `None`.
- `ntkutils.dark_title_bar(window)`: Make the titlebar of a window dark. Credit to [Olikonsti](https://github.com/Olikonsti)

Useless features:

- `ntkutils.sunvalley(window, theme)`: Imports [rdbendes Sun-Valley ttk theme](https://github.com/rdbende/Sun-Valley-ttk-theme). I made this because i use this theme very often.
- `ntkutils.sv_msgbox(parent, title, details, icon, *, buttons)` I didnt make these, i just added them in here because i didn't want to put the file in every project where i want to use these. They were made by [rdbende](https://github.com/rdbende).

Now have fun with this! (Or dont lmao)
