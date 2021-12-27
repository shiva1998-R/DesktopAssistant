import tkinter as tk

import voice_assistant

window=tk.Tk()
window.title('Desktop Assistant')

# configuring main window cells properties
window.rowconfigure(0,minsize=100,weight=1)
window.columnconfigure(0,minsize=200,weight=1)

# configuring buttons frame cells properties
btns_frame=tk.Frame(master=window,relief=tk.RAISED, bd=3)
btns_frame.rowconfigure(0,weight=1)
btns_frame.columnconfigure(list(range(3)),weight=1)

# Adding buttons
btn_voice_ass = tk.Button(master=btns_frame,text='Voice Assistant 🎤',command= voice_assistant.clickVoiceAssistantButton)
btn_open_apps=tk.Button(master=btns_frame,text='Open Applications',command= voice_assistant.clickOpenApplicationsButton)
btn_music_player=tk.Button(master=btns_frame,text='Play music',command= voice_assistant.clickMusicPlayerButton)

# Placing buttons
btn_voice_ass.grid(row=0,column=0)
btn_open_apps.grid(row=0,column=1)
btn_music_player.grid(row=0,column=2)
# Placing frame
btns_frame.grid(row=0, column=0,sticky='nsew')

# starting mainloop
height=300
width=400
window.geometry(f'{width}x{height}')
window.mainloop()