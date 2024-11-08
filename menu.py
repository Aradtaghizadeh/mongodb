from customtkinter import *
from random import randint
from PIL import Image
from CTkMessagebox import CTkMessagebox as mess
import re,pymongo,time
from CTkScrollableDropdown import *

#===========================================Plus/Minus==================================================

a1=0
def p1():
    global a1
    global pp
    if a1<100:
        a1 = a1+1
        lpm1.configure(text=a1)
        pp=a1*10
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ") 
        lato1.configure(text=(f"{pp}$"))
a2=0
def p12():
    global a2
    if a2<100:
        a2 = a2+1
        lpm4.configure(text=a2)
        pi=a2*12
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato12.configure(text=(f"{pi}$"))
a3=0
def p13():
    global a3
    if a3<100:
        a3 = a3+1
        lpm5.configure(text=a3)
        pb=a3*14
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato13.configure(text=(f"{pb}$"))
n1=0
def p2():
    global n1
    if n1<100:
        n1 = n1+1
        lpm2.configure(text=n1)
        b=n1*5
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato2.configure(text=(f"{b}$"))
n2=0
def p22():
    global n2
    if n2<100:
        n2 = n2+1
        lpm6.configure(text=n2)
        cb=n2*6
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato22.configure(text=(f"{cb}$"))
n3=0
def p23():
    global n3
    if n3<100:
        n3 = n3+1
        lpm7.configure(text=n3)
        dcb=n3*10
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato23.configure(text=(f"{dcb}$"))
c1=0
def p3():
    global c1
    if c1<100:
        c1 = c1+1
        lpm3.configure(text=c1)
        ms=c1*3
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato3.configure(text=(f"{ms}$"))
c2=0
def p32():
    global c2
    if c2<100:
        c2 = c2+1
        lpm8.configure(text=c2)
        ss=c2*5
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato32.configure(text=(f"{ss}$"))
c3=0
def p33():
    global c3
    if c3<100:
        c3 = c3+1
        lpm9.configure(text=c3)
        bs=c3*4
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato33.configure(text=(f"{bs}$"))
def m1():
    global a1
    if a1>0:
        a1 = a1-1
        lpm1.configure(text=a1)
        pp=a1*10
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato1.configure(text=(f"{pp}$"))
def m12():
    global a2
    if a2>0:
        a2 = a2-1
        lpm4.configure(text=a2)
        pi=a2*12
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato12.configure(text=(f"{pi}$"))
def m13():
    global a3
    if a3>0:
        a3 = a3-1
        lpm5.configure(text=a3)
        pb=a3*14
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato13.configure(text=(f"{pb}$"))
def m2():
    global n1
    if n1>0:
        n1 = n1-1
        lpm2.configure(text=n1)
        b=n1*5
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato2.configure(text=(f"{b}$"))
def m22():
    global n2
    if n2>0:
        n2 = n2-1
        lpm6.configure(text=n2)
        cb=n2*6
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato22.configure(text=(f"{cb}$"))
def m23():
    global n3
    if n3>0:
        n3 = n3-1
        lpm7.configure(text=n3)
        dcb=n3*10
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato23.configure(text=(f"{dcb}$"))
def m3():
    global c1
    if c1>0:
        c1 = c1-1
        lpm3.configure(text=c1)
        ms=c1*3
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato3.configure(text=(f"{ms}$"))
def m32():
    global c2
    if c2>0:
        c2 = c2-1
        lpm8.configure(text=c2)
        ss=c2*5
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato32.configure(text=(f"{ss}$"))
def m33():
    global c3
    if c3>0:
        c3 = c3-1
        lpm9.configure(text=c3)
        bs=c3*4
        aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
        lato.configure(text=f"Total:                                                                                        {aa}$ ")
        lato33.configure(text=(f"{bs}$"))

class DatabaseManager:
    def __init__(self, db_name, coll_name):
        self.client= pymongo.MongoClient("mongodb://localhost:27017")
        self.db=self.client[db_name]
        self.coll=self.db[coll_name]
    def add(self, data):
        self.coll.insert_one(data)
        
    def readAll(self):
        doc=self.coll.find()
        for data in doc:
            print(data)

    def update_many(self, query, newdata):
        self.coll.update_many(query, {"$set":{newdata}})
        
    def delete_many(self, query):
        self.coll.delete_many(query)
        
    def find_ones(self, query):
        self.coll.find_one(query)
        return collection.find_one(query)
    def close_db(self):
        self.client.close()

if __name__ == "__main__":
    db = DatabaseManager("oopDB", "newcoll")
    db.add({"Name":"Arad", "Age":15})
    # db.readAll({"Name"})
# subject = "a"
# body = "hello "

# sender = "aradtaghizadeh2010@gmail.com"
# recipients = ["aradtaghizadeh2010.python@gmail.com"]
# password = "Arad2010taghizadeh"


# def send_email(subject, body, sender, recipients, password):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = ', '.join(recipients)
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
#        smtp_server.login(sender, password)
#        smtp_server.sendmail(sender, recipients, msg.as_string())
#     print("Message sent!")


# send_email(subject, body, sender, recipients, password)

def ex():
    msg=mess(title='Exit?', message="Do you want to exit this program?", icon="question", option_1="Cancel", option_2="No", option_3="Yes",
         font=("impact", 15), width=450, fade_in_duration=2, option_focus=0, sound=True, button_color="#0a9412", button_hover_color="#045909", text_color="khaki", button_text_color="#f7b314", title_color="#f7b314")
    response=msg.get()
    if response=="Yes":
        root.destroy()
        client.close()
    else:
        pass

def b(a, c):
    a.withdraw()
    c.deiconify()

def light():
    al1.configure(fg_color="#cccfce")
    al2.configure(fg_color="#cccfce")
    al3.configure(fg_color="#cccfce")
    al4.configure(fg_color="#cccfce")
    al5.configure(fg_color="#cccfce")
    al6.configure(fg_color="#cccfce")
    btnbp5.configure(fg_color="#cccfce", hover_color="#9d9ea1")
    btnbp6.configure(fg_color="#e1e3e2", hover_color="#cccccc")
    baccount.configure(fg_color="#e1e3e2", hover_color="#cccccc")
    ba1.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    ba2.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    ba3.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    ba4.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    ba5.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    ba6.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    bn3.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    bn4.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    bn5.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    bn6.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    bn7.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    bn8.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    bc1.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    bc2.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    bc3.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    bc4.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    bc5.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")
    bc6.configure(fg_color="#cdd1cf", hover_color="#b4b5b8")

def update_time_l():
        c = time.strftime('%I:%M:%S %p')
        cl.configure(text=c)
        login.after(1,update_time_l)
def update_time_r():
    c = time.strftime('%I:%M:%S %p')
    cl4.configure(text=c)
    root.after(1,update_time_r)
def update_time_app():
    c = time.strftime('%I:%M:%S %p')
    cla.configure(text=c)
    app.after(1,update_time_app)
def l():
    cl.configure(text=" ")
    nn=ts1.get()
    nl=ts2.get()
    ag=ts3.get()
    gg=genderVar.get()
    gm=ts4.get()
    oo=wv2.get()
    
    if nn=="":
        mess(title='Nick Name Error', message="You've not imported Name!", icon="cancel",
            font=("Comic Sans MS", 12, "bold"), width=450, fade_in_duration=2, option_focus=0, sound=True)
        le4.configure(text=".")
    else:
        le4.configure(text=" ")
    if nl=="":
        mess(title='Last Name Error', message="You've not imported Last Name!", icon="cancel",
            font=("Comic Sans MS", 12, "bold"), width=450, fade_in_duration=2, option_focus=0, sound=True)
        le5.configure(text=".")
    else:
        le5.configure(text=" ")
    try:
        agi=int(ag)
        if agi>120:
            mess(title='Age Error1', message="You've imported incorrect Age!", icon="cancel",
                font=("Comic Sans MS", 12, "bold"), width=450, fade_in_duration=2, option_focus=0, sound=True)
            le1.configure(text=".")
        elif agi<10:
            mess(title='Age Error2', message="You can't login!", icon="cancel",
                font=("Comic Sans MS", 12, "bold"), width=450, fade_in_duration=2, option_focus=0, sound=True)
            root.destroy()
        else:
            le1.configure(text=" ")
    except ValueError:
        mess(title='Age Error3', message="You've not imported Age!", icon="cancel",
            font=("Comic Sans MS", 12, "bold"), width=450, fade_in_duration=2, option_focus=0, sound=True)
        le3.configure(text=".")
    if re.search(pattern, gm):
        le7.configure(text=" ")
    else:
        mess(title='Email Error', message="You've written incorrect Email!", icon="cancel",
            font=("Comic Sans MS", 12, "bold"), width=450, fade_in_duration=2, option_focus=0, sound=True)
        le7.configure(text=".")
    if gg=="":
        mess(title='Gender Error', message="You've not selected any Gender!", icon="cancel",
            font=("Comic Sans MS", 12, "bold"), width=450, fade_in_duration=2, option_focus=0, sound=True)
        le6.configure(text=".")
    else:
        if gg=='Male':
            baccount.configure(image=pha)
        elif gg=='Female':
            baccount.configure(image=pha2)
        elif gg=='Unknown':
            baccount.configure(image=pha3)
        Account.configure(text=nn + " " + nl)
        le6.configure(text=" ")
    if oo=="":
        mess(title='Occupation Error', message="You've not selected any Occupation!", icon="cancel",
            font=("Comic Sans MS", 12, "bold"), width=450, fade_in_duration=2, option_focus=0, sound=True)
        le2.configure(text=".")
    else:
        le2.configure(text=" ")
    try:
        if oo!="" and nn!="" and nl!="" and gg!="" and gm!="":
            if 10<int(ag)<120:
                if re.search(pattern, gm):
                    login.withdraw()
                    root.deiconify()
                    collection.insert_one({"Title":"User Info", "Name": nn, "Lastname": nl, "Age": int(ag), "Gender": gg, "Email": gm, "Occupation": oo})
    
    except:
        pass
def sa():
    name=sc1.get()
    lname=sc2.get()
    age=sc3.get()
    gmail=sc4.get()
    gg=gv.get()
    job=w2.get()
    theme2=appear.get()
    color=c_changer.get()
    dic=collection.find_one({"Title":"User Info"})
    account_name=dic["Name"]
    account_last_name=dic["Lastname"]
    account_age=dic["Age"]
    account_occupation=dic["Occupation"]
    account_gender=dic["Gender"]
    account_email=dic["Email"]
    theme=collection.find_one({"Title":"Theme"})
    appearance=theme["Appearance_Mode"]
    colour=theme["Colour"]

    try:
        if name!="" and name!=account_name:
            if lname!="" and lname!=account_last_name: 
                n=name
                l=lname
                al1.configure(text=f"Your nick name is {n}.")
                al6.configure(text=f"Your full name is {n} {l}.")
                Account.configure(text=n+ " " + l )
                collection.update_one({"Name": account_name}, {"$set": {"Name":n}})
                collection.update_one({"Lastname": account_last_name}, {"$set": {"Lastname":l}}) 
                ec1.delete(0, END)
                ec2.delete(0, END)
            else:
                n=name
                collection.update_one({"Name": account_name}, {"$set": {"Name":n}}) 
                al1.configure(text=f"Your nick name is {n}.")
                al6.configure(text=f"Your full name is {n} {account_last_name}.")
                Account.configure(text=n + " " + account_last_name)
                ec1.delete(0, END)
        elif lname!="" and lname!=account_last_name:
            l=lname
            al6.configure(text=f"Your full name is {account_name} {l}.")
            Account.configure(text=account_name+ " " + l )
            collection.update_one({"Lastname": account_last_name}, {"$set": {"Lastname":l}}) 
            ec2.delete(0, END)
        if age!="" and age!=account_age:
            try:
                ag=int(age)
                if ag>120 or ag<10:
                    mess(title='Age Error 1', message="You've written incorrect age!", icon="cancel",
                    font=("Comic Sans MS", 12), width=280, height=150, fade_in_duration=2, option_focus=0, sound=True)
                    leg2.configure(text=".")
                else:
                    al2.configure(text=f"You are {ag} years old.")
                    leg2.configure(text=" ")
                    collection.update_one({"Age": account_age}, {"$set": {"Age":ag}}) 
                    ec3.delete(0, END)
            except:
                mess(title='Age Error 2', message="You've written incorrect age!", icon="cancel",
                    font=("Comic Sans MS", 12), width=280, fade_in_duration=2, height=150, option_focus=0, sound=True)
                leg2.configure(text=".")
        elif age=="" or age==account_name:
            leg2.configure(text=" ")
        if gg!="" and gg!=account_gender:
            if gg=='Male':
                baccount.configure( image=pha)
                maleRadioButton2.deselect()
            elif gg=='Female':
                baccount.configure(image=pha2)
                femaleRadioButton2.deselect()
            elif gg=='Unknown':
                baccount.configure(image=pha3)
                noneRadioButton2.deselect()
            collection.update_one({"Gender": account_gender}, {"$set": {"Gender":gg}})
            al3.configure(text=f'Your gender is {gg}.' )
            
        if job!="" and job!=account_occupation:
            oo=job
            al5.configure(text=f"Your occupation is {oo}.")   
            collection.update_one({"Occupation": account_occupation}, {"$set": {"Occupation":oo}}) 
            w2.set("")    
        if gmail!="" and gmail!=account_email:
            if re.search(pattern, gmail):
                g=gmail
                al4.configure(text=f"Your email is {g}.")
                leg.configure(text=" ")
                collection.update_one({"Email": account_email}, {"$set": {"Email":g}}) 
                ec4.delete(0,END)
            else:
                mess(title='Email Error 2 ', message="You've written incorrect email!", icon="cancel",
                    font=("Comic Sans MS", 12), width=280,height=150, fade_in_duration=2, option_focus=0, sound=True)
                leg.configure(text=".")
        elif gmail=="" or gmail==account_email:
            leg.configure(text=" ")
        if theme2!="" and theme2!=appearance:
            collection.update_one({"Title":"Theme"},{"$set":{"Appearance_Mode":theme2}})
            appear.set("")
            # set_appearance_mode(theme2)
            # if theme2=="Light":
            #     light()
    
        if color!="" and color!=colour:
            collection.update_one({"Title":"Theme"},{"$set":{"Colour":color}})
            c_changer.set("") 
    except:
        pass
    
    try:
        if name+lname+gg+job+gmail+age+color+theme2!="" and name!=account_name and lname!=account_last_name and gg!=account_gender and gmail!=account_email and age!=account_age and color!=colour and theme2!=appearance:
            if age=="" and gmail=="":
                b(p6, p5)
                mess(title="Save", message="Information has been saved successfully!", icon="check",
                            font=("Comic Sans MS", 12), fade_in_duration=5, option_focus=0, sound=True)
            elif age!="" and gmail=="":
                if 10<int(age)<120:
                    b(p6, p5)
                    mess(title="Save", message="Information has been saved successfully!", icon="check",
                            font=("Comic Sans MS", 12), fade_in_duration=5, option_focus=0, sound=True)
            elif gmail!="" and age=="":
                if re.search(pattern, gmail):
                    b(p6, p5)
                    mess(title="Save", message="Information has been saved successfully!", icon="check",
                            font=("Comic Sans MS", 12), fade_in_duration=5, option_focus=0, sound=True)
            elif gmail!="" and age!="":
                if 10<int(age)<120:
                    if re.search(pattern, gmail):
                        b(p6, p5)
                        mess(title="Save", message="Information has been saved successfully!", icon="check",
                            font=("Comic Sans MS", 12), fade_in_duration=5, option_focus=0, sound=True)
    except:
        pass  
    
def acc():
    b(root, p5)
    dic=collection.find_one({"Title":"User Info"})
    account_name=dic["Name"]
    account_last_name=dic["Lastname"]
    account_age=dic["Age"]
    account_occupation=dic["Occupation"]
    account_gender=dic["Gender"]
    account_email=dic["Email"]
    al1.configure(text=f"Your nick name is {account_name}.")
    al6.configure(text=f"Your full name is {account_name} {account_last_name}.")
    al2.configure(text=f"You are {account_age} years old.")
    al3.configure(text=f'Your gender is {account_gender}.')
    al4.configure(text=f"Your email is {account_email}.")
    al5.configure(text=f"Your occupation is {account_occupation}.")
def card():
    card_detail.deiconify()
    receipt.withdraw()
    card_info=collection.find_one({"Title":"Card_info"})
    card_pin=card_info["Card PIN"]
    card_2nd=card_info["Card 2nd PIN"]
    card_cvv2=card_info["CVV2"]
    card_year=card_info["Expiration year"]
    card_month=card_info["Expiration month"]
    cl1.configure(text=f"PIN:                {card_pin}")
    cl2.configure(text=f"Second PIN:          {card_2nd}")
    cv.configure(text=f'CVV2:                     {card_cvv2}')
    cy.configure(text=f"year:       {card_year}")
    cm.configure(text=f"             month:      {card_month}")
def c(a):
    text_input.set(a[0])
    text_input8.set(str(card_2nd))
    text_input2.set(str(card_cvv2))
    text_input4.set(str(card_year))
    text_input5.set(str(card_month))
def again():
    global ca
    ca=randint(1000, 9999)
    LT7=CTkLabel(app, text=ca, font=("Comic Sans MS", 20), bg_color="white", corner_radius=100, width=100, height=30).place(x=130, y=402)
    text_input7.set("")
    return ca
aa=0
def submit():
    global aa
    aa=a1*10+a2*12+a3*14+n1*5+n2*6+n3*10+c1*3+c2*5+c3*4
    latol.configure(text=f"Total:                                                                                        {aa}$ ")
    if aa==0:
        mess(title="Total Error", message="You've not select any items!\n Please select something.", icon="cancel",
                font=("impact", 15), width=450, fade_in_duration=5, option_focus=0, sound=True, button_color="#0a9412", button_hover_color="#045909", text_color="khaki", button_text_color="#f7b314", title_color="#f7b314")
    else:
        b(root, app) 
def pay():
    
    card1=text_input.get()
    card2=text_input8.get()
    cvv2=text_input2.get()
    security=text_input7.get()
    year=text_input4.get()
    month=text_input5.get()
    if a1!=0:
        ppl.configure(text=f"pepperoni pizza")
        ppp.configure(text=f"{a1}$")
        tppp.configure(text=f"{a1*10}$")
        ppl.grid(row=0, column=0)
        ppp.grid(row=0, column=1)
        tppp.grid(row=0, column=2)
    if a2!=0:
        bpl.configure(text=f"beef pizza")
        pbp.configure(text=f"{a2}$")
        tpbp.configure(text=f"{a2*12}$")
        bpl.grid(row=1, column=0)
        pbp.grid(row=1, column=1)
        tpbp.grid(row=1, column=2)
    if a3!=0:
        ipl.configure(text=f"italian pizza")
        pip.configure(text=f"{a3}$")
        tpip.configure(text=f"{a3*14}$")
        ipl.grid(row=2, column=0)
        pip.grid(row=2, column=1)
        tpip.grid(row=2, column=2)
    if n1!=0:
        bl.configure(text=f"burger")
        pb.configure(text=f"{n1}$")
        tpb.configure(text=f"{n1*5}$")
        bl.grid(row=3, column=0)
        pb.grid(row=3, column=1)
        tpb.grid(row=3, column=2)
    if n2!=0:
        cbl.configure(text=f"cheese burger")
        pcb.configure(text=f"{n2}$")
        tpcb.configure(text=f"{n2*6}$")
        cbl.grid(row=4, column=0)
        pcb.grid(row=4, column=1)
        tpcb.grid(row=4, column=2)
    if n3!=0:
        dcbl.configure(text=f"double cheese burger")
        pdcb.configure(text=f"{n3}$")
        tpdcb.configure(text=f"{n3*10}$")
        dcbl.grid(row=5, column=0) 
        pdcb.grid(row=5, column=1)
        tpdcb.grid(row=5, column=2)
    if c1!=0:
        msl.configure(text=f"milk shake")
        pms.configure(text=f"{c1}$")
        tpms.configure(text=f"{c1*3}$")
        msl.grid(row=7, column=0) 
        pms.grid(row=7, column=1) 
        tpms.grid(row=7, column=2)
    if c2!=0:
        ssl.configure(text=f"strawbwrry shake")
        pss.configure(text=f"{c2}$")
        tpss.configure(text=f"{c2*5}$")
        ssl.grid(row=6, column=0)
        pss.grid(row=6, column=1)
        tpss.grid(row=6, column=2)
    if c3!=0:
        icl.configure(text=f"ice cream")
        pic.configure(text=f"{c3}$")
        tpic.configure(text=f"{c3*4}$")
        icl.grid(row=8, column=0)
        pic.grid(row=8, column=1)
        tpic.grid(row=8, column=2)
    tl.configure(text="Total fee")
    ttl.configure(text=f"{aa}")
    tl.grid(row=10, column=0)
    ttl.grid(row=10, column=2)
    try:
        if int(card1)>9999999999999999 or int(card1)<=999999999999999:
            mess(title='Card PIN Error 1', message="You've written incorrect PIN!", icon="cancel",
                font=("Comic Sans MS", 12), width=450, fade_in_duration=2, option_focus=0, sound=True)
            ale1.configure(text=".")
        else:
            ale1.configure(text=" ")
    except:
        mess(title='Card PIN Error 2', message="You've written incorrect PIN or haven't written that!", icon="cancel",
            font=("Comic Sans MS", 12), width=450, fade_in_duration=2, option_focus=0, sound=True)
        ale1.configure(text=".")
    try:
        if int(card2)>99999999 or int(card2)<=9999999:
            mess(title='Card 2nd PIN Error 1', message="You've written incorrect PIN!", icon="cancel",
                font=("Comic Sans MS", 12), width=450, fade_in_duration=2, option_focus=0, sound=True)
            ale2.configure(text=".")
        else:
            ale2.configure(text=" ")
    except:
        mess(title='Card 2nd PIN Error 2', message="You've written incorrect PIN or haven't written that!", icon="cancel",
            font=("Comic Sans MS", 12), width=450, fade_in_duration=2, option_focus=0, sound=True)
        ale2.configure(text=".")
    try:
        if int(cvv2)>9999  or int(cvv2)<=99:
            mess(title='CVV2 Error 1', message="You've written incorrect CVV2!", icon="cancel",
                font=("Comic Sans MS", 12), width=450, fade_in_duration=2, option_focus=0, sound=True)
            ale3.configure(text=".")
        else:
            ale3.configure(text=" ")
    except:
        mess(title='CVV2 Error 2', message="You've written incorrect CVV2 or haven't written that!", icon="cancel",
            font=("Comic Sans MS", 12), width=450, fade_in_duration=2, option_focus=0, sound=True)
        ale3.configure(text=".")
    try:
        if  int(year)<ay or int(year)==ay and int(month)<am:
            mess(title='Expiration Error 1', message="Your card is expired!", icon="cancel",
                font=("Comic Sans MS", 12), width=450, fade_in_duration=2, option_focus=0, sound=True)
            ale4.configure(text=".")
        else:
            ale4.configure(text=" ")
    except:
        mess(title='Expiration Error 2', message="You've written incorrect year or haven't written that!", icon="cancel",
            font=("Comic Sans MS", 12), width=450, fade_in_duration=2, option_focus=0, sound=True)
        ale4.configure(text=".")
    try:
        if  int(month)>12 or int(month)<1:
            mess(title='Expiration Error 3', message="You've written incorrect month!", icon="cancel",
                font=("Comic Sans MS", 12), width=450, fade_in_duration=2, option_focus=0, sound=True)
            ale5.configure(text=".")
        else:
            ale5.configure(text=" ")
    except:
        mess(title='Expiration Error 4', message="You've written incorrect month or haven't written that!", icon="cancel",
            font=("Comic Sans MS", 12), width=450, fade_in_duration=2, option_focus=0, sound=True)
        ale5.configure(text=".")
    try:
        if int(security)!=ca:
            mess(title='Security Code Error 1', message="You've written incorrect security code!", icon="cancel",
                font=("Comic Sans MS", 12), width=450, fade_in_duration=2, option_focus=0, sound=True)
            ale6.configure(text=".")
            
        else:
            ale6.configure(text=" ")
    except:
        mess(title='Security Code Error 2', message="You've written incorrect Security Code or haven't written that!", icon="cancel",
            font=("Comic Sans MS", 12), width=450, fade_in_duration=2, option_focus=0, sound=True)
        ale6.configure(text=".")
        
    try:
        if a[0]==int(card1) :
            if int(security)==ca:
                if card_2nd!=int(card2) or card_cvv2!=int(cvv2) or card_year!=int(year) or card_month!=int(month):
                    if 9999999999999999>int(card1)>=999999999999999:
                        if 99999999>int(card2)>=9999999:
                            if 9999>int(cvv2)>=99:
                                if int(year)==ay and int(month)>=am or int(year)>ay and month:
                                    if 13>int(month)>=1:
                                        info=mess(title='Card Info', message="Are you sure to update your card info?", icon="question",
                                            font=("Comic Sans MS", 17), width=450, fade_in_duration=2, option_focus=1, sound=True, option_1="Yes", option_2="No", option_3="Cancle")
                                        i=info.get()
                                        if i=="Yes":
                                            collection.replace_one({"Title":"Card_info"}, {"Title": "Card_info","Card PIN": int(card1), "Card 2nd PIN": int(card2), "CVV2": int(cvv2), "Expiration year": int(year),"Expiration month": int(month)})
                                            receipt.deiconify()
                                            app.withdraw()  
                else:
                    receipt.deiconify()
                    app.withdraw()   
        else:
            if 9999999999999999>int(card1)>=999999999999999:
                if 99999999>int(card2)>=9999999:
                    if 9999>int(cvv2)>=99:
                        if int(year)==ay and int(month)>=am or int(year)>ay :
                            if 13>int(month)>=1:
                                if int(security)==ca:
                                    collection.insert_one({"Title": "Card_info","Card PIN": int(card1), "Card 2nd PIN": int(card2), "CVV2": int(cvv2), "Expiration year": int(year),"Expiration month": int(month)})
                                    receipt.deiconify()
                                    app.withdraw() 
    except:
        try:
            if 9999999999999999>int(card1)>=999999999999999:
                if 99999999>int(card2)>=9999999:
                    if 9999>int(cvv2)>=99:
                        if (int(year)+int(month))>(ay+am):
                            if 12>int(month)>1:
                                if int(security)==ca:
                                    collection.insert_one({"Title": "Card_info","Card PIN": int(card1), "Card 2nd PIN": int(card2), "CVV2": int(cvv2), "Expiration year": int(year),"Expiration month": int(month)})
                                    receipt.deiconify()
                                    app.withdraw()
        except:
            pass
    again()

#==================Create_Pages====================
root=CTk()
login=CTkToplevel(root)
p5=CTkToplevel(root)
p6=CTkToplevel(root)
app = CTkToplevel(root)
receipt=CTkToplevel(root)
card_detail=CTkToplevel(root)
#==================Show/Hide========================
login.withdraw()
p5.withdraw()
p6.withdraw()
app.withdraw()
receipt.withdraw()
card_detail.withdraw()
#==================Title============================
root.title('MENU')
login.title("Login Page")
p5.title("Account Info")
p6.title("Change Account")
app.title('Payment Page')
receipt.title('Recepit')
card_detail.title("Card Info")
#==================Geometry=========================
root.geometry('1520x830+0+0')
login.geometry("1520x830+0+0")
p5.geometry("560x435")
p6.geometry("560x700")
app.geometry("1520x830+0+0")
card_detail.geometry("350x500")
#==================ANA==============================
r=receipt
#==================Pattern==========================
pattern="^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
#===========================================client======================================================
client=pymongo.MongoClient("mongodb://localhost:27017")
db=client["app"]
collection=db["user_data"]
#==========================================Root==========================================================
l1=CTkLabel(root, text="FAST FOOD",text_color="#f7b314", font=("impact", 14))
l2=CTkLabel(root, text="MENU", text_color="#f7b314", font=("impact", 35))
cl4=CTkLabel(root, font=("impact", 17), text_color="#f7b314")
cl4.place(x=1400, y=20)
update_time_r()
#==========================================Account=======================================================
pha =  CTkImage(Image.open("Menu\men_account.png"), size=(50, 50))
pha2 =  CTkImage(Image.open("Menu\women_account.png"), size=(50, 50))
pha3 =  CTkImage(Image.open("Menu\question.png"), size=(50, 50))
baccount= CTkButton(master=root,image=pha,text="", corner_radius=25, width=75,height=75, fg_color="#2f2f30", font=("Comic Sans MS", 20), hover_color="#202021", command=acc)
baccount.place(x=800, y=50)
Account=CTkLabel(root, text="", font=("impact", 20))
Account.place(x=800, y=130)
try:
    dic=collection.find_one({"Title":"User Info"})
    account_name=dic["Name"]
    account_last_name=dic["Lastname"]
    account_age=dic["Age"]
    account_occupation=dic["Occupation"]
    account_gender=dic["Gender"]
    account_email=dic["Email"]
    Account.configure(text=account_name + " " + account_last_name)
    
    if account_gender=="Male":
        baccount.configure(image=pha)
    elif account_gender=="Female":
        baccount.configure(image=pha2)
    elif account_gender=="Unknown":
        baccount.configure(image=pha3)
    
except:
    root.withdraw()
    login.deiconify()


    

#==========================================Pizza=========================================================
lf1=CTkFrame(root)
ph1=CTkImage(Image.open('Menu\pizza.png'), size=(150, 150))
lph1=CTkLabel(lf1, image=ph1, text="")
lt1=CTkLabel(root, text="Pizza", font=("impact", 24), text_color="khaki" )
lf4=CTkFrame(root)
la1=CTkLabel(lf4, text="pepperoni pizza                          10$         ", text_color="#f7b314", font=("impact", 16))
la2=CTkLabel(lf4, text="italian pizza                                  12$          ", text_color="#f7b314", font=("impact", 16))
la3=CTkLabel(lf4, text="beef pizza                                      14$          ", text_color="#f7b314", font=("impact", 16))
ba1=CTkButton(lf4, text="+",text_color="green", font=("impact", 9, "bold"),hover_color="#043304",fg_color="#302d2d", width=3, command=p1)
lpm1=CTkLabel(lf4, text=a1,text_color="black", font=("impact", 14), width=3)
ba2=CTkButton(lf4, text="-", text_color="red", font=("impact", 9, "bold"),hover_color="#a1050d", fg_color="#302d2d", width=3, command= m1)
ba3=CTkButton(lf4, text="+", fg_color="#302d2d", text_color="green", font=("impact", 9, "bold"),hover_color="#043304", width=3, command=p12)
lpm4=CTkLabel(lf4, text=a2, text_color="black", font=("impact", 14), width=3)
ba4=CTkButton(lf4, text="-", fg_color="#302d2d", text_color="red", font=("impact", 9, "bold"),hover_color="#a1050d", width=3, command= m12)
ba5=CTkButton(lf4, text="+", fg_color="#302d2d", text_color="green", font=("impact", 9, "bold"),hover_color="#043304", width=3, command=p13)
lpm5=CTkLabel(lf4, text=a3, text_color="black", font=("impact", 14), width=3)
ba6=CTkButton(lf4, text="-", fg_color="#302d2d", text_color="red", font=("impact", 9, "bold"),hover_color="#a1050d", width=3, command= m13)
#============================================Burger=======================================================
lf2=CTkFrame(root)
ph2=CTkImage(Image.open('Menu/burger1.png'), size=(150, 150))
lph2=CTkLabel(lf2, image=ph2, text="")
lt2=CTkLabel(root, text="Burger", font=("impact", 24), text_color="khaki" )
lf5=CTkFrame(root)
ln1=CTkLabel(lf5, text="burger                                              5$          ", text_color="#f7b314", font=("impact", 16))
ln2=CTkLabel(lf5, text="cheese burger                              6$         ", text_color="#f7b314", font=("impact", 16))
ln3=CTkLabel(lf5, text="double cheese  burger           10$         ", text_color="#f7b314", font=("impact", 16))
bn3=CTkButton(lf5, text="+", fg_color="#302d2d", text_color="green", font=("impact", 9, "bold"), hover_color="#043304", width=3, command=p2)
lpm2=CTkLabel(lf5, text=n1, text_color="black", font=("impact", 14), width=3)
bn4=CTkButton(lf5, text="-", fg_color="#302d2d", text_color="red", font=("impact", 9, "bold"),hover_color="#a1050d", width=3, command= m2)
bn5=CTkButton(lf5, text="+", fg_color="#302d2d", text_color="green", font=("impact", 9, "bold"), hover_color="#043304", width=3, command=p22)
lpm6=CTkLabel(lf5, text=n1, text_color="black", font=("impact", 14), width=3)
bn6=CTkButton(lf5, text="-", fg_color="#302d2d", text_color="red", font=("impact", 9, "bold"),hover_color="#a1050d", width=3, command= m22)
bn7=CTkButton(lf5, text="+", fg_color="#302d2d", text_color="green", font=("impact", 9, "bold"),hover_color="#043304", width=3, command=p23)
lpm7=CTkLabel(lf5, text=n1, text_color="black", font=("impact", 14), width=3)
bn8=CTkButton(lf5, text="-", fg_color="#302d2d", text_color="red", font=("impact", 9, "bold"),hover_color="#a1050d", width=3, command= m23)
#============================================drinks=======================================================
lf3=CTkFrame(root)
ph3=CTkImage(Image.open('Menu\ice_cream.png'), size=(150, 150))
lph3=CTkLabel(lf3, image=ph3, text="")
lt3=CTkLabel(root, text="Drink", font=("impact", 24), text_color="khaki" )
lf6=CTkFrame(root)
lc1=CTkLabel(lf6, text="milk shake                                      3$          ", text_color="#f7b314", font=("impact", 16))
lc2=CTkLabel(lf6, text="strawberry shake                        5$         ", text_color="#f7b314", font=("impact", 16))
lc3=CTkLabel(lf6, text="ice cream                                        4$          ", text_color="#f7b314", font=("impact", 16))
bc1=CTkButton(lf6, text="+", fg_color="#302d2d", text_color="green", font=("impact", 9, "bold"),hover_color="#043304", width=3, command=p3)
lpm3=CTkLabel(lf6, text=c1, text_color="black", font=("impact", 14), width=3)
bc2=CTkButton(lf6, text="-", fg_color="#302d2d", text_color="red", font=("impact", 9, "bold"),hover_color="#a1050d", width=3, command= m3)
bc3=CTkButton(lf6, text="+", fg_color="#302d2d", text_color="green", font=("impact", 9, "bold"),hover_color="#043304", width=3, command=p32)
lpm8=CTkLabel(lf6, text=c1, text_color="black", font=("impact", 14), width=3)
bc4=CTkButton(lf6, text="-", fg_color="#302d2d", text_color="red", font=("impact", 9, "bold"),hover_color="#a1050d", width=3, command= m32)
bc5=CTkButton(lf6, text="+", fg_color="#302d2d", text_color="green", font=("impact", 9, "bold"),hover_color="#043304", width=3, command=p33)
lpm9=CTkLabel(lf6, text=c1, text_color="black", font=("impact", 14), width=3)
bc6=CTkButton(lf6, text="-", fg_color="#302d2d", text_color="red", font=("impact", 9, "bold"),hover="#a1050d", width=3, command= m33)
#============================================total=======================================================
bato=CTkButton(root, text="submit",  font=("impact", 18), fg_color="#0a9412", width=140, height=37, corner_radius=10, text_color="#f7b314", text_color_disabled="#cf9100", hover_color="#045909",command=submit)
exb=CTkButton(root, text="Exit", fg_color="#8f010b", hover_color="#540107",  font=("impact", 18), width=140, height=37,corner_radius=10, text_color="#f7b314", text_color_disabled="#cf9100", command=ex)
lft=CTkFrame(root, height=30, width=390)
lft.place(x=223, y=670)
lato=CTkLabel(lft, text=f"Total:                                                                                        {0}$ ", font=("impact", 18), text_color="#048a0b")
lato.place(x=10, y=1)
lato1=CTkLabel(root, text="0$", font=("impact", 18), text_color="#03960c")
lato12=CTkLabel(root, text="0$", font=("impact", 18), text_color="#03960c")
lato13=CTkLabel(root, text="0$", font=("impact", 18), text_color="#03960c")
lato2=CTkLabel(root, text="0$", font=("impact", 18), text_color="#03960c")
lato22=CTkLabel(root, text="0$", font=("impact", 18), text_color="#03960c")
lato23=CTkLabel(root, text="0$", font=("impact", 18), text_color="#03960c")
lato3=CTkLabel(root, text="0$", font=("impact", 18), text_color="#03960c")
lato32=CTkLabel(root, text="0$", font=("impact", 18), text_color="#03960c")
lato33=CTkLabel(root, text="0$", font=("impact", 18), text_color="#03960c")
# if aa>100:
#     n=0
#     for i in range(5):
#         n=n+1
#     print(n)
#     lft.configure(width=n)
    
#==========title============
l1.place(x=5, y=5)
l2.place(x=5, y=28)
#==========pizza============
lf1.place(x=5, y=80)
lph1.grid(row=0, column=0, padx=20, pady=20)
lf4.place(x=223, y=150)
lt1.place(x=220, y=100)
la1.grid(row=0, column=0, padx=3, pady=3)
ba1.grid(row=0, column=1, padx=3, pady=3)
lpm1.grid(row=0, column=2)
ba2.grid(row=0, column=3, padx=3, pady=3)
la2.grid(row=1, column=0, padx=3, pady=3)
ba3.grid(row=1, column=1, padx=3, pady=3)
lpm4.grid(row=1, column=2)
ba4.grid(row=1, column=3, padx=3, pady=3)
la3.grid(row=2, column=0, padx=3, pady=3)
ba5.grid(row=2, column=1, padx=3, pady=3)
lpm5.grid(row=2, column=2)
ba6.grid(row=2, column=3, padx=3, pady=3)
#==========burger============
lf2.place(x=5, y=280)
lph2.grid(row=0, column=0, padx=20, pady=20)
lf5.place(x=223, y=350)
lt2.place(x=220, y=300)
ln1.grid(row=0, column=0, padx=3, pady=3)
bn3.grid(row=0, column=1, padx=3, pady=3)
lpm2.grid(row=0, column=2)
bn4.grid(row=0, column=3, padx=3, pady=3)
ln2.grid(row=1, column=0, padx=3, pady=3)
bn5.grid(row=1, column=1, padx=3, pady=3)
lpm6.grid(row=1, column=2)
bn6.grid(row=1, column=3, padx=3, pady=3)
ln3.grid(row=2, column=0, padx=3, pady=3)
bn7.grid(row=2, column=1, padx=3, pady=3)
lpm7.grid(row=2, column=2)
bn8.grid(row=2, column=3, padx=3, pady=3)
#==========drinks============
lf3.place(x=5, y=480)
lph3.grid(row=0, column=0, padx=20, pady=20)
lf6.place(x=223, y=550)
lt3.place(x=220, y=500)
lc1.grid(row=0, column=0, padx=3, pady=3)
bc1.grid(row=0, column=1, padx=3, pady=3)
lpm3.grid(row=0, column=2)
bc2.grid(row=0, column=3, padx=3, pady=3)
lc2.grid(row=1, column=0, padx=3, pady=3)
bc3.grid(row=1, column=1, padx=3, pady=3)
lpm8.grid(row=1, column=2)
bc4.grid(row=1, column=3, padx=3, pady=3)
lc3.grid(row=2, column=0, padx=3, pady=3)
bc5.grid(row=2, column=1, padx=3, pady=3)
lpm9.grid(row=2, column=2)
bc6.grid(row=2, column=3, padx=3, pady=3)
#==========total============
bato.place(x=230, y=720)
exb.place(x=380, y=720)
lato1.place(x=550, y=150)
lato12.place(x=550, y=185)
lato13.place(x=550, y=220)
lato2.place(x=550, y=350)
lato22.place(x=550, y=385)
lato23.place(x=550, y=420)
lato3.place(x=550, y=550)
lato32.place(x=550, y=585)
lato33.place(x=550, y=620)

#===============================================Login=========================================================
ts1=StringVar()
ts2=StringVar()
ts3=StringVar()
ts4=StringVar()
wv2=StringVar()

wv=['Other','Student', 'Teacher', 'Doctor', 'Dentist', 'Accountant', 'Architect', 'Electrician', 'Actuaries', 'Athor', 'Baker', 'Chef', 'Farmer', 'Firefighter', 'Lawyer', 'Nurse']
nameLabel = CTkLabel(login,text="Nick Name", font=("Comic Sans MS", 20))
nameLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
nameEntry = CTkEntry(login, textvariable=ts1, font=("Comic Sans MS", 18), height=33)
nameEntry.grid(row=0, column=1,columnspan=3, padx=20,pady=20, sticky="ew")

name2Label = CTkLabel(login,text="Last Name", font=("Comic Sans MS", 20))
name2Label.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
name2Entry = CTkEntry(login,textvariable=ts2, font=("Comic Sans MS", 18), height=33)
name2Entry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

ageLabel = CTkLabel(login, text="Age", font=("Comic Sans MS", 20))
ageLabel.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
ageEntry = CTkEntry(login, textvariable=ts3, font=("Comic Sans MS", 18), height=33)
ageEntry.grid(row=2, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

gmailLabel = CTkLabel(login, text="Email", font=("Comic Sans MS", 20))
gmailLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
gmailEntry = CTkEntry(login, textvariable=ts4, font=("Comic Sans MS", 18), height=33)
gmailEntry.grid(row=3, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

genderLabel = CTkLabel(login, text="Gender", font=("Comic Sans MS", 20))
genderLabel.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

genderVar = StringVar()

maleRadioButton = CTkRadioButton(login, text="Male", variable=genderVar, value="Male", font=("Comic Sans MS", 15))
maleRadioButton.grid(row=4, column=1, padx=20,pady=20, sticky="ew")

femaleRadioButton = CTkRadioButton(login, text="Female", variable=genderVar,value="Female", font=("Comic Sans MS", 15))
femaleRadioButton.grid(row=4, column=2, padx=20, pady=20, sticky="ew")
        
noneRadioButton = CTkRadioButton(login, text="Prefer not to say", variable=genderVar,value="Unknown", font=("Comic Sans MS", 15))
noneRadioButton.grid(row=4, column=3,padx=20, pady=20, sticky="ew")

occupationLabel = CTkLabel(login,   text="Occupation", font=("Comic Sans MS", 20))
occupationLabel.grid(row=5, column=0, padx=20, pady=20, sticky="ew")
occupationOptionMenu = CTkOptionMenu(login, variable=wv2, font=("Comic Sans MS", 18), height=33)
occupationOptionMenu.grid(row=5, column=1, padx=20, pady=20, columnspan=2, sticky="ew")
CTkScrollableDropdown(occupationOptionMenu, values=wv, font=("Comic Sans MS", 18))
generateResultsButton = CTkButton(login, font=("Comic Sans MS", 20), corner_radius=14, width=180, height=35, text='Login', command=l)
generateResultsButton.grid(row=6, column=1, columnspan=2, padx=20, pady=20, sticky="ew")  
cl = CTkLabel(login, font=("Comic Sans MS", 15))
cl.place(x=1400,y=20)
le4=CTkLabel(login, text="", text_color="#8a0303", font=("Comic Sans MS", 35, "bold"))
le5=CTkLabel(login, text="", text_color="#8a0303", font=("Comic Sans MS", 35, "bold"))
le1=CTkLabel(login, text="", text_color="#8a0303", font=("Comic Sans MS", 35, "bold"))
le3=CTkLabel(login, text="", text_color="#8a0303", font=("Comic Sans MS", 35, "bold"))
le7=CTkLabel(login, text="", text_color="#8a0303", font=("Comic Sans MS", 35, "bold"))
le6=CTkLabel(login, text="", text_color="#8a0303", font=("Comic Sans MS", 35, "bold"))
le2=CTkLabel(login, text="", text_color="#8a0303", font=("Comic Sans MS", 35, "bold"))
le4.place(x=122, y=-10)
le5.place(x=115, y=57)
le1.place(x=88, y=137)
le7.place(x=100, y=200)
le6.place(x=102, y=273)
le2.place(x=120, y=341)
le3.place(x=88, y=137)
update_time_l()

#===============================================P5=========================================================
cl3=CTkLabel(p5, font=("Comic Sans MS", 13))
cl3.place(x=450, y=20)
def update_time():
    c = time.strftime('%I:%M:%S %p')
    cl3.configure(text=c)
    p5.after(1,update_time)    
al1=CTkLabel(p5, text=f"", font=("Comic Sans MS", 20), fg_color="#2f2f30", corner_radius=8, width=400)
al1.place(x=30, y=70)
al6=CTkLabel(p5, text=f"", font=("Comic Sans MS", 20), fg_color="#2f2f30", corner_radius=8, width=400)
al6.place(x=30, y=120)
al2=CTkLabel(p5, text=f"" ,font=("Comic Sans MS", 20),fg_color="#2f2f30", corner_radius=8, width=400)
al2.place(x=30, y=170)
al3=CTkLabel(p5, text=f'' ,font=("Comic Sans MS", 20),fg_color="#2f2f30", corner_radius=8, width=400)
al3.place(x=30, y=220)
al4=CTkLabel(p5, text=f"", font=("Comic Sans MS", 20),fg_color="#2f2f30", corner_radius=8, width=400)
al4.place(x=30, y=270)
al5=CTkLabel(p5, text=f"", font=("Comic Sans MS", 20),fg_color="#2f2f30", corner_radius=8, width=400)
al5.place(x=30, y=320)
change1=CTkButton(p5, text="Account Setting", command=lambda:b(p5, p6), height=40, corner_radius=8)
change1.place(x=100, y=20)
# btnb = CTkButton(p5, width=60, text='Back', fg_color="#09a0ad", hover_color="#043d42", command=lambda:b(p5, root)).place(x=188, y=30)
pha4=CTkImage(Image.open("Menu/Back.png"), size=(30,30))
btnbp5 = CTkButton(p5,width=10, text='', corner_radius=8, height=40, image=pha4, fg_color="#242323", hover_color="#202021", command=lambda:b(p5, root))
btnbp5.place(x=30, y=20)

update_time()

#===============================================P6=========================================================
leg=CTkLabel(p5, text="", text_color="#8a0303", font=("Comic Sans MS", 25, "bold"))
leg2=CTkLabel(p5, text="", text_color="#8a0303", font=("Comic Sans MS", 25, "bold"))
leg2.place(x=657, y=150)
leg.place(x=667, y=190)    
w=['Other','Student', 'Teacher', 'Doctor', 'Dentist', 'Accountant', 'Architect', 'Electrician', 'Actuaries', 'Athor', 'Baker', 'Chef', 'Farmer', 'Firefighter', 'Lawyer', 'Nurse']
change_appearance=['Dark', 'Light', 'System']
change_colour=['green', 'blue']
w2=StringVar()
appear=StringVar()
c_changer=StringVar()
sc1=StringVar()
sc2=StringVar()
sc3=StringVar()
sc4=StringVar()
gv =StringVar()
lec1=CTkLabel(master=p6, text="Change Nick Name", font=("Comic Sans MS", 14), corner_radius=8)
lec1.place(x=20, y=70)
ec1=CTkEntry(master=p6, textvariable=sc1, font=("Comic Sans MS", 12), width=250 )
ec1.place(x=200, y=70)
lec2=CTkLabel(master=p6, text="Change Last Name ", font=("Comic Sans MS", 14), corner_radius=8)
lec2.place(x=20, y=120)
ec2=CTkEntry(master=p6, textvariable=sc2, font=("Comic Sans MS", 12), width=250 )
ec2.place(x=200, y=120)
lec3=CTkLabel(master=p6, text="Change Age ", font=("Comic Sans MS", 14), corner_radius=8)
lec3.place(x=20, y=170)
ec3=CTkEntry(master=p6, textvariable=sc3, font=("Comic Sans MS", 12), width=250 )
ec3.place(x=200, y=170)
lec4=CTkLabel(master=p6, text="Change Gmail ", font=("Comic Sans MS", 14), corner_radius=8)
lec4.place(x=20, y=220)
ec4=CTkEntry(master=p6, textvariable=sc4, font=("Comic Sans MS", 12), width=250 )
ec4.place(x=200, y=220)
lec5=CTkLabel(master=p6, text="Change Gender ", font=("Comic Sans MS", 14), corner_radius=8)
lec5.place(x=20, y=270)
maleRadioButton2 = CTkRadioButton(p6, text="Male", variable=gv, value="Male", font=("Comic Sans MS", 12))
maleRadioButton2.place(x=200, y=270)
femaleRadioButton2 = CTkRadioButton(p6, text="Female", variable=gv,value="Female", font=("Comic Sans MS", 12))
femaleRadioButton2.place(x=300, y=270)
noneRadioButton2 = CTkRadioButton(p6, text="Prefer not to say", variable=gv,value="Unknown", font=("Comic Sans MS", 12))
noneRadioButton2.place(x=400, y=270)

lec6=CTkLabel(master=p6, text="Change Occupation ", font=("Comic Sans MS", 14), corner_radius=10)
lec6.place(x=20, y=320)
job = CTkOptionMenu(p6,font=("Comic Sans MS", 12), variable=w2, width=160)
job.place(x=200, y=320)
CTkScrollableDropdown(job, values=w,font=("Comic Sans MS", 12))

lec7=CTkLabel(master=p6, text="Change Appearance", font=("Comic Sans MS", 14), corner_radius=10)
lec7.place(x=20, y=370)
changing_appearance = CTkOptionMenu(p6,font=("Comic Sans MS", 12), variable=appear, width=160)
changing_appearance.place(x=200, y=370)
CTkScrollableDropdown(changing_appearance, values=change_appearance,font=("Comic Sans MS", 12))

lec8=CTkLabel(master=p6, text="Change Colour", font=("Comic Sans MS", 14), corner_radius=10)
lec8.place(x=20, y=420)
changing_colour = CTkOptionMenu(p6,font=("Comic Sans MS", 12), variable=c_changer, width=160)
changing_colour.place(x=200, y=420)
CTkScrollableDropdown(changing_colour, values=change_colour,font=("Comic Sans MS", 12))

save=CTkButton(p6, text="Save", width=160,font=("Comic Sans MS", 12), command=sa)
save.place(x=200, y=470)
btnbp6 = CTkButton(p6,width=10, text='', corner_radius=8, height=40, image=pha4, fg_color="#242323", hover_color="#202021", command=lambda:b(p6, p5))
btnbp6.place(x=20, y=20)

#===============================================App=========================================================
a=time.localtime()
am=a.tm_mon
ay=a.tm_year
ca=randint(1000, 9999)
text_input  = StringVar()
text_input2 = StringVar()
text_input4 = StringVar()
text_input5 = StringVar()
text_input7 = StringVar()
text_input8 = StringVar()
cla = CTkLabel(app, font=("Comic Sans MS", 15))
cla.place(x=1400,y=20)
L1=CTkLabel(app, text="Card information", font=("Comic Sans MS", 28, "bold")).place(x=30, y=20)
LT1=CTkLabel(app, text="Card PIN", font=("Comic Sans MS", 20)).place(x=30, y=100)
card1Entry = CTkEntry(app, width=400, height=35, textvariable=text_input, font=("Comic Sans MS", 16))
card1Entry.place(x=173, y=100)
Li1=CTkLabel(app, text="* 16 character", font=("", 11), text_color="#87c78d").place(x=600, y=103)
LT8=CTkLabel(app, text="Card 2nd PIN", font=("Comic Sans MS", 20)).place(x=30, y=150)
txtDisplay8 = CTkEntry(app, font=("Comic Sans MS", 16), textvariable=text_input8, width=400, height=35)
txtDisplay8.place(x=173, y=150)
Li2=CTkLabel(app, text="* 8 character", font=("", 11), text_color="#87c78d").place(x=600, y=153)
LT2=CTkLabel(app, text="CVV2:", font=("Comic Sans MS", 20)).place(x=30, y=200)
txtDisplay2 = CTkEntry(app, font=("Comic Sans MS", 16), textvariable=text_input2, width=200, height=35)
txtDisplay2.place(x=173, y=200)
Li3=CTkLabel(app, text="* 3/4 character", font=("", 11), text_color="#87c78d").place(x=600, y=203)
LT3=CTkLabel(app, text="Expiration date", font=("Comic Sans MS", 20)).place(x=30, y=250)
LT4=CTkLabel(app, text="Year:", font=("Comic Sans MS", 17)).place(x=130, y=300)
LT5=CTkLabel(app, text="Month", font=("Comic Sans MS", 17)).place(x=450, y=300)
txtDisplay4 = CTkEntry(app, font=("Comic Sans MS", 16), textvariable=text_input4, width=100, height=35)
txtDisplay4.place(x=185, y=300)
Li4=CTkLabel(app, text=f"* Example: {ay}", font=("", 11), text_color="#87c78d").place(x=300, y=303)
txtDisplay5 = CTkEntry(app, font=("Comic Sans MS", 16), textvariable=text_input5, width=100, height=35)
txtDisplay5.place(x=520, y=300)
Li5=CTkLabel(app, text=f"* Example: {am}", font=("", 11), text_color="#87c78d").place(x=640, y=303)
LT6=CTkLabel(app, text="Security code:", font=("Comic Sans MS", 20)).place(x=30, y=350)
LT7=CTkLabel(app, text=ca, font=("Comic Sans MS", 20), bg_color="white", corner_radius=100, width=100, height=30).place(x=130, y=402)
txtDisplay7 = CTkEntry(app, font=("Comic Sans MS", 16),textvariable=text_input7, width=100, height=35)
txtDisplay7.place(x=275, y=400)
phr =  CTkImage(Image.open("Menu/retry3.png"), size=(26, 26))
B1 = CTkButton(master=app, image=phr, text="", corner_radius=10, width=30, height=35, command=again).place(x=425, y=400)
latol=CTkLabel(app, text="",font=("Comic Sans MS", 20), text_color="green")
latol.place(x=223, y=670)
btnb = CTkButton(app, font=('calibry', 15, 'bold'), corner_radius=14, width=180, height=35, text='Back', command=lambda:b(app, root)).place(x=188, y=560)
btnpay = CTkButton(app, font=('calibry', 15, 'bold'), corner_radius=14, width=180, height=35, text='Pay', fg_color="#063b01", hover_color="#06300a", command=pay).place(x=380, y=560)
cls=CTkScrollableDropdown(card1Entry,font=("", 20), command=c, width=400)
update_time_app()

try:
    data=[]
    card_info=collection.find({"Title":"Card_info"})
    for i in card_info:
        a=i["Card PIN"]
        a=[f"{a}"]
        card_pin=i["Card PIN"]
        card_pin_l=[f"{card_pin}"]
        card_2nd=i["Card 2nd PIN"]
        card_2nd_l=[f"{card_2nd}"]
        card_cvv2=i["CVV2"]
        card_cvv2_l=[f"{card_cvv2}"]
        card_year=i["Expiration year"]
        card_year_l=[f"{card_year}"]
        card_month=i["Expiration month"]
        card_month_l=[f"{card_month}"]
        data.append(a)
    cls.configure(values=data) 

except:
    ...
ale4=CTkLabel(app, text="", text_color="#8a0303", font=("Comic Sans MS", 25, "bold"))
ale5=CTkLabel(app, text="", text_color="#8a0303", font=("Comic Sans MS", 25, "bold"))
ale1=CTkLabel(app, text="", text_color="#8a0303", font=("Comic Sans MS", 30, "bold"))
ale3=CTkLabel(app, text="", text_color="#8a0303", font=("Comic Sans MS", 30, "bold"))
ale6=CTkLabel(app, text="", text_color="#8a0303", font=("Comic Sans MS", 30, "bold"))
ale2=CTkLabel(app, text="", text_color="#8a0303", font=("Comic Sans MS", 30, "bold"))
ale4.place(x=172, y=280)
ale5.place(x=507, y=280)
ale1.place(x=112, y=65)
ale6.place(x=170, y=325)
ale2.place(x=155, y=116)
ale3.place(x=90, y=175)
#===============================================Receipt=========================================================
r1=CTkFrame(r)
r1.pack(padx=10, pady=10)

ppl=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
ppp=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
tppp=CTkLabel(r1, text="", font=("Comic Sans MS", 15))


bpl=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
pbp=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
tpbp=CTkLabel(r1, text="", font=("Comic Sans MS", 15))

ipl=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
pip=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
tpip=CTkLabel(r1, text="", font=("Comic Sans MS", 15))

bl=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
pb=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
tpb=CTkLabel(r1, text="", font=("Comic Sans MS", 15))

cbl=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
pcb=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
tpcb=CTkLabel(r1, text="", font=("Comic Sans MS", 15))

dcbl=CTkLabel(r1, text="", font=("Comic Sans MS", 15)) 
pdcb=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
tpdcb=CTkLabel(r1, text="", font=("Comic Sans MS", 15))

msl=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
pms=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
tpms=CTkLabel(r1, text="", font=("Comic Sans MS", 15))

ssl=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
pss=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
tpss=CTkLabel(r1, text="", font=("Comic Sans MS", 15))

icl=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
pic=CTkLabel(r1, text="", font=("Comic Sans MS", 15))
tpic=CTkLabel(r1, text="", font=("Comic Sans MS", 15))

tl=CTkLabel(r1, text="", font=("Comic Sans MS", 16, "bold"), text_color="green")
ttl=CTkLabel(r1, text="", font=("Comic Sans MS", 16, "bold"), text_color="green")

blr=CTkLabel(r1, text="____________________________________________", font=("Comic Sans MS", 16, "bold")).grid(row=9, column=0, columnspan=3)
bb=CTkButton(r1, text="Rechoose", command=lambda:b(r, root)).grid(row=11, column=1, padx=5, pady=5)
cb=CTkButton(r1, text="Card Info", command=card).grid(row=11, column=2, padx=5, pady=5)

#===============================================Card_Info=========================================================

cl1=CTkLabel(card_detail)
cl1.place(x=20, y=50)
cl2=CTkLabel(card_detail)
cl2.place(x=20, y=100)
cv=CTkLabel(card_detail)
cv.place(x=20, y=150)
ce=CTkLabel(card_detail, text="Expiration").place(x=20, y=200)
cy=CTkLabel(card_detail)
cy.place(x=40, y=250)
cm=CTkLabel(card_detail)
cm.place(x=140, y=250)
back=CTkButton(card_detail, text="Back", command=lambda:b(card_detail, r)).place(x=80, y=300)

try:
    client=DatabaseManager(db_name="app", coll_name="user_data")
    theme=client.find_ones(query={'Title':'Theme'})
    appearance=theme["Appearance_Mode"]
    colour=theme["Colour"]
    set_appearance_mode(appearance)
    set_default_color_theme(colour)
    #===============================================change_appearance=========================================================
    if appearance=="Light":
        light()
    

except:
    collection.insert_one({"Title":"Theme", "Appearance_Mode":"Dark", "Colour":"green"})
    set_appearance_mode("Dark")
    set_default_color_theme("green")
root.mainloop()