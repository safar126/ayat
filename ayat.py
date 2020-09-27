#coding=utf-8
import requests as r
from bs4 import BeautifulSoup as soup

url = "https://tafsirweb.com/#gsc.tab=0"
def qur():
	res = r.get(url)
	data = []
	angka = -1
	sop = soup(res.text, "html.parser")
	for x in sop.find_all("a"):
		angka += 1
		print(str([angka]),x.text)
		data.append([x.text,x["href"]])
	inp = int(input("Pilih No Ayat : "))
	print(data[inp][1])
	res2 = r.get(data[inp][1])
	sop2 = soup(res2.text, "html.parser")
	angka = 0
	for x2 in sop2.find_all("p", class_="text_Latin"):
		angka += 1
		print(str([angka]),x2.text)
	balik = input("Tekan Enter untuk kembali...")
	qur()



qur()