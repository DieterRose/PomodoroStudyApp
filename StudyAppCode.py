from tkinter import *
import tkinter as tk
import pygame
import datetime
import pandas as pd

uhrzeiten = []
events = []
task = []
export_dict = dict() 

volume= 0.5

try: # versuche, eine Datei zu lesen, die heute schon erstellt wurde
    filename = (str(datetime.datetime.now())[:10]) + ".xlsx"
    df = pd.read_excel (filename)
    events = df['event'].tolist() # lese die Spalte event, konvertiere zu Liste und überschreibe events
    task = df['task'].tolist()
    uhrzeiten = df['Unnamed: 0'].tolist()
except: print ("did not find file from today or could not read it")    

root = Tk()
root.title("Nates Study App")

pygame.mixer.init() #das wird verwendet, um die Audiodateien abzuspielen

def play():
    pygame.mixer.music.load("RegenPomodoro.mp3")
    pygame.mixer.music.play(loops=0)
    global volume
    pygame.mixer.music.set_volume(volume)
    time = str(datetime.datetime.now())[11:19]
    date = str(datetime.datetime.now())[:10]
    start_label["text"] = "Pomodoro started on " +  date + " at " + time #dieses start_label["text"] bedeutet: in dem Objekt(?) start_label, verändere die Variable "text"
    uhrzeiten.append(time)    
    events.append ("started")
    task.append(entry.get()) #diese Zeile holt das, was der User in das Input-Feld getippt hat
    
def pause():
    pygame.mixer.music.pause()
    time = str(datetime.datetime.now())[11:19]
    pause_label["text"] = "paused studying at " + time
    uhrzeiten.append(time)    
    events.append ("paused")
    task.append("") # um zu verhindern, dass die Listen task, uhrzeiten, events "desynchronisieren"
    
def unpause():    
    pygame.mixer.music.unpause()
    time = str(datetime.datetime.now())[11:19]
    pause_label["text"] = "resumed studying at " + time
    uhrzeiten.append(time)    
    events.append ("resumed")
    task.append("")
    
def export():
    filename = (str(datetime.datetime.now())[:10]) + ".xlsx"
    x = 0
    for uhrzeit in uhrzeiten : 
        export_dict[uhrzeit] = events[x], task[x]
        x = x + 1
    pd.DataFrame.from_dict(export_dict, orient='index', columns = ['event', 'task']).to_excel(filename)    
    
def export_tocsv(): #noch nicht fertig!
    filename = (str(datetime.datetime.now())[:10]) + ".csv"
    #pd.DataFrame(events, task, index=uhrzeiten).to_csv(filename)
    x = 0
    for uhrzeit in uhrzeiten : 
        export_dict[uhrzeit] = events[x], task[x]
        x = x + 1
    pd.DataFrame.from_dict(export_dict, orient='index', columns = ['event', 'task']).to_csv(filename)

def volup():
    global volume
    volume = min (1, (volume + 0.05))
    pygame.mixer.music.set_volume(volume)

def voldown():
    global volume
    volume = max (0, (volume - 0.05))
    pygame.mixer.music.set_volume(volume)


    
export_frame = tk.Frame(root, bg='#9B2915', bd=10)
export_frame.pack(side="bottom")            

entry_frame = tk.Frame(root, bg='#9B2915', bd=10)
entry_frame.pack(side="bottom")

volume_frame = tk.Frame(root, bg='#9B2915', bd=10)
volume_frame.pack(side="bottom")
        
lower_frame = tk.Frame(root, bg='#9B2915', bd=10)
lower_frame.pack(side="bottom")

label = tk.Label(entry_frame, text = "What are you studying?", bg="white")
label.pack(side="left")

entry = tk.Entry(entry_frame, font=40)
entry.pack(side="bottom")


#buttons
pause_button = Button(lower_frame, text="Pause", font=("Helvetica", 10), command=pause)
pause_button.pack(side="right")

play_button = Button(lower_frame, text="Start Pomodoro Unit", font=("Helvetica", 15), command=play)
play_button.pack(side="left")

unpause_button = Button(lower_frame, text="Resume", font=("Helvetica", 10), command=unpause)
unpause_button.pack(side="right")

export_button = Button(export_frame, text="export to .xlsx", font=("Helvetica", 10), command=export)
export_button.pack(side="right")

export_tocsv_button = Button(export_frame, text="export to .csv", font=("Helvetica", 10), command=export_tocsv)
export_tocsv_button.pack(side="right")

volup_button = Button(volume_frame, text="louder", font=("Helvetica", 10), command=volup)
volup_button.pack(side="right")

voldown_button = Button(volume_frame, text="quieter", font=("Helvetica", 10), command=voldown)
voldown_button.pack(side="right")

#/buttons

#labels und Feedback
start_label = tk.Label(lower_frame, text = "ready to start", bg="white",)
start_label.pack(side="bottom")

pause_label = tk.Label(lower_frame, text = " ", bg="white")
pause_label.pack(side="bottom",)

root.mainloop()
