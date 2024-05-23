# from tkinter import *
# import speedtest

# def speedtest():
#     sp=speedtest.Speedtest()
#     # sp.get_serverd
#     sp.get_servers()
#     down=str(round(sp.download()/(10**6),3))+" Mbps"
#     up=str(round(sp.upload()/(10**6),3))+" Mbps"
#     lab_down.config(text=down)
#     lab_up.config(text=up)
    
    
    

# sp=Tk()
# sp.title(" Internet SPeed Test")
# sp.geometry("500x600")
# sp.config(background="Red")

# lab=Label(sp,text="Internet Speed Test",font=("Time New Roman",30,"bold"),bg="red",fg="pink")
# lab.place(x=56,y=40,height=50,width=380)

# lab=Label(sp,text="Downlosd speed",font=("Time New Roman",30,"bold"))
# lab.place(x=56,y=130,height=50,width=380)
   
# lab_down=Label(sp,text="00",font=("Time New Roman",30,"bold"))
# lab_down.place(x=56,y=200,height=50,width=380)

# lab=Label(sp,text="Upload Speed ",font=("Time New Roman",30,"bold"))
# lab.place(x=56,y=290,height=50,width=380)

# lab_up=Label(sp,text="00",font=("Time New Roman",30,"bold"))
# lab_up.place(x=56,y=360,height=50,width=380)

# button=Button(sp,text=("Check speed"),font=("Time New Romen",30,"bold"),relief=RAISED,background="blue",command=speedtest)
# button.place(x=60,y=490,height=50,width=380)



# sp.mainloop()

from tkinter import *
import speedtest
from tkinter import ttk

def speed():
    button.config(state=DISABLED)
    progress.start()
    
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 3)) + " Mbps"
    up = str(round(sp.upload()/(10**6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)
    
    progress.stop()
    button.config(state=NORMAL)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x600")
sp.config(background="#282C34")

lab_title = Label(sp, text="Internet Speed Test", font=("Arial", 24, "bold"), bg="#282C34", fg="#61DAFB")
lab_title.pack(pady=(20, 10))

lab_down_label = Label(sp, text="Download Speed", font=("Arial", 18), bg="#282C34", fg="#ABB2BF")
lab_down_label.pack(pady=(20, 5))

lab_down = Label(sp, text="0 Mbps", font=("Arial", 18, "bold"), bg="#282C34", fg="#E06C75")
lab_down.pack(pady=(5, 20))

lab_up_label = Label(sp, text="Upload Speed", font=("Arial", 18), bg="#282C34", fg="#ABB2BF")
lab_up_label.pack(pady=(20, 5))

lab_up = Label(sp, text="0 Mbps", font=("Arial", 18, "bold"), bg="#282C34", fg="#E06C75")
lab_up.pack(pady=(5, 20))

button = Button(sp, text="Check Speed", font=("Arial", 18, "bold"), bg="#61DAFB", fg="#282C34", command=speed)
button.pack(pady=20)

progress = ttk.Progressbar(sp, orient=HORIZONTAL, length=300, mode='indeterminate')
progress.pack(pady=20)

sp.mainloop()
