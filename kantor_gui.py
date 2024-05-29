import tkinter as tk
from tkinter import ttk
from kantor import calculate

waluty = ["USD", "EUR"]


def przelicz():
    co = combobox.get()
    ile = ilosc.get()
    result = calculate(co, int(ile))
    print(co, ile)
    wynik_label.config(text=f"{result} PLN")


root = tk.Tk()
root.title("Prosty Kantor")
root.geometry("800x400")

label = tk.Label(root, text="Hello witaj w Kantorze")
label.pack()


waluta_label = tk.Label(root, text="Wybierz kod waluty")
waluta_label.pack()
combobox = ttk.Combobox(root, values=waluty)
combobox.pack()


ilosc_label = tk.Label(root, text="Ile chcesz kupic")
ilosc_label.pack()
ilosc = tk.Entry(root)
ilosc.pack()

wykonaj = tk.Button(root, text="Przelicz", command=przelicz)
wykonaj.pack()

wynik_label = tk.Label(root, text="-")
wynik_label.pack()

root.mainloop()
print("Koniec")