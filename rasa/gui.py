from tkinter import *
from spellingCorrector import process_str
from botMessageAPI import botInput

def run():
    try:
        botInput('a', 'b')
        pass
    except Exception as e:
        raise
    WIDTH = 360
    HEIGTH = 480

    window = None
    chat_body = None
    text_input = None
    button = None

    def send(aux):
        return botInput(aux,"JOHN")

    def update_text(aux,user=True):
        if(user):
            chat_body.insert(END,"(You): " + aux + "\n\n")
            text_entry.delete(0,'end')
        else:
            chat_body.insert(END,"(Bot): " + aux + "\n\n")

    def on_click():
        aux_s = text_input.get()
        update_text(aux_s)
        aux_s = process_str(aux_s)
        update_text(send(aux_s),False)

    window = Tk()
    window.title("Potato ChatBot")
    window.geometry(str(WIDTH) + "x" + str(HEIGTH))
    window.resizable(0, 0)

    chat_body = Text(window)
    chat_body.place(x=0,
                    y=0,
                    width=WIDTH,
                    height=HEIGTH - 50)
    #chat_body.bindtags((chat_body, window, "all"))
    scrool = Scrollbar(window, orient="vertical", command=chat_body.yview)
    chat_body.configure(yscrollcommand=scrool.set)



    text_input = StringVar()
    text_entry = Entry(textvariable=text_input)
    text_entry.place(x=10,
                    y=HEIGTH-40-5,
                    width=(WIDTH*.80),
                    height=40)

    button = Button(window, text="SEND",
                    command=on_click)
    button.place(x= WIDTH-(WIDTH*.18)-5,
                    y=HEIGTH-40-5,
                    width=(WIDTH*.18),
                    height=40)

    #initialize program loop    
    window.mainloop()

