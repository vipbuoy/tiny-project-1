import shutil,os,bs4,requests
from tkinter import *
import re
from pathlib import Path as p

import googlesearch

def go():
    #print(current_data.get(),destination_data.get(),sep='\n')
    if not (os.path.exists(current_data.get()) and os.path.exists(destination_data.get())):
        windoww=Tk();
        windoww.title("ERROR!")
        c=Label(windoww,text="Enter valid location or use forward slash instead of backward")
        c.config(font=(1))
        c.grid(row=0,column=0,pady=2)
        window.destroy()
    try:
        i=float(imdb_data.get())
    except:
        windoww=Tk();
        windoww.title("ERROR!")
        c=Label(windoww,text="Enter a number")
        c.config(font=(1))
        c.grid(row=0,column=0,pady=2)
        window.destroy()
        

    make=[]
    if i<0 or i>10:
        windoww=Tk();
        windoww.title("ERROR!")
        c=Label(windoww,text="Enter rating in range 0 to 10")
        c.config(font=(1))
        c.grid(row=0,column=0,pady=2)
        window.destroy()
    for file,folder,sub in os.walk(current_data.get()):
       for s in sub:
           make.append(file+'\\'+s)

            
    for j in make:
        temp=p(j)
        if temp.suffix==".mkv" or temp.suffix==".mp4" or temp.suffix==".avi":
            for k in googlesearch.search(temp.stem+"+ imdb",tld='com',num=1,stop=1,pause=2):
                try:
                    res=requests.get(k)
                except:
                    break;
                no=bs4.BeautifulSoup(res.text,'html.parser')
                tt=no.find(itemprop='ratingValue')
                if tt==None:
                    break
                t=tt.get_text()
                t=float(t)
                if t>=i:
                   shutil.copy(j,destination_data.get()+'/')

    window.destroy()
window=Tk()
window.title("Movie and series sorter")


current=Label(window,text="Enter current location:")
current.config(font=(1))
current.grid(row=0,column=0,pady=2)

current_data=StringVar()
current_box=Entry(window,textvariable=current_data,width=50)
current_box.grid(row=0,column=10,pady=2)


destination=Label(window,text="Enter destination location:")
destination.config(font=(2))
destination.grid(row=2,column=0,pady=2)

destination_data=StringVar()
destination_box=Entry(window,textvariable=destination_data,width=50)
destination_box.grid(row=2,column=10,pady=2)


imdb=Label(window,text="Enter IMDB rating:")
imdb.config(font=(1))
imdb.grid(row=3,column=0,pady=2)

imdb_data=StringVar()
imdb_box=Entry(window,textvariable=imdb_data,width=50)
imdb_box.grid(row=3,column=10,pady=2)


button=Button(window,text="GO!",bg="green",width='10',command=go)
button.config(font=(20))
button.grid(row=4,column=5)






        
window.mainloop()
 


