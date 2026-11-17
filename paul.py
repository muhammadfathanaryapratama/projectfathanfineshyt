import tkinter as tk
from tkinter import ttk, messagebox

def popup_sukses(nama, ttgl, email, gender, jurusan) :
    # Buat jendela pop-up kustom 
    pop = tk. Toplevel(root)
    pop.title("Konfirmasi Pendaftaran")
    pop.geometry("400x320")
    pop.resizable(False, False)
    pop.configure(bg="#ffffff")

    # Membuat pop-up tetap berada di paling depan
    pop.transient(root)
    pop.grab_set()

    # Header / Judul
    lbl_header = tk.Label(
        pop,
        text="Pendaftaran Berhasil!",
        font=("Helvetica", 14, "bold"),
        fg="#2e7d32",
        bg="#e8f5e9",
        pady=12
    )
    lbl_header.pack(fill="x")

    # Frame Konten Data
    frame_data = tk.Frame(pop, bg="#ffffff", padx=25, pady=20)
    frame_data.pack(fill="both", expand=True)

    list_data = [
        ("Nama", nama),
        ("TTL", ttgl),
        ("Email", email),
        ("Jenis Kelamin", gender),
        ("Jurusan", jurusan)
    ]

    # Menampilkan data secara sejajar dengan Grid
    for i, (label, val) in enumerate(list_data) :
        tk.label(
            frame_data, text=label, font=("Helvetica", 10, "bold"),
            bg="#ffffff", fg="#333333", anchor="w"
        ).grid(row=i, column=0, sticky="w", pady=4)

        tk.Label(
            frame_data, text=":", font=("Hevectica", 10, "bold"),
            bg="#ffffff", fg="#333333"
        ).grid(row=i, column=1, padx=8, pady=4)

        tk.Label(
            frame_data, text=val, font=("Helvetica", 10),
            bg="#ffffff", fg="#555555", anchor="w"
        ).grid(row=i, column=2, sticky="w", pady=4)

        # Tombol Tutup / OK
        btn_ok = tk.Button(
            pop,
            text="OK",
            font=("Helvetica", 10, "bold"),
            bg="#2e7d32",
            fg="white",
            width=12,
            bd=0,
            cursor='hand2',
            command=pop.destroy
        )
        btn_ok.pack(pady=(0, 20))


def simpan_data():
    nama = entry_nama.get()
    ttgl = entry_ttgl.get()
    email = entry_email.get()
    gender = var_gender.get()
    jurusan = combo_jurusan.get()

    # Validasi sederhana
    if not nama or ttgl or not email or jurusan == "-- Pilih Jurusan --":
        messagebox.showwarning("Peringatan", "Mohon isi semua data yang diperlukan!")
        return

        # Tampilkan pop-up sukses kustom
        popup_sukses(nama, ttgl, email, gender, jurusan)
        
         # Reset form
        reset_form()

def reset_form():
   entry_nama.delete(0, tk.END)
   entry_ttgl.delete(0, tk.END)
   entry_email.delete(0, tk.END)
   var_gender.set("Laki-laki")
   combo_jurusan.current(0)

# Inisialisasi Window Utama
root = tk.Tk() #Tk = Membuat jendela utama dan membuat engine Tk.
root.title("Form Pendaftaran GUI")
root.geometry("600x520")
root.resizable(True, True)
root.state('zoomed') #memaksimalkan jendela utama (maximize window) hingga memenuhi seluruh layar desktop

# Pembuatan Judul JENDELA
label_judul = tk.Label(root, text="FORM PENDAFTARAN MAHASISWA", bg="#6BC1F3", fg="#ffffff", font=("Helvetica", 14, "bold"))
label_judul.pack(fill="x", pady=15)
# -----------------------------------------------------------------------------------------------------------------------------

# Pembuatan Frame berisi Form
frame_form = tk.Frame(root, bg="#1E6D9B", padx=20, pady=10)
frame_form.pack(fill="both", expand=True) # both = melebar (sumbu X) dan meninggi (sumbu Y).
# ------------------------------------------------------------------------------------------------------------------------------

# label Nama
lbl_nama = tk.Label(frame_form, bg="#6BC1F3", text="Nama Lengkap:", font="bold", anchor="w")
lbl_nama.pack(fill="x", pady=(15, 0))

# Entry Nama
entry_nama = tk.Entry(frame_form, font=("Helvetica", 10))
entry_nama.pack(fill="x", pady=(0, 10))
# ------------------------------------------------------------------------------------------------------------------------------

# Label TTGL
lbl_ttgl = tk.Label(frame_form, bg="#6BC1F3", text="Tempat/Tanggal Lahir:", font="bold", anchor="w")
lbl_ttgl.pack(fill="x", pady=(5, 0))

# Entry TTGL
entry_ttgl = tk.Entry(frame_form, font=("Helvetica", 10))
entry_ttgl.pack(fill="x", pady=(0, 10))
# ------------------------------------------------------------------------------------------------------------------------------

# Label Email
lbl_email = tk.Label(frame_form, bg="#6BC1F3", text="Email", font="bold", anchor="w")
lbl_email.pack(fill="x", pady=(0, 10))

# Entry Email
entry_email = tk.Entry(frame_form, font=("Helvetica", 10))
entry_email.pack(fill="x", pady=(0, 10))
# ------------------------------------------------------------------------------------------------------------------------------

# Label Jenis Kelamin
lbl_gender = tk.Label(frame_form, bg="#6BC1F3", text="Jenis Kelamin", font="bold", anchor="w")
lbl_gender.pack(fill="x", pady=(5, 0))
# ------------------------------------------------------------------------------------------------------------------------------

var_gender = tk.StringVar(value="Laki-laki")
frame_gender = tk.Frame(frame_form, bg="#f2f8f9", highlightbackground="#cccccc", padx=20, pady=10)
frame_gender.pack(fill="x", pady=(0, 10))

rb_pria = tk.Radiobutton(frame_gender, text="Laki-laki", font="bold", variable=var_gender, value="Laki-laki")
rb_pria.pack(side="left", padx=(0, 10))

rb_wanita = tk.Radiobutton(frame_gender, text="Perempuan", font="bold", variable=var_gender, value="Perempuan")
rb_wanita.pack(side="left")
# -----------------------------------------------------------------------------------------------------------------------------

# Combobox Jurusan
lbl_jurusan = tk.Label(frame_form, text="Jurusan / Pilihan:", font="bold", anchor="w")
lbl_jurusan.pack(fill="x", pady=(5, 0))

root.option_add ("*TCombobox*Listbox.font", ("Helvetica", 12))

daftar_jurusan = ["-- Pilihan Jurusan --", "Teknik Informatika", "sistem Informasi", "Desain Grafis", "Manajemen"]
combo_jurusan = ttk.Combobox(frame_form, values=daftar_jurusan, state="readonly", font=("Helvetica", 12))
combo_jurusan.current(0)
combo_jurusan.pack(fill="x", pady=(0, 20))

# Tombol Submit
frame_tombol = tk.Frame(frame_form, bg="#6BC1F5")
frame_tombol.pack(fill="x")

btn_simpan = tk.Button(frame_tombol, text="Daftar", bg="#4C70AF", fg="white", font=("Helvetica", 10, "bold"), command=simpan_data)
btn_simpan.pack(side="left", fill="x", expand=True, padx=(0, 40))

# Tombol Reset
btn_reset = tk.Button(frame_tombol, text="Reset", bg="#4C70AF", fg="white", font=("Helvetica", 10, "bold"), command=reset_form)
btn_reset.pack(side="right", fill="x", expand=True, padx=(40, 0)) 


root.mainloop()