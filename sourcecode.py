#importing the libraries
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2
import pyautogui
import datetime


#getting date and time in a string.
present=str(datetime.datetime.now())
present=present.replace(':','')
present=present.replace('-','')
present=present.replace(' ','')
present=present[:-7]


window=Tk()
window.title("Sketcher")
window.configure(background='grey')

#setting the configuration of window
window_width=1000
window_height=1000
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=(screen_width/2)-(window_width/2)
y=(screen_height/2)-(window_height/2)
window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

#selection of icons
try:
    window.iconbitmap('assets/logo.ico')
except:
    pass    
    
try:
    blackcam1=PhotoImage(file='assets/blackcam1.png')
except:
    blackcam1=None

try:
    blackcam2=PhotoImage(file='assets/blackcam2.png')
except:
    blackcam2=None

try:
    blackgallery1=PhotoImage(file='assets/blackgallery1.png')
except:
    blackgallery1=None

try:
    blackgallery2=PhotoImage(file='assets/blackgallery2.png')
except:
    blackgallery2=None

try:
    blackhome=PhotoImage(file='assets/blackhome.png')
except:
    blackhome=None



def image_address_ask():
    window.image_location=filedialog.askopenfilename(title="Select your image" , filetypes=(("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg")))
    return window.image_location


def cam_size(cap):
    cap.set(3,1600)
    cap.set(4,1000)

def img_size(img):
    new_img = cv2.resize(img,(1600,1000))
    return new_img

#original
def original(x):
    if x==0:
        cap=cv2.VideoCapture(0)
        cam_size(cap)
        while(1):
            ret, frame = cap.read()
            cv2.imshow('Original Camera',frame)
            if cv2.waitKey(1)==27:
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(1)==13:
                img_name='original_cam_{}.png'.format(present)
                cv2.imwrite(img_name,frame)
    elif x==1:
        image_address=image_address_ask()
        image=cv2.imread(image_address)
        final = img_size(image)
        while(1):
            cv2.imshow('Original Image',final)
            if cv2.waitKey(1)==27:
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(1)==13:
                img_name='original_img_{}.png'.format(present)
                cv2.imwrite(img_name,image)

#oil_painting        
def oil_painting(x):
    def oil_painting_process(y):
        result = cv2.xphoto.oilPainting(y, 7, 1)
        return result
    if x==0:
        cap = cv2.VideoCapture(0)
        cam_size(cap)
        while(1):
            ret, frame = cap.read()
            cv2.imshow('Oil Painting Camera',oil_painting_process(frame))
            if cv2.waitKey(1)==27:
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(1)==13:
                img_name='oilpainting_cam_{}.png'.format(present)
                cv2.imwrite(img_name,oil_painting_process(frame))
    elif x==1:
        image_address=image_address_ask()
        image=cv2.imread(image_address)
        result = oil_painting_process(image)
        final = img_size(result)
        while(1):
            cv2.imshow('Oil Painting Image',final)
            if cv2.waitKey(1)==27:
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(1)==13:
                img_name='oilpainting_img_{}.png'.format(present)
                cv2.imwrite(img_name,result)

#water_color        
def water_color(x):
    def water_color_process(y):
        result = cv2.stylization(y, sigma_s=60, sigma_r=0.6)
        return result
    if x==0:
        cap = cv2.VideoCapture(0)
        cam_size(cap)
        while(1):
            ret, frame = cap.read()
            cv2.imshow('Water Color Camera',water_color_process(frame))
            if cv2.waitKey(1)==27:
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(1)==13:
                img_name='watercolor_cam_{}.png'.format(present)
                cv2.imwrite(img_name,water_color_process(frame))
    elif x==1:
        image_address=image_address_ask()
        image=cv2.imread(image_address)
        result = water_color_process(image)
        final = img_size(result)
        while(1):
            cv2.imshow('Water Color Image',final)
            if cv2.waitKey(1)==27:
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(1)==13:
                img_name='watercolor_img_{}.png'.format(present)
                cv2.imwrite(img_name,result)

#sketch
def sketch(x,y):
    def sketch_process(z):
        result1, result2 = cv2.pencilSketch(z, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
        if y==0:
            return result1
        elif y==1:
            return result2
    if x==0:
        cap = cv2.VideoCapture(0)
        cam_size(cap)
        while(1):
            ret, frame = cap.read()
            if y==0:
                cv2.imshow('Pencil Sketch Camera',sketch_process(frame))
            elif y==1:
                cv2.imshow('Color Pencil Sketch Camera',sketch_process(frame))
            
            if cv2.waitKey(1)==27:
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(1)==13:
                if y==0:
                    img_name='pencilsketch_cam_{}.png'.format(present)
                elif y==1:
                    img_name='colorpencilsketch_cam_{}.png'.format(present)
                cv2.imwrite(img_name,sketch_process(frame))
    elif x==1:
        image_address=image_address_ask()
        image=cv2.imread(image_address)
        result = sketch_process(image)
        final = img_size(result)
        while(1):
            if y==0:
                cv2.imshow('Pencil Sketch Image',final)
            elif y==1:
                cv2.imshow('Color Pencil Sketch Image',final)
            
            if cv2.waitKey(1)==27:
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(1)==13:
                if y==0:
                    img_name='pencilsketch_img_{}.png'.format(present)
                elif y==1:
                    img_name='colorpencilsketch_img_{}.png'.format(present)
                cv2.imwrite(img_name,result)

#outlines
def outlines(x):
    def outlines_process(image):
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
        canny_edges = cv2.Canny(img_gray_blur, 10, 70)
        ret, result = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
        return result
    if x==0:
        cap = cv2.VideoCapture(0)
        cam_size(cap)
        while(1):
            ret, frame = cap.read()
            cv2.imshow('Outlines Camera',outlines_process(frame))
            if cv2.waitKey(1)==27:
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(1)==13:
                img_name='outlines_cam_{}.png'.format(present)
                cv2.imwrite(img_name,outlines_process(frame))
    elif x==1:
        image_address=image_address_ask()
        image=cv2.imread(image_address)
        result = outlines_process(image)
        final = img_size(result)
        while(1):
            cv2.imshow('Outlines Image',final)
            if cv2.waitKey(1)==27:
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(1)==13:
                img_name='outlines_img_{}.png'.format(present)
                cv2.imwrite(img_name,result)


#selection of tabs
def home_tab_click(x):
    if x==1:
        tabs.select(1)
    elif x==2:
        tabs.select(2)

tabs=ttk.Notebook(window)
tabs.pack()

#creations of tabs
home_tab=Frame(tabs,width=1000,height=1000,bg='red')
camera_tab=Frame(tabs,width=1000,height=1000,bg='green')
gallery_tab=Frame(tabs,width=1000,height=1000,bg='blue')

#adding tabs into the window
tabs.add(home_tab,image=blackhome)
tabs.add(camera_tab,image=blackcam2)
tabs.add(gallery_tab,image=blackgallery2)

#creation of labels
save_camera=Label(camera_tab,text="Press \"Enter\" key to save your image.",bg="green",fg="black")
save_image=Label(gallery_tab,text="Press \"Enter\" key to save your image.",bg="blue",fg="white")

close_camera=Label(camera_tab,text="Press \"Esc\" key to close you camera.",bg="green",fg="black")
close_image=Label(gallery_tab,text="Press \"Esc\" key to close you image.",bg="blue",fg="white")

#creation of buttons in home tab
camera=Button(home_tab,image=blackcam1,text="Camera Tab",borderwidth=5,padx=0,pady=0,bg='white',command=lambda:home_tab_click(1))
gallery=Button(home_tab,image=blackgallery1,text="Gallery Tab",borderwidth=5,padx=0,pady=0,bg='white',command=lambda:home_tab_click(2))

#creation of buttons in camera tab
cam_image_original=Button(camera_tab,text='Original',borderwidth=1,padx=83,pady=20,command=lambda:original(0))
cam_image_oil_painting=Button(camera_tab,text='Oil Painting',borderwidth=1,padx=65,pady=20,command=lambda:oil_painting(0))
cam_image_water_color=Button(camera_tab,text='Water Color',borderwidth=1,padx=65,pady=20,command=lambda:water_color(0))
cam_image_pencil_sketch=Button(camera_tab,text='Pencil Sketch',borderwidth=1,padx=60,pady=20,command=lambda:sketch(0,0))
cam_image_color_pencil_sketch=Button(camera_tab,text='Color Pencil Sketch',borderwidth=1,padx=33,pady=20,command=lambda:sketch(0,1))
cam_image_outlines=Button(camera_tab,text='Outline Sketch',borderwidth=1,padx=55,pady=20,command=lambda:outlines(0))

#creation of buttons in gallery tab
gal_image_original=Button(gallery_tab,text='Original',borderwidth=1,padx=83,pady=20,command=lambda:original(1))
gal_image_oil_painting=Button(gallery_tab,text='Oil Painting',borderwidth=1,padx=65,pady=20,command=lambda:oil_painting(1))
gal_image_water_color=Button(gallery_tab,text='Water Color',borderwidth=1,padx=65,pady=20,command=lambda:water_color(1))
gal_image_pencil_sketch=Button(gallery_tab,text='Pencil Sketch',borderwidth=1,padx=60,pady=20,command=lambda:sketch(1,0))
gal_image_color_pencil_sketch=Button(gallery_tab,text='Color Pencil Sketch',borderwidth=1,padx=33,pady=20,command=lambda:sketch(1,1))
gal_image_outlines=Button(gallery_tab,text='Outline Sketch',borderwidth=1,padx=55,pady=20,command=lambda:outlines(1))

#positioning of buttons in home tab.
camera.place(relx=0.3,rely=0.5,anchor=CENTER)
gallery.place(relx=0.7,rely=0.5,anchor=CENTER)

#positioning of buttons in camera tab.
save_camera.place(relx=0,rely=0)
close_camera.place(relx=0,rely=0.1)

cam_image_original.place(relx=0.5,rely=0.2,anchor=CENTER)
cam_image_oil_painting.place(relx=0.5,rely=0.3,anchor=CENTER)
cam_image_water_color.place(relx=0.5,rely=0.4,anchor=CENTER)
cam_image_pencil_sketch.place(relx=0.5,rely=0.5,anchor=CENTER)
cam_image_color_pencil_sketch.place(relx=0.5,rely=0.6,anchor=CENTER)
cam_image_outlines.place(relx=0.5,rely=0.7,anchor=CENTER)

#positioning of buttons in gallery tab.
save_image.place(relx=0,rely=0)
close_image.place(relx=0,rely=0.1)

gal_image_original.place(relx=0.5,rely=0.2,anchor=CENTER)
gal_image_oil_painting.place(relx=0.5,rely=0.3,anchor=CENTER)
gal_image_water_color.place(relx=0.5,rely=0.4,anchor=CENTER)
gal_image_pencil_sketch.place(relx=0.5,rely=0.5,anchor=CENTER)
gal_image_color_pencil_sketch.place(relx=0.5,rely=0.6,anchor=CENTER)
gal_image_outlines.place(relx=0.5,rely=0.7,anchor=CENTER)

def resize(e):
    home_tab.config(width=screen_width,height=screen_height)
    camera_tab.config(width=screen_width,height=screen_height)
    gallery_tab.config(width=screen_width,height=screen_height)


window.bind('<Configure>',resize)

window.mainloop()
