import Tkinter as tk 

li = "This Text Will Keep Changing Every Time You Click!".split()
global i
i=0


def toggle_text():
    global i
    global new_txt
    global old_txt
    
    if i == len(li):

        old_txt = lbl["text"]
        lbl["text"] = "Hi!"
        i=0
        new_txt = lbl["text"]
        
    else:
        old_txt = lbl["text"]
        lbl["text"] = li[i]
        new_txt = lbl["text"]
        i=i+1
        
        
            
root = tk.Tk()
root.title("Click the Button")
button = tk.Button( text="Click", width=12, command=toggle_text)
button.pack(padx=100, pady=10)
lbl = tk.Label(root, text="Hi!")
lbl.pack()
root.mainloop()
