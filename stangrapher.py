from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
import os

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.output_image_size = 0
        self.d_image_size = 0
        self.d_image_w = 0
        self.d_image_h = 0

        self.art = '''¯\_(ツ)_/¯'''
        self.art2 = '''          _ _ __
      /  _ _  
     |    ( )   |
          \_ _ _ _/
              | |
              | |
              | |
              \_/

                                                                                      @--lakshay'''

        self.main()

    def main(self):
        self.root.title('Image Steganographer')
        self.root.geometry('500x600')
        self.root.resizable(width=False, height=False)
        f = Frame(self.root)

        title = Label(f, text='''  IMAGE 
 ------------
STEGANOGRAPHY
-----------------------------''')
        title.config(font=('Helvetica', 29, 'bold'))
        title.grid(pady=10)

        b_encode = Button(f, text="Encode", command=lambda: self.frame1_encode(f), padx=14)
        b_encode.config(font=('Arial', 14, 'bold'), bg='#4CAF50', fg='white')
        b_decode = Button(f, text="Decode", padx=14, command=lambda: self.frame1_decode(f))
        b_decode.config(font=('Arial', 14, 'bold'), bg='#FF5733', fg='white')
        b_decode.grid(pady=12)

        ascii_art = Label(f, text=self.art)
        ascii_art.config(font=('Arial', 60))
        ascii_art2 = Label(f, text=self.art2)
        ascii_art2.config(font=('Arial', 12, 'bold'))

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        style = ttk.Style()
        style.theme_use("clam")  # Choose a theme (e.g., "clam", "winnative", "default")

        f.grid()
        title.grid(row=1)
        b_encode.grid(row=2)
        b_decode.grid(row=3)
        ascii_art.grid(row=4, pady=10)
        ascii_art2.grid(row=5, pady=5)

    def home(self, frame):
        frame.destroy()
        self.main()

    def frame1_decode(self, f):
        f.destroy()
        d_f2 = Frame(self.root)
        label_art = Label(d_f2, text='٩(^‿^)۶')
        label_art.config(font=('Arial', 90))
        label_art.grid(row=1, pady=50)
        l1 = Label(d_f2, text='Select Image with Hidden text:')
        l1.config(font=('Arial', 18))
        l1.grid()
        bws_button = Button(d_f2, text='Select', command=lambda: self.frame2_decode(d_f2))
        bws_button.config(font=('Arial', 18), bg='#4CAF50', fg='white')
        bws_button.grid()
        back_button = Button(d_f2, text='Back', command=lambda: self.home(d_f2))
        back_button.config(font=('Arial', 18), bg='#FF5733', fg='white')
        back_button.grid(pady=15)
        back_button.grid()
        d_f2.grid()

    def frame2_decode(self, d_f2):
        d_f3 = Frame(self.root)
        myfile = filedialog.askopenfilename(filetypes=([('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'),
                                                          ('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            try:
                myimg = Image.open(myfile, 'r')
                myimage = myimg.resize((300, 200))
                img = ImageTk.PhotoImage(myimage)
                l4 = Label(d_f3, text='Selected Image:')
                l4.config(font=('Arial', 18))
                l4.grid()
                panel = Label(d_f3, image=img)
                panel.image = img
                panel.grid()
                hidden_data = self.decode(myimg)
                l2 = Label(d_f3, text='Hidden data is:')
                l2.config(font=('Arial', 18))
                l2.grid(pady=10)
                text_area = Text(d_f3, width=50, height=10)
                text_area.insert(INSERT, hidden_data)
                text_area.configure(state='disabled')
                text_area.grid()
                back_button = Button(d_f3, text='Back', command=lambda: self.page3(d_f3))
                back_button.config(font=('Arial', 11))
                back_button.grid(pady=15)
                back_button.grid()
                show_info = Button(d_f3, text='More Info', command=self.info)
                show_info.config(font=('Arial', 11))
                show_info.grid()
                d_f3.grid(row=1)
                d_f2.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Could not open the image: {e}")

    def decode(self, image):
        data = ''
        imgdata = iter(image.getdata())

        while True:
            pixels = [value for value in imgdata.__next__()[:3] +
                      imgdata.__next__()[:3] +
                      imgdata.__next__()[:3]]
            binstr = ''
            for i in pixels[:8]:
                binstr += '0' if i % 2 == 0 else '1'

            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return data

    def frame1_encode(self, f):
        f.destroy()
        f2 = Frame(self.root)
        label_art = Label(f2, text='\'\(°Ω°)/\'')
        label_art.config(font=('Arial', 70))
        label_art.grid(row=1, pady=50)
        l1 = Label(f2, text='Select the Image in which \nyou want to hide text:')
        l1.config(font=('Arial', 18))
        l1.grid()

        bws_button = Button(f2, text='Select', command=lambda: self.frame2_encode(f2))
        bws_button.config(font=('Arial', 18), bg='#4CAF50', fg='white')
        bws_button.grid()
        back_button = Button(f2, text='Back', command=lambda: self.home(f2))
        back_button.config(font=('Arial', 18), bg='#FF5733', fg='white')
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()

    def frame2_encode(self, f2):
        ep = Frame(self.root)
        myfile = filedialog.askopenfilename(filetypes=([('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'),
                                                        ('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            try:
                myimg = Image.open(myfile)
                myimage = myimg.resize((300, 200))
                img = ImageTk.PhotoImage(myimage)
                l3 = Label(ep, text='Selected Image')
                l3.config(font=('courier', 18))
                l3.grid()
                panel = Label(ep, image=img)
                panel.image = img
                self.output_image_size = os.stat(myfile)
                self.o_image_w, self.o_image_h = myimg.size
                panel.grid()
                l2 = Label(ep, text='Enter the message')
                l2.config(font=('courier', 18))
                l2.grid(pady=15)
                text_area = Text(ep, width=50, height=10)
                text_area.grid()
                encode_button = Button(ep, text='Cancel', command=lambda: self.home(ep))
                encode_button.config(font=('courier', 11))
                back_button = Button(ep, text='Encode', command=lambda: [self.enc_fun(text_area, myimg), self.home(ep)])
                back_button.config(font=('courier', 11))
                back_button.grid(pady=15)
                encode_button.grid()
                ep.grid(row=1)
                f2.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Could not open the image: {e}")

    def info(self):
        try:
            str_info = 'Original Image:\nSize: {}mb\nWidth: {}\nHeight: {}\n\n' \
                       'Decoded Image:\nSize: {}mb\nWidth: {}\nHeight: {}'.format(
                self.output_image_size.st_size / 1000000,
                self.o_image_w, self.o_image_h,
                self.d_image_size / 1000000,
                self.d_image_w, self.d_image_h)
            messagebox.showinfo('Information', str_info)
        except Exception as e:
            messagebox.showinfo('Information', f'Unable to get the information: {e}')

    def genData(self, data):
        newd = [format(ord(i), '08b') for i in data]
        return newd

    def modPix(self, pix, data):
        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)

        for i in range(lendata):
            pixels = [value for value in imdata.__next__()[:3] +
                      imdata.__next__()[:3] +
                      imdata.__next__()[:3]]
            for j in range(8):
                if datalist[i][j] == '0' and pixels[j] % 2 != 0:
                    pixels[j] -= 1
                elif datalist[i][j] == '1' and pixels[j] % 2 == 0:
                    pixels[j] -= 1
            if i == lendata - 1:
                if pixels[-1] % 2 == 0:
                    pixels[-1] -= 1
            else:
                if pixels[-1] % 2 != 0:
                    pixels[-1] -= 1
            pixels = tuple(pixels)
            yield pixels[0:3]
            yield pixels[3:6]
            yield pixels[6:9]

    def encode_enc(self, newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)
        for pixel in self.modPix(newimg.getdata(), data):
            newimg.putpixel((x, y), pixel)
            if x == w - 1:
                x = 0
                y += 1
            else:
                x += 1

    def enc_fun(self, text_area, myimg):
        data = text_area.get("1.0", "end-1c")
        if len(data) == 0:
            messagebox.showinfo("Alert", "Kindly enter text in TextBox")
        else:
            newimg = myimg.copy()
            self.encode_enc(newimg, data)
            temp = os.path.splitext(os.path.basename(myimg.filename))[0]
            new_filename = filedialog.asksaveasfilename(initialfile=temp, filetypes=[('png', '*.png')],
                                                        defaultextension=".png")
            if new_filename:
                newimg.save(new_filename)
                self.d_image_size = os.stat(new_filename).st_size
                self.d_image_w, self.d_image_h = newimg.size
                messagebox.showinfo("Success", "Encoding Successful\nFile is saved in the selected directory")

    def page3(self, frame):
        frame.destroy()
        self.main()

root = Tk()
app = SteganographyApp(root)
root.mainloop()
