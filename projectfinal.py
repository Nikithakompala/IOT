from tkinter import *
from time import strftime
import random
import webbrowser
#main window
window = Tk()
window.geometry("1920x1080")
#canvas creation
cm=Canvas(window,height=1000,width=1600,bg="black")
cm.place(x=0,y=0)
#oval
oval= Canvas(window, width=500, height=500,bg="black",highlightthickness=0)
oval.place(x=1100,y=470)
oval.create_oval(20,20,400,250,outline = "black", fill = "red")
#visheh offer
flash_delay = 500
flash_colours_vo = ('white', 'black') 
def flashColourvo(object, colour_index):
    object.config(foreground = flash_colours_vo[colour_index])
    window.after(flash_delay, flashColourvo, object, 1 - colour_index)
labelvo =Label(window,text="vishesh spl offer",
               font="times 24 bold underline ",background="red",
                      foreground = flash_colours_vo[0])
labelvo.place(x=1200, y=530)
flashColourvo(labelvo, 0)
labelof=Label(window,text="On this occasion \n 20% off on all items",font="roman 20 bold",fg="white",bg="red")
labelof.place(x=1200,y=590)
#heading colour
c=Canvas(window,height=105,width=1600,bg="orange")
c.pack()
#mrec photo
canvas = Canvas(window, width = 100, height = 100,bg="orange")      
canvas.place(x=25 ,y=3)     
img = PhotoImage(file="MREC_logo3.png")      
canvas.create_image(20,20,anchor=NW ,image=img)
#mrec canteen name
labelh = Label(window, text="MALLAREDDY CANTEEN SERVICES",
               font="times 30 underline bold",bg="orange")
labelh.place(x=500, y=50, anchor="center")
#quote under heading
labelq=Label(window,text="Nothing brings people together rather than food ",
                font="arial 14 italic bold ",foreground="green",bg="orange")
labelq.place(x=500, y=75,anchor="nw")
#address in top
labelad = Label(window, text="Maisammaguda,Secundrabad.",
               font="times 14 bold",foreground="blue",bg="orange")
labelad.place(x=875, y=50)
#contact address code
labelcad=Label(window,text="Contact us:",font="times 18 bold", foreground="red",bg="orange")
labelcad.place(x=1150,y=10)
labelgmail=Label(window,text="www.mreccanteenservices.com",font="times 14 bold",foreground="black",bg="orange")
labelgmail.place(x=1150,y=75)
labelgmail=Label(window,text="ph: 8247081289",font="times 14 bold",foreground="black",bg="orange")
labelgmail.place(x=1150,y=55)
labelgmail=Label(window,text="mallareddycanteenservices@gmail.com",font="times 14 bold",foreground="black",bg="orange")
labelgmail.place(x=1150,y=35)

#TOP picks code
flash_delay = 500
flash_colours_tp = ('red', 'white')

def flashColour1(object, colour_index):
    object.config(foreground = flash_colours_tp[colour_index])
    window.after(flash_delay, flashColour1, object, 1 - colour_index)
label3 =Label(window,text="Top Picks of the day",
               font="times 28 bold underline",background="black",
                      foreground = flash_colours_tp[0])
label3.place(x=900, y=120)
flashColour1(label3, 0)

label5 = Label(window, text="Biryani  Starting from..........",font="times 20",fg="white",bg="black")#Biryani
label5.place(x=900, y=170)
label6 = Label(window, text="Rs 149/-",font="times 20",fg="white",bg="black")
label6.place(x=1200, y=170)
label7 = Label(window, text="Puffs Starting from...........",font="times 20",fg="white",bg="black")#Puff
label7.place(x=900, y=210)
label8 = Label(window, text="Rs 19/-",font="times 20",fg="white",bg="black")
label8.place(x=1200, y=210)
label9 = Label(window, text="Cool Drink............",font="times 20",fg="white",bg="black")#Cool drink 
label9.place(x=900, y=250)
label10 = Label(window, text="Rs 20/-",font="times 20",fg="white",bg="black")
label10.place(x=1200, y=250)
#combos
flash_delay = 500
flash_colours_c = ('white', 'red')

def flashColour3(object, colour_index):
    object.config(foreground = flash_colours_c[colour_index])
    window.after(flash_delay, flashColour3, object, 1 - colour_index)
labelc =Label(window,text="Combos in Canteen",
               font="times 28 bold underline",background="black",
                      foreground = flash_colours_c[0])
labelc.place(x=900, y=300)
flashColour3(labelc, 0)
#combo1
combo1 = Menubutton(window, text = "Combo 1",font="times 24",fg="white",bg="black")       
combo1.menu = Menu(combo1)  
combo1["menu"]= combo1.menu
combo1.menu.add_checkbutton(label = "Rate = 149/-",font="times 18")
combo1.menu.add_checkbutton(label = "Biryani",font="times 18")
combo1.menu.add_checkbutton(label = "Cool drink",font="times 18")
combo1.menu.add_checkbutton(label = "Gulab jam",font="times 18")
combo1.place(x=900,y=350)
ec1=Entry(window)
ec1.place(x=1055,y=365)
#combo2
combo2 = Menubutton(window, text = "Combo 2",font="times 24",fg="white",bg="black")       
combo2.menu = Menu(combo2)  
combo2["menu"]= combo2.menu
combo2.menu.add_checkbutton(label = "Rate = 129/-",font="times 18")
combo2.menu.add_checkbutton(label = "Chicken fried rice",font="times 18")
combo2.menu.add_checkbutton(label = "Chicken manchuria",font="times 18")
combo2.menu.add_checkbutton(label = "Ice cream",font="times 18")
combo2.place(x=900,y=395)
ec2=Entry(window)
ec2.place(x=1055,y=410)
#combo3
combo3 = Menubutton(window, text = "Combo 3",font="times 24",fg="white",bg="black")       
combo3.menu = Menu(combo3)  
combo3["menu"]= combo3.menu
combo3.menu.add_checkbutton(label = "Rate = 99/-",font="times 18")
combo3.menu.add_checkbutton(label = "Puff",font="times 18")
combo3.menu.add_checkbutton(label = "Sandwich",font="times 18")
combo3.menu.add_checkbutton(label = "2 Cooldrinks",font="times 18")
combo3.place(x=900,y=440)
ec3=Entry(window)
ec3.place(x=1055,y=455)
#MENU TOTAL CODE

#menu heading and flashing
flash_delay = 500
flash_colours = ('white', 'yellow')

def flashColour2(object, colour_index):
    object.config(foreground = flash_colours[colour_index])
    window.after(flash_delay, flashColour2, object, 1 - colour_index)
label17 =Label(window,text="MENU",
               font="roman 40 bold underline",bg="black",
                      foreground = flash_colours[0])
label17.place(x=100, y=120)
flashColour2(label17, 0)

#biryani
labelb=Label(window,text="Biryani",font="times 25 underline",fg="white",bg="black")
labelb.place(x=20,y=220)
labelqt=Label(window,text="*Quantity",font="times 15",fg="white",bg="black")
labelqt.place(x=280,y=225)

labelcb=Label(window,text="Chicken Biryani   149/-",font="times 18",fg="white",bg="black")
labelcb.place(x=20,y=270)
ecb=Entry(window)
ecb.place(x=260,y=275)

labelmb=Label(window,text="Mutton Biryani    199/-",font="times 18",fg="white",bg="black")
labelmb.place(x=20,y=295)
emb=Entry(window)
emb.place(x=260,y=300)

labelpb=Label(window,text="Prawns Biryani    249/-",font="times 18",fg="white",bg="black")
labelpb.place(x=20,y=320)
epb=Entry(window)
epb.place(x=260,y=325)
#puffs
labelpf=Label(window,text="Puffs",font="times 25 underline",fg="white",bg="black")
labelpf.place(x=20,y=360)

labelcpf=Label(window,text="Chiken Puffs       39/-",font="times 18",fg="white",bg="black")
labelcpf.place(x=20,y=410)
ecpf=Entry(window)
ecpf.place(x=260,y=415)

labelepf=Label(window,text="Egg Puffs             29/-",font="times 18",fg="white",bg="black")
labelepf.place(x=20,y=435)
eepf=Entry(window)
eepf.place(x=260,y=440)

labelvpf=Label(window,text="Veg Puffs            19/-",font="times 18",fg="white",bg="black")
labelvpf.place(x=20,y=460)
evpf=Entry(window)
evpf.place(x=260,y=465)
#Cooldrinks
labelcd=Label(window,text="Cool Drinks",font="times 25 underline",fg="white",bg="black")
labelcd.place(x=450,y=220)
labelqt=Label(window,text="*Quantity",font="times 15",fg="white",bg="black")
labelqt.place(x=700,y=220)

labeldc=Label(window,text="Diet coke             30/-",font="times 18",fg="white",bg="black")
labeldc.place(x=450,y=270)
edc=Entry(window)
edc.place(x=680,y=275)

labelsp=Label(window,text="Sprit 300ml          20/-",font="times 18",fg="white",bg="black")
labelsp.place(x=450,y=295)
esp=Entry(window)
esp.place(x=680,y=300)

labelmd=Label(window,text="Mountain dew     30/-",font="times 18",fg="white",bg="black")
labelmd.place(x=450,y=320)
emd=Entry(window)
emd.place(x=680,y=325)
#icecreams
labelic=Label(window,text="Ice creams",font="times 25 underline",fg="white",bg="black")
labelic.place(x=450,y=360)

labelv=Label(window,text="Vannila               40/-",font="times 18",fg="white",bg="black")
labelv.place(x=450,y=410)
ev=Entry(window)
ev.place(x=680,y=415)

labelch=Label(window,text="Chocalate           50/-",font="times 18",fg="white",bg="black")
labelch.place(x=450,y=435)
ech=Entry(window)
ech.place(x=680,y=440)

labelbs=Label(window,text="Butter scotch      70/-",font="times 18",fg="white",bg="black")
labelbs.place(x=450,y=460)
ebs=Entry(window)
ebs.place(x=680,y=465)

labels=Label(window,text="Strawberry          60/-",font="times 18",fg="white",bg="black")
labels.place(x=450,y=485)
es=Entry(window)
es.place(x=680,y=490)
#calculation of bill part

def calculate():
        bill=Toplevel(window)
        bill.geometry("800x800")
        c2=Canvas(bill,height=1000,width=800,bg="BLACK")
        c2.place(x=1,y=1)
        c1=Canvas(bill,height=95,width=800,bg="orange")
        c1.pack()
        dic = {1: [ecb, 149,"Chiken biryani"],
               2: [emb,199,"Mutton biryani"],
               3: [epb,249,"Prawns biryani"],
               4: [ecpf,39,"Chicken puff"],
               5: [eepf,29,"Egg puff"],
               6: [evpf,19,"Veg puff"],
               7: [edc,30,"Diet coke"],
               8: [esp,20,"Sprit"],
               9:[emd,30,"Mountain dew"],
               10:[ev,40,"Vannila"],
               11:[ech,50,"Choclate"],
               12:[ebs,70,"Butterscotch"],
               13:[es,60,"strawberry"],
               14:[ec1,149,"Combo 1"],
               15:[ec2,129,"Combo 2"],
               16:[ec3,99,"Combo 3"]}
        total = 0
        i=j=k=l=130
        #bill totaling loop
        for key, val in dic.items():
            if val[0].get() != "":
                total += int(val[0].get())*val[1]
        #bill item printing loop
        for key, val in dic.items():
            if val[0].get() !="":
                string=val[2]
                labelpbi=Label(bill,text=string,font="times 16",fg="white",bg="black")
                labelpbi.place(x=50,y=i)
                i+=30
                qty=val[0].get()
                labelpbq=Label(bill,text=qty,font="times 16",fg="white",bg="black")
                labelpbq.place(x=250,y=j)
                j+=30
                price=val[1]
                labelpbr=Label(bill,text=str(price)+"/-",font="times 16",fg="white",bg="black")
                labelpbr.place(x=350,y=k)
                k+=30
                rate=val[1]*int(val[0].get())
                labelpbr=Label(bill,text=str(rate)+"/-",font="times 16",fg="white",bg="black")
                labelpbr.place(x=450,y=l)
                l+=30
    #bill outline code
        def openNewWindow():
            newWindow = Toplevel(bill)
            newWindow.title("payment")
            newWindow.geometry("500x500")
            cp=Canvas(newWindow,height=600,width=600,bg="black")
            cp.place(x=0,y=0)
            labelph = Label(newWindow, text="ONLINE PAYMENTS",font="times 30 underline bold",bg="orange")
            labelph.place(x=200, y=30, anchor="center")
            def openpaytmwebsite():
                webbrowser.open("https://www.paytm.com",new=1)
                labelending=Label(newWindow,text="Payment done!!\nThanks and visit again!!",font="times 28",fg="white",bg="black")
                labelending.place(x=50,y=400)
            def opengpaywebsite():
                webbrowser.open("https://www.googlepay.com",new=1)
                labelending=Label(newWindow,text="Payment done!!\nThanks and visit again!!",font="times 28",fg="white",bg="black")
                labelending.place(x=50,y=400)
            def openphonepwebsite():
                webbrowser.open("https://www.phonepe.com",new=1)
                labelending=Label(newWindow,text="Payment done!!\nThanks and visit again!!",font="times 28",fg="white",bg="black")
                labelending.place(x=50,y=400)
            def cash():
                cash=Toplevel(newWindow)
                cash.geometry("500x500")
                cc=Canvas(cash,height=1000,width=1000,bg="black")
                cc.place(x=0,y=0)
                labelending=Label(cash,text="Thanks and visit again!!",font="times 28",fg="white",bg="black")
                labelending.place(x=80,y=175)
            buttonpaytm=Button(newWindow,text="pay with paytm",font="times 16",fg="white",bg="black",command=openpaytmwebsite)
            buttonpaytm.place(x=50,y=100)
            buttongpay=Button(newWindow,text="pay with G-pay",font="times 16",fg="white",bg="black",command=opengpaywebsite)
            buttongpay.place(x=50,y=150)
            buttonppay=Button(newWindow,text="pay with Phone pay",font="times 16",fg="white",bg="black",command=openphonepwebsite)
            buttonppay.place(x=50,y=200)
            buttonppay=Button(newWindow,text="pay with cash",font="times 16",fg="white",bg="black",command=cash)
            buttonppay.place(x=50,y=250) 
        btn = Button(bill,text ="payment",font="times 22 " ,fg="light green",bg="black",command = openNewWindow)
        btn.place(x=400,y=600)
        labelbillh=Label(bill,text="MALLAREDDY CANTEEN SERVICES ",font="times 26 underline bold",bg="orange")
        labelbillh.place(x=45,y=5)
        labelbillsh=Label(bill,text="BILL",font="times 20",bg="orange")
        labelbillsh.place(x=280,y=60)
        n=random.randint(1000,9999)
        labelbillsn=Label(bill,text="Serial no:"+str(n),font="romans 14",bg="orange")
        labelbillsn.place(x=50,y=60)
    
        #time
        time_string=strftime("%d-%m-%y\n %H:%M %p \n %A")
        labeldandt=Label(bill,text=time_string,font="romans 12",bg="orange")
        labeldandt.place(x=700,y=36)
        labelitem=Label(bill,text="Item",fg="yellow",bg="black",font="times 14")
        labelitem.place(x=50,y=100)
        labelqty=Label(bill,text="Quantity",fg="yellow",bg="black",font="times 14")
        labelqty.place(x=250,y=100)
        labelrate=Label(bill,text="Price",fg="yellow",bg="black",font="times 14")
        labelrate.place(x=350,y=100)
        labelst=Label(bill,text="Sub total",fg="yellow",bg="black",font="times 14")
        labelst.place(x=450,y=100)
        #total amount
        labelt = Label(bill,text="Total amount is "+str(total)+"/-",font="times 20",fg="yellow",bg="black")
        labelt.place(x=50, y=610)
        #payment options

 
labelq=Label(window,text="developed by PYTHON TECHIES  ",
                font="arial 12 italic bold ",foreground="green",bg="orange")
labelq.place(x=1250,y=750)

def tables():
    n=random.randint(1,50)
    labeltablen=Label(window,text="table no: "+str(n)+"  is alloted to you ",font="romans 18",bg="orange")
    labeltablen.place(x=320,y=640)
#table booking
buttontable=Button(text="Click to book Table",font="times 20",command=tables)
buttontable.place(x=70,y=630)
#buy button
buttonbuy=Button(window,text="Buy",font="times 24",command=calculate)
buttonbuy.place(x=800,y=700)

window.mainloop()

