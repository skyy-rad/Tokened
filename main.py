from pymongo import MongoClient
import customtkinter as ctk
from login import loginPage
from signup import signUpPage
from student import student

# Database Link
cluster = MongoClient("mongodb+srv://riyon:<password>@tokened.urunqhy.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Tokened"]
collection = db["userInfo"]


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.title("Tokened")
        self.geometry("800x500")
        self.resizable(False, False)

        container = ctk.CTkFrame(self, height=800, width=500)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (loginPage, signUpPage, student): # Add new pages here
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Starts on Login Page
        self.show_frame(loginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


if __name__ == "__main__": # Runs the window
    app = App()
    app.mainloop()
