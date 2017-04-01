import Tkinter as tk
def toggle():
    index_dict={"True": "False", "False": "True"}
    index[0] = index_dict[index[0]]
    t_btn['text'] = index[0]
root = tk.Tk()
root.title("Click the Button")
index=["True"]
t_btn = tk.Button(text=index[0], width=35, command=toggle)
t_btn.pack(pady=5)
root.mainloop()
