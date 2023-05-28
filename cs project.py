import sys
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk ,Image
import mysql.connector as ms
import re

#connecting to sql
mycon=ms.connect(host='localhost',user='',passwd='',database='school')
mycur=mycon.cursor()

def check(email):
    regex = '^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$'
    return (re.search(regex,email))

def isValid(s):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(s)

#managing status of booked and unbooked seats
def OnClick(btn,clicked):
    text = btn.cget("text")

    if btn['bg']!='green':
        btn['bg']='green'

    elif (btn['bg']=='green') and (text[0]=='G' or text[0]=='F'):
        btn['bg']='red'

    else:
        btn['bg']='black'

    if text not in clicked:
        clicked.append(text)
    else:
        clicked.remove(text)
    seat2=''
    for i in range(len(clicked)):
        seat2=seat2+clicked[i]+' '

    q='update csproj set seat=%s where phone=%s'
    mycur.execute(q,(seat2,phone))
    mycon.commit()
    global bill
    bill=0
    for i in clicked:
        if i[0]=="G" or i[0]=='F':
            bill+=80
        else:
            bill+=200
    global gst
    gst1=0.18*bill
    gst=round(gst1,2)

    global total
    total=bill+gst
#bill calculation
def billing():
    movie3.quit()
    movie3.destroy()

    global pay
    pay=Tk()
    pay.geometry('400x400')
    pay.title('Bill')
    #displaying an image
    img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\aishu\Downloads\movieseat.jpg"))
    m1=Label(pay,image=img1)
    m1.pack()
    
    #creating a label
    L3 = Label(pay, text= 'BILL',fg='black',width=10)
    L3.place(x=150,y=80)

    L3 = Label(pay, text='Amount : ',fg='black',width=10)
    L3.place(x=90,y=140)

    L3 = Label(pay, text='GST :',fg='black',width=10)
    L3.place(x=90,y=200)

    L3 = Label(pay, text='TOTAL BILL :',fg='black',width=12)
    L3.place(x=90,y=260)

    L3 = Label(pay, text=bill,fg='black',width=10)
    L3.place(x=210,y=140)

    L3 = Label(pay, text=gst,fg='black',width=10)
    L3.place(x=210,y=200)

    L3 = Label(pay, text=total,fg='black',width=10)
    L3.place(x=210,y=260)

    #creating a button
    B = Button(pay,text='PAY!',height=1,bg='black',fg='white',command=end)
    B.place(x=150,y=300)


def end():
    pay.quit()
    pay.destroy()


def preview():
    movie2.quit()
    movie2.destroy()

    global movie3
    movie3=Tk()
    movie3.geometry('600x600')
    movie3.title('PREVIEW')

    img1 = ImageTk.PhotoImage(Image.open("C:/Users/aishu/Downloads/x.png"))
    m1=Label(movie3,image=img1)
    m1.place(x=0, y=0,relwidth=1, relheight=1)

    L3 = Label(movie3, text='',fg='black',width=10)
    L3.place(x=50,y=100)

    a="select * from csproj  where phone= '%s'"%(phone)
    mycur.execute(a)
    q=mycur.fetchall()
    n=q[0][0]
    e=q[0][1]
    m=q[0][2]
    s=q[0][3]
    t=q[0][4]
    p=q[0][5]
    se=q[0][6]

    L3 = Label(movie3, text= 'NAME',fg='black',width=10)
    L3.place(x=200,y=130)

    L3 = Label(movie3, text='EMAIL',fg='black',width=10)
    L3.place(x=200,y=190)

    L3 = Label(movie3, text='MOVIE',fg='black',width=10)
    L3.place(x=200,y=250)

    L3 = Label(movie3, text='SCREEN',fg='black',width=10)
    L3.place(x=200,y=310)

    L3 = Label(movie3, text='TIME',fg='black',width=10)
    L3.place(x=200,y=370)

    L3 = Label(movie3, text='PHONE NO.',fg='black',width=10)
    L3.place(x=200,y=430)

    L3 = Label(movie3, text='SEAT',fg='black',width=10)
    L3.place(x=200,y=490)

    L3 = Label(movie3, text=n,fg='black',width=10)
    L3.place(x=350,y=130)

    L3 = Label(movie3, text=e,fg='black')
    L3.place(x=350,y=190)

    L3 = Label(movie3, text=m,fg='black',width=10)
    L3.place(x=350,y=250)

    L3 = Label(movie3, text=s,fg='black',width=10)
    L3.place(x=350,y=310)

    L3 = Label(movie3, text=t,fg='black',width=10)
    L3.place(x=350,y=370)

    L3 = Label(movie3, text=p,fg='black',width=10)
    L3.place(x=350,y=430)

    L3 = Label(movie3, text=se,fg='black',width=10)
    L3.place(x=350,y=490)

    B = Button(movie3,text='Continue',height=1,bg='black',fg='white',command=billing)
    B.place(x=300,y=550)
i=0

def show1(moviename):
    movie.quit()
    movie.destroy()
    q="update csproj set moviename = %s where phone =%s"
    mycur.execute(q,(moviename,phone))
    mycon.commit()

    global show
    show=Tk()
    show.geometry('500x400')
    show.config(bg='indian red')
    show.title("SCREEN")
    mycur.execute("select*from showdet")
    img1 = ImageTk.PhotoImage(Image.open("C:/Users/aishu/Downloads/x.png"))
    m1=Label(show,image=img1)
    m1.place(x=0, y=0,relwidth=1, relheight=1)
    n=0
    global show_details
    show_details = {}
    for i in range(1,5):
        x=mycur.fetchone()
        a=x[1]
        b=x[2]
        show_details[a] = b
        c='screen  '+str(a)
        l1=Label(show,text=c, width=15,bg='black',fg='white')
        l1.place(x=100,y=100+n)
        l1=Label(show,text=b, width=10,bg='black',fg='white')
        l1.place(x=300,y=100+n)
        n+=50

    global var
    var=IntVar()
    R1 = Radiobutton(show,text=" ",variable=var, value=0)
    R1.place( x=400,y=100 )
    R2 = Radiobutton(show,text=" ", variable=var,value=1)
    R2.place( x=400,y=150 )
    R3 = Radiobutton(show,text=" ", variable=var, value=2)
    R3.place( x=400,y=200 )
    R4 = Radiobutton(show,text=" ", variable=var,value=3)
    R4.place( x=400,y=250 )
    B = Button(show, text="NEXT",height=1,fg="white",bg='black',command= lambda : seat(moviename))
    B.place(x=250,y=300)
    show.mainloop()

def seat(moviename):
    global scr
    global times

    radio=int(var.get())
    scr=str(list(show_details.keys())[radio])
    times=str(list(show_details.values())[radio])
    q="update csproj set scr = %s , times =%s where phone =%s"
    mycur.execute(q,(scr,times,phone))
    mycon.commit()
    show.quit()
    show.destroy()
    global movie2
    movie2=Tk()
    movie2.geometry('600x500')
    movie2.title('SEAT')
    movie2.config(bg='indian red')

    img1 = ImageTk.PhotoImage(Image.open("C:/Users/aishu/Downloads/x.png"))
    m1=Label(movie2,image=img1)
    m1.place(x=0, y=0,relwidth=1, relheight=1)

    clicked=[]
    n=0
    x=0

    for i in range(65,72):
        for j in range(1,10):
            a=str(chr(i)+str(j))
            if a[0]=='G' or a[0]=='F':
                z='red'
                w='black'
            else:
                z='black'
                w='white'
            disabled_seats="select seat from csproj where scr=%s and moviename=%s"
            mycur.execute(disabled_seats,(scr,moviename))
            q=mycur.fetchall()
            blocked_seats = []
            for k in q:
                p=k[0]
                if p!= None:
                    for seat in p.strip().split(' '):
                        blocked_seats.append(seat)
            B3 = Button(movie2, text=a,height=1,fg=w,bg=z)
            B3.place(x=100+x,y=180+n)
            B3.config(command=lambda btn=B3: OnClick(btn, clicked))
            if B3['text'] in blocked_seats:
                B3['state']='disabled'
            bill=0

            x+=40
        x=0
        n+=40

    B3 = Button(movie2,text='economy',bg='red',height=1,fg='black')
    B3.place(x=130,y=100)
    B4 = Button(movie2,text='premium',height=1,bg='black',fg='white')
    B4.place(x=210,y=100)
    L3 = Label(movie2, text="SEAT CLASS-",fg='black',width=10)
    L3.place(x=50,y=100)
    label_0 =Label(movie2,text="SELECT SEATS", width=30,font=("bold","16"))
    label_0.place(x=100,y=40)
    B5 = Button(movie2,text='NEXT',height=1,bg='black',fg='white',command=preview)
    B5.place(x=270,y=460)

    movie2.mainloop()


def movie1():
    top.quit()
    top.destroy()
    global movie
    movie=Tk()
    movie.geometry('1100x700')
    movie.title("MOVIE")
    movie.config(bg="indian red")

    img1 = ImageTk.PhotoImage(Image.open("C:/Users/aishu/Downloads/x.png"))
    m1=Label(movie,image=img1)
    m1.place(x=0, y=0,relwidth=1, relheight=1)
    l1=Label(movie,text="SELECT THE MOVIE", width=30,font=("bold",20))
    l1.place(x=300,y=50)
    img8 = ImageTk.PhotoImage(Image.open("C:/Users/aishu/Downloads/master.jpg"))
    m8=Label(movie,image=img8)
    m8.place(x=30,y=110)
    B1= Button(movie, text="MASTER",height=1,fg="white",bg='black',command= lambda : show1("master"))
    B1.place(x=140,y=290)
    img2 = ImageTk.PhotoImage(Image.open("C:/Users/aishu/Downloads/ala1.jpg"))
    m2=Label(movie,image=img2)
    m2.place(x=400,y=110)
    B2 = Button(movie, text="ALAVAIKUNTAPURAMULOO",height=1,fg="white",bg='black',command= lambda : show1("alavaikuntapuramuloo"))
    B2.place(x=480,y=290)
    img3 = ImageTk.PhotoImage(Image.open("C:/Users/aishu/Downloads/sadak.jpg"))
    m3=Label(movie,image=img3)
    m3.place(x=770,y=110)
    B3 = Button(movie, text="SADAK2",height=1,fg="white",bg='black',command= lambda : show1("sadak2"))
    B3.place(x=900,y=290)
    img4 = ImageTk.PhotoImage(Image.open("C:/Users/aishu/Downloads/kaithi2.jpg"))
    m4=Label(movie,image=img4)
    m4.place(x=400,y=400)
    B4 = Button(movie, text="KAITHI",height=1,fg="white",bg='black',command= lambda : show1("kaithi"))
    B4.place(x=500,y=620)
    img5 = ImageTk.PhotoImage(Image.open("C:/Users/aishu/Downloads/padmavat.jpg"))
    m5=Label(movie,image=img5)
    m5.place(x=30,y=400)
    B5 = Button(movie, text="PADMAVAT",height=1,fg="white",bg='black',command= lambda : show1("padmavat"))
    B5.place(x=140,y=620)
    img6 = ImageTk.PhotoImage(Image.open("C:/Users/aishu/Downloads/mahanati.jpg"))
    m6=Label(movie,image=img6)
    m6.place(x=770,y=400)
    B6 = Button(movie, text="MAHANATI",height=1,fg="white",bg='black',command= lambda : show1("mahanati"))
    B6.place(x=890,y=620)

    movie.mainloop()

#checks validity of phone number and email
def checkboth():
    global name
    global email
    global phone
    global address

    name = E1.get()
    email = E2.get()
    phone = E3.get()
    address=E4.get()
    def x():
            query="insert into csproj(name,email,phone) values('{0}','{1}',{2})".format(name,email,phone)
            mycur.execute(query)
            mycon.commit()

    a = None
    if address=='' or name=='' or phone=='' or email=='':
            messagebox.showerror(title='error',message="pls enter the details")
            top.destroy()
            wid()

    if isValid(phone)==None and check(email)==None:
        messagebox.showerror(title='error',message="email and number are invalid")
        a=messagebox.askokcancel(message="try again?")

    elif isValid(phone) == None:
        messagebox.showerror(title='error',message="number is invalid")
        a=messagebox.askokcancel(message="try again?")

    elif check(email) == None:
        messagebox.showerror(title='error',message="email is invalid")
        a=messagebox.askokcancel(message="try again?")

    if a == None:
        x()
        movie1()
    elif a==True:
        top.quit()
        top.destroy()
        wid()
    elif a==False:
        top.quit()
        top.destroy()


def wid():
    global top
    top = Tk()
    top.geometry('500x500')
    #top.resizable(0,0)
    top.title("DETAILS")


    img1 = ImageTk.PhotoImage(Image.open("C:/Users/aishu/Downloads/x.png"))
    m1=Label(top,image=img1)
    m1.place(x=0, y=0,relwidth=1, relheight=1)
    label_0 =Label(top,text="ENTER YOUR DETAILS",font="bold")
    label_0.place(x=160,y=60)
    L1 = Label(top, text="NAME:",fg='black',font=("bold",10))
    L1.place(x=80,y=130)
    L2 = Label(top, text="EMAIL:",fg='black',font=("bold",10))
    L2.place(x=80,y=190)
    L3 = Label(top, text="PHONE NO:",fg='black',font=('fixed sys', 10))
    L3.place(x=50,y=250)
    L4 = Label(top, text="ADDRESS:",fg='black',font=("bold",10))
    L4.place(x=70,y=310)
    L4.focus_set()

    global E1
    global E2
    global E3
    global E4

    E1 = Entry(top, bd =2,bg="gray20",fg="white",width=40)
    E1.place(x=150,y=130)
    E2 = Entry(top, bd =2,bg="gray20",fg="white",width=40)
    E2.place(x=150,y=190)
    E3 = Entry(top, bd =2,bg="gray20",fg="white",width=40)
    E3.place(x=150,y=250)
    E4 = Entry(top, bd =2,bg="gray20",fg="white",width=40)
    E4.place(x=150,y=310)
    E4.focus_set()
    B = Button(top, text="NEXT", command = checkboth,height=1,fg="white",bg='black')
    B.place(x=250,y=370)
    top.mainloop()
if __name__ == "__main__":
    wid()
