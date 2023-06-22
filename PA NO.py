#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
# GUI
root = Tk()
root.title("Parki Assist")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"



# Send function
def send():
    
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower()
    
    

    if (user == "hello" or user== "hi"):
        txt.insert(END, "\n\n" + "Bot -> Hi there, how can I help?")

    elif (user == "can you tell me about Parkinson's disease" or user=="what is parkinson's disease"):
        txt.insert(END, "\n\n" + "Bot -> Parkinson’s disease is an age-related degenerative brain condition, meaning it causes " "\n" "\t" "parts of your brain to deteriorate. It’s best known for causing slowed movements,""\n" "\t" "tremors, balance" " problems and more. Most cases happen for unknown reasons, but ""\n" "\t""some are inherited. The condition"  " isn’t curable, but there are many different treatment" "\n" "\t" "options.")

    elif (user == "are there any treatments" or user=="what is the treatment"):
        txt.insert(END, "\n\n" + "Bot -> For now, Parkinson’s disease is not curable, but there are multiple ways to manage its\n symptoms.")

    elif (user == "what causes it" or user == "what are the causes"):
        txt.insert(END, "\n\n" + "Bot -> There are various causes including genetic factors,environmental factors , protein \n aggregation etc.")

    elif (user == "thanks" or user == "thank you" or user == "now its my time"):
        txt.insert(END, "\n\n" + "Bot -> Any time !")

    elif (user == "is it contagious"):
        txt.insert(END, "\n\n" + "Bot -> Parkinson’s disease is not contagious, and you can't contract it from another person.")

    elif (user == "is there a platform to know more about the disease" or user == "where to know more about the disease"):
        txt.insert(END, "\n\n" + "Bot -> Please visit the following website \n https://www.parkinsonssocietyindia.com/locate-a-support-center/")

    else:
        txt.insert(END, "\n\n" + "Bot -> Sorry! I didn't understand that")

    e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=75)
txt.grid(row=1, column=0, columnspan=2)
txt.insert(END,"\n" + "Bot -> Hi there, Parki Assist at your service.Please let me know how I can help" "\n")
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=70)
e.grid(row=3, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,command=send).grid(row=3, column=1)
#root.geometry("800x600")

root.mainloop() 


# In[ ]:




