from tkinter import *
from PIL import ImageTk ,Image
from tkinter import filedialog
from tkinter.filedialog import askopenfile

window = Tk()
window.attributes('-fullscreen', True)
window.title("MR.PVT.LTD")

bg_img = PhotoImage(file="bgimg.png")

width= window.winfo_screenwidth()
height= window.winfo_screenheight()

my_canva = Canvas(window)
my_canva.pack(fill="both",expand = True)

imgTemp = Image.open("bgimg.png")
img2 = imgTemp.resize((width,height))
img = ImageTk.PhotoImage(img2)

bg1 = Image.open("bgimg.png")
resizedbg = bg1.resize((window.winfo_screenwidth(),window.winfo_screenheight()), Image.ANTIALIAS)
newbg = ImageTk.PhotoImage(resizedbg)

bg2 = Image.open("blr.png")
resizedbg2 = bg2.resize((int(window.winfo_screenwidth()/1.3),int(window.winfo_screenheight()/1.3)), Image.ANTIALIAS)
newbg2 = ImageTk.PhotoImage(resizedbg2)

bg3 = Image.open("prev.png")
resizedbg3 = bg3.resize((int(window.winfo_screenwidth()/2),int(window.winfo_screenheight()/2.2)), Image.ANTIALIAS)
newbg3 = ImageTk.PhotoImage(resizedbg3)

my_canva.create_image(0,0,image=newbg, anchor="nw")
my_canva.create_image(width/2,height/2,image=newbg2, anchor="center")
my_canva.create_image(width/2,height/1.8,image=newbg3, anchor="center")
my_canva.create_text(width/2,30, text="Segmentation of Teeth in Panoramic X-ray Image", font=("Times", "28", "bold italic"))

def minimiz():

    window.overrideredirect(False)

    window.iconify()

    window.wm_attributes('-fullscreen', 'True')
    
def exitt(event):
    window.destroy

def resizer(e):
    global bg1, resizebg, newbg
    bg1 = Image.open("bgimg.png")
    resizedbg = bg1.resize((e.width,e.height), Image.ANTIALIAS)
    newbg = ImageTk.PhotoImage(resizedbg)
    my_canva.create_image(0,0,image=newbg, anchor="nw")
    my_canva.create_text(width/2,250, text="Segmentation of Teeth in Panoramic X-ray Image", font=("Arial Bold Italic", 20))

def upload_file():
    global bg3, resizedbg3, newbg3
    f_types = [('PNG Files','*.png'),('JPG Files','*.jpg')]   # type of files to select 
    filename = filedialog.askopenfilename(filetypes=f_types)
    bg3 = Image.open(filename)
    resizedbg3 = bg3.resize((int(window.winfo_screenwidth()/2),int(window.winfo_screenheight()/2.2)), Image.ANTIALIAS)
    newbg3 = ImageTk.PhotoImage(resizedbg3)
    my_canva.create_image(width/2,height/1.8,image=newbg3, anchor="center")
        
            
b1_img = PhotoImage(file = 'ex.png')
exit_button = Button(window, borderwidth=0, text="Exit",width = 50, height = 50, image=b1_img, command=window.destroy,bg = "white")
ex1 = my_canva.create_window(10,10,anchor="nw",window = exit_button)

image = PhotoImage(file = r'mb.png')
min_button = Button(window, borderwidth=0, text="Min",width = 50, height = 50,image=image, command=minimiz,bg = "white")
min1 = my_canva.create_window(70,10,anchor="nw",window = min_button)

b3_img = PhotoImage(file = 'upm.png')
upload_button = Button(window, borderwidth=0,width = 180, height = 48, image=b3_img ,command=upload_file )
up1 = my_canva.create_window(width/2,height/4,anchor="center",window = upload_button)

#window.bind("<Configure>",resizer)
window.mainloop()