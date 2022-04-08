# Feature documentation:
    
- `ntkutils.placeappincenter`: Place a tkinter window in the center of your screen. Specify the window with the window parameter.
- `ntkutils.dark_title_bar`: Make the titlebar of a window dark. Credit to [Olikonsti](https://github.com/olikonsti).
- `ntkutils.blur_window_background`: Uses Mica to blur the background of a window (requires windows 11.22000 or newer).
- `ntkutils.windowsetup`: A simpler way of configuring your tkinter window.
- `ntkutils.ttktheme`: A simpler way of loading ttk themes.
- `ntkutils.isint`: Check if the specified string is an integer. It also supports checking if the integer is above or below a certain value that can be specified with the `bottomlimit` and `upperlimit` parameter.

### `ntkutils.cfgtools`:

**Getting started**:

To get started, put the following line at the top of your script (after the imports of course):
```
cfg = ntkutils.cfgtools.init({})
```
This will search for a `cfg.json` in the directory of your python file, and if none is found, create one with the provided default settings.
Provide the default settings inside the `{}` Curly brackets.

You can then acces the settings from the `cfg.json` with `cfg[setting_name_here]`.

**Saving**

You can change the config by assigning new values to the settings and then running `ntkutils.cfgtools.SaveCFG(cfg)`.

**Example**

```python
import ntkutils
import tkinter

cfg = ntkutils.cfgtools.init({"setting1": True, "setting2": "abc123"})

if cfg[setting1] == True:
    print("True")
else:
    print("False")
    
print(f"Setting 2 is {cfg[setting2]}")

root = tkinter.Tk()

save():
    cfg[setting2] = entry.get()
    ntkutils.cfgtools.SaveCFG(cfg)

entry = ttk.entry(root)
entry.pack()

btn = ttk.Button(root, command=lambda:save()).pack()

root.mainloop()
```

Of course you can swap out `cfg` for anything else, i just recommend doing it this way.
