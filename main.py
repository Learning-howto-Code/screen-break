import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
idea= "get a glass of water"

#calls frames(like a grid)
top_frame = tk.Frame(master=window, width=500, height=200, )
button_frame = tk.Frame(master=window, width=500, height=200)

Title = tk.Label(top_frame,text="Get back to Realtiy!",font=("Arial", 34))
break_message = tk.Label(top_frame,text="Take a quick 5 minute break",font=("Arial", 22))
break_idea=tk.Label(top_frame,text=idea,font=("Arial", 22))

#updates #completed counter
def read_counter(): # gets number fromt txt file as var
    with open("counter.txt") as f: #reads counter.txt
        counter = int(f.read()) #converts to int
        print(counter)
        return counter
def update_counter(): #adds onto var
    counter = read_counter()
    with open("counter.txt", "w") as f:
        counter+= 1
        f.write(str(counter)) # adds one to counter, then converts to str

#buttons
completed = tk.Button(button_frame, text="Did it!", command=update_counter, width=8)
skipped= tk.Button(button_frame, text="Skipped it", width=8)

#places items in frame
top_frame.grid(row=0, column=1)
button_frame.grid(row=4, column=1)
button_frame.grid_propagate(False)
button_frame.grid_columnconfigure(1, weight=2)

#items in top frame
Title.grid(row=0, column=0)
break_message.grid(row=1, column=0)
break_idea.grid(row=2, column=0)

# items in button frame
completed.grid(row=3, column=0, padx=50)
skipped.grid(row=3, column= 2, padx=50)

window.mainloop()

