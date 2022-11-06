import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk
#from authtoken import auth_token

from torch import autocast
import torch
from diffusers import StableDiffusionPipeline

################################################################ Generate function and model  ################################################################################

def generate():
    with autocast(device):
        image = pipe(prompt.get(), guidance_scale=8.5)["sample"][0]
    
    image.save('generatedimage.png')
    img = ImageTk.PhotoImage(image)
    imgLabel.configure(image=img)
        

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision = "fp16", torch_dtypes=torch.float16,use_auth_token=True)#, use_auth_token = auth_token)
pipe.to(device)
#######################################################################   Creating the UI of the App   #######################################################################

app = tk.Tk()  #In order to create a tkinter application, we generally create an instance of tkinter frame, i.e., Tk().

app.geometry("532x622")
app.title("Meme maker (Stable Diffusion)")
ctk.set_appearance_mode("dark")

prompt = ctk.CTkEntry(height=40, width=512, font = ("Arial", 15), text_color = "black", fg_color="white")  # Textbox for Entering the Text
prompt.place(x=10,y=10) # The referred video advices to use text-font in CTkEntry to define the attributes of text but it resulted in an error. Using "font" worked.

imgLabel = ctk.CTkLabel(height=512,width=512)
imgLabel.place(x=10,y=110)

trigger = ctk.CTkButton(height=40,width=120, text_font = ("Arial", 15), text_color = "white", fg_color="yellow", text="Generate", command = generate)
# trigger.configure(text="Generate") ### This doesn't work ###
trigger.place(x=206,y=60)

##############################################################################################################################################################################

app.mainloop() # There is a method known by the name mainloop() is used when your application is ready to run. 
               # Mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
               

##############################################################################################################################################################################