import tkinter as tk

#Window initialized
window = tk.Tk()

#Window 1 with just text
greeting = tk.Label(text="Hello World",
                    foreground="white",
                    background="black",
                    width=10,
                    height=3)
greeting.pack()
window.mainloop()

#Window 2 with just a button
button = tk.Button(text="Click Here",
                    foreground="black",
                    background="red",
                    height=4,
                    width=20)
button.pack()
window.mainloop()
