import qrcode
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

class QrCodeGenerator:

    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")

        self.label = Label(master, text="Enter Text:")
        self.label.pack()

        self.text_entry = Entry(master)
        self.text_entry.pack()

        self.generate_button = Button(master, text="Generate", command=self.generate_qr)
        self.generate_button.pack()

        self.image_label = Label(master)
        self.image_label.pack()

        self.save_button = Button(master, text="Save", command=self.save_qr, state=DISABLED)
        self.save_button.pack()

    def generate_qr(self):
        # Get the text from the entry widget
        text = self.text_entry.get()

        # Generate the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)

        # Convert the QR code to an image
        img = qr.make_image(fill_color="black", back_color="white")

        # Display the QR code in the GUI
        img = img.resize((250, 250))
        self.img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.img_tk)
        self.image_label.image = self.img_tk

        # Enable the save button
        self.save_button.config(state=NORMAL)

    def save_qr(self):
        # Get the filename from the user
        filename = filedialog.asksaveasfilename(defaultextension=".png")

        # Save the QR code image to the file
        img = Image.open(self.img_tk)
        img.save(filename)

root = Tk()
my_gui = QrCodeGenerator(root)
root.mainloop()
