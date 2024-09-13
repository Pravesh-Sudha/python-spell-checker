import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")

# Update the background to a softer blue
root.config(background="#e0ebf8")

def checkSpelling():
    word = enter_text.get()  # Get the word from the entry widget
    a = TextBlob(word)       # Use TextBlob to process the word
    right = str(a.correct()) # Correct the spelling

    # Update the label with correct text
    cs = Label(root, text="Correct Text is:", font=("poppins", 20), bg="#e0ebf8", fg="#2f507c")
    cs.place(x=100, y=250)  # Place the label on the window
    
    # Update the spell label to show the corrected word
    spell.config(text=right)


# Heading label with updated colors
heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#e0ebf8", fg="#2f507c")
heading.pack(pady=(50, 0))

# Entry widget with black text for better contrast
enter_text = Entry(root, justify="center", width=30, font=("poppins", 25), bg="white", fg="#000000", border=2)
enter_text.pack(pady=20)
enter_text.focus()

# Button with a teal background and white text for a fresh look
button = Button(root, text="Check", font=("arial", 20, "bold"), fg="white", bg="red", command=checkSpelling)
button.pack(pady=(20))

# Label to show the corrected spelling with adjusted colors
spell = Label(root, font=("poppins", 20, "bold"), bg="#e0ebf8", fg="#2f507c")
spell.place(x=350, y=250)

# Start the main loop
root.mainloop()

