import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk
from auth_token import AuthToken

from torch import autocast
from diffusers import StableDiffusionPipeline

##        Creating the App           ##

app = tk.Tk()  #In order to create a tkinter application, we generally create an instance of tkinter frame, i.e., Tk().

app.geometry("532x622")
app.title("Meme maker (Stable Diffusion)")
ctk.set_appearance_mode("dark")

app.mainloop() # There is a method known by the name mainloop() is used when your application is ready to run. 
               # Mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
