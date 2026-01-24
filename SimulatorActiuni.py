import matplotlib
matplotlib.use("TkAgg")
import tkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
from dataclasses import dataclass

from OperatiiActiuni import Actiuni

@dataclass()
class Simulator(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulator")
        self.geometry("500x625")
        self.minsize(400,500)

        self.graf()
        
        '''self.text1=tkinter.StringVar()
        self.text1.set("Introduce datele.") 
        StringVar e folosit pentru a sincroniza textul obiectului text1 cu orice eticheta(label) asociata.'''
        
        self.label=tkinter.Label(text="Introduceti datele.")
        self.label.pack()
        
        self.componente_input()

    def graf(self):
        self.FiguraGrafic = Figure(figsize=(8, 4))
        
        self.Grafic = self.FiguraGrafic.add_subplot(111)
        self.Grafic.set_xlabel("Timp(luni)")
        self.Grafic.set_ylabel("Suma")
        self.Grafic.grid(True)
        
        self.Panou = FigureCanvasTkAgg(self.FiguraGrafic, master=self)
        self.Navigare=NavigationToolbar2Tk(self.Panou,self)
        self.Navigare.pack(side="top")
        self.Panou.get_tk_widget().pack(pady=10,fill=tkinter.BOTH,expand=True)
        self.Panou.draw() #.draw_idle()

    def componente_input(self):
        self.Control=tkinter.Frame(self)

        self.nume_label=tkinter.Label(self.Control,text="Nume")
        self.nume_label.grid(row=0,column=0,padx=0,pady=5)
        
        self.nume_entry=tkinter.Entry(self.Control)
        self.nume_entry.grid(row=0,column=1,padx=0,pady=5)
        
        self.performanta_label=tkinter.Label(self.Control,text="Performanta")
        self.performanta_label.grid(row=1,column=0,padx=0,pady=5)
        
        self.performanta_entry=tkinter.Entry(self.Control)
        self.performanta_entry.grid(row=1,column=1,padx=0,pady=5)
        
        self.volatilitate_label=tkinter.Label(self.Control,text="Volatilitate")
        self.volatilitate_label.grid(row=2,column=0,padx=0,pady=5)

        self.volatilitate_entry=tkinter.Entry(self.Control)
        self.volatilitate_entry.grid(row=2,column=1,padx=0,pady=5)
        
        self.suma_initiala_label=tkinter.Label(self.Control,text="Suma Initiala")
        self.suma_initiala_label.grid(row=3,column=0,padx=0,pady=5)
        
        self.suma_entry=tkinter.Entry(self.Control)
        self.suma_entry.grid(row=3,column=1,padx=0,pady=5)
        
        self.durata_label=tkinter.Label(self.Control,text="Durata(ani)")
        self.durata_label.grid(row=4,column=0,padx=0,pady=5)
        
        self.durata_entry=tkinter.Entry(self.Control)
        self.durata_entry.grid(row=4,column=1,padx=0,pady=5)
        
        self.contributie_lunara_label=tkinter.Label(self.Control,text="Contributie(pe luna)")
        self.contributie_lunara_label.grid(row=5,column=0,padx=0,pady=5)
        
        self.contributie_entry=tkinter.Entry(self.Control)
        self.contributie_entry.insert(0,"0")
        self.contributie_entry.grid(row=5,column=1,padx=0,pady=5)
        
        self.buton_adauga=tkinter.Button(self.Control,text="Adauga",command=self.adaugare)
        self.buton_adauga.grid(row=0,column=2,padx=20,pady=5)
        
        self.buton_anulare=tkinter.Button(self.Control,text="Cancel",command=self.reincepe)
        self.buton_anulare.grid(row=1,column=2,padx=20,pady=5)
        
        self.buton_rebalansare=tkinter.Button(self.Control,text="Aplica rebalansare",command=self.adauga_portofoliu)
        self.buton_rebalansare.grid(row=2,column=2,padx=20,pady=5)
        
        self.optiuni_actiuni=["Niciuna"]
        self.optiuni=ttk.Combobox(self.Control,values=self.optiuni_actiuni,state="readonly")
        self.optiuni.current(0)
        self.optiuni.grid(row=3,column=2)
        
        self.Control.pack(expand=True)
        
    def adauga_portofoliu(self):
        x=list(range(Actiuni.luni))
        y=Actiuni.rebalansare()

        self.Grafic.plot(x,y,label="Portofoliu")
        self.Grafic.legend(loc="lower right")
        self.Panou.draw()
        self.stergere_input()
        
    def adaugare(self):
        erori=""
        
        if self.nume_entry.get().strip()=="":
            erori+="Nume lipsa."
        else:
            nume_actiune=self.nume_entry.get().strip()
            
        try:
            valoare_performanta=float(self.performanta_entry.get())
        except ValueError:
            erori+="Performanta invalida."
            
        try:
            valoare_volatilitate=float(self.volatilitate_entry.get())
        except ValueError:
            erori+="Volatilitate invalida."
        
        try:
            valoare_suma=float(self.suma_entry.get())
        except ValueError:
            erori+="Suma initiala invalida."
            
        try:
            valoare_durata=float(self.durata_entry.get())
        except ValueError:
            erori+="Durata invalida"
            
        try:
            valoare_contributie=float(self.contributie_entry.get())
        except ValueError:
            erori+="Contributii invalide"
            
        if erori!="":
            self.label.config(text=erori)
        else:
            self.label.config(text="Date adaugate")
            if Actiuni.luni==0:
                Actiuni.timp_actiuni(valoare_durata)
                
            Actiuni.date_actiune(nume_actiune,valoare_performanta,valoare_volatilitate)
            
            x=list(range(Actiuni.luni))
            y=Actiuni.valori_actiune(nume_actiune,valoare_suma,valoare_contributie)
            
            self.Grafic.plot(x,y,label=nume_actiune)
            self.Grafic.legend(loc="lower right")
            self.Panou.draw()
            self.stergere_input()

    def stergere_input(self):
        self.nume_entry.delete(0,tkinter.END)
        self.performanta_entry.delete(0,tkinter.END)
        self.volatilitate_entry.delete(0,tkinter.END)
        
    def reincepe(self):
        self.stergere_input()
        
        self.suma_entry.delete(0,tkinter.END)
        self.durata_entry.delete(0,tkinter.END)
        self.contributie_entry.delete(0,tkinter.END)
        self.contributie_entry.insert(0,"0")
        
        Actiuni.resetare()
        
        self.Grafic.clear()
        self.Panou.draw()


def main():
    fereastra=Simulator()
    fereastra.mainloop()
    
if __name__=="__main__":
    main()