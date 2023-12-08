from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

root = Tk()
root.geometry("900x400")
root.title("Translator")
root.config(bg="cyan")

language = list(LANGUAGES.values())

dropdown_from = ttk.Combobox(root,state="readonly",values=language,width=30)
dropdown_from.place(relx=0.3,rely=0.2,anchor=CENTER)
dropdown_from.set("english")

label_head = Label(root,text="Language Translator",bg="cyan",font=("black",18,"bold","italic"))
label_head.place(relx=0.5,rely=0.1,anchor=CENTER)

label1 = Label(root,text="Enter Text",bg="cyan",font=("black",18,"bold"))
label1.place(relx=0.1,rely=0.2,anchor=CENTER)

text_area_from = Text(root,bg="white",height=10,width=40,wrap=WORD,padx=10,pady=10,bd=0)
text_area_from.place(relx=0.22,rely=0.5,anchor=CENTER)

dropdown_to = ttk.Combobox(root,state="readonly",values=language,width=30)
dropdown_to.place(relx=0.85,rely=0.2,anchor=CENTER)
dropdown_to.set("choose output language")

label1 = Label(root,text="Output",bg="cyan",font=("black",18,"bold"))
label1.place(relx=0.65,rely=0.2,anchor=CENTER)

text_area_to = Text(root,bg="white",height=10,width=40,wrap=WORD,padx=10,pady=10,bd=0)
text_area_to.place(relx=0.77,rely=0.5,anchor=CENTER)

def Translate():
    from_lang = dropdown_from.get()
    to_lang = dropdown_to.get()
    

    translator = Translator()
    try:
        to_text = translator.translate(text=text_area_from.get(1.0,END), src= from_lang.get(), dest= to_lang.get())
        text_area_to.delete(1.0,END)
        text_area_to.insert(END, to_text.text)

    except:
        print("Try again")






button1 = Button(root,text="Translate",font=("Arial",12),relief=FLAT,pady=7,bg="orange",command=Translate())
button1.place(relx=0.5,rely=0.8,anchor=CENTER)
root.mainloop()