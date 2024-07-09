import tkinter as tk
import joblib
import numpy as np

model=joblib.load("package-predictor.joblib")

def mypredictor():
    cgpa=ent.get()
    cgpa=np.array([float(cgpa)])
    new_cgpa=cgpa.reshape(-1,1)

    pkg=model.predict(new_cgpa)
    pkg=str(pkg[0])
    newpkg=pkg[1:4]

    showpackage.config(text=f"Your package is {newpkg} lakhs per month")

    ent.delete(0,tk.END)

app=tk.Tk()
app.geometry("600x400")
app.title("Package-Predictor")
app.config(background="#c981b0")

header =tk.Label(app,text="Check your Package on CGPA",font=("robort",30,"bold"), fg="#6b0247",bg="#f2d0f0")
header.pack(fill="x",ipady=10)

lbl=tk.Label(app,text="Enter CGPA",font= ("robort",30,"bold"),fg="#6b0247",bg="#c981b0")
lbl.pack(pady=16)

ent=tk.Entry(app,font=("robort",20,"italic"))
ent.pack()

btn=tk.Button(app, text="Check Package",font=("robort",15,"bold"),bg="#c981b0", command= mypredictor)
btn.pack(pady=15 )

showpackage=tk.Label(app,text="",fg="#6b0247",bg="#c981b0",font=("robort",15))
showpackage.pack(pady=20)

app.mainloop()