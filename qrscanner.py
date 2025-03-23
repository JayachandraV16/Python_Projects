from tkinter import *
import qrcode

root=Tk()
root.title("QR Code Generator")  #Title
root.geometry("800x600")        #Geometry of window
root.config(bg="#B0E0E6")        #Background Color
root.attributes("-alpha", 0.90)  # 90% opacity (range: 0.0 to 1.0)
root.resizable(False,False)      #Checks if The  window can be resized or not(x,y)

#icon image
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("qrcode1/"+str(name)+".png") # makes file name 
    
    global Image
    Image=PhotoImage(file="qrcode1/"+str(name)+".png")
    Image_view.config(image=Image)

Image_view=Label(root,bg="#AE2321")
Image_view.pack(padx=50,pady=10,side=RIGHT)

# Title Label (Placed at the Top)
title_label =Label(root, text="QR Code Generator", font=("Century Gothic", 16, "bold"), 
fg="white", bg="#001F3F")
title_label.pack(pady=10)  # Adds some spacing

Label(root,text="Enter Title ",fg="white",bg="#191970",font=("Century Gothic", 16, "bold")).place(x=50,y=170)

title=Entry(root,width=13,font="arial 15")
title.place(x=160,y=170)

Label(root,text="Enter Link ",fg="white",bg="#191970",font=("Century Gothic", 16, "bold")).place(x=50,y=220)

entry=Entry(root,width=28,font="arial 15")
entry.place(x=50,y=250)

Button(root,text="Generate",width=12,height=2,bg="#191970",font=("Century Gothic", 10, "bold"),fg="white",command=generate).place(x=50,y=300)

root.mainloop()