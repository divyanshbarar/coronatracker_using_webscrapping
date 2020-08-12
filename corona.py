from tkinter import * 
import tkinter.ttk as ttk
import requests
import bs4
import plyer
import time
import datetime
import threading

def get_html_data(url):
    data=requests.get(url)
    return data

def get_corona_detail_of_india():
    url ="https://www.mygov.in/covid-19/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div=bs.find("div",class_="information_row").find_all("div", class_="iblock")
    all_details=""

    for tag in info_div:
        text=tag.find("div",class_="info_label").get_text()
        count=tag.find("span",class_="icount").get_text()
        all_details = all_details + text + " : " + count + "\n"
        
        
    return all_details

    
def refresh():
    newdata = get_corona_detail_of_india()
    print("Refreshing..")
    mainLabel['text'] = newdata
    mainLabel1['text'] = time.asctime()

# function for notifying...
def notify_me():
    while True:
        plyer.notification.notify(
            title="COVID 19 cases of INDIA",
            message=get_corona_detail_of_india(),
            timeout=10,
            app_icon='coronaicon.ico'
        )
        time.sleep(30)



root=Tk()
root.geometry("900x1080")

root.title("corona virus tracker india")
root.configure(bg="light green")
#icon
img = PhotoImage(file = 'coronaicon.ico') 
root.tk.call('wm', 'iconphoto', root._w, img)

#backgroundimage

mainLabel =Label(root, text=get_corona_detail_of_india(), font=("times",20,"bold"), bg='white')
mainLabel.pack()
mainLabel1 =Label(root, text=time.asctime(), font=("times",10,"bold"), bg='white')
mainLabel1.pack()
reBtn =Button(root, text="REFRESH", font=("times",10,"bold"), relief='solid', command=refresh)
reBtn.pack()

framehome=Frame(root)
framehome.pack(fill=BOTH,expand=True)
imghome = PhotoImage(file = 'background.png') 
imlabel=ttk.Label(framehome,image=imghome)
imlabel.pack(fill=BOTH,expand=True)

# create a new thread
th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()
root.mainloop()
