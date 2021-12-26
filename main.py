import tkinter as tk

import voice_assitant
window=tk.Tk()
window.title('Desktop Assistant')


def clickVoiceAssistantButton():
    lbl_help['text']='Voice Assistant mode'
    voice_assitant.clickVoiceAssistantButton()
    lbl_help['text']='Instructions...'


def clickOpenApplicationsButton():
    lbl_help['text']='Opening applications...'
    voice_assitant.clickOpenApplicationsButton()
    lbl_help['text']='Instructions...'



window.rowconfigure([0,1],minsize=100,weight=1)
window.columnconfigure(0,minsize=200,weight=1)

btns_frame=tk.Frame(master=window,relief=tk.RAISED, bd=3)
btns_frame.rowconfigure(0,weight=1)
btns_frame.columnconfigure([0,1],weight=1)

btn_voice_ass = tk.Button(master=btns_frame,text='Voice Assistant',command= clickVoiceAssistantButton)
btn_open_apps=tk.Button(master=btns_frame,text='Open Applications',command= clickOpenApplicationsButton)

btn_voice_ass.grid(row=0,column=0)
btn_open_apps.grid(row=0,column=1)



lbl_help = tk.Label(text='Instructions...')

btns_frame.grid(row=0, column=0,sticky='nsew')
lbl_help.grid(row=1,column=0)

height=300
width=400
window.geometry(f'{width}x{height}')
window.mainloop()