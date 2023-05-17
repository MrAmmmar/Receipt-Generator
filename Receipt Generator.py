#importing modules
from tkinter import *
from tkinter import messagebox
import math
import random
import os
# MAKING RGB FUNVTION:

#deffining class for the receipt maker
class Receipt_Maker:
    # using __init__() function to assign values to the objects
    def __init__ (self,root):
        self.root = root
        #main structure
        # size of the structure
        self.root.geometry('1350x700+0+0')
        # title
        self.root.title('Receipt Generator')
        # background colour
        bg_colour = "#000000"
        title = Label(self.root, text="Sunset Mart", bd=12, relief=GROOVE, font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        # defining items
        # cosmetics:
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.perfume = IntVar()
        self.spray = IntVar()
        self.lotion = IntVar()

        # staples
        self.rice = IntVar()
        self.sugar = IntVar()
        self.flour = IntVar()
        self.cooking_oil = IntVar()
        self.lentils = IntVar()
        self.salt = IntVar()

        # Beverages

        self.soft_drink = IntVar()
        self.energy_drink = IntVar()
        self.lemonade = IntVar()
        self.fruit_juice = IntVar()
        self.water = IntVar()
        self.chilled_latte = IntVar()


        # price and taxes

        self.cosmetics_price = StringVar()
        self.staples_price = StringVar()
        self.beverages_price = StringVar()

        self.cosmetics_tax = StringVar()
        self.staples_tax = StringVar()
        self.beverages_tax = StringVar()

        #customer details

        self.name = StringVar()
        self.phone_no = StringVar()
        self.bill_no = StringVar()

        # assigning random value for bill number
        x = random.randint(1,100)
        self.bill_no.set(str(x))

        # frame customer details
        # main frame

        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"), fg='gold', bg=bg_colour )
        F1.place(x=0, y=80, relwidth=1)

        # customer name label and entry box

        name_lbl = Label(F1, text="Customer Name", font=("times new roman", 18, 'bold'), bg=bg_colour, fg='white').grid(row=0, column=0, padx=20, pady=5)
        name_txt = Entry(F1,width=15, font="arial 15",bd=7,textvariable=self.name,relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        # customer phone number label and entry box

        phone_lbl = Label(F1, text="Phone No", font=("times new roman", 18, 'bold'), bg=bg_colour, fg='white').grid(row=0, column=2, padx=20, pady=5)
        phone_txt = Entry(F1, width=15, font="arial 15",textvariable=self.phone_no, bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        # bill number label and entry box

        bill_lbl = Label(F1, text="Bill Number", font=("times new roman", 18, 'bold'), bg=bg_colour, fg='white').grid(row=0, column=4, padx=20, pady=5)
        bill_txt = Entry(F1, width=15, font="arial 15", bd=7,textvariable=self.bill_no, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

       

        # frame cosmetics

        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),fg='gold',bg=bg_colour)
        F2.place(x=5, y=180, width=325,height=380)

        # beauty soap label and entry box

        bath_lbl=Label(F2,text ='Beauty Soap',font=('times new roman',15,'bold'),bg=bg_colour,fg='lightgreen').grid(row=0,column=0,padx=10,pady=10,sticky='w')
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=('times new roman',15,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        # face cream label and entry box

        face_cream_lbl = Label(F2, text='Face Cream', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='lightgreen').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        # face wash label and entry box
        
        face_wash_lbl = Label(F2, text='Face Wash', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='lightgreen').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        face_wash_txt = Entry(F2, width=10,textvariable=self.face_wash, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        # perfume label and entry 
        
        perfume_lbl = Label(F2, text='Perfume', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='lightgreen').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        perfume_txt = Entry(F2, width=10,textvariable=self.perfume, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        # hair spray label and entry box

        hair_spray_lbl = Label(F2, text='Hair Spray', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='lightgreen').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        hair_spray_text = Entry(F2, width=10, textvariable=self.spray, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        # lotion label and entry box

        lotion_lbl = Label(F2, text='Body Lotion', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='lightgreen').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        lotion_txt = Entry(F2, width=10,textvariable=self.lotion, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        # frame staples

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Staples", font=("times new roman",15,"bold"),fg='gold', bg=bg_colour)
        F3.place(x=340, y=180, width=325, height=380)

        # rice label and entry box

        rice_lbl = Label(F3, text='Rice', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='lightgreen').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        rice_txt = Entry(F3, width=10,textvariable=self.rice, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        # cooking oil label and entry box

        oil_lbl = Label(F3, text='Cooking Oil', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='lightgreen').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        oil_txt = Entry(F3, width=10,textvariable=self.cooking_oil, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        # lentils label and entry box

        lentils_lbl = Label(F3, text='Lentils', font=('times new roman', 15, 'bold'), bg=bg_colour,fg='lightgreen').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        lentils_txt = Entry(F3, width=10,textvariable=self.lentils, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        # flour label and entry box

        flour_lbl = Label(F3, text='Flour', font=('times new roman', 15, 'bold'), bg=bg_colour,fg='lightgreen').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        flour_txt = Entry(F3, width=10,textvariable=self.flour, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        # sugar label and entry box
        
        sugar_lbl = Label(F3, text='Sugar', font=('times new roman', 15, 'bold'), bg=bg_colour,fg='lightgreen').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        sugar_txt = Entry(F3, width=10,textvariable=self.sugar, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=4,column=1, padx=10,pady=10)

        # salt label and entry box
        
        salt_lbl = Label(F3, text='Salt', font=('times new roman', 15, 'bold'), bg=bg_colour,fg='lightgreen').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        salt_txt = Entry(F3, width=10,textvariable=self.salt, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # frame beverages

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Beverages", font=("times new roman", 15, "bold"),fg='gold', bg=bg_colour)
        F4.place(x=670, y=180, width=325, height=380)

        # soft drinks label and entry box

        softdrink_lbl = Label(F4, text='Soft Drink', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='lightgreen').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        softdrink_txt = Entry(F4, width=10,textvariable=self.soft_drink, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        # energy drinks label and entry box

        energydrink_lbl = Label(F4, text='Energy Drink', font=('times new roman', 15, 'bold'), bg=bg_colour,fg='lightgreen').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        energydrink_txt = Entry(F4, width=10,textvariable=self.energy_drink, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        # lemonade label and entry box

        lemonade_lbl = Label(F4, text='Lemonade', font=('times new roman', 15, 'bold'), bg=bg_colour,fg='lightgreen').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        lemonade_txt = Entry(F4, width=10,textvariable=self.lemonade, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        # juice label and entry box

        juice_lbl = Label(F4, text='Fruit Juice', font=('times new roman', 15, 'bold'), bg=bg_colour,fg='lightgreen').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        juice_txt = Entry(F4, width=10,textvariable=self.fruit_juice, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10, pady=10)

        # chilled latte label and entry box
        
        latte_lbl = Label(F4, text='Chilled Latte', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='lightgreen').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        latte_txt = Entry(F4, width=10,textvariable=self.chilled_latte, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        # water label and entry box
        
        water_lbl = Label(F4, text='Water', font=('times new roman', 15, 'bold'), bg=bg_colour,fg='lightgreen').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        water_txt = Entry(F4, width=10,textvariable=self.water, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # receipt

        F5 = LabelFrame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        # receipt title

        receipt_title = Label(F5,text='Receipt',font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_y.config(command=self.txtarea.yview)
        
        self.txtarea.pack(fill=BOTH,expand =1)

        # total and tax area

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Total", font=("times new roman", 15, "bold"),fg='gold',bg=bg_colour)
        F6.place(x=0, y=560, relwidth=1, height=140)

        # total price cosmetics

        m1_lbl=Label(F6,text='Total Cosmetics Price',font=('times new roman',14,'bold'),bg=bg_colour,fg="white").grid(row=0,column=0,padx=20,pady=1,sticky='w')
        m1_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cosmetics_price,bd=8,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        # total price staples

        m2_lbl = Label(F6, text='Total Staples Price', font=('times new roman', 14, 'bold'), bg=bg_colour,fg="white").grid(row=1, column=0, padx=20, pady=1, sticky='w')
        m2_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.staples_price, bd=8, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        # total price beverages

        m3_lbl = Label(F6, text='Total Beverages Price', font=('times new roman', 14, 'bold'), bg=bg_colour, fg="white").grid(row=2, column=0, padx=20, pady=1, sticky='w')
        m3_txt = Entry(F6, width=18, font="arial 10 bold", bd=8,textvariable=self.beverages_price, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        # cosmetics tax

        c1_lbl = Label(F6, text='Cosmetics Tax', font=('times new roman', 14, 'bold'), bg=bg_colour, fg="white").grid(row=0, column=2, padx=20, pady=1, sticky='w')
        c1_txt = Entry(F6, width=18, font="arial 10 bold", bd=8,textvariable=self.cosmetics_tax, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        # staples tax

        c2_lbl = Label(F6, text='Staples Tax', font=('times new roman', 14, 'bold'), bg=bg_colour, fg="white").grid(row=1, column=2, padx=20, pady=1, sticky='w')
        c2_txt = Entry(F6, width=18, font="arial 10 bold", bd=8,textvariable=self.staples_tax, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        # Beverages tax

        c3_lbl = Label(F6, text='Beverages Tax', font=('times new roman', 14, 'bold'), bg=bg_colour, fg="white").grid(row=2, column=2, padx=20, pady=1, sticky='w')
        c3_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.beverages_tax, bd=8, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        # buttons

        btn_frame =Frame(F6,bd=7,relief=GROOVE)
        btn_frame.place(x=750,width=585,height=105)
        
        # total button
        total_btn = Button(btn_frame,command=self.total,text='Total',bg='red',fg='white',pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=0,padx=100,pady=5)

        # generate receipt button
        g_btn = Button(btn_frame, text='Generate\nReceipt',command=self.receipt_area, bg='red', fg='white', pady=5, width=10, bd=2, font="arial 15 bold").grid(row=0, column=1, padx=0, pady=5)
        
    # defining function for total cost
    def total(self):
        # defining price and calculating its cost
        self.c_s_p= self.soap.get() * 40
        self.c_fc_p= self.face_cream.get() * 120
        self.c_fw_p= self.face_wash.get() * 250
        self.c_spray_p= self.spray.get() * 240
        self.c_g_p= self.perfume.get() * 450
        self.c_l_p= self.lotion.get() * 140

        # computing total for cosmetics
        if self.c_s_p >= 0 and self.c_fc_p >= 0 and self.c_fw_p >= 0 and self.c_spray_p >=0 and self.c_g_p >= 0 and self.c_l_p >= 0:
            self.total_cosmetic_price = float(
                     self.c_s_p+
                     self.c_fc_p+
                     self.c_fw_p+
                     self.c_spray_p+
                     self.c_g_p+
                     self.c_l_p
            )
        else:
            messagebox.showerror("Error", "Quantity should be a positive integer")
        # setting cosmetic total and tax
        self.cosmetics_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price * 0.07),2)
        self.cosmetics_tax.set("Rs. "+str(self.c_tax))

        # defining price and calculating its cost

        self.g_r_p = self.rice.get() * 150
        self.g_oil_p = self.cooking_oil.get() * 140
        self.g_l_p = self.lentils.get() * 150
        self.g_f_p = self.flour.get() * 120
        self.g_s_p = self.sugar.get() * 140
        self.g_st_p = self.salt.get() * 40
        
        # computing total for staples
        if self.g_r_p >= 0 and self.g_oil_p >= 0 and self.g_l_p >= 0 and self.g_f_p >= 0 and self.g_s_p >= 0 and self.g_st_p >= 0:
            self.total_staples_price = float(
                 self.g_r_p+
                 self.g_oil_p+
                 self.g_l_p+
                 self.g_f_p+
                 self.g_s_p+
                 self.g_st_p
            )
        else:
            messagebox.showerror("Error", "Quantity should be a positive integer")
       # setting staples total and tax
        self.staples_price.set("Rs. "+str(self.total_staples_price))
        self.g_tax=round((self.total_staples_price*0.13),2)
        self.staples_tax.set("Rs. "+str(self.g_tax))
        
        # defining price and calculating its cost
        self.sd_p =  self.soft_drink.get() * 50
        self.ed_p =  self.energy_drink.get() * 100
        self.l_p =  self.lemonade.get() * 70
        self.fj_p =  self.fruit_juice.get() * 150
        self.cl_p = self.chilled_latte.get() * 90
        self.w_p = self.water.get() * 40

        # computing total for beverages
        if self.sd_p >= 0 and self.ed_p>=0 and self.l_p >= 0 and self.fj_p >= 0 and self.cl_p>=0 and self.w_p>=0:
            self.total_beverage_price = float(
                 self.sd_p+
                 self.ed_p+
                 self.l_p+
                 self.fj_p+
                 self.cl_p+
                 self.w_p
            )
        else:
            messagebox.showerror("Error", "Quantity should be a positive integer")
        

        # setting beverages total and tax
        self.beverages_price.set("Rs. "+str(self.total_beverage_price))
        self.bvg_tax=round((self.total_beverage_price * 0.1),2)
        self.beverages_tax.set("Rs. "+str(self.bvg_tax))

        # computing total bill

        self.total_bill=round(float(self.total_cosmetic_price+
                              self.total_staples_price+
                              self.total_beverage_price+
                              self.c_tax+
                              self.g_tax+
                              self.bvg_tax
                              ),3)
    # generating main receipt
    def  main_receipt(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END, "\tWelcome to Sunset Mart\n")
        self.txtarea.insert(END, f"\nBill Number: {self.bill_no.get()} ")
        self.txtarea.insert(END, f"\nCustomer Name: {self.name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.phone_no.get()}")
        self.txtarea.insert(END, "\n======================================")
        self.txtarea.insert(END, "\nProducts\t\tQTY\t\tPrice ")
        self.txtarea.insert(END, "\n======================================")
    # function for main receipt area
    def receipt_area(self):
        if self.name.get()== "" or  self.phone_no.get()=="":
            messagebox.showerror("Error","Customer Details not found") # receipt will not generate if customer details are not found 
        elif self.cosmetics_price.get()=="Rs. 0.0" and self.staples_price.get()=="Rs. 0.0" and self.beverages_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Selected") # receipt will not generate if products are not found
        else:
            self.main_receipt()
            # Cosmetics
            # checking every item for printing on main receipt
            if self.soap.get() > 0:
                self.txtarea.insert(END, f"\nBath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            
            if self.face_cream.get() > 0:
                self.txtarea.insert(END, f"\nFace Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            
            if self.face_wash.get() > 0:
                self.txtarea.insert(END, f"\nFace Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            
            if self.spray.get() > 0:
                self.txtarea.insert(END, f"\nHair Spray\t\t{self.spray.get()}\t\t{self.c_spray_p}")
            
            if self.perfume.get() > 0:
                self.txtarea.insert(END, f"\nPerfume\t\t{self.perfume.get()}\t\t{self.c_g_p}")
            
            if self.lotion.get() > 0:
                self.txtarea.insert(END, f"\nBody Lotion\t\t{self.lotion.get()}\t\t{self.c_l_p}")
            
            # Staples
            if self.rice.get() > 0:
                self.txtarea.insert(END, f"\nRice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            
            if self.cooking_oil.get() > 0:
                self.txtarea.insert(END, f"\nCooking Oil\t\t{self.cooking_oil.get()}\t\t{self.g_oil_p}")
            
            if self.lentils.get() > 0:
                self.txtarea.insert(END, f"\nLentils\t\t{self.lentils.get()}\t\t{self.g_l_p}")
            
            if self.flour.get() > 0:
                self.txtarea.insert(END, f"\nFlour\t\t{self.flour.get()}\t\t{self.g_f_p}")
            
            if self.sugar.get() > 0:
                self.txtarea.insert(END, f"\nSugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
                
            if self.salt.get() > 0:
                self.txtarea.insert(END, f"\nSalt\t\t{self.salt.get()}\t\t{self.g_st_p}")
                
            # Beverages
            
            if self.soft_drink.get() > 0:
                self.txtarea.insert(END, f"\nSoft Drink\t\t{self.soft_drink.get()}\t\t{self.sd_p}")
                
            if self.energy_drink.get() > 0:
                self.txtarea.insert(END, f"\nEnergy Drink\t\t{self.energy_drink.get()}\t\t{self.ed_p}")
                
            if self.lemonade.get() > 0:
                self.txtarea.insert(END, f"\nLemonade\t\t{self.lemonade.get()}\t\t{self.l_p}")
                
            if self.fruit_juice.get() > 0:
                self.txtarea.insert(END, f"\nFruit Juice\t\t{self.fruit_juice.get()}\t\t{self.fj_p}")
                
            if self.chilled_latte.get() > 0:
                self.txtarea.insert(END, f"\nChilled Latte\t\t{self.chilled_latte.get()}\t\t{self.cl_p}")
                
            if self.water.get() > 0:
                self.txtarea.insert(END, f"\nWater\t\t{self.water.get()}\t\t{self.w_p}")
                
            self.txtarea.insert(END, "\n--------------------------------------")
            
            if self.cosmetics_tax.get() != 'Rs. 0.0' or self.staples_tax.get() != 'Rs. 0.0' or self.beverages_tax.get() != 'Rs. 0.0':
                
                self.total_tax = round(float (self.c_tax+ self.g_tax+self.bvg_tax),3)
                self.txtarea.insert(END, f"\nTotal Tax\t\t\t    Rs:{self.total_tax} ")
            
            self.txtarea.insert(END, f"\nTotal Bill: \t\t\t    Rs:{self.total_bill} ")
            self.txtarea.insert(END, "\n--------------------------------------\n")
            self.txtarea.insert(END, "\nThank you for Shopping at Sunset Mart")
            self.txtarea.insert(END, "\n--------------------------------------")
# calling the class
root = Tk()
obj = Receipt_Maker(root)
root.mainloop()

            


        
    

        
        
