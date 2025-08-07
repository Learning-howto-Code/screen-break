url="https://github.com/Learning-howto-Code/screen-break/tree/main"

import tkinter as tk
import time
import webbrowser

window = tk.Tk()

#updates #completed counter
def read_counter(): # gets number fromt txt file as var
    with open("counter.txt") as f: #reads counter.txt
        counter = int(f.read()) #converts to int
        print(counter)
        return counter
counter=read_counter()
def update_counter(): #adds onto var
    counter = read_counter()
    with open("counter.txt", "w") as f:
        counter+= 1
        f.write(str(counter)) # adds one to counter, then converts to str
    print("clicked")
    completed.config(state="disabled") #disables button for 2 seconds to prevent spammming
    window.after(5000, lambda: completed.config(state="normal"))
    time.sleep(.3)
    window.destroy()
def delete_window():# becuase buttons can only call funtions
    time.sleep(.3)
    window.destroy()
def ideas(): #returns the idea nuber in the list that corsponds to the number in ideas number.txt
   
   with open("ideas.txt") as f: #reads ideas.txt 
    ideas = f.readlines()
    num_lines=len(ideas)
    with open("idea#.txt") as f: # reads ideas to figure out where we left off
     number = int(f.read().strip())
    with open("idea#.txt", "w") as f:
        number+= 1
        if number>=num_lines:
           number=0
        f.write(str(number))
    final_idea = ideas[number] # prints the idea in the list that the var number is at
    print(number)
    return final_idea
def openlink(event=None):
   webbrowser.open_new(url)
final_idea = ideas()

#calls frames(like a grid)
top_frame = tk.Frame(master=window, width=500, height=200, bg="#2E3440" )
button_frame = tk.Frame(master=window, width=500, height=200, bg="#2E3440")
amount_completed=tk.Frame(master=window, width=500, height=200, bg="#2E3440")
link_text=tk.Frame(master=window, width=500, height=200, bg="#2E3440")

#labels
Title = tk.Label(top_frame,text="Get back to Reality!",font=("Arial Rounded MT Bold", 34), bg="#2E3440",fg="#c1d3fe" )
break_message = tk.Label(top_frame,text="Take a quick break",font=("Comic Sans MS", 22), bg="#2E3440",fg="#c1d3fe")
break_idea=tk.Label(top_frame,text=final_idea,font=("Comic Sans MS", 22), bg="#2E3440",fg="#c1d3fe")
completed_text=tk.Label(amount_completed, text=f"You've completed {counter} side quests!", font=("Comic Sans MS", 22), bg="#2E3440",fg="#c1d3fe")
repo_link=tk.Label(amount_completed, text="made with :3 by Jake",font=("Comic Sans MS", 12), bg="#2E3440",fg="white", cursor="hand2")

#buttons
completed = tk.Button(button_frame, text="Did it!", command=update_counter, width=8,height=1,fg="#434957",font=("Comic Sans MS", 12))
skipped= tk.Button(button_frame, text="Skipped it", command=delete_window, width=8,height=1,fg="#434957",font=("Comic Sans MS", 12))

#places items in frame
top_frame.grid(row=0, column=1)
button_frame.grid(row=1, column=1)
button_frame.grid_propagate(False)
button_frame.grid_columnconfigure(1, weight=2)
amount_completed.grid(row=1,column=1)
amount_completed.grid_rowconfigure(3,weight=1)
link_text.grid(row=5, column=1)
repo_link.grid(row=4,column=1)

repo_link.bind("<Button-1>", lambda e: openlink(url))

#items in top frame
Title.grid(row=0, column=0, padx=10, pady=20)
# break_message.grid(row=1, column=0)
break_idea.grid(row=2, column=0)

# items in button frame
completed.grid(row=2, column=0, padx=50)
skipped.grid(row=2, column= 2, padx=50)

#items in amount completed frame
completed_text.grid(row=1, column=1, padx=10)
#calls size of pop up window
window_width=500
window_height=300
#gets size of screen
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
#finds middle of window
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.resizable(False, False)
window.configure(bg="#2E3440")
window.title("Screen Break")
window.mainloop()



