#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import subprocess
import os
import yaml

fname = "configfile.yaml"

### variables from configfile
with open(fname, "r") as ymlfile:
   configfile = yaml.safe_load(ymlfile)

current_fps = configfile['camera_parameters']['fps']
current_camera_number = configfile['camera_parameters']['camera_number']
current_interval = configfile['config']['interval']
current_destination_path = configfile['path_vars']['dest_folder']
current_percentage = configfile['development']['percentage']
current_width = configfile['camera_parameters']['width']
current_height = configfile['camera_parameters']['height']

###
top = Tk()
top.geometry("800x400")
top.resizable(width=False, height=False)
top.title("OpenCV USB Camera Tool")

### frame
labelframe = LabelFrame(top, text = "Cam Configuration", width=250, height=80)
labelframe.pack(fill = "both", expand = "yes")

                        ######  Caption Section   ######

### caption (radio buttons)
var = StringVar()
label = Label( top, textvariable=var, relief=FLAT )

var.set("Select  video  resolution")
label.pack()
label.place(x = 280,y = 40)

### caption (day light limit)
var_day = StringVar()
label = Message( top, textvariable = var_day, relief = FLAT, width = 200 )

var_day.set("Video lenght in seconds")
label.pack()
label.place(x = 560,y = 40)

### caption (fps)
var_day = StringVar()
label = Message( top, textvariable = var_day, relief = FLAT, width = 200 )

var_day.set("Frames per secons")
label.pack()
label.place(x = 560,y = 80)

### caption (camera number)
var_day = StringVar()
label = Message( top, textvariable = var_day, relief = FLAT, width = 200 )

var_day.set("Camera number")
label.pack()
label.place(x = 560,y = 120)

### caption (Folder Size)
var_day = StringVar()
label = Message( top, textvariable = var_day, relief = FLAT, width = 200 )

var_day.set("Max percent of drive")
label.pack()
label.place(x = 560,y = 160)

### caption (width)
var_day = StringVar()
label = Message( top, textvariable = var_day, relief = FLAT, width = 200 )

var_day.set("Width")
label.pack()
label.place(x = 280,y = 70)

### caption (lenght)
var_day = StringVar()
label = Message( top, textvariable = var_day, relief = FLAT, width = 200 )

var_day.set("Height")
label.pack()
label.place(x = 390,y = 70)

                        ######  Button Section  ######

### button 1
def open_readme():
    subprocess.call(['lxterminal', '-e', 'mousepad ./readme.txt'])

B1 = Button(top, text = "Open  'ReadMe'", command = open_readme, bg='dimgrey', fg='white', width=20)
B1.place(x = 10,y = 40)

### button 2
def view_configfile():
    subprocess.call(['lxterminal', '-e', 'mousepad configfile.yaml'])

B2 = Button(top, text = "View  configfile", command = view_configfile, bg='dimgrey', fg='white', width=20)
B2.place(x = 10,y = 80)

### button 3 (start camera)
def start_camera():
    subprocess.call(['lxterminal', '-e', 'python3 video-save-5.py cam_configfile.yaml'])
    subprocess.call(['lxterminal', '-e', 'bash limit-folder-size.sh'])

B3 = Button(top, text = "Start Camera", command = start_camera, bg='green', fg='white', width=20)
B3.place(x = 10,y = 200)

### button 4 (stop camera)
def stop_camera():
    subprocess.call(['lxterminal', '-e', 'kill $(ps aux | grep "5.py" | awk "{print $2}")'])
    subprocess.call(['lxterminal', '-e', 'kill $(ps aux | grep "size.sh" | awk "{print $2}")'])

B4 = Button(top, text = "Stop Camera", command = stop_camera, bg='red', fg='white', width=20)
B4.place(x = 10,y = 240)

### Button 5  apply button (save to configfile)
def apply_button():
    #sel_resolution()
    spbx1_day_light_limit()
    spbx2_fps()
    spbx3_camera()
    spbx4_folder_size()
    spbx5_width()
    spbx6_height()
    entrybox1()
    
    with open(fname, "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
        #cfg['camera_parameters']['resolution'] = sel_resolution.selected
        cfg['camera_parameters']['fps'] = spbx2_fps.selectionn
        cfg['camera_parameters']['camera_number'] = spbx3_camera.selectionn
        cfg['config']['interval'] = spbx1_day_light_limit.selectionn
        cfg['path_vars']['dest_folder'] = entrybox1.selection
        cfg['development']['percentage'] = spbx4_folder_size.selectionn
        cfg['camera_parameters']['width'] = spbx5_width.selectionn
        cfg['camera_parameters']['height'] = spbx6_height.selectionn
    with open(fname, 'w') as outfile:
        yaml.dump(cfg, outfile, default_flow_style=False, sort_keys=False)

B4 = Button(top, text = "Apply and save to configfile", command = apply_button, bg='orange', fg='white', width=20)
B4.place(x = 10,y = 160)

### button 6 (preview)
def preview():
    subprocess.call(['lxterminal', '-e', 'python3 preview.py'])
    
B4 = Button(top, text = "Preview (q to close)", command = preview, bg='dimgrey', fg='white', width=20)
B4.place(x = 10,y = 120)

#### radiobuttons (resolution)
#def sel_resolution():
#   selected_resolution = str(var.get())
#   sel_resolution.selected = selected_resolution#\
#
root = top
#var = StringVar()
#var.set (current_resolution)
#
#R1 = Radiobutton(root, text="1920x1080,   4:3,   FOV full", variable=var, value='1920, 1080', command=sel_resolution)
#R1.place(x = 280,y = 80)
#
#R2 = Radiobutton(root, text="1280x720,   16:9,   FOV partial", variable=var, value='1280, 720', command=sel_resolution)
#R2.place(x = 280,y = 110)


                        ######  SpinBox Section  ######

### spinbox1 day light limit
def spbx1_day_light_limit():
   spbx1_selection_day = int(spbx1var.get())
   spbx1_day_light_limit.selectionn = spbx1_selection_day

spbx1var = IntVar()
spbx1var.set(current_interval)
spinbox_day = Spinbox( top, from_=1, to=1000, width=5, textvariable=spbx1var )
spinbox_day.place(x = 730,y = 40)

### spinbox2 fps
def spbx2_fps():
   spbx2_frame_per_second = int(spbx2var.get())
   spbx2_fps.selectionn = spbx2_frame_per_second

spbx2var = IntVar()
spbx2var.set(current_fps)
spinbox_fps = Spinbox( top, from_=1, to=1000, width=5, textvariable=spbx2var )
spinbox_fps.place(x = 730,y = 80)

### spinbox3 camera number
def spbx3_camera():
   spbx3_camera_number = int(spbx3var.get())
   spbx3_camera.selectionn = spbx3_camera_number

spbx3var = IntVar()
spbx3var.set(current_camera_number)
spinbox_camera = Spinbox( top, from_=0, to=18, width=5, textvariable=spbx3var )
spinbox_camera.place(x = 730,y = 120)

### spinbox4 camera number
def spbx4_folder_size():
   spbx4_percentage = int(spbx4var.get())
   spbx4_folder_size.selectionn = spbx4_percentage

spbx4var = IntVar()
spbx4var.set(current_percentage)
spinbox_percentage = Spinbox( top, from_=0, to=100, width=5, textvariable=spbx4var )
spinbox_percentage.place(x = 730,y = 160)

### spinbox5 width
def spbx5_width():
   spbx5_xwidth = int(spbx5var.get())
   spbx5_width.selectionn = spbx5_xwidth

spbx5var = IntVar()
spbx5var.set(current_width)
spinbox_width = Spinbox( top, from_=0, to=10000, width=5, textvariable=spbx5var )
spinbox_width.place(x = 280,y = 100)

### spinbox6 height
def spbx6_height():
   spbx6_yheight = int(spbx6var.get())
   spbx6_height.selectionn = spbx6_yheight

spbx6var = IntVar()
spbx6var.set(current_height)
spinbox_height = Spinbox( top, from_=0, to=10000, width=5, textvariable=spbx6var )
spinbox_height.place(x = 390,y = 100)

                        ######  Entry Box Section  ######

### entry box1 (day photo destination)
def entrybox1():
    entrbx1 = str(e1_str.get())
    entrybox1.selection = entrbx1

my_w = top
l1 = Label(my_w,  text='Video Files Destination:', width=20)  # added one Label
l1.place(x = 8, y = 310)

e1_str = StringVar()
e1_str.set(current_destination_path)
e1 = Entry(my_w,   width=70,bg='yellow', textvariable=e1_str) # added one Entry box
e1.place(x = 195, y = 310)

label = Label(root)
label.pack()

### end
top.mainloop()
