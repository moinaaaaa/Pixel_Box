import tkinter as tk
from tkinter import Tk, Canvas
import os
import subprocess
import pyautogui
import keyboard
from PIL import Image, ImageTk
from pathlib import Path


#pyinstaller Pixelbox.py


testext: str = "Around the Rom around the Roooom."

emptyspace: float = 0
blankspace: float = 10
#emulators
nesemu: str 
snesemu: str 
n64emu: str 
gbaemu: str 
ndsemu: str 
ps1emu: str 
pspemu: str 

#lileastereggthing :)
emu: str = "emulators/opensnake.exe"
rompath: str = "./roms"
rompathcoin: float = 0
bgimage: str = "BG/black.jpg"

#left_right arrows
lr_text="""
                    /$$   
                    |  $$  
                    \  $$ 
 /$$$$$$\  $$
|______/ /$$/
                    /$$/ 
                /$$/  
                |__/   
"""

la_text="""
   $$\       
  $$  |      
 $$  /       
$$  /$$$$$$\ 
\$$< \______|
 \$$\        
  \$$\       
   \__|          
"""

# viewport
root = tk.Tk()
root.title("PixelBox")
root.geometry("800x600")
root.resizable(False, False)

canvas = tk.Canvas(root, width=800, height=600, bg="black")
canvas.pack()

canvas.create_text(400, 50, text=testext, font=("comic sans ms bold", 24), fill="black")
canvas.create_text(403, 54, text=testext, font=("comic sans ms bold", 24), fill="white")

print("""                                                                        
                                                                                                                                     
▄     ▄        ▀▀█                                      ▄▄▄▄▄▄▄               ▄▄▄▄▄    ▀                  ▀▀█    ▄▄▄▄▄               
█  █  █  ▄▄▄     █     ▄▄▄    ▄▄▄   ▄▄▄▄▄   ▄▄▄            █     ▄▄▄          █   ▀█ ▄▄▄    ▄   ▄   ▄▄▄     █    █    █  ▄▄▄   ▄   ▄ 
▀ █▀█ █ █▀  █    █    █▀  ▀  █▀ ▀█  █ █ █  █▀  █           █    █▀ ▀█         █▄▄▄█▀   █     █▄█   █▀  █    █    █▄▄▄▄▀ █▀ ▀█   █▄█  
 ██ ██▀ █▀▀▀▀    █    █      █   █  █ █ █  █▀▀▀▀           █    █   █         █        █     ▄█▄   █▀▀▀▀    █    █    █ █   █   ▄█▄  
 █   █  ▀█▄▄▀    ▀▄▄  ▀█▄▄▀  ▀█▄█▀  █ █ █  ▀█▄▄▀           █    ▀█▄█▀         █      ▄▄█▄▄  ▄▀ ▀▄  ▀█▄▄▀    ▀▄▄  █▄▄▄▄▀ ▀█▄█▀  ▄▀ ▀▄ 
                                                                                                                                     
      by Moina, with love :)
                    """)

#edit paths in the config file
def get_rompaths():
    global nesemu
    global snesemu
    global n64emu
    global gbaemu
    global ndsemu
    global ps1emu
    global pspemu
    print("Current Emulators:")
    with open("Config.txt", 'r') as file:
        pathstoemu = file.read().splitlines()
        nesemu = pathstoemu[0]
        snesemu = pathstoemu[1]
        n64emu = pathstoemu[2]
        gbaemu = pathstoemu[3]
        ndsemu = pathstoemu[4]
        ps1emu = pathstoemu[5]
        pspemu = pathstoemu[6]
        
        for pathstoemu in pathstoemu :
            print(pathstoemu)

get_rompaths()

def execute(rom: str):
    # Run the emulator with the ROM file as an argument
    emu_path = Path(emu)
    if emu_path.is_file():
        if rom == "":
            print("no rom")
        elif canvas.find_withtag("rom"):
            subprocess.run([emu, rom])
        else: 
            print("error : tried to run the emulator with the rom as argument on an item which isnt a rompath")
    else:
        print("The required emulator,(" + str(emu) + ") to play this system, isnt installed. download the Emulator at: https://moina3.itch.io/pixelbox and place it in the emulators folder; if you do not find an emulators folder, (although you should have one) just make sure you create a folder named [emulators] and put your emulator there.")

def on_mouse_click(event):
    # Get the closest canvas item to the mouse click
    clicked_item = canvas.find_closest(event.x, event.y)
    if clicked_item :
        _tags = canvas.gettags(clicked_item)
        if "rom" in _tags :
            # Get the ROM name of the clicked item
            rom_name = canvas.itemcget(clicked_item[0], "text")
            rom_path = os.path.join(rompath, rom_name) 
            if rom_path:
                _, file_extension = os.path.splitext(rom_name)
                execute(rom_path)
        elif "run_emu" in _tags:
            subprocess.run(emu)
        else:
            if "LR" in _tags:
                rightarrow()
            elif "LA" in _tags:
                leftarrow()
            

def print_roms(printr : bool):
    if printr:
        print ("    ")
        print ("rompath:")
        print (rompath)
        print("roms:")
    canvas.delete("rom")
    global blankspace
    blankspace = 20
    for item in os.listdir(rompath):
        # Check if the item is a file
        if os.path.isfile(os.path.join(rompath, item)) and not item.endswith(".sav") or item.endswith(".exe"):
            if printr:
                print(item)
            blankspace += 20 
            # Create a text item for each ROM and bind click
            text_id = canvas.create_text(402, 202 + blankspace + emptyspace, text=item, font=("Comic sans Ms", 12), fill="black",tags= "rom", )
            canvas.tag_raise("rom")
            text_id = canvas.create_text(400, 200 + blankspace + emptyspace, text=item, font=("Comic sans Ms", 12), fill="white",tags= "rom", )

            canvas.tag_bind(text_id, "<Button-1>", on_mouse_click)
            canvas.tag_bind(text_id, "<Enter>", on_mouse_hover)
            canvas.tag_bind(text_id, "<Leave>", on_mouse_leave)
    
    text_id = canvas.create_text(102, 542, text= "run emulator", font=("Comic sans Ms", 13), fill="black",tags= "run emu background", )
    text_id = canvas.create_text(100, 540, text= "run emulator", font=("Comic sans Ms", 13), fill="white",tags= "run_emu", )

    canvas.tag_bind(text_id, "<Button-1>", on_mouse_click)
    canvas.tag_bind(text_id, "<Enter>", on_mouse_hover)
    canvas.tag_bind(text_id, "<Leave>", on_mouse_leave)


def buildbackdrop():
    canvas.delete("bg_id")
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
    global rompathcoin
    rompathcoin -= 1
    checkroms()
    buildbackdrop()

def rightarrow():
    global rompathcoin
    rompathcoin += 1
    checkroms()
    buildbackdrop()

def uparrow():
    global emptyspace
    emptyspace -= 20
    print_roms(False)

def downarrow():
    global emptyspace
    emptyspace += 20
    print_roms(False)

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
    if rompathcoin == 2:
        emu = snesemu
        rompath = "./roms/snes"
        bgimage = "BG/temporary_snes_bg.png"
    if rompathcoin == 3:
        emu = n64emu
        rompath = "./roms/n64"
        bgimage = "BG/temporary_n64_bg.png"
    if rompathcoin == 4:
        emu = gbaemu
        rompath = "./roms/gb+gbc"
        bgimage = "BG/temporary_gb_bg.png"
    if rompathcoin == 5 :  
        emu = gbaemu
        rompath = "./roms/gba"
        bgimage = "BG/temporary_gba_bg.png"
    if rompathcoin == 6 :  
        emu = ndsemu
        rompath = "./roms/nds"
        bgimage = "BG/temporary_nds_bg.png"
    if rompathcoin == 7 :  
        emu = ps1emu
        rompath = "./roms/ps1"
        bgimage = "BG/temporary_ps1_bg.jpg"
    if rompathcoin == 8 :  
        emu = pspemu
        rompath = "./roms/psp"
        bgimage = "BG/temporary_psp_bg.jpg"
    print_roms(True)

def draw_arrows():
    text_id = canvas.create_text(62, 202 + blankspace + emptyspace, text = la_text, font=("Comic sans Ms", 6), fill="black",tags= "LA", )
    text_id = canvas.tag_raise("rom")
    text_id = canvas.create_text(60, 200 + blankspace + emptyspace, text = la_text, font=("Comic sans Ms", 6), fill="white",tags= "LA", )

    canvas.tag_bind(text_id, "<Button-1>", on_mouse_click)
    canvas.tag_bind(text_id, "<Enter>", on_mouse_hover)
    canvas.tag_bind(text_id, "<Leave>", on_mouse_leave)

    text_id = canvas.create_text(750, 202 + blankspace + emptyspace, text = lr_text, font=("Comic sans Ms", 6), fill="black",tags= "LR", )
    text_id = canvas.tag_raise("rom")
    text_id = canvas.create_text(748, 200 + blankspace + emptyspace, text = lr_text, font=("Comic sans Ms", 6), fill="white",tags= "LR", )

    canvas.tag_bind(text_id, "<Button-1>", on_mouse_click)
    canvas.tag_bind(text_id, "<Enter>", on_mouse_hover)
    canvas.tag_bind(text_id, "<Leave>", on_mouse_leave)
#Mouse Overdrive
def M_up():
    pyautogui.move(+0, -20, duration=0.2) 
def M_down():
    pyautogui.move(+0, +20, duration=0.2) 
def M_left():
    pyautogui.move(-60, 0, duration=0.2) 
def M_right():
    pyautogui.move(+60, 0, duration=0.2) 



#bindings
root.bind("<MouseWheel>", lambda e: uparrow() if e.delta > 0 else downarrow())
keyboard.add_hotkey("x", pyautogui.click)
keyboard.add_hotkey("w", M_up)
keyboard.add_hotkey("s", M_down)
keyboard.add_hotkey("a", M_left)
keyboard.add_hotkey("d", M_right)
keyboard.add_hotkey("left", leftarrow)
keyboard.add_hotkey("right", rightarrow)
keyboard.add_hotkey("up", uparrow)
keyboard.add_hotkey("down", downarrow)

print_roms(False)
draw_arrows()

root.mainloop()
