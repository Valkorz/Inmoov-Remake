import tkinter 
import customtkinter
from Voices.Voice import voice
from Detect.Detection_hand import detection
from Identification.Checking import identify
#from LLM.Illama2_API import api_called


root_window = tkinter.Tk()
root_window.geometry("720x720")
root_window.title("Inmoov")

# Criando a label sem usar pack()
label = customtkinter.CTkLabel(root_window, text="Welcome", font=("arial bold", 32))
label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

def get_text(text_box):
    input_text = text_box.get("1.0", tkinter.END)
    print("Info get from the input thext")
    #Calling the LLAMA API and recieving a string (input_text = returned string)
    #response = api_called(input_text)
    #voice(response)  

def button_function1():
    print("Open Camera")
    detection()
    
def button_function2():
    print("Voice Talk")
    window1 = tkinter.Toplevel(root_window)
    window1.geometry("720x720")
    window1.title("Voice window")
    
    text_box = tkinter.Text(master=window1, width=100, height=10)
    text_box.pack()
    
    button_window1_1 = customtkinter.CTkButton(master=window1, 
                                               corner_radius=10, 
                                               command=lambda: get_text(text_box), 
                                               text="Click to submit")
    button_window1_1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    
def button_function3():
    print("Sign Language")
    
def button_function4():
    identify(1)
    
    

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
                                  text="Image Classifier")
button3.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

button4 = customtkinter.CTkButton(master=root_window, 
                                  corner_radius=10, 
                                  command=button_function4, 
                                  text="Sign UP")
button4.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)



root_window.mainloop()
