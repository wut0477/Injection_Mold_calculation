from tkinter import *
from tkinter import ttk, messagebox
from injectionclass import *
from plasticdb import *
from dataforcal import *

FONT1 = ('tahoma', 12)
sc = injectioncalculator()         
sb = dataforcal()

class mainwindow:

    def __init__(self):
        self.info = 'Injection Molding Calculation'

    def GUIWindow(self):
        GUI = Tk()
        GUI.title('Plastic Injection Calculator ')
        GUI.geometry('500x500')
        GUI.attributes('-topmost', False)
    
        lblProgramname = ttk.Label(GUI,text='โปรแกรมคำนวณงานฉีดพลาสติก',font=FONT1)
        lblProgramname.pack(pady=20)
        ss = plasticmoldmenu() # Class plasticmoldmenu ()
        ss.injectiondata(GUI)  # Call function injectiondata in plasticmoldmenu class 

        GUI.mainloop()

class plasticmoldmenu():
    def injectiondata(self, GUI):
        Frm_button = Frame(GUI)
        Frm_button.place(x=50,y=80)
        BT= ttk.Style()
        BT.configure('a.TButton',font=('Calibri',12))
    
        Btn_injectcalulate = ttk.Button(Frm_button,style="a.TButton",text='คำนวณการฉีด',command=sc.injectioncalform) #Calculate injection data for injection parameter
        Btn_injectcalulate.grid(row=0,column=0,ipadx=30,ipady=20,padx=20,pady=10)

        Btn_clampingfource = ttk.Button(Frm_button,style="a.TButton",text='แรงปิดแม่พิมพ์',command=sb.clampingforce)  # Mold Clapping Force
        Btn_clampingfource.grid(row=1,column=0,ipadx=30,ipady=20,padx=20,pady=10)

        Btn_plasticsdata  = ttk.Button(Frm_button,style="a.TButton",text='ข้อมูลพลาสติก',command=sb.materialdensitydata) # The plastic data for calculate 
        Btn_plasticsdata.grid(row=2,column=0,ipadx=30,ipady=20,padx=20,pady=10)

        Btn_shrinkage  = ttk.Button(Frm_button,style="a.TButton",text='ค่าการหดตัว') #Shrinkage ค่าการหดตัว
        Btn_shrinkage.grid(row=3,column=0,ipadx=30,ipady=20,padx=20,pady=10)

        
        Btn_4 = ttk.Button(Frm_button,style="a.TButton",text='ชนาดสกรู',command=sc.injectioncalform) #Calculate injection data for injection parameter
        Btn_4.grid(row=0,column=1,ipadx=30,ipady=20,padx=20,pady=10)

        Btn_5 = ttk.Button(Frm_button,style="a.TButton",text='ชนาดเครื่องฉีด',command=sb.clampingforce)  # Mold Clapping Force
        Btn_5.grid(row=1,column=1,ipadx=30,ipady=20,padx=20,pady=10)

        Btn_6  = ttk.Button(Frm_button,style="a.TButton",text='เครื่องมือ',command=sb.materialdensitydata) # The plastic data for calculate 
        Btn_6.grid(row=2,column=1,ipadx=30,ipady=20,padx=20,pady=10)

        Btn_7  = ttk.Button(Frm_button,style="a.TButton",text='อื่นๆ') #Shrinkage ค่าการหดตัว
        Btn_7.grid(row=3,column=1,ipadx=30,ipady=20,padx=20,pady=10)

mainGUI = mainwindow()
mainGUI.GUIWindow()






