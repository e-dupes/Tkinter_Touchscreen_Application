#imports
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import Toplevel
from tkhtmlview import HTMLLabel

#this class is the GUI
class MyGUI:

    #initialize the GUI
    def __init__(self):

        self.bg_color = '#557A95' #All the colours available to use
        self.color_1 = '#5D5C61'
        self.color_2 = '#379683'
        self.color_3 = '#7395AE'
        self.color_4 = '#B1A296'

        self.font = 'Modern' #CHANGE THIS

        self.current_image_staff = -1 #for the slideshows, they all start at image 1
        self.current_image_itri = -1
        self.current_image_collab = -1
        self.current_image_courses = -1
        self.current_image_info = -1
        self.current_image_pearses = -1
        
        #If twitter API works someday...
        '''
        self.consumer_key = 'jpDYw1GARzL4OccWwl2FgCaKC'
        self.consumer_secret = '3ZYRXx38gvNJMn84AUgoxt0SlVlSG3loooH6tEAu7p63DJXV89'
        self.access_token = '1303324731832139776-ANyt9azsQvqC8Fk5b8DS6FwlVdTLvu'
        self.access_token_secret = 'OVoypIunqjTfU3hFwCrKYW5XvuduoascFytC7Ra24RYXx'

        #Bearer token: AAAAAAAAAAAAAAAAAAAAAI8QngEAAAAAvwytZ5ZPj8PiTE9Hs0cPu5u7ovE%3DhO6ZMgYGGqOu37vj5Xhh2Qzu8m8PrcSyYwvGJ04lR9ZWuGV4Cv
        
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)
        
        '''

        #This creates the actual gui, the main window
        self.root = tk.Tk()
        self.root.title('Main Menu')
        self.root.geometry('1440x900')
        self.root.configure(background=self.bg_color)

        #This creates the menu bar that is generated at the top of the GUI
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Close', command=self.on_closing)
        self.menubar.add_cascade(menu=self.filemenu, label='File')
        self.root.config(menu=self.menubar)

        #The welcome message
        self.welcome_message = tk.Label(self.root, text='Welcome to the PHI!', font=(self.font, 55), fg=self.color_4)
        self.welcome_message.pack(padx=10, pady=10)
        self.welcome_message.place(x=20, y=20)
        self.welcome_message.configure(background=self.bg_color)

        #More text
        self.ask = tk.Label(self.root, text='What would you like to learn about today?', font=(self.font, 25), fg=self.color_4)
        self.ask.place(x=50, y=150)
        self.ask.configure(background=self.bg_color)

        #Image on main page
        self.image_1 = Image.open('main_images/phi_image.jpeg')
        self.image_1 = self.image_1.resize((575, 425), Image.LANCZOS) #or ANTIALIAS
        self.picture_1 = ImageTk.PhotoImage(self.image_1)
        self.label_image_1 = tk.Label(image=self.picture_1)
        self.label_image_1.place(x=750, y=50)

        #link to twitter acount
        self.my_label = HTMLLabel(self.root, html='<a class="twitter-timeline" href="https://twitter.com/PearseHub?ref_src=twsrc%5Etfw">Tweets by PearseHub</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> ')
        self.my_label.configure(height=20, width=40)
        self.my_label.place(x=1100, y=550)

        #more text
        self.twitter_label = tk.Label(self.root, text='Click the link to the right to access the\n PHI Twitter account!', font=(self.font, 25), fg=self.color_4)
        self.twitter_label.place(x=650, y=750)
        self.twitter_label.configure(background=self.bg_color)

        #Text above button
        self.label_but_1 = tk.Label(self.root, text='The PHI Staff', font=(self.font, 22), fg=self.color_4)
        self.label_but_1.place(x=350, y=260)
        self.label_but_1.configure(background=self.bg_color)
        # Open the image file
        image_1 = Image.open('main_images/staff.png')
        # Resize the image 
        w_1, h_1 = image_1.size
        min_1 = 400/w_1 if 400/w_1 < 150/h_1 else 150/h_1
        w_1 = int(w_1 * min_1)
        h_1 = int(h_1 * min_1)
        image_1 = image_1.resize((w_1, h_1), Image.LANCZOS)  # Adjust the size as desired
        # Convert the image to PhotoImage format
        photoimage_1 = ImageTk.PhotoImage(image_1)
        #Create the button
        self.button_staff = tk.Button(self.root, image=photoimage_1, text='Staff', font=(self.font, 18), command=self.open_staff, height=h_1, width=w_1, bg=self.bg_color)
        self.button_staff.image = photoimage_1  # Store a reference to avoid garbage collection
        self.button_staff.place(x=350, y=300)
        
        self.label_but_2 = tk.Label(self.root, text='What do we do?', font=(self.font, 22), fg=self.color_4)
        self.label_but_2.place(x=350, y=460)
        self.label_but_2.configure(background=self.bg_color)
         # Open the image file
        image_2 = Image.open('main_images/info.png')
        # Resize the image 
        w_2, h_2 = image_2.size
        min_2 = 400/w_2 if 400/w_2 < 150/h_2 else 150/h_2
        w_2 = int(w_2 * min_2)
        h_2 = int(h_2 * min_2)
        image_2 = image_2.resize((w_2, h_2), Image.LANCZOS)  # Adjust the size as desired
        # Convert the image to PhotoImage format
        photoimage_2 = ImageTk.PhotoImage(image_2)
        #Create the button
        self.button_info = tk.Button(self.root, image=photoimage_2, text='Info', font=(self.font, 18), command = self.open_info, height=h_2, width=w_2)
        self.button_info.pack(padx=10, pady=10)
        self.button_info.place(x=350, y=500)

        self.label_but_3 = tk.Label(self.root, text='I-TRI', font=(self.font, 22), fg=self.color_4)
        self.label_but_3.place(x=350, y=660)
        self.label_but_3.configure(background=self.bg_color)
        # Open the image file
        image_3 = Image.open('main_images/itri.png')
        # Resize the image if needed
        w_3, h_3 = image_3.size
        min_3 = 400/w_3 if 400/w_3 < 150/h_3 else 150/h_3
        w_3 = int(w_3 * min_3)
        h_3 = int(h_3 * min_3)
        image_3 = image_3.resize((w_3, h_3), Image.LANCZOS)  # Adjust the size as desired
        # Convert the image to PhotoImage format
        photoimage_3 = ImageTk.PhotoImage(image_3)
        self.button_itri = tk.Button(self.root, image=photoimage_3, text='I-TRI', font=(self.font, 18), command = self.open_itri, height=h_3, width=w_3)
        self.button_itri.pack(padx=10, pady=10)
        self.button_itri.place(x=350, y=700)


        self.label_but_4 = tk.Label(self.root, text='PHI Courses', font=(self.font, 22), fg=self.color_4)
        self.label_but_4.place(x=50, y=260)
        self.label_but_4.configure(background=self.bg_color)
        # Open the image file
        image_4 = Image.open('main_images/courses.png')
        # Resize the image if needed
        w_4, h_4 = image_4.size
        min_4 = 400/w_4 if 400/w_4 < 150/h_4 else 150/h_4
        w_4 = int(w_4 * min_4)
        h_4 = int(h_4 * min_4)
        image_4 = image_4.resize((w_4, h_4), Image.LANCZOS)  # Adjust the size as desired
        # Convert the image to PhotoImage format
        photoimage_4 = ImageTk.PhotoImage(image_4)
        self.button_courses = tk.Button(self.root, image=photoimage_4, text='Courses', font=(self.font, 18), command = self.open_courses, height=h_4, width=w_4)
        self.button_courses.pack(padx=10, pady=10)
        self.button_courses.place(x=50, y=300)

        self.label_but_5 = tk.Label(self.root, text='Collaborations', font=(self.font, 22), fg=self.color_4)
        self.label_but_5.place(x=50, y=460)
        self.label_but_5.configure(background=self.bg_color)
        # Open the image file
        image_5 = Image.open('main_images/collab.png')
        # Resize the image if needed
        w_5, h_5 = image_5.size
        min_5 = 400/w_5 if 400/w_5 < 150/h_5 else 150/h_5
        w_5 = int(w_5 * min_5)
        h_5 = int(h_5 * min_5)
        image_5 = image_5.resize((w_5, h_5), Image.LANCZOS)  # Adjust the size as desired
        # Convert the image to PhotoImage format
        photoimage_5 = ImageTk.PhotoImage(image_5)
        self.button_collaboration = tk.Button(self.root, image=photoimage_5, text='Collaboration', font=(self.font, 18), command = self.open_collaboration, height=h_5, width=w_5)
        self.button_collaboration.pack(padx=10, pady=10)
        self.button_collaboration.place(x=50, y=500)

        self.label_but_6 = tk.Label(self.root, text='The Pearses', font=(self.font, 22), fg=self.color_4)
        self.label_but_6.place(x=50, y=660)
        self.label_but_6.configure(background=self.bg_color)
        # Open the image file
        image_6 = Image.open('collab/IMG_0988.jpeg')
        # Resize the image if needed
        w_6, h_6 = image_6.size
        min_6 = 400/w_6 if 400/w_6 < 150/h_6 else 150/h_6
        w_6 = int(w_6 * min_6)
        h_6 = int(h_6 * min_6)
        image_6 = image_6.resize((w_6, h_6), Image.LANCZOS)  # Adjust the size as desired
        # Convert the image to PhotoImage format
        photoimage_6 = ImageTk.PhotoImage(image_6)
        self.button_pearses = tk.Button(self.root, image=photoimage_6, text='The Pearses', font=(self.font, 18), command=self.open_pearses, height=h_6, width=w_6)
        self.button_pearses.pack(padx=10, pady=10)
        self.button_pearses.place(x=50, y=700)

        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Do you really want to quit?'):
            self.root.destroy()
    
    def open_staff(self):
        w2 = Toplevel()
        w2.title('PHI Staff')
        w2.geometry('1440x900')
        w2.configure(background=self.color_1)
        back_button = tk.Button(w2, text='Back', font=(self.font, 18), command=w2.destroy) 
        back_button.place(x=30, y=20)
        welcome_message = tk.Label(w2, text='The PHI Staff', font=(self.font, 55), fg=self.color_2)
        welcome_message.configure(background=self.color_1)
        welcome_message.place(x=130, y=30)
        with open('staff/staff.txt', 'r') as file:
            lines = file.readlines()
        max_width = 45  # Maximum width of the label
        joined_lines = '\n'.join(lines)
        message = tk.Label(w2, text=joined_lines, font=(self.font, 18), fg=self.color_3, bd=1, relief='sunken', width=max_width)
        message.place(x=30, y=130)
        message.configure(background=self.color_1, justify='left')
        
        image_files = ['staff/IMG_1274.jpg', 'staff/IMG_1453.jpg', 'staff/IMG_8856.jpg', 'staff/IMG_0610.jpg', 'staff/IMG_1941.jpg', 'staff/IMG_1960.jpg', 'staff/IMG_1188.jpg']
        images = []

        def change_image():
            self.current_image_staff = (self.current_image_staff + 1) % len(images)
            imageLabel.configure(image=images[self.current_image_staff])
            infoLabel.configure(text=f'Image {self.current_image_staff + 1} of {len(images)}')

        imageLabel = tk.Label(w2)
        infoLabel = tk.Label(w2, font=(self.font, 20))
        button = tk.Button(w2, text='Next Image', width=30, height=5, bg=self.color_1, fg=self.color_2, command=change_image)

        imageLabel.place(x=600, y=130)
        infoLabel.place(x=600, y=130)
        button.place(x=750, y=750)

        for file in image_files:
                image = Image.open(file)
                w, h = image.size
                min = 800/w if 800/w < 600/h else 600/h
                w = int(w * min)
                h = int(h * min)
                image = image.resize((w, h))
                photo = ImageTk.PhotoImage(image)
                images.append(photo)
         
        change_image()  

        link_site = HTMLLabel(w2, html='<a href="https://www.loomischaffee.org/academics/pearse-hub-for-innovation">Learn more about the staff on the Loomis Website!</a>')
        link_site.configure(height=10, width=20)
        link_site.place(x=1330, y=750)

    def open_info(self):
        w3=Toplevel()
        w3.title('What do we do')
        w3.geometry('1440x900')
        w3.configure(background=self.color_1)
        back_button = tk.Button(w3, text='Back', font=(self.font, 18), command=w3.destroy) 
        back_button.place(x=20, y=20)
        welcome_message = tk.Label(w3, text='What do we do?', font=(self.font, 55), fg=self.color_2)
        welcome_message.configure(background=self.color_1)
        welcome_message.place(x=130, y=30)
        with open('info/info.txt', 'r') as file:
            lines = file.readlines()
        max_width = 45  # Maximum width of the label
        joined_lines = '\n'.join(lines)
        message = tk.Label(w3, text=joined_lines, font=(self.font, 18), fg=self.color_3, bd=1, relief='sunken', width=max_width)
        message.place(x=30, y=130)
        message.configure(background=self.color_1, justify='left')

        image_files = ['info/IMG_1979.jpg', 'info/IMG_9330.jpg', 'info/IMG_8442.jpg', 'info/IMG_8544.jpg', 'info/IMG_8689.jpg', 'info/IMG_1111.jpg']
        images = []

        def change_image():
            self.current_image_info = (self.current_image_info + 1) % len(images)
            imageLabel.configure(image=images[self.current_image_info])
            infoLabel.configure(text=f'Image {self.current_image_info + 1} of {len(images)}')

        imageLabel = tk.Label(w3)
        infoLabel = tk.Label(w3, font=(self.font, 20))
        button = tk.Button(w3, text='Next Image', width=30, height=5, bg=self.color_1, fg=self.color_2, command=change_image)

        imageLabel.place(x=600, y=130)
        infoLabel.place(x=600, y=130)
        button.place(x=750, y=750)

        for file in image_files:
            image = Image.open(file)
            w, h = image.size
            min = 800/w if 800/w < 600/h else 600/h
            w = int(w * min)
            h = int(h * min)
            image = image.resize((w, h))
            photo = ImageTk.PhotoImage(image)
            images.append(photo)

        change_image()

    def open_itri(self):
        w4=Toplevel()
        w4.title('I-TRI')
        w4.geometry('1440x900')
        w4.configure(background=self.color_1)
        back_button = tk.Button(w4, text='Back', font=(self.font, 18), command=w4.destroy) 
        back_button.place(x=20, y=20)
        welcome_message = tk.Label(w4, text='I-TRI', font=(self.font, 55), fg=self.color_2)
        welcome_message.configure(background=self.color_1)
        welcome_message.place(x=130, y=30)
        with open('itri/itri.txt', 'r') as file:
            lines = file.readlines()
        max_width = 45  # Maximum width of the label
        joined_lines = '\n'.join(lines)
        message = tk.Label(w4, text=joined_lines, font=(self.font, 18), fg=self.color_3, bd=1, relief='sunken', width=max_width)
        message.place(x=30, y=130)
        message.configure(background=self.color_1, justify='left')

        image_files = ['itri/IMG_2304.jpg', 'itri/IMG_2326.jpg', 'itri/IMG_2333.jpg', 'itri/IMG_2356.jpg', 'itri/IMG_2491.jpg', 'itri/IMG_2498.jpg', 'itri/IMG_2580.jpg', 'itri/IMG_2597.jpg', 'itri/IMG_9456.jpg']
        images = []

        def change_image():
            self.current_image_itri = (self.current_image_itri + 1) % len(images)
            imageLabel.configure(image=images[self.current_image_itri])
            infoLabel.configure(text=f'Image {self.current_image_itri + 1} of {len(images)}')

        imageLabel = tk.Label(w4)
        infoLabel = tk.Label(w4, font=(self.font, 20))
        button = tk.Button(w4, text='Next Image', width=30, height=5, bg=self.color_1, fg=self.color_2, command=change_image)

        imageLabel.place(x=600, y=130)
        infoLabel.place(x=600, y=130)
        button.place(x=750, y=750)

        for file in image_files:
            image = Image.open(file)
            w, h = image.size
            min = 800/w if 800/w < 600/h else 600/h
            w = int(w * min)
            h = int(h * min)
            image = image.resize((w, h))
            photo = ImageTk.PhotoImage(image)
            images.append(photo)


        change_image()

        link_site = HTMLLabel(w4, html='<a href="https://www.loomischaffee.org/academics/pearse-hub-for-innovation/innovation-trimester">Learn more about I-TRI!</a>')
        link_site.configure(height=10, width=20)
        link_site.place(x=1300, y=750)

    def open_courses(self):
        w5=Toplevel()
        w5.title('Courses')
        w5.geometry('1440x900')
        w5.configure(background=self.color_1)
        back_button = tk.Button(w5, text='Back', font=(self.font, 18), command=w5.destroy) 
        back_button.place(x=20, y=20)
        welcome_message = tk.Label(w5, text='PHI Courses', font=(self.font, 55), fg=self.color_2)
        welcome_message.configure(background=self.color_1)
        welcome_message.place(x=130, y=30)
        with open('courses/courses.txt', 'r') as file:
            lines = file.readlines()
        max_width = 45  # Maximum width of the label
        joined_lines = '\n'.join(lines)
        message = tk.Label(w5, text=joined_lines, font=(self.font, 18), fg=self.color_3, bd=1, relief='sunken', width=max_width)
        message.place(x=30, y=130)
        message.configure(background=self.color_1, justify='left')

        image_files = ['courses/IMG_0375.jpg', 'courses/IMG_8280.jpg', 'courses/IMG_0515.jpg', 'courses/IMG_8941.jpg', 'courses/IMG_9609.jpg']
        images = []

        def change_image():
            self.current_image_courses = (self.current_image_courses + 1) % len(images)
            imageLabel.configure(image=images[self.current_image_courses])
            infoLabel.configure(text=f'Image {self.current_image_courses + 1} of {len(images)}')

        imageLabel = tk.Label(w5)
        infoLabel = tk.Label(w5, font=(self.font, 20))
        button = tk.Button(w5, text='Next Image', width=30, height=5, bg=self.color_1, fg=self.color_2, command=change_image)

        imageLabel.place(x=600, y=130)
        infoLabel.place(x=600, y=130)
        button.place(x=750, y=750)

        for file in image_files:
            image = Image.open(file)
            w, h = image.size
            min = 800/w if 800/w < 600/h else 600/h
            w = int(w * min)
            h = int(h * min)
            image = image.resize((w, h))
            photo = ImageTk.PhotoImage(image)
            images.append(photo)

        change_image()

        link_site = HTMLLabel(w5, html='<a href="https://issuu.com/loomischaffee/docs/coursedescriptionbook_2022-23_final-issuu/54">Visit the course catalogue!</a>')
        link_site.configure(height=10, width=20)
        link_site.place(x=1300, y=750)

    def open_collaboration(self):
        w6=Toplevel()
        w6.title('Collaboration')
        w6.geometry('1440x900')
        w6.configure(background=self.color_1)
        back_button = tk.Button(w6, text='Back', font=(self.font, 18), command=w6.destroy) 
        back_button.place(x=20, y=20)
        welcome_message = tk.Label(w6, text='Collaborations', font=(self.font, 55), fg=self.color_2)
        welcome_message.configure(background=self.color_1)
        welcome_message.place(x=130, y=30)
        with open('collab/collab.txt', 'r') as file:
            lines = file.readlines()
        max_width = 45  # Maximum width of the label
        joined_lines = '\n'.join(lines)
        message = tk.Label(w6, text=joined_lines, font=(self.font, 18), fg=self.color_3, bd=1, relief='sunken', width=max_width)
        message.place(x=30, y=130)
        message.configure(background=self.color_1, justify='left')

        image_files = ['collab/IMG_0988.jpeg', 'collab/IMG_8178.jpg', 'collab/IMG_3644.jpg', 'collab/IMG_1068.jpg', 'collab/IMG_1290.jpg', 'collab/IMG_1552.jpg', 'collab/IMG_0449.jpg', 'collab/IMG_0550.jpg', 'collab/IMG_3264.jpg', 'collab/IMG_3706.jpg', 'collab/IMG_1010.jpg']
        images = []

        def change_image():
            self.current_image_collab = (self.current_image_collab + 1) % len(images)
            imageLabel.configure(image=images[self.current_image_collab])
            infoLabel.configure(text=f'Image {self.current_image_collab + 1} of {len(images)}')

        imageLabel = tk.Label(w6)
        infoLabel = tk.Label(w6, font=(self.font, 20))
        button = tk.Button(w6, text='Next Image', width=30, height=5, bg=self.color_1, fg=self.color_2, command=change_image)

        imageLabel.place(x=600, y=130)
        infoLabel.place(x=600, y=130)
        button.place(x=750, y=750)

        for file in image_files:
            image = Image.open(file)
            w, h = image.size
            min = 800/w if 800/w < 600/h else 600/h
            w = int(w * min)
            h = int(h * min)
            image = image.resize((w, h))
            photo = ImageTk.PhotoImage(image)
            images.append(photo)

        change_image()

    def open_pearses(self):
        w7 = Toplevel()
        w7.title('The Pearse Family')
        w7.geometry('1440x900')
        w7.configure(background=self.color_1)
        back_button = tk.Button(w7, text='Back', font=(self.font, 18), command=w7.destroy) 
        back_button.place(x=30, y=20)
        welcome_message = tk.Label(w7, text='The Pearse Family', font=(self.font, 55), fg=self.color_2)
        welcome_message.configure(background=self.color_1)
        welcome_message.place(x=130, y=30)
        with open('pearses/pearses.txt', 'r') as file:
            lines = file.readlines()
        max_width = 45  # Maximum width of the label
        joined_lines = '\n'.join(lines)
        message = tk.Label(w7, text=joined_lines, font=(self.font, 18), fg=self.color_3, bd=1, relief='sunken', width=max_width)
        message.place(x=30, y=130)
        message.configure(background=self.color_1, justify='left')
        
        '''

        image_files = ['pearses/IMG_XXXX.jpg', 'pearses/IMG_XXXX.jpg', 'pearses/IMG_XXXX.jpg', 'pearses/IMG_XXXX.jpg', 'pearses/IMG_XXXX.jpg', 'pearses/IMG_XXXX.jpg', 'pearses/IMG_XXXX.jpg']
        images = []

        def change_image():
            self.current_image_staff = (self.current_image_staff + 1) % len(images)
            imageLabel.configure(image=images[self.current_image_staff])
            infoLabel.configure(text=f'Image {self.current_image_staff + 1} of {len(images)}')

        imageLabel = tk.Label(w7)
        infoLabel = tk.Label(w7, font=(self.font, 20))
        button = tk.Button(w7, text='Next Image', width=30, height=5, bg=self.color_1, fg=self.color_2, command=change_image)

        imageLabel.place(x=600, y=130)
        infoLabel.place(x=600, y=130)
        button.place(x=750, y=750)

        for file in image_files:
            image = Image.open(file)
            w, h = image.size
            min = 800/w if 800/w < 600/h else 600/h
            w = int(w * min)
            h = int(h * min)
            image = image.resize((w, h))
            photo = ImageTk.PhotoImage(image)
            images.append(photo)

        change_image()
        '''

MyGUI()

 



