# NTKUtils by not-nef

import tkinter
from tkinter import ttk
from functools import partial
import ctypes

win_error = "Your window specification does not appear to be a tkinter window."

def placeappincenter(window):
    try:
        window.update()
        x_coordinate = int((window.winfo_screenwidth() / 2) - (window.winfo_width() / 2))
        y_coordinate = int((window.winfo_screenheight() / 2) - (window.winfo_height() / 2))
        window.geometry("+{}+{}".format(x_coordinate, y_coordinate - 20))
    except:
        print(f"{win_error}")

def ttktheme(window, source_file, theme):
    try:
        try:
            window.tk.call("source", f"{source_file}")
        except:
            print("The specified theme file doesnt seem to exist.")

        if theme == "dark" or theme == "light":
            window.tk.call("set_theme", f"{theme}")
        else:
            print("Unknown theme specification. Use dark or light.")
    except:
        print("Your window specification does not appear to be a tkinter window.")

def windowsetup(window, title, icon, resizeable, size):
    if not title == None:
        try:
            window.title(f"{title}")
        except:
            print(f"{win_error}")
    else:
        pass

    if not icon == None:
        try:
            icon_image = tkinter.PhotoImage(file=f"{icon}")
            window.iconphoto(False, icon_image)
        except:
            print("The file that your specified path leads to either doesnt exist or your window specification is not a tkinter window")
    else:
        pass

    if not resizeable == True:
        try:
            window.resizable(False, False)
        except:
            print(f"{win_error}")
    else:
        pass

    if not size == "":
        try:
            window.geometry(f"{size}")
        except:
            print("Your size specification seems to be wrong. Do it like this: WIDTHxHEIGHT")
    else:
        pass

def sv_msgbox(parent, title, details, icon, *, buttons):
    dialog = tkinter.Toplevel()

    result = None

    big_frame = ttk.Frame(dialog)
    big_frame.pack(fill="both", expand=True)
    big_frame.columnconfigure(0, weight=1)
    big_frame.rowconfigure(0, weight=1)

    info_frame = ttk.Frame(big_frame)
    info_frame.grid(row=0, column=0, sticky="nsew")
    info_frame.columnconfigure(1, weight=1)
    info_frame.rowconfigure(1, weight=1)

    try:
        color = big_frame.tk.call("set", "themeColors::dialogInfoBg")
    except tkinter.TclError:
        color = big_frame.tk.call("ttk::style", "lookup", "TFrame", "-background")

    icon_label = ttk.Label(info_frame, image=icon, anchor="nw", background=color)
    if icon is not None:
        icon_label.grid(row=0, column=0, sticky="nsew", padx=(12, 0), pady=10, rowspan=2)

    title_label = ttk.Label(info_frame, text=title, anchor="nw", font=("Segoe UI Variable", 14, "bold"), background=color)
    title_label.grid(row=0, column=1, sticky="nsew", padx=(12, 17), pady=(10, 8))

    detail_label = ttk.Label(info_frame, text=details, anchor="nw", background=color, font=("Segoe UI", 10))
    detail_label.grid(row=1, column=1, sticky="nsew", padx=(12, 17), pady=(5, 10))

    button_frame = ttk.Frame(big_frame, padding=(22, 22, 12, 22), style="Dialog_buttons.TFrame")
    button_frame.grid(row=2, column=0, sticky="nsew")

    def on_button(value):
        nonlocal result
        result = value
        dialog.destroy()

    for index, button_value in enumerate(buttons):
        style = None
        state = None
        default = False
        sticky = "nes" if len(buttons) == 1 else "nsew"

        if len(button_value) > 2:
            if button_value[2] == "accent":
                style = "Accent.TButton"
                default = True
            elif button_value[2] == "disabled":
                state = "disabled"
            elif button_value[2] == "default":
                default = True

        button = ttk.Button(button_frame, text=button_value[0], width=18, command=partial(on_button, button_value[1]), style=style, state=state)
        if default:
            button.bind("<Return>", button["command"])
            button.focus()

        button.grid(row=0, column=index, sticky=sticky, padx=(0, 10))
        button_frame.columnconfigure(index, weight=1)

    dialog.update()

    placeappincenter(dialog)

    dialog.transient(parent)
    dialog.grab_set()

    dialog.wait_window()
    return result

def dark_title_bar(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ctypes.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ctypes.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ctypes.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ctypes.byref(value), ctypes.sizeof(value))