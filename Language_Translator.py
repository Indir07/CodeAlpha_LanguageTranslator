from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()
root.title("Language Translator")
root.geometry('590x370')
root.config(bg='#202640')

frame1 = Frame(root, width=590, height=370, relief=RAISED, borderwidth=5, bg='#202640')
frame1.place(x=0, y=0)

Label(root, text="Language Translator", font='Helvetica 20 bold', fg="white", bg='#202640').pack(pady=10)


def translate():
    lang = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()

    if lang == '':
        messagebox.showerror('Language translator', 'Please, Enter the text to translate!')
    else:
        translator = Translator()
        output = translator.translate(lang, dest=cl)
        text_entry2.delete("1.0", "end")  # Clear any existing text in the output text box
        text_entry2.insert(END, output.text)


def clear():
    text_entry1.delete("1.0", "end")
    text_entry2.delete("1.0", "end")


auto_variable = tk.StringVar()
auto_select = ttk.Combobox(frame1, width=27, textvariable=auto_variable, state='randomly', font=('Arial', 12, 'bold'))
auto_select['values'] = (
    'Auto Select',
)
auto_select.place(x=10, y=60)
auto_select.current(0)

lang_variable = tk.StringVar()
choose_language = ttk.Combobox(frame1, width=27, textvariable=lang_variable, state='randomly',
                               font=('Arial', 12, 'bold'))

choose_language['values'] = (
    'English',
    'German',
    'Hindi',
    'Chinese',
    'Arabic',
    'Urdu',
    'French',
    'Spanish',
    'Russian',
    'Italian',
    'Polish',
    'Persian',
    'Korean'
)
choose_language.place(x=300, y=60)
choose_language.current(0)

# Text Entry to translate text
text_entry1 = Text(frame1, width=23, height=8, borderwidth=2, relief=RIDGE,
                   font=('Arial', 15), fg="black", bg="white")
text_entry1.place(x=10, y=100)

text_entry2 = Text(frame1, width=23, height=8, borderwidth=2, relief=RIDGE,
                   font=('Arial', 15), fg="black", bg="white")
text_entry2.place(x=300, y=100)

translate_button = Button(frame1, command=translate, text="Translate", relief=RAISED, borderwidth=2,
                          font=('Arial', 15, 'bold'), bg='#034864', fg='white', cursor='hand2')
translate_button.place(x=161, y=310)

clear_button = Button(frame1, command=clear, text="Clear Text", relief=RAISED, borderwidth=2,
                      font=('Arial', 15, 'bold'), bg='#f1a22d', fg='white', cursor='hand2')
clear_button.place(x=300, y=310)

root.mainloop()
