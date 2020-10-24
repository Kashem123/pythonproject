import tkinter
import cv2
import PIL .Image,PIL.ImageTk
set_width = 650
set_height= 368
window = tkinter.Tk()
window.title()
window.title("CodewithHarry Third Umpire Decision Review Kit")
cv_img = cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOE_BGR2RGB)
canvas = tkinter.canvas(window,width = set_height,height=set_width)
photo = PTL.ImageTk.PhotoImage(import=PIL.image.fromarray)(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()
window.mainloop()
