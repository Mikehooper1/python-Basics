from email.headerregistry import Group
from textwrap import fill
from tkinter import*
from turtle import bgcolor, right
class Bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("CSW Billing")
        bg_color = "#343434"
        title=Label(self.root,text="CSW Billing",bd=12,relief=GROOVE,bg="#343434",fg="#F39C12",font=("times new roman",30,"bold"),pady=2).pack( fill=X)
        #__________________________________Variables__________________________________________________
        #__________________________________Item Details________________________________________________
        self.Chocolate_Tea=IntVar()
        self.Rose_Tea=IntVar()
        self.Elichi_Tea=IntVar()
        self.Tea=IntVar()

        #__________________________________Total Item Price & Tax ________________________________________________
        self.Itemdetail_price=StringVar()

        self.Itemdetail_tax=StringVar()

        #__________________________________Total Item Price & Tax ________________________________________________
        self.c_name=StringVar()
        self.c_mobile=StringVar()
        self.bill_no=StringVar()
        self.search_bill=StringVar()




        #_______________Customer Detail Frame___________________________________________________________________________________________________________________________________
        F1 = LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bd=10,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphone_lbl=Label(F1,text="Mobile Number",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,textvariable=self.c_mobile,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cbill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)

        #___________________Item Details____________________
        F2 = LabelFrame(self.root,text="Item Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=170,width=325,height=380)

        cho_tea=Label(F2,text="Chocolate Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="#F1C40F").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        cho_tea_txt=Entry(F2,width=10,textvariable=self.Chocolate_Tea,font=("times now roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        rose_tea=Label(F2,text="Rose Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="#F1C40F").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        rose_tea_txt=Entry(F2,width=10,textvariable=self.Rose_Tea,font=("times now roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        eli_tea=Label(F2,text="Elichi Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="#F1C40F").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        eli_tea_txt=Entry(F2,width=10,textvariable=self.Elichi_Tea,font=("times now roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        tea=Label(F2,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="#F1C40F").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        tea_txt=Entry(F2,width=10,textvariable=self.Tea,font=("times now roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        #_________________________Bill Area_________________________________
        F3 = Frame(self.root,bd=10,relief=GROOVE)
        F3.place(x=340,y=170,width=325,height=380,)
        bill_title=Label(F3,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F3,orient=VERTICAL)
        self.txtarea=Text(F3,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #_________________________Button Frame_________________________________
        F4 = LabelFrame(self.root,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=0,y=560,relwidth=1,height=140)
        m1_lbl=Label(F4,text="Total Item Price",bg=bg_color,fg="#F1C40F",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F4,width=18,textvariable=self.Itemdetail_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        t1_lbl=Label(F4,text="Total Tax",bg=bg_color,fg="#F1C40F",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        t1_txt=Entry(F4,width=18,textvariable=self.Itemdetail_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        btn_F=Frame(F4,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5 )
        GBill_btn=Button(btn_F,text="Genrate Bill",bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5 )
        Clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5 )
        Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5 )


    def total(self):
        self.total_Itemdetail_price=(
                                    (self.Chocolate_Tea.get()*10)+
                                    (self.Rose_Tea.get()*10)+
                                    (self.Elichi_Tea.get()*10)+
                                    (self.Tea.get()*10)
            )
        self.Itemdetail_price.set(str(self.total_Itemdetail_price))

root=Tk()
obj = Bill_app(root)
root.mainloop()