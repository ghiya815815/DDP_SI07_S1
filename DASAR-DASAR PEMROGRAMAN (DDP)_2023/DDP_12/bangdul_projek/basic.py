#import modules
import tkinter as tk

#dungsi deklarasi
def tambahkan():
    angka1 = int(input1.get())
    angka2 = int(input2.get())
    hasil = angka1 + angka2
    label_hasil["text"] = f"Hasil= {hasil}"

#main window (tabel putih)
root = tk.Tk()
root.title("kalkulator penjumlahan")
root.geometry('500x500') #lebarxtinggi

#widgets declarasi
label = tk.Label(master=root, text="kalkulator penjumlahan")
labelplus = tk.Label(master=root, text="+")
label_hasil = tk.Label(master=root, text="hasil:")

#entry
input1 = tk.Entry(master=root)
input2 = tk.Entry(master=root)

#button
button = tk.Button(master=root, text="tambahkan",
command=tambahkan)




#widgets placement
label.pack()
input1.pack()
labelplus.pack()
input2.pack()
button.pack()
label_hasil.pack()


#main loop
root.mainloop()
