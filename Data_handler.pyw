from Tkinter import *
import sqlite3
from tkMessageBox import * 
#() Tuple
#[] List
#[(,,,),(a,b,v)]

root2=Tk()
img=PhotoImage(file='deep.gif')

def fun(e):
    root2.destroy()
    root =Tk()
    #root.geometry('800x1500')
    root.configure(background="Black")
    root.title('Data Handler')
    global e1,e2,e3
    z11=showinfo(title="Alert Box",message="Hello owner!Welcome to Data Handler ")
    z12=showinfo(title="Alert Box",message="Please note that you can only add a single name to THE Data Handler OCCUPANT.THANK YOU ")
    z13=showinfo(title="Alert Box",message="Please note that you can update and search any item only by its name which you have inserted.So in the entry boxes above Update and Search button only type the name of the item inserted earlier.THANK YOU!")
    z11=showinfo(title="Alert Box",message="Sorry for the FUSS!But instructions are essential.KEEP CALM!For further queries you can click on HELP button.STAYCOOL!")

    con=sqlite3.Connection("mydinvent1dbms")
    cur=con.cursor()
            


    cur.execute("create table if not exists inventory1(iname varchar(20) primary key,ln varchar(20), id int,city varchar(20) )")



    def delete():
        con.close()

    def insertar():        
        a1=a.get()
        b1=(b.get())
        c1=float(c.get())
        d1=bb1.get()
        cur.execute("insert into inventory1 values(?,?,?,?)",(a1,b1,c1,d1))
        #if c1<=10:           
         #   d=showinfo(title="Alert Box",message="This item is less.Please add it soon")
        #s=showinfo(title="Alert Box",message="Items are successfully addded")
            
        con.commit()   
        
    def listar():
        s5=showinfo(title="Alert Box",message="Click the LOAD button twice to see the services in the new window!Dont notice this message after clicking LOAD button for the second time")
        widget=Tk()
        widget.title("Stored DATA")
        widget.configure(background="yellow")
        
        var=cur.fetchall() 
        cur.execute('SELECT * FROM inventory1')
        Label(widget,text="NAME  OCCUPATION  PHONE NUMBER  CITY",bg="green",fg="white").grid(row=0)
        #Button(widget,text="ITEMS ALERT",bg="red",fg="white",command=messagebox).grid(row=1)
        print len(var)
        j=0
        while j< len(var):
            
            print var[j]
            
     
            Label(widget,text=var[j],bg="yellow",fg="green",font="20").grid(row=j+2)
     
            j=j+1

          
        




    def box():
        global e1,e2,e3
        widget2=Tk()
        widget2.title("Update Screen")
        widget2.configure(background="yellow")
        Label(widget2,text="enter occupation of occupant to be updated").grid(row=0)
        e1=Entry(widget2)
        e1.grid(row=1,column=1)
        Label(widget2,text="enter phone no. of occupant to be added which is updated").grid(row=2)
        e2=Entry(widget2)
        e2.grid(row=3,column=1)
        Label(widget2,text="enter city of occupant to be added which is updated").grid(row=4)
        e3=Entry(widget2)
        e3.grid(row=5,column=1)
        Button(widget2, text='Add Now',bg="green",fg="white",command=update).grid(row =6, column=1, columnspan=4,
        sticky='w')     #   if i <3:
        


    def update():
        global e1,e2
        z=e.get()
        x=(e1.get())
        y=float(e2.get())
        
        q=e3.get()
        try:
            
            
            
            
            cur.execute('delete from inventory1 where iname=?',(z,))
            cur.execute("insert into inventory1 values(?,?,?,?)",(z,x,y,q))
            print cur.fetchall()
            con.commit()
            
        
        except sqlite3.OperationalError as message:
            em=message.args[0]
            showerror("error",em)
        s4=showinfo(title="Alert Box",message="Your item is added .Now close this window and you can check")
        #delete * from inventory where iname=?
        #insert ...............
    def search():                             #("SELECT * FROM addresses WHERE FIRST_NAME = ? ",t)
        yo=Tk()
        yo.title("Searched Item")
        r=str()
        r=d.get()
        connection=sqlite3.connect("mydinvent1dbms")
        cursor=connection.cursor()
        
        cursor.execute('SELECT * FROM inventory1 where iname=?',(r,))
        var2=cursor.fetchall()
        
        print len(var2)
        i=0
        Label(yo,text="the person info is ",bg="red",fg="white",font="40").grid(row=0)
        while i< len(var2):
            
            print var2[i]
            Label(yo,text="Note:The first entry displayed is name of the occupant",fg="blue",font="40").grid(row=1)
            Label(yo,text="Note:The second entry displayed is the service the person is providing ",fg="blue",font="40").grid(row=2)
            Label(yo,text="Note:The third entry displayed is the phone number of the person",fg="blue",font="40").grid(row=3)
            Label(yo,text="Note:The fourth entry displayed is the city of the person",fg="blue",font="40").grid(row=4)
            Label(yo,text=var2[i],fg="red",font="40").grid(row=6)
     
            i=i+1
        
        

    def reset():



        
        s2=showinfo(title="Alert Box",message="Fill your items again now")   
        cur.execute("DROP TABLE inventory1")

        cur.execute("create table if not exists inventory1(iname varchar(20) primary key,ln varchar(20), id int,city varchar(20) )")
        con.commit()    
                
    def Help():
        s8=showinfo(title="Alert Box",message="Click on INSERT button to insert the name of occupant,service name,phone number of the person and the city to be added.Click on LOAD to display all the items that are added.Click on RESET to remove sll the entries added and start adding fresh entries in empty fresh table,Click on UPDATE to change information regarding any entry.Click on SEARCH to find the information regarding any person by typing personname in the entrybox") 

        
        
    def onclick1(x):
        a.insert(25,x)




    def onclick2(y):
        b.insert(25,y)
        


        


    def onclick3(z):
        c.insert(25,z)



    def onclick4(z1):
        bb1.insert(25,z1)





        

    def press1():
        root2=Tk()
        root2.title("OCCUPANT enter")
        
        Button(root2,text="q",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('q')).grid(row=12,column=7,sticky=N+W+S+E)
        Button(root2,text="w",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('w')).grid(row=12,column=8,sticky=N+W+S+E)
        Button(root2,text="e",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('e')).grid(row=12,column=9,sticky=N+W+S+E)
        Button(root2,text="r",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('r')).grid(row=12,column=10,sticky=N+W+S+E)
        Button(root2,text="t",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('t')).grid(row=12,column=11,sticky=N+W+S+E)
        Button(root2,text="y",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('y')).grid(row=12,column=12,sticky=N+W+S+E)
        Button(root2,text="u",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('u')).grid(row=12,column=13,sticky=N+W+S+E)
        Button(root2,text="i",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('i')).grid(row=12,column=14,sticky=N+W+S+E)
        Button(root2,text="o",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('o')).grid(row=12,column=15,sticky=N+W+S+E)
        Button(root2,text="p",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('p')).grid(row=12,column=16,sticky=N+W+S+E)
        Button(root2,text="7",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('7')).grid(row=12,column=17,sticky=N+W+S+E)
        Button(root2,text="8",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('8')).grid(row=12,column=18,sticky=N+W+S+E)
        Button(root2,text="9",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('9')).grid(row=12,column=19,sticky=N+W+S+E)




        Button(root2,text="a",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('a')).grid(row=13,column=7,sticky=N+W+S+E)
        Button(root2,text="s",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('s')).grid(row=13,column=8,sticky=N+W+S+E)
        Button(root2,text="d",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('d')).grid(row=13,column=9,sticky=N+W+S+E)
        Button(root2,text="f",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('f')).grid(row=13,column=10,sticky=N+W+S+E)
        Button(root2,text="g",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('g')).grid(row=13,column=11,sticky=N+W+S+E)
        Button(root2,text="h",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('h')).grid(row=13,column=12,sticky=N+W+S+E)
        Button(root2,text="j",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('j')).grid(row=13,column=13,sticky=N+W+S+E)
        Button(root2,text="k",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('k')).grid(row=13,column=14,sticky=N+W+S+E)
        Button(root2,text="l",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('l')).grid(row=13,column=15,sticky=N+W+S+E)
        Button(root2,text="-",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('-')).grid(row=13,column=16,sticky=N+W+S+E)
        Button(root2,text="4",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('4')).grid(row=13,column=17,sticky=N+W+S+E)
        Button(root2,text="5",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('5')).grid(row=13,column=18,sticky=N+W+S+E)
        Button(root2,text="6",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('6')).grid(row=13,column=19,sticky=N+W+S+E)







        Button(root2,text="z",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('z')).grid(row=14,column=7,sticky=N+W+S+E)
        Button(root2,text="x",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('x')).grid(row=14,column=8,sticky=N+W+S+E)
        Button(root2,text="c",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('c')).grid(row=14,column=9,sticky=N+W+S+E)
        Button(root2,text="v",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('v')).grid(row=14,column=10,sticky=N+W+S+E)
        Button(root2,text="b",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('b')).grid(row=14,column=11,sticky=N+W+S+E)
        Button(root2,text="n",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('n')).grid(row=14,column=12,sticky=N+W+S+E)
        Button(root2,text="m",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('m')).grid(row=14,column=13,sticky=N+W+S+E)
        Button(root2,text=",",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1(',')).grid(row=14,column=14,sticky=N+W+S+E)
        Button(root2,text=".",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('.')).grid(row=14,column=15,sticky=N+W+S+E)
        Button(root2,text="/",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('/')).grid(row=14,column=16,sticky=N+W+S+E)
        Button(root2,text="1",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('1')).grid(row=14,column=17,sticky=N+W+S+E)
        Button(root2,text="2",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('2')).grid(row=14,column=18,sticky=N+W+S+E)
        Button(root2,text="3",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('3')).grid(row=14,column=19,sticky=N+W+S+E)




    def press2():
        root1=Tk()
        root1.title("SERVICE enter")
        Button(root1,text="q",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('q')).grid(row=12,column=7,sticky=N+W+S+E)
        Button(root1,text="w",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('w')).grid(row=12,column=8,sticky=N+W+S+E)
        Button(root1,text="e",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('e')).grid(row=12,column=9,sticky=N+W+S+E)
        Button(root1,text="r",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('r')).grid(row=12,column=10,sticky=N+W+S+E)
        Button(root1,text="t",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('t')).grid(row=12,column=11,sticky=N+W+S+E)
        Button(root1,text="y",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('y')).grid(row=12,column=12,sticky=N+W+S+E)
        Button(root1,text="u",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('u')).grid(row=12,column=13,sticky=N+W+S+E)
        Button(root1,text="i",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('i')).grid(row=12,column=14,sticky=N+W+S+E)
        Button(root1,text="o",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('o')).grid(row=12,column=15,sticky=N+W+S+E)
        Button(root1,text="p",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('p')).grid(row=12,column=16,sticky=N+W+S+E)
        Button(root1,text="7",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('7')).grid(row=12,column=17,sticky=N+W+S+E)
        Button(root1,text="8",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('8')).grid(row=12,column=18,sticky=N+W+S+E)
        Button(root1,text="9",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('9')).grid(row=12,column=19,sticky=N+W+S+E)




        Button(root1,text="a",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('a')).grid(row=13,column=7,sticky=N+W+S+E)
        Button(root1,text="s",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('s')).grid(row=13,column=8,sticky=N+W+S+E)
        Button(root1,text="d",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('d')).grid(row=13,column=9,sticky=N+W+S+E)
        Button(root1,text="f",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('f')).grid(row=13,column=10,sticky=N+W+S+E)
        Button(root1,text="g",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('g')).grid(row=13,column=11,sticky=N+W+S+E)
        Button(root1,text="h",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('h')).grid(row=13,column=12,sticky=N+W+S+E)
        Button(root1,text="j",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('j')).grid(row=13,column=13,sticky=N+W+S+E)
        Button(root1,text="k",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('k')).grid(row=13,column=14,sticky=N+W+S+E)
        Button(root1,text="l",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('l')).grid(row=13,column=15,sticky=N+W+S+E)
        Button(root1,text="-",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('-')).grid(row=13,column=16,sticky=N+W+S+E)
        Button(root1,text="4",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('4')).grid(row=13,column=17,sticky=N+W+S+E)
        Button(root1,text="5",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('5')).grid(row=13,column=18,sticky=N+W+S+E)
        Button(root1,text="6",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('6')).grid(row=13,column=19,sticky=N+W+S+E)







        Button(root1,text="z",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('z')).grid(row=14,column=7,sticky=N+W+S+E)
        Button(root1,text="x",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('x')).grid(row=14,column=8,sticky=N+W+S+E)
        Button(root1,text="c",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('c')).grid(row=14,column=9,sticky=N+W+S+E)
        Button(root1,text="v",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('v')).grid(row=14,column=10,sticky=N+W+S+E)
        Button(root1,text="b",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('b')).grid(row=14,column=11,sticky=N+W+S+E)
        Button(root1,text="n",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('n')).grid(row=14,column=12,sticky=N+W+S+E)
        Button(root1,text="m",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('m')).grid(row=14,column=13,sticky=N+W+S+E)
        Button(root1,text=",",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2(',')).grid(row=14,column=14,sticky=N+W+S+E)
        Button(root1,text=".",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('.')).grid(row=14,column=15,sticky=N+W+S+E)
        Button(root1,text="/",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('/')).grid(row=14,column=16,sticky=N+W+S+E)
        Button(root1,text="1",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('1')).grid(row=14,column=17,sticky=N+W+S+E)
        Button(root1,text="2",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('2')).grid(row=14,column=18,sticky=N+W+S+E)
        Button(root1,text="3",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('3')).grid(row=14,column=19,sticky=N+W+S+E)






    def press3():
        root3=Tk()
        root3.title("PHONE NUMBER Enter")
        Button(root3,text="7",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('7')).grid(row=21,column=7,sticky=N+W+S+E)
        Button(root3,text="8",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('8')).grid(row=21,column=8,sticky=N+W+S+E)
        Button(root3,text="9",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('9')).grid(row=21,column=9,sticky=N+W+S+E)
        Button(root3,text="4",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('4')).grid(row=22,column=7,sticky=N+W+S+E)
        Button(root3,text="5",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('5')).grid(row=22,column=8,sticky=N+W+S+E)
        Button(root3,text="6",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('6')).grid(row=22,column=9,sticky=N+W+S+E)
        Button(root3,text="1",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('1')).grid(row=23,column=7,sticky=N+W+S+E)
        Button(root3,text="2",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('2')).grid(row=23,column=8,sticky=N+W+S+E)
        Button(root3,text="3",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('3')).grid(row=23,column=9,sticky=N+W+S+E)
        Button(root3,text="/",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('/')).grid(row=24,column=7,sticky=N+W+S+E)
        Button(root3,text="0",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('0')).grid(row=24,column=8,sticky=N+W+S+E)
        Button(root3,text=".",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('.')).grid(row=24,column=9,sticky=N+W+S+E)
        

        

    def press4():
        root5=Tk()
        root5.title("CITY enter")
        Button(root5,text="q",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('q')).grid(row=12,column=7,sticky=N+W+S+E)
        Button(root5,text="w",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('w')).grid(row=12,column=8,sticky=N+W+S+E)
        Button(root5,text="e",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('e')).grid(row=12,column=9,sticky=N+W+S+E)
        Button(root5,text="r",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('r')).grid(row=12,column=10,sticky=N+W+S+E)
        Button(root5,text="t",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('t')).grid(row=12,column=11,sticky=N+W+S+E)
        Button(root5,text="y",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('y')).grid(row=12,column=12,sticky=N+W+S+E)
        Button(root5,text="u",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('u')).grid(row=12,column=13,sticky=N+W+S+E)
        Button(root5,text="i",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('i')).grid(row=12,column=14,sticky=N+W+S+E)
        Button(root5,text="o",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('o')).grid(row=12,column=15,sticky=N+W+S+E)
        Button(root5,text="p",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('p')).grid(row=12,column=16,sticky=N+W+S+E)
        Button(root5,text="7",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('7')).grid(row=12,column=17,sticky=N+W+S+E)
        Button(root5,text="8",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('8')).grid(row=12,column=18,sticky=N+W+S+E)
        Button(root5,text="9",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('9')).grid(row=12,column=19,sticky=N+W+S+E)




        Button(root5,text="a",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('a')).grid(row=13,column=7,sticky=N+W+S+E)
        Button(root5,text="s",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('s')).grid(row=13,column=8,sticky=N+W+S+E)
        Button(root5,text="d",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('d')).grid(row=13,column=9,sticky=N+W+S+E)
        Button(root5,text="f",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('f')).grid(row=13,column=10,sticky=N+W+S+E)
        Button(root5,text="g",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('g')).grid(row=13,column=11,sticky=N+W+S+E)
        Button(root5,text="h",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('h')).grid(row=13,column=12,sticky=N+W+S+E)
        Button(root5,text="j",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('j')).grid(row=13,column=13,sticky=N+W+S+E)
        Button(root5,text="k",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('k')).grid(row=13,column=14,sticky=N+W+S+E)
        Button(root5,text="l",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('l')).grid(row=13,column=15,sticky=N+W+S+E)
        Button(root5,text="-",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('-')).grid(row=13,column=16,sticky=N+W+S+E)
        Button(root5,text="4",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('4')).grid(row=13,column=17,sticky=N+W+S+E)
        Button(root5,text="5",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('5')).grid(row=13,column=18,sticky=N+W+S+E)
        Button(root5,text="6",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('6')).grid(row=13,column=19,sticky=N+W+S+E)







        Button(root5,text="z",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('z')).grid(row=14,column=7,sticky=N+W+S+E)
        Button(root5,text="x",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('x')).grid(row=14,column=8,sticky=N+W+S+E)
        Button(root5,text="c",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('c')).grid(row=14,column=9,sticky=N+W+S+E)
        Button(root5,text="v",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('v')).grid(row=14,column=10,sticky=N+W+S+E)
        Button(root5,text="b",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('b')).grid(row=14,column=11,sticky=N+W+S+E)
        Button(root5,text="n",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('n')).grid(row=14,column=12,sticky=N+W+S+E)
        Button(root5,text="m",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('m')).grid(row=14,column=13,sticky=N+W+S+E)
        Button(root5,text=",",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4(',')).grid(row=14,column=14,sticky=N+W+S+E)
        Button(root5,text=".",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('.')).grid(row=14,column=15,sticky=N+W+S+E)
        Button(root5,text="/",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('/')).grid(row=14,column=16,sticky=N+W+S+E)
        Button(root5,text="1",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('1')).grid(row=14,column=17,sticky=N+W+S+E)
        Button(root5,text="2",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('2')).grid(row=14,column=18,sticky=N+W+S+E)
        Button(root5,text="3",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick4('3')).grid(row=14,column=19,sticky=N+W+S+E)

        


    Label(root,text="Type the name of the occupant to be added ",font='Times 12 bold',bg="Black",fg="White").grid(row=0,column=0,sticky='e')
    a=Entry(root,bd=3,bg='Light Grey')
    a.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=5)

    Label(root,text="Type the Service of the occupant  to be added",font='Times 12 bold',bg="Black",fg="White").grid(row=1,column=0,sticky='e')
    b=Entry(root,bd=3,bg='Light Grey')
    b.grid(row=1,column=1,padx=2,pady=2,sticky='we',columnspan=5)

    Label(root,text="Type the phone number of the occupant to be added  ",font='Times 12 bold',bg="Black",fg="White").grid(row=2,column=0,sticky='e')
    c=Entry(root,bd=3,bg='Light Grey')
    c.grid(row=2,column=1,padx=2,pady=2,sticky='we',columnspan=5)

    Label(root,text="Type the City of the occupant  to be added",font='Times 12 bold',bg="Black",fg="White").grid(row=3,column=0,sticky='e')
    bb1=Entry(root,bd=3,bg='Light Grey')
    bb1.grid(row=3,column=1,padx=2,pady=2,sticky='we',columnspan=5)


    Button(root, text="Insert",bg="Grey",fg="Black",command=insertar).grid(row=0, column=7, sticky='ew', padx=2,
    pady=2)
    Button(root, text="Load",bg="Grey",fg="Black",command=listar).grid(row=1, column=7, sticky='ew', padx=2)
    #Button(root, text="Close DBMS",bg="green",fg="white",command=delete).grid(row=2, column=7, sticky='ew', padx=2)
    Button(root, text="Reset",bg="Grey",fg="Black",command=reset).grid(row=3, column=7, sticky='ew',
    padx=2)
    d=Entry(root,bd=3,bg='Light Grey')
    d.grid(row =5, column=1,
    columnspan=6, sticky='w')
    Button(root, text='Search',bg="Grey",fg="Black",command=search).grid(row =7, column=1, columnspan=4,
    sticky='w')
    e=Entry(root,bd=3,bg='Light Grey')
    e.grid(row =5, column=7,
    columnspan=5, sticky='w')
    Button(root, text='Update',bg="Grey",fg="Black",command=box).grid(row =7, column=7, columnspan=4,
    sticky='w')




    Label(root, text="To activate ONSCREE KEYBOARD for typing the NAME of the occupant to be added PRESS the button below",font='Times 12 bold',bg="Black",fg="White").grid(row=10, column=6, sticky='w')
    Button(root,text="Press Button",bg="Grey",fg="Black",command=press1).grid(row=11,column=6)

    Label(root, text="To activate ONSCREEN KEYBOARD for typing the SERVICE of the occupant added PRESS the button below",font='Times 12 bold',bg="Black",fg="White").grid(row=12, column=6, sticky='w')
    Button(root,text="Press Button",bg="Grey",fg="Black",command=press2).grid(row=13,column=6)

    Label(root, text="To activate ONSCREEN KEYBOARD for typing the PHONE NO. of occupant added PRESS the button below",font='Times 12 bold',bg="Black",fg="White").grid(row=14, column=6, sticky='w')
    Button(root,text="Press Button",bg="Grey",fg="Black",command=press3).grid(row=15,column=6)


    Label(root, text="To activate ONSCREEN KEYBOARD for typing the CITY of occupant added PRESS the button below",font='Times 12 bold',bg="Black",fg="White").grid(row=16, column=6, sticky='w')
    Button(root,text="Press Button",bg="Grey",fg="Black",command=press4).grid(row=17,column=6)

    Button(root,text="Help",bg="Grey",fg="Black",command=Help).grid(row=17)

    def quit1():
        q=askyesno('Quit','Do You Want to Quit?')
        if q==True:
            root.destroy()
    Button(root,text='Quit',bg="Grey",fg="Black",command=quit1).grid(row=18)

    root.mainloop()

    

a=Label(root2,image=img)
a.bind('<Motion>',fun)
a.pack()
root2.mainloop()
