import tkinter as tk
from tkinter import filedialog,messagebox
from PIL import ImageTk, Image
from generation import generate_qr_code
from file import save_qrfile, add_logo, read_file

class QRApp :
    def __init__(self, master):
        self.master = master
        self.master.title("QR Code Generator")
        self.master.geometry("500x600")
        self.master.configure(bg="white")
        self.flag1 = False

        # Fichier sélectionné
        self.file_path = tk.StringVar()
        self.output_name = tk.StringVar()
        self.dest_path = tk.StringVar()
        self.logo_path = tk.StringVar()

        # --- Interface ---
        frame_details = tk.Frame(master, width=500, height=200, borderwidth=5, relief=tk.GROOVE)
        frame_details.pack(pady=10)

        frame_file = tk.Frame(frame_details, width=250, height=100, borderwidth=5, relief=tk.GROOVE)
        frame_file.pack_propagate(False)
        frame_file.pack(side=tk.LEFT)
        tk.Label(frame_file, text="Sélectionner un fichier :").pack(side=tk.TOP,padx=10, pady=10)
        tk.Entry(frame_file, textvariable=self.file_path, width=25).pack(side=tk.LEFT,padx=4, pady=10)
        tk.Button(frame_file, text="Parcourir", command=self.browse_file).pack(side=tk.LEFT,padx=4, pady=10)
        
        frame_dest = tk.Frame(frame_details, width=250, height=100, borderwidth=5, relief=tk.GROOVE)
        frame_dest.pack_propagate(False)
        frame_dest.pack(side=tk.LEFT)
        tk.Label(frame_dest, text="Destination :").pack(side=tk.TOP,padx=10, pady=10)
        tk.Entry(frame_dest, textvariable=self.dest_path, width=25).pack(side=tk.LEFT,padx=4, pady=10)
        tk.Button(frame_dest, text="Parcourir", command=self.browse_dest).pack(side=tk.RIGHT,padx=4, pady=10)
        

        frame_output = tk.Frame(master, width=500, height=300, borderwidth=5, relief=tk.GROOVE)
        frame_output.pack_propagate(False)
        frame_output.pack(pady=10)
        tk.Label(frame_output, text="Nom du QR Code :").pack()
        tk.Entry(frame_output, textvariable=self.output_name).pack()

        frame_actions = tk.Frame(master, width=250, height=50, background="white")
        frame_actions.pack_propagate(False)
        frame_actions.pack(side=tk.BOTTOM, pady=50)
        tk.Button(frame_actions, text="Générer QR Code", command=self.generate).pack(side=tk.LEFT,pady=10)
        tk.Button(frame_actions, text="Sauvegarder", command=self.save).pack(side=tk.RIGHT,pady=10)

        self.qr_preview = tk.Label(frame_output)
        self.qr_preview.pack(side=tk.BOTTOM, pady=10, padx=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Sélectionner un fichier de 2Ko maximun")
        if file_path:
            self.file_path.set(file_path)
            try:
                with open(file_path, 'rb') as file:
                    data = file.read()
                if(len(data) < 3000):
                    self.flag1 = True
                else:
                    messagebox.showerror("Erreur", "Le fichier est trop long pour être encodé dans un QR code.")
                    messagebox.showinfo("Info", "Le lien vers le fichier sera utilisé à la place.")

            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de lire le fichier : {e}")
        

    def browse_logo(self):
        logo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if logo_path:
            self.logo_path.set(logo_path)

    def browse_dest(self):
        dest_path = filedialog.askdirectory()
        if dest_path:
            self.dest_path.set(dest_path)

    def generate(self):
        data = self.file_path.get()
        logo_path = self.logo_path.get()

        if(self.flag1):
            self.data = read_file(data)
            self.flag1 = False

        self.img = generate_qr_code(data)
        if logo_path:
            self.img = add_logo(self.img, logo_path)
        
        if self.img:
            messagebox.showinfo("QR Code généré")

            preview = self.img.copy()
            preview.thumbnail((200, 200))
            preview_img = ImageTk.PhotoImage(preview)
            self.qr_preview.config(image=preview_img)
            self.qr_preview.image = preview_img

        return None

    def save(self):
        if self.img:
            output_name = self.output_name.get() or "qr_code.png"
            self.path = save_qrfile(self.img, output_name, self.dest_path.get())
            messagebox.showinfo("QR Code enregistré", f"QR Code enregistré sous {self.path}")
        else:
            messagebox.showerror("Erreur", "Aucun QR Code à enregistrer")


def launch_ui():
    root = tk.Tk()
    app = QRApp(root)
    root.mainloop()