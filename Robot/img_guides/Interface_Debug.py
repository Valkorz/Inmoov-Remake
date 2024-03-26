import tkinter 
import customtkinter
from Voices.Voice import voice
from Detection import detection

root_window = tkinter.Tk()
root_window.geometry("1280x720")
root_window.title("Inmoov")

# Criando a label sem usar pack()
label = customtkinter.CTkLabel(root_window, text="Welcome", font=("arial bold", 32))
label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

def get_text(text_box):
    input_text = text_box.get("1.0", tkinter.END)
    voice(input_text)

def button_function1():
    print("Open Camera")
    detection()
    
def button_function2():
    print("Voice Talk")
    window1 = tkinter.Toplevel(root_window)
    window1.geometry("800x400")
    window1.title("Voice window")
    
    text_box = tkinter.Text(master=window1, width=100, height=10)
    text_box.pack()
    
    button_window1_1 = customtkinter.CTkButton(master=window1, corner_radius=10, 
                                               command=lambda: get_text(text_box), 
                                               text="Click to submit")
    button_window1_1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    
def button_function3():
    print("Sign Language")

button1 = customtkinter.CTkButton(master=root_window, corner_radius=10, 
                                  command=button_function1, 
                                  text="Open Camera")
button1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

button2 = customtkinter.CTkButton(master=root_window, corner_radius=10, 
                                  command=button_function2, 
                                  text="Voice Talk")
button2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button3 = customtkinter.CTkButton(master=root_window, 
                                  corner_radius=10, 
                                  command=button_function3, 
                                  text="Sign Language")
button3.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

root_window.mainloop()
