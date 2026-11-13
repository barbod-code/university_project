from tkinter import*
import pandas as pd
use=""
def Login():
    global use
    use=textbar_username.get()
    pas=textbar_password.get()
    shape=df.shape    
    for i in range(shape[0]):
       if df["username"][i].lower()==use.lower() and df["password"][i]==pas :
           btn_bardasht.config(state="normal")
           btn_variz.config(state="normal")
           textbar_bardasht.config(state="normal")
           textbar_balance.config(state="normal")
           textbar_variz.config(state="normal")
           textbar_password.config(state="disable")
           textbar_username.config(state="disable")
           btn_login.config(state="disable")
           name=df["first_name"][i]
           Label_ok.config(text=f"welcome {name}")
           mojodi=df["balance"][i]
           textbar_balance.insert(0,mojodi)
           break
def variz_m():
    shape=df.shape
    for i in range(shape[0]):
        variz=float(textbar_variz.get())
        if df["username"][i].lower()!= use.lower():
            continue
       
        new_balance_variz=df["balance"][i]+variz
        df.loc[i, "balance"] = new_balance_variz 
        Label_variz_pool.config(text="movafag")
        textbar_balance.delete(0,END)
        textbar_balance.insert(0,new_balance_variz)
        df.to_excel(path,index=False)
        break
def bardasht_m():
    shape = df.shape
    for i in range(shape[0]):
        if df["username"][i].lower() != use.lower():
            continue

        bardasht = float(textbar_bardasht.get())

        if df["balance"][i] >= bardasht:
            new_balance = df["balance"][i] - bardasht

            df.loc[i, "balance"] = new_balance

            Label_bardasht_pool.config(text="movafagh")
            textbar_balance.delete(0, END)
            textbar_balance.insert(0, new_balance)
            df.to_excel(path, index=False)
            break
        else:
            Label_bardasht_pool.config(text="mojodi nakafi")    
app=Tk()
app.title("Account")
app.geometry("500x450")
Label(app,text="Username",).place(x=20,y=10)
Label_ok=Label(app,text="",font=200,fg="green")
Label_ok.place(x=160,y=79)
Label_bardasht_pool=Label(app,text="",font=200,fg="green")
Label_bardasht_pool.place(x=100,y=370)
Label_variz_pool=Label(app,text="",font=200,fg="green")
Label_variz_pool.place(x=100,y=320)
textbar_username=Entry(app,width=15,bg="#92EEFF",fg="black",font=20,state=NORMAL)
textbar_username.place(x=10,y=40)
Label(app,text="Password").place(x=160,y=10)
textbar_password=Entry(app,width=15,bg="#92EEFF",fg="black",font=20,state=NORMAL,show="*")
textbar_password.place(x=160,y=40)
Label(app,text="Balance",font=20,).place(x=50,y=200)
btn_login=Button(app,text="Login",font=50,width=10,state=NORMAL,command=Login)
btn_login.place(x=310,y=35)
textbar_balance=Entry(app,fg="green",font=50,state=DISABLED)
textbar_balance.place(x=55,y=230)
textbar_variz=Entry(app,fg="black",font=50,state=DISABLED)
textbar_variz.place(x=55,y=300)
btn_variz=Button(app,text="Variz",width=16,command=variz_m,state=DISABLED)
btn_variz.place(x=270,y=300)
textbar_bardasht=Entry(app,fg="black",font=50,state=DISABLED)
textbar_bardasht.place(x=54,y=350)
btn_bardasht=Button(app,text="Bardasht",width=16,command=bardasht_m,state=DISABLED)
btn_bardasht.place(x=270,y=347)
app.mainloop()
path="C:/Users/shiraz computer/Desktop/iran_account (1).xlsx"
df=pd.read_excel(path)
df.to_excel(path,index=False)

