import tkinter as tk
from tkinter import messagebox

def hisaab():
    try:
        kol = float(entry_bill.get())
        tedad = int(entry_people.get())
        
        if kol <= 0:
            messagebox.showerror("khata", "mablagh bayad bishtar az sefr bashad")
            return
            
        if tedad <= 0:
            messagebox.showerror("khata", "tedad nafar bayad bishtar az sefr bashad")
            return
        
        sahme_har_nafar = kol / tedad
        
        messagebox.showinfo("natije", f"sahme har nafar: {sahme_har_nafar:,.0f} toman")
        
    except ValueError:
        messagebox.showerror("khata", "lotfan faghat adad vared konid")
    except ZeroDivisionError:
        messagebox.showerror("khata", "tedad nafar nemitavanad sefr bashad")

root = tk.Tk()
root.title("dong calculator")
root.geometry("300x200")

label_title = tk.Label(root, text="sahme har nafar", font=("Arial", 14))
label_title.pack(pady=10)

label_bill = tk.Label(root, text="mablaghe kol (toman):")
label_bill.pack()

entry_bill = tk.Entry(root)
entry_bill.pack(pady=5)

label_people = tk.Label(root, text="tedade nafarat:")
label_people.pack()

entry_people = tk.Entry(root)
entry_people.pack(pady=5)

btn_calculate = tk.Button(root, text="hisaab", command=hisaab, bg="green", fg="white")
btn_calculate.pack(pady=20)

root.mainloop()