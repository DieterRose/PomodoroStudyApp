# PomodoroStudyApp
This is a small program to help me study. It opens a GUI using tkinter and plays an audio file that is 25 minutes long (which I think is a perfect duration for studying).

Using the text field, a user can input what it is they're studying. This information is saved when starting a pomodoro session and can be exported to .xlsx and .csv, using the buttons, respectively. Watch out, as this information will be lost when closing the program if you didn't export it.

The files will be exported to the same folder where the code is saved. 
The program attempts to read an .xlsx file with the current date when starting up. This allows for documenting progress and closing the app inbetween sessions on the same day.

The file "RegenPomodoro.mp3" is necessary for the app to function. You could, of course, modify the file to your needs or rename a different audio-based-timer to "RegenPomodoro.mp3".

Have fun studying! Bonus points if you recognize the audio cue that signals the end of the session.
