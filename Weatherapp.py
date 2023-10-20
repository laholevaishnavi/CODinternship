#importing modules
from tkinter import *
from tkinter import ttk
import requests
import pytz
#defining function to get input
def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9c69a404ef2062b36812058b938c7698").json()
    wlabel1.config(text = data["weather"][0]["main"])
    Dlabel1.config(text = data["weather"][0]["description"])
    Tlabel1.config(text = str(int(data["main"]["temp"]-273.15)))
    Plabel1.config(text = data["main"]["pressure"])

#creating GUI of weater app
win = Tk()
win.title("Weather App")
win.iconbitmap(r'icon.ico')
win.config(bg = "cadetblue4")
win.maxsize(width = 800 , height =800 )
win.minsize(width = 800 , height =800 )
toplabel= Label(win,text="WEATHER APP",font=("Time New Roman",30,"bold"))
toplabel.place(x="100", y="50" , width=600 , height=45)
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
# creating combobox
com=ttk.Combobox(win,text="WEATHER APP",values=list_name,font=("Time New Roman",15),textvariable=city_name)
com.place(x="100",y="150",width="600",height="35")

wlabel=Label(win,text="Climate",font=("Times New Roman",20))
wlabel.place(x="150",y="300",width="225",height=25)
wlabel1=Label(win,text=" ",font=("Times New Roman",20,))
wlabel1.place(x="475",y="300",width="225",height=25)
Dlabel=Label(win,text="Description",font=("Times New Roman",20))
Dlabel.place(x="150",y="370",width="225",height=25)
Dlabel1=Label(win,text=" ",font=("Times New Roman",20))
Dlabel1.place(x="475",y="370",width="225",height=25)
Tlabel=Label(win,text="Temperature",font=("Times New Roman",20))
Tlabel.place(x="150",y="440",width="225",height=25)
Tlabel1=Label(win,text=" ",font=("Times New Roman",20))
Tlabel1.place(x="475",y="440",width="225",height=25)
Plabel=Label(win,text="Pressure",font=("Times New Roman",20))
Plabel.place(x="150",y="510",width="225",height=25)
Plabel1=Label(win,text=" ",font=("Times New Roman",20))
Plabel1.place(x="475",y="510",width="225",height=25)
logo_image=PhotoImage(file="logo.png")
logo=Label(image=logo_image)
logo.place(x="300",y="540")
done_button=Button(win,text="DONE",font=("Time New Roman",10,"bold"),command=data_get)
done_button.place(x="350",y="225",width="100",height="30")

win.mainloop()