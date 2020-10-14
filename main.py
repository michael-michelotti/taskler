import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Text area in the top left of the GUI
        self.text_box = tk.Text(self, height=5, width=30)
        self.text_box.insert('end', 'Please enter whatever text you want here...')
        self.scroll_bar = tk.Scrollbar(self)
        self.text_box.grid(row=0, column=0)
        self.scroll_bar.grid(row=0, column=1)
        self.text_box.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.text_box.yview)

        # Radio button menu at the top right of the GUI
        BUTTONS = [
            ("Option 1", "1"),
            ("Option 2", "2"),
            ("Option 3", "3"),
            ("Option 4", "4")
        ]
        self.radio_selection = tk.StringVar()
        self.radio_selection.set("1")

        for text, mode in BUTTONS:
            b = tk.Radiobutton(self, text=text, variable=self.radio_selection, value=mode, padx=20)
            b.grid(row=0, column=2)

        # Dropdown menu on the second row of the GUI
        self.dropdown_selection = tk.StringVar()
        self.dropdown_selection.set("one")
        opt_menu = tk.OptionMenu(self, self.dropdown_selection, "one", "two", "three")
        opt_menu.grid(row=1, column=0, columnspan=2)

        # Submit and cancel buttons
        submit_button = tk.Button(self, text='Submit', command=self.submit)
        cancel_button = tk.Button(self, text='Cancel', highlightcolor='red', command=self.master.destroy)
        submit_button.grid(row=2, column=0)
        cancel_button.grid(row=2, column=1)

    def print_contents(self, event):
        print('Hi, the current entry content is: ', self.contents.get())

    def submit(self):
        print(f'The radio button selection is: {self.radio_selection.get()}\n'
              f'The dropdown selection is: {self.dropdown_selection.get()}')


root = tk.Tk()
app = Application(master=root)
app.mainloop()
