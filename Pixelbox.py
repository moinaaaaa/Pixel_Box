import tkinter as tk
from tkinter import Tk, Canvas
import os
import subprocess
import pyautogui
import keyboard
from PIL import Image, ImageTk

#Pyinstaller Pixelbox.py


testext: str = "In ROMS we trust."
blankspace: float = 10
#emulators
nesemu: str = "emulators/nestopia_1.52.0-win32/nestopia.exe"
snesemu: str = "emulators/bsnes-nightly/bsnes.exe"
n64emu: str = "emulators/Project64-3.0.1-5664-2df3434/Project64.exe"
gbcemu: str = "emulators/mGBA-0.10.5-win64/mGBA.exe"
gbaemu: str = "emulators\\mGBA-0.10.5-win64\\mGBA.exe" 
ndsemu: str = "emulators/melonDS-windows-x86_64(1)/melonDS.exe"
ps1emu: str = "emulators/duckstation-windows-x64-release/duckstation-qt-x64-ReleaseLTCG.exe"
pspemu: str = "emulators/ppsspp_win/PPSSPPWindows64.exe"

emu: str = "emulators/opensnake.exe"

rompath: str = "./roms"
rompathcoin: float = 0
bgimage: str = "BG/black.jpg"

# viewport
root = tk.Tk()
root.title("PixelBox")
root.geometry("800x600")
root.resizable(False, False)

canvas = tk.Canvas(root, width=800, height=600, bg="black")
canvas.pack()

canvas.create_text(400, 50, text=testext, font=("comic sans ms bold", 24), fill="black")
canvas.create_text(403, 54, text=testext, font=("comic sans ms bold", 24), fill="white")

print("Welcome To Pixelbox")

def execute(rom: str):
    # Run the emulator with the ROM file as an argument
    subprocess.run([emu, rom])

def on_mouse_click(event):
    # Get the closest canvas item to the mouse click
    clicked_item = canvas.find_closest(event.x, event.y)
    if clicked_item :
        # Get the ROM name of the clicked item
        rom_name = canvas.itemcget(clicked_item[0], "text")
        rom_path = os.path.join(rompath, rom_name) 

        # Check the file extension
        _, file_extension = os.path.splitext(rom_name)
        execute(rom_path)
        if file_extension == "" :
            subprocess.run(emu)
        else: 
            print(f"running absolutely nothing")
            print(f"Unsupported file type: {file_extension}")




def print_roms():
    canvas.delete("rom")
    global blankspace
    for item in os.listdir(rompath):
        # Check if the item is a file
        if os.path.isfile(os.path.join(rompath, item)) and not item.endswith(".sav" or ".exe"):
            blankspace += 20
            # Create a text item for each ROM and bind click
            text_id = canvas.create_text(402, 202 + blankspace, text=item, font=("Comic sans Ms", 12), fill="black",tags= "rom", )
            canvas.tag_raise("rom")
            text_id = canvas.create_text(400, 200 + blankspace, text=item, font=("Comic sans Ms", 12), fill="white",tags= "rom", )

            canvas.tag_bind(text_id, "<Button-1>", on_mouse_click)
            canvas.tag_bind(text_id, "<Enter>", on_mouse_hover)
            canvas.tag_bind(text_id, "<Leave>", on_mouse_leave)
    
    text_id = canvas.create_text(102, 542, text= "run emulator", font=("Comic sans Ms", 13), fill="black",tags= "ui", )
    canvas.tag_raise("ui")
    text_id = canvas.create_text(100, 540, text= "run emulator", font=("Comic sans Ms", 13), fill="white",tags= "ui", )

    canvas.tag_bind(text_id, "<Button-1>", on_mouse_click)
    canvas.tag_bind(text_id, "<Enter>", on_mouse_hover)
    canvas.tag_bind(text_id, "<Leave>", on_mouse_leave)


def buildbackdrop():
    print("backdrop built")
    background = Image.open(bgimage)
    fbg = ImageTk.PhotoImage(background)
    canvas.bg_image = fbg

    bg_id = canvas.create_image(400, 300, image=fbg)
    canvas.tag_lower(bg_id)
    

def on_mouse_hover(event):
    hovered_item = canvas.find_withtag("current")
    if hovered_item:
        canvas.itemconfig(hovered_item, fill="yellow")

def on_mouse_leave(event):
    left_item = canvas.find_withtag("current")
    if left_item:
        canvas.itemconfig(left_item, fill="white")


def leftarrow():
    print("left")
    global rompathcoin
    rompathcoin -= 1
    checkroms()
    buildbackdrop()

def rightarrow():
    print("right")
    global rompathcoin
    rompathcoin += 1
    checkroms()
    buildbackdrop()

def uparrow():
    print("up")
    global blankspace
    blankspace -= 60
    print_roms()

def downarrow():
    print("down")
    global blankspace
    print_roms()

#1 gba 2 psp 3gb 4 gbc
def checkroms():
    global emu
    global blankspace
    global rompath
    global rompathcoin
    global bgimage
    #work on bg images next

    if rompathcoin < 1 :
        rompathcoin = 8
    if rompathcoin > 8 :
        rompathcoin = 1

    blankspace = 10
    
    if rompathcoin == 1 :
        emu = nesemu
        rompath = "./roms/nes"
        bgimage = "BG/temporary_nes_bg.png"
        print_roms()
    if rompathcoin == 2:
        emu = snesemu
        rompath = "./roms/snes"
        bgimage = "BG/temporary_snes_bg.png"
        print_roms()
    if rompathcoin == 3:
        emu = n64emu
        rompath = "./roms/n64"
        bgimage = "BG/temporary_n64_bg.png"
        print_roms()
    if rompathcoin == 4:
        emu = gbaemu
        rompath = "./roms/gb+gbc"
        bgimage = "BG/temporary_gb_bg.png"
        print_roms()
    if rompathcoin == 5 :  
        emu = gbaemu
        rompath = "./roms/gba"
        bgimage = "BG/temporary_gba_bg.png"
        print_roms()
    if rompathcoin == 6 :  
        emu = ndsemu
        rompath = "./roms/nds"
        bgimage = "BG/temporary_nds_bg.png"
        print_roms()
    if rompathcoin == 7 :  
        emu = ps1emu
        rompath = "./roms/ps1"
        bgimage = "BG/temporary_ps1_bg.jpg"
        print_roms()
    if rompathcoin == 8 :  
        emu = pspemu
        rompath = "./roms/psp"
        bgimage = "BG/temporary_psp_bg.jpg"
        print_roms()

#Mouse Overdrive
def M_up():
    pyautogui.move(+0, -20, duration=0.2) 
def M_down():
    pyautogui.move(+0, +20, duration=0.2) 
def M_left():
    pyautogui.move(-60, 0, duration=0.2) 
def M_right():
    pyautogui.move(+60, 0, duration=0.2) 



#lr
keyboard.add_hotkey("x", pyautogui.click)
keyboard.add_hotkey("w", M_up)
keyboard.add_hotkey("s", M_down)
keyboard.add_hotkey("a", M_left)
keyboard.add_hotkey("d", M_right)
keyboard.add_hotkey("left", leftarrow)
keyboard.add_hotkey("right", rightarrow)
keyboard.add_hotkey("up", uparrow)
keyboard.add_hotkey("down", downarrow)





print_roms()

root.mainloop()
