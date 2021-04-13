from bs4 import BeautifulSoup
from tkinter import *
import threading
import requests
import time

class FrmMain:
    def __init__(self):
        self.frm = Tk()
        self.frm.geometry("300x80")
        self.frm.title("Monitor")
        self.frm.config(background="#333")
        self.frm.resizable(0,0)
        photo = PhotoImage(file="bitcoin.png")
        self.frm.iconphoto(False, photo)
        self.ChargeControls()
        self.last_price = -1
        self.frm.after(1000, self.LoopPrice)
        self.frm.mainloop()
    def ChargeControls(self):
        self.LblTitle = Label(self.frm, fg="white", text="Precio Bitcoin", font=("Century Gothic", 20))
        self.LblTitle.config(background="#333")
        self.LblTitle.grid(row=0, column=0)
        self.LblPrice = Label(self.frm, fg="white", text="", font=("Century Gothic", 16))
        self.LblPrice.config(background="#333")
        self.LblPrice.grid(row=1, column=0)
    def GetPrice(self, coin):
        #url
        url = "https://www.google.com/search?q="+coin+"+price"
        # request http
        HTTP = requests.get(url)
        # Parse html response
        soup = BeautifulSoup(HTTP.text, "html.parser")
        # Find current price
        # div class='dDoNo ikb4Bb vk_bk gsrt gzfeS'
        text = soup.find("div", attrs={"class" : "BNeawe iBp4i AP7Wnd"}).find("div", attrs={"class" : "BNeawe iBp4i AP7Wnd"}).text
        return text
    def LoopPrice(self):
        # Choose the cryptocurrency
        crypt = 'bitcoin'
        # get the price
        price = self.GetPrice(crypt)
        # check price change
        if price != self.last_price:
            self.LblPrice.config(text=price)
            self.last_price = price
        time.sleep(3)
FrmMain()