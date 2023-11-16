from tkinter import *
from tkinter import ttk, messagebox
from plasticdb import *
from dataforcal import *
import math

class injectioncalculator:

    FONT2 = ('tahoma',12)
    FONT3 = ('tahoma', 10)  

  #------------ Calculate Injection Data -----------------------------------------------------------------#  

    def injectiondataresult(self,GUI1):
        Frminj = Frame(GUI1)
        Frminj.place(x=10,y=50)
        lblVolumnatmeltcalculator = ttk.Label(GUI1,text='1.Volume at melt calculator (ปริมาตรเหลว)',font=self.FONT2)
        lblVolumnatmeltcalculator.place(x=10,y=20)


        lblpartname = ttk.Label(Frminj,text='Product Name *',font=self.FONT3,anchor='w')
        lblpartname.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        partname = StringVar()
        Epartname = ttk.Entry(Frminj,textvariable=partname,width=25,font=self.FONT3)
        Epartname.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        lblpartweight = ttk.Label(Frminj,text='Part weight  (gm) *',font=self.FONT3,anchor='w')
        lblpartweight.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        partweight = StringVar()
        Epartweight = ttk.Entry(Frminj,textvariable=partweight,width=10,font=self.FONT3)
        Epartweight.grid(row=2,column=1,padx=10,pady=10,sticky=W)

                

        lblmaterial = ttk.Label(Frminj,text='Material *',font=self.FONT3,anchor='w')
        lblmaterial.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        material = StringVar()
        datamaterial = []
        for row in view_data('matdesity'):
              datamaterial.append(row[1])
        Cbomaterial = ttk.Combobox(Frminj,textvariable=material,width=10,font=self.FONT3)
        Cbomaterial['values'] = datamaterial   
        Cbomaterial.grid(row=3,column=1,padx=10,pady=5,sticky=W)  

     
#------------------------------------------------------------------------------------------------------------#      
        

        def showdensity(event):
              d = float(density.get())
              result = d * 3.14
              print(result)
              
        #--Density at melt------------------------------------------------------------------------#
        lbldensity = ttk.Label(Frminj,text='Density at melt gr./cm3 *',font=self.FONT3,anchor='w')
        lbldensity.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        density  = StringVar()
        datadensity = []
        for row in view_data('matdesity'):
              datadensity.append(row[2])
        Cbodensity = ttk.Combobox(Frminj,textvariable=density,width=10,font=self.FONT3)
        Cbodensity['values'] = datadensity
        Cbodensity.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        Cbodensity.bind('<<ComboboxSelected>>', showdensity)
        material = dataforcal()
        btn_material = ttk.Button(Frminj,text='...',command=material.materialdensity)  
        btn_material.place(x=350,y=190)
        #-----------------------------------------------------------------------------------------#
  

        lblcavity = ttk.Label(Frminj,text='Cavity *',font=self.FONT3,anchor='w')
        lblcavity.grid(row=5,column=0,padx=10,pady=5,sticky=W)
        cavity = StringVar()
        Ecavity= ttk.Entry(Frminj,textvariable=cavity,width=10,font=self.FONT3)
        Ecavity.grid(row=5,column=1,padx=10,pady=5,sticky=W)    

#----------------------------------------   2. Shot stroke calculator -----------------------------------------------------------#
        s = ttk.Style()
        # s.layout("EntryStyle.TEntry",
        #            [('Entry.plain.field', {'children': [(
        #                'Entry.background', {'children': [(
        #                    'Entry.padding', {'children': [(
        #                        'Entry.textarea', {'sticky': 'nswe'})],
        #               'sticky': 'nswe'})], 'sticky': 'nswe'})],
        #               'border':'2', 'sticky': 'nswe'})])
        # s.configure("EntryStyle.TEntry",
        #          background="blue", 
        #          foreground="red",
        #          fieldbackground="lightgray")
     
        s.layout("EntryStyle.TEntry",
                    [('Entry.plain.field', {'children': [(
                        'Entry.background', {'children': [(
                           'Entry.padding', {'children': [(
                                'Entry.textarea', {'sticky': 'nswe'})],
                      'sticky': 'nswe'})], 'sticky': 'nswe'})],
                      'border':'2', 'sticky': 'nswe'})])

        s.configure("EntryStyle.TEntry",fieldbackground="yellow")

        Frm2 = Frame(GUI1)
        Frm2.place(x=10,y=280)
        lblstrokecalculator = ttk.Label(GUI1,text='2.Shot stroke calcalator',width=25,font=self.FONT2)
        lblstrokecalculator.place(x=10,y=240)


        lblscrewdia = ttk.Label(Frm2,text='Screw Diameter     mm. *',font=self.FONT3,anchor='w')
        lblscrewdia.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        screwdiameter = StringVar()
        Escrewdiameter = ttk.Entry(Frm2,textvariable=screwdiameter,width=10,font=self.FONT3)
        Escrewdiameter.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        lblvolumnmelt = ttk.Label(Frm2,text='Volumn at melt cm3',font=self.FONT3,anchor='w')
        lblvolumnmelt.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        volumnmelt = StringVar()
        Evolumnmelt  = ttk.Entry(Frm2,textvariable=volumnmelt,width=10,font=self.FONT3,style="EntryStyle.TEntry",state=DISABLED)
        Evolumnmelt .grid(row=2,column=1,padx=10,pady=10,sticky=W)


        lblshortstroke = ttk.Label(Frm2,text='Short Stroke mm.',font=self.FONT3,anchor='w')
        lblshortstroke.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        shortstroke = StringVar()
        Eshortstroke = ttk.Entry(Frm2,textvariable=shortstroke,width=10,font=self.FONT3,style="EntryStyle.TEntry",state=DISABLED)
        Eshortstroke.grid(row=3,column=1,padx=10,pady=10,sticky=W)

#---------------------------------------------- 3. Shot size setting & Hold position -----------------------------------------#
        Frm3 = Frame(GUI1)
        Frm3.place(x=10,y=490)
        lblshotsize = ttk.Label(GUI1,text='3.Shot size setting & Hold position',font=self.FONT2)
        lblshotsize.place(x=10,y=450)


        lblcushion = ttk.Label(Frm3,text='Cushion mm. *',font=self.FONT3,anchor='w')
        lblcushion.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        cushion = StringVar()
        cushion.set(3.0)
        Ecushion = ttk.Entry(Frm3,textvariable=cushion,width=10,font=self.FONT3)
        Ecushion.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        lblshotshotsizesetting = ttk.Label(Frm3,text='Shot size  mm.',font=self.FONT3,anchor='w')
        lblshotshotsizesetting.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        shotsizesetting = StringVar()
        Eshotsizesetting  = ttk.Entry(Frm3,textvariable=shotsizesetting,width=10,font=self.FONT3,style="EntryStyle.TEntry",state=DISABLED)
        Eshotsizesetting.grid(row=2,column=1,padx=10,pady=10,sticky=W)


        lblholdposition = ttk.Label(Frm3,text='Hold position mm.',font=self.FONT3,anchor='w')
        lblholdposition.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        holdposition = StringVar()
        Eholdposition = ttk.Entry(Frm3,textvariable=holdposition,width=10,font=self.FONT3,style="EntryStyle.TEntry",state=DISABLED)
        Eholdposition.grid(row=3,column=1,padx=10,pady=10,sticky=W)

#---------------------------------------------- 4.Maximum flow rate  Gate diameter limit  -----------------------------------------#
        Frm4 = Frame(GUI1)
        Frm4.place(x=400,y=50)
        lblshotsize = ttk.Label(GUI1,text='4.Maximum flow rate  Gate diameter limit',font=self.FONT2)
        lblshotsize.place(x=400,y=20)


        lbldiameter = ttk.Label(Frm4,text='Diameter mm.',font=self.FONT3,anchor='w')
        lbldiameter.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        diagate = StringVar()
        Ediameter = ttk.Entry(Frm4,textvariable=diagate,width=10,font=self.FONT3)
        Ediameter.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        lblnumberofgate = ttk.Label(Frm4,text='Number of Gate',font=self.FONT3,anchor='w')
        lblnumberofgate.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        numberofgate = StringVar()
        Enumberofgate  = ttk.Entry(Frm4,textvariable=numberofgate,width=10,font=self.FONT3)
        Enumberofgate.grid(row=2,column=1,padx=10,pady=10,sticky=W)


        lblshearrate = ttk.Label(Frm4,text='Shear rate 1/Sec',font=self.FONT3,anchor='w')
        lblshearrate.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        shearrate = StringVar()
        Eshearrate = ttk.Entry(Frm4,textvariable=shearrate,width=10,font=self.FONT3)
        Eshearrate.grid(row=3,column=1,padx=10,pady=10,sticky=W)
        shearrate.set(100000)

        lblflowrate = ttk.Label(Frm4,text='Flow rate cm3/Sec.',font=self.FONT3,anchor='w')
        lblflowrate.grid(row=4,column=0,padx=10,pady=10,sticky=W)
        flowrate = StringVar()
        Eflowrate = ttk.Entry(Frm4,textvariable=flowrate,width=10,font=self.FONT3,style="EntryStyle.TEntry",state=DISABLED)
        Eflowrate.grid(row=4,column=1,padx=10,pady=10,sticky=W)

#--------- 5. Injection time เวลาในการฉีดพลาสติก -------------------------------------------------------------------------------------#

        Frm5 = Frame(GUI1)
        Frm5.place(x=400,y=260)
        lblinjectiontime = ttk.Label(GUI1,text='5. Injection time',font=self.FONT2,anchor='w')
        lblinjectiontime.place(x=400,y=240)


        lblinjtime = ttk.Label(Frm5,text='Injection time.     ',font=self.FONT3,anchor='w')
        lblinjtime.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        injtime = StringVar()
        Einjtime = ttk.Entry(Frm5,textvariable=injtime,width=10,font=self.FONT3,style="EntryStyle.TEntry",state=DISABLED)
        Einjtime.grid(row=0,column=1,padx=10,pady=10,sticky=W)


#------------6. Holding time -----------------------------------------------------------------------------------------------------#

        Frm6 = Frame(GUI1)
        Frm6.place(x=400,y=340)
        lblholdtime = ttk.Label(GUI1,text='6. Holding time',font=self.FONT2)
        lblholdtime.place(x=400,y=310)

        lblholdtime1 = ttk.Label(Frm6,text='* sec.          ',font=self.FONT3,anchor='w')
        lblholdtime1.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        holdtime = StringVar()
        Eholdtime = ttk.Entry(Frm6,textvariable=holdtime,width=10,font=self.FONT3,style="EntryStyle.TEntry")
        Eholdtime.grid(row=0,column=1,padx=10,pady=10,sticky=W)


        lblmaxholdtime = ttk.Label(Frm6,text='* Max sec.          ',font=self.FONT3,anchor='w')
        lblmaxholdtime.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        maxholdtime = StringVar()
        Emaxholdtime = ttk.Entry(Frm6,textvariable=maxholdtime,width=10,font=self.FONT3,style="EntryStyle.TEntry")
        Emaxholdtime.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        lblminholdtime = ttk.Label(Frm6,text='* Min sec.          ',font=self.FONT3,anchor='w')
        lblminholdtime.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        minholdtime = StringVar()
        Eminholdtime = ttk.Entry(Frm6,textvariable=minholdtime,width=10,font=self.FONT3,style="EntryStyle.TEntry")
        Eminholdtime.grid(row=2,column=1,padx=10,pady=10,sticky=W)
#----------------7. Injection Speed -----------------------------------------------------------------------------------------------#
        Frm7 = Frame(GUI1)
        Frm7.place(x=400,y=510)
        lblinjectionspeed = ttk.Label(GUI1,text='7. Injection Speed',font=self.FONT2)
        lblinjectionspeed.place(x=400,y=480)

        lblinjspeed = ttk.Label(Frm7,text='Injection speed mm./sec.',font=self.FONT3,anchor='w')
        lblinjspeed.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        injspeed = StringVar()
        Einjspeed = ttk.Entry(Frm7,textvariable=injspeed,width=10,font=self.FONT3,style="EntryStyle.TEntry")
        Einjspeed.grid(row=0,column=1,padx=10,pady=10,sticky=W)
#--------------8. Cooling Time estimate -------------------------------------------------------------------------------------------#
        Frm8 = Frame(GUI1)
        Frm8.place(x=700,y=130)
        lblinjectionspeed = ttk.Label(GUI1,text='8. Cooling time estimate',font=self.FONT2)
        lblinjectionspeed.place(x=700,y=100)

        lbleffectthermal = ttk.Label(Frm8,text='Effective thermal diffusivity *',font=self.FONT3,anchor='w')
        lbleffectthermal.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        effthermal = StringVar()
        Eeffthermal = ttk.Entry(Frm8,textvariable=effthermal,width=10,font=self.FONT3)
        Eeffthermal.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        effthermal.set(0.067)

        lblpartthick = ttk.Label(Frm8,text='Part Thickness mm. *',font=self.FONT3,anchor='w')
        lblpartthick.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        partthickness = StringVar()
        Epartthickness = ttk.Entry(Frm8,textvariable=partthickness,width=10,font=self.FONT3)
        Epartthickness.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        partthickness.set(1.35)

        lblmelttemp = ttk.Label(Frm8,text='Melt tem.°c *',font=self.FONT3,anchor='w')
        lblmelttemp.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        melttemp = StringVar()
        Emelttemp = ttk.Entry(Frm8,textvariable=melttemp,width=10,font=self.FONT3)
        Emelttemp.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        melttemp.set(230)

        lblmoldtemp = ttk.Label(Frm8,text='Mold tem.°c *',font=self.FONT3,anchor='w')
        lblmoldtemp.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        moldtemp = StringVar()
        Emoldtemp = ttk.Entry(Frm8,textvariable=moldtemp,width=10,font=self.FONT3)
        Emoldtemp.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        moldtemp.set(18)

        
        lblejectortemp = ttk.Label(Frm8,text='Ejector temp. °C *',font=self.FONT3,anchor='w')
        lblejectortemp.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        ejectortemp = StringVar()
        Eejectortemp = ttk.Entry(Frm8,textvariable=ejectortemp,width=10,font=self.FONT3)
        Eejectortemp.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        ejectortemp.set(90)


        lblglasstransition = ttk.Label(Frm8,text='Glass transition °c *',font=self.FONT3,anchor='w')
        lblglasstransition.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        glasstransition = StringVar()
        data = []
        for row in view_data('glass_transition'):
              data.append(row[2])
        Cboglasstransition = ttk.Combobox(Frm8,textvariable=glasstransition,width=10,font=self.FONT3)
        Cboglasstransition['values'] = data
        Cboglasstransition.grid(row=5,column=1,padx=10,pady=5,sticky=W)
        glasstransition.set(130)

        lblcoolingtime = ttk.Label(Frm8,text='Cooling time sec.',font=self.FONT3,anchor='w')
        lblcoolingtime.grid(row=6,column=0,padx=10,pady=5,sticky=W)
        coolingtime = StringVar()
        Ecoolingtime = ttk.Entry(Frm8,textvariable=coolingtime,width=10,font=self.FONT3,style="EntryStyle.TEntry")
        Ecoolingtime.grid(row=6,column=1,padx=10,pady=5,sticky=W)

#-----------------------Calculate Injection Data --------------------------------------------------------------------------------#
        def volumneatmeltcalculator():
                try:
                        pw = float(partweight.get()) # Part weight
                        cav =  float(cavity.get())   # Cavity of mold
                        d = float(density.get())     # Material density
                        scd = float(screwdiameter.get()) #Screw Diameter
                        cush = float(cushion.get())  # Cushion Setting
                        dia_gate = float(diagate.get())
                        numgate = float(numberofgate.get())
                        shear = float(shearrate.get())
                        partthick = float(partthickness.get())
                        effther = float(effthermal.get())
                        meltT = float(melttemp.get())
                        moldT = float(moldtemp.get())
                        ejectorT = float(ejectortemp.get())
                        glasstrans = float(glasstransition.get())
                        screwD = float(screwdiameter.get())

                        volumnmeltresult = round((pw * cav) / d ,0)   #Volumn at melt cm3
                        volumnmelt.set(volumnmeltresult)     #seting value to Entry Result

                        shortstrokeResult = round(((28 * volumnmeltresult / (22 * (scd / 10 ) **2))*10),0) # Short Stroke mm.
                        shortstroke.set(shortstrokeResult)

                        shotsize_data = round(cush + shortstrokeResult,0)  # shot size mm.
                        shotsizesetting.set(shotsize_data)

                        holdpos = round((shortstrokeResult * 0.1) + cush ,0)
                        holdposition.set(holdpos)

                        flowratedata = round(((shear * 3.142857 * (dia_gate / 20)**3)/4) * numgate,2)
                        flowrate.set(flowratedata)

                        injtimeresult = round((volumnmeltresult * 0.9) / flowratedata,2)
                        injtime.set(injtimeresult)

                        holdtimeresult = round((0.1729 * (partthick ** 2)/ effther ) * math.log((1.6023) * (meltT - moldT)/(glasstrans - moldT)),0)
                        holdtime.set(holdtimeresult)

                        cooltp = round((partthick) **2 / (3.142857 ** 2 * effther) * math.log((4/3.142857) * (meltT - moldT) / (ejectorT - moldT)),2)
                        coolingtime.set(cooltp)

                        maxholdT =  (0.8 * cooltp)
                        maxholdtime.set(maxholdT)

                        minholdT =  (0.2 * cooltp)
                        minholdtime.set(minholdT)

                        injsp = flowratedata * 1000 * 4 / ((22/7) * (screwD ** 2))
                        injspeed.set(injsp) 
                        

                except ValueError as error:
                        messagebox.showinfo('แจ้งเตือน',f'{error}')
                        
                        #GUI1.focus_force()
                        
                        
        def Savedata():
                pn = partname.get()
                pw = float(partweight.get()) # Part weight
                cav =  float(cavity.get())   # Cavity of mold
                # d = float(density.get())     # Material density
                # scd = float(screwdiameter.get()) #Screw Diameter
                # cush = float(cushion.get())  # Cushion Setting
                # dia_gate = float(diagate.get())
                # numgate = float(numberofgate.get())
                # shear = float(shearrate.get())
                # partthick = float(partthickness.get())
                # effther = float(effthermal.get())
                # meltT = float(melttemp.get())
                # moldT = float(moldtemp.get())
                # ejectorT = float(ejectortemp.get())
                # glasstrans = float(glasstransition.get())
                # screwD = float(screwdiameter.get())
                print(pn,pw,cav)
                print('Save Complete')




        Btn_Calculate = ttk.Button(GUI1,text='คำนวณ',style='a.TButton',command=volumneatmeltcalculator)
        Btn_Calculate.place(x=700,y=500,width=150)

        Btn_save = ttk.Button(GUI1,text='บันทึกข้อมูล',style='a.TButton',command=Savedata)
        Btn_save.place(x=700,y=550,width=150)

        GUI1.attributes('-topmost', False)

        
#----------------------------------------------------------------------------------------------------------------------------------#       

#---------------form injection data -----------------------------------------------------------------------------------------------#

    def injectioncalform(self):
        
        BT= ttk.Style()
        BT.configure('a.TButton',font=('Calibri',14))


        GUI1  = Toplevel()
        GUI1.geometry('1000x650')
        #GUI1.state('zoom')
        GUI1.title('คำนวณค่าเบื้องต้นในการปรับเครื่องฉีด')

        self.injectiondataresult(GUI1)
        
                        
       
       
        GUI1.attributes('-topmost', False)
        GUI1.focus_force()
        GUI1.grab_set()
        GUI1.mainloop()
      
      
#--------------------------------------------------------------------------------------------------------------------------------------#

        




