import tkinter as tk
from tkinter import INSERT, messagebox
from tkinter.ttk import *
import takeData

class GUI():
    def __init__(self):
        self.control = False
        self.window = tk.Tk()
        self.window.title('ENDEKSLEME VE ARAMA')
        self.window.geometry('1920x1080')

        self.nameLabel = tk.Label(text = 'Gizem Beden\n210911175')
        self.nameLabel.pack(padx = 0, pady=0, side=tk.TOP)

        self.emeklemeyiBaslatButton = tk.Button(self.window,command = lambda m = '':self.emeklemeyiBaslatButtonClicked(), text = 'Emeklemeyi baslat')
        self.emeklemeyiBaslatButton.pack(padx=0,pady=0, side = tk.TOP)

        self.wordsLabel = tk.Label(text = 'Arama yapılacak kelime ya da kelimeleri giriniz:')
        self.wordsLabel.pack()

        self.wordsTextBox = tk.Text(height=1, width=50)
        self.wordsTextBox.pack()

        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        
        self.kelimeFrekansi = tk.Checkbutton( text='Kelime Frekansı', onvalue=1, offvalue=0, variable = self.var1)
        self.kelimeFrekansi.pack()
        
        self.inboundLink = tk.Checkbutton( text='Inbound Link', onvalue=1, offvalue=0, variable = self.var2)
        self.inboundLink.pack()

        self.programiBaslat = tk.Button(self.window,command = lambda m = '':self.inputControl(), text = 'ARA')
        self.programiBaslat.pack(padx=0,pady=0, side = tk.TOP)

        self.resultScreen = tk.Text(height=25, width=175)
        self.resultScreen.pack()
        
        self.window.mainloop()

    def inputControl(self):
        if self.control == True:
            if (self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0) or self.wordsTextBox.get('1.0','end-1c') == '':
                messagebox.showinfo(title = 'HATA!', message = 'PARAMETRE BELIRTILMEDI!')
            else:
                inputValue = self.wordsTextBox.get('1.0', 'end-1c')
                inputList = list()
                kelimeFrekansi = False
                inboundLink = False
                pageRank = False
                if ',' in inputValue:
                    inputList = inputValue.lower().split(',')
                elif '-' in inputValue:
                    inputList = inputValue.lower().split('-')
                else:
                    inputList.append(inputValue.lower())
                if self.var1.get() == 1:
                    kelimeFrekansi = True
                if self.var2.get() == 1:
                    inboundLink = True
                
                self.resultOutput = self.startProgram.arananKelimeler(inputList, kelimeFrekansi=kelimeFrekansi, inboundLink=inboundLink)
                self.resultScreen.insert(INSERT, 'Sonuç: ')
                 
                self.resultScreen.delete('1.0','end')
                self.resultScreen.insert(INSERT, 'Sonuç: \n\n')
                for result in self.resultOutput:
                    self.resultScreen.insert(INSERT, str(result)+'\n\n') 
        elif self.control == False:
            messagebox.showinfo(title = 'HATA!', message = 'ONCE EMEKLEME BASLATILMALI!')

    def emeklemeyiBaslatButtonClicked(self):
        if self.control == False:
            self.startProgram = takeData.TakeData('https://ois.istinye.edu.tr/bilgipaketi/eobsakts/ogrenimprogrami/program_kodu/0401001/menu_id/p_38/tip/L/submenuheader/2/ln/tr/print/1')
            messagebox.showinfo(title = 'BASLATILDI!', message = 'EMEKLEME BASLATILDI!')
            self.resultScreen.insert(INSERT, 'Arama yapabilirsiniz, lütfen yukarıdaki kutucuğa kelime ya da kelimeleri giriniz.')
            self.control = True
            
        elif self.control == True:
            messagebox.showinfo(title = 'Zaten Çalısıyor!', message = 'EMEKLEME ZATEN AKTİF')
GUI()