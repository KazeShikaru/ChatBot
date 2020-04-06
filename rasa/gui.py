from tkinter import *
from spellingCorrector import process_str
from botMessageAPI import botInput

#size of the screen
WIDTH = 360
HEIGTH = 480
run()
#test bot input
def run():
    try:
        botInput('a', 'b')
        pass
    except Exception as e:
        raise

    #initialize some objects
    window = None
    chat_body = None
    text_input = None
    button = None

    #send message to the bot and get its answer back
    def send(aux):
        return botInput(aux,"JOHN")

    #prints the text into the screen
    def update_text(aux,user=True):
        if(user):
            chat_body.insert(END,"(You): " + aux + "\n\n")
            text_entry.delete(0,'end')
        else:
            chat_body.insert(END,"(Bot): " + aux + "\n\n")

    #on click send inputs to bot and display input and answer
    def on_click():
        aux_s = text_input.get()
        update_text(aux_s)
        aux_s = process_str(aux_s)
        update_text(send(aux_s),False)

    #initializes tkinter window root
    window = Tk()
    #window title
    window.title("Potato ChatBot")
    #window size
    window.geometry(str(WIDTH) + "x" + str(HEIGTH))
    #is the window resizable
    window.resizable(0, 0)

    #setup the text showinf widget
    chat_body = Text(window)
    chat_body.place(x=0,
                    y=0,
                    width=WIDTH,
                    height=HEIGTH - 50)
    #make the text scrolable
    scrool = Scrollbar(window, orient="vertical", command=chat_body.yview)
    chat_body.configure(yscrollcommand=scrool.set)

    #set the text input widtget
    text_input = StringVar()
    text_entry = Entry(textvariable=text_input)
    text_entry.place(x=10,
                    y=HEIGTH-40-5,
                    width=(WIDTH*.80),
                    height=40)

    #set the button to comfirm input
    button = Button(window, text="SEND",
                    command=on_click)
    button.place(x= WIDTH-(WIDTH*.18)-5,
                    y=HEIGTH-40-5,
                    width=(WIDTH*.18),
                    height=40)

    #initialize program loop    
    window.mainloop()