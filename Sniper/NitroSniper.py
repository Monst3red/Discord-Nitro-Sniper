import discord
from discord.ext import commands
import os
from colorama import Fore, init
import ctypes
import requests
import json
from datetime import datetime
init()

ctypes.windll.kernel32.SetConsoleTitleW("[>_Mσnsτεгεɗ#0069] Nitro Sniper")
client = commands.Bot(command_prefix = "!", self_bot = True)


token = input("> Token: ")

@client.event
async def on_ready():
    print()
    os.system("cls")
    print(Fore.RED + f"""
    \t\t\t\t  ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███  
    \t\t\t\t▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
    \t\t\t\t░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
    \t\t\t\t  ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
    \t\t\t\t▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
    \t\t\t\t▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
    \t\t\t\t░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
    \t\t\t\t░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ 
    \t\t\t\t      ░           ░  ░              ░  ░   ░                                            
    """)
    print(Fore.RED + "        \t\t\t\t\tUsername: " + Fore.RESET + client.user.name + "#" + Fore.RESET + client.user.discriminator)
    print(Fore.RED + "        \t\t\t\t\tID: " + Fore.RESET + str(client.user.id))
    print()

@client.event
async def on_message(message):
    if "discord.gift/" in message.content:
        code = message.content.split('discord.gift/')[1].split(' ')[0]
        payload = {"channel_id": str(message.channel.id)}
        headers = {"authorization": token, "content-type": "application/json"}
        r = requests.post(f"https://discord.com/api/v8/entitlements/gift-codes/{code}/redeem", headers=headers, data=json.dumps(payload))

        if r.status_code == 200:
            print(Fore.GREEN + "Successfully Claimed:" + Fore.RESET + f"https://discord.gift/{code} | " + str(datetime.now()))
        else:
            print(Fore.RED + "Unknown gift: " + Fore.RESET + f"https://discord.gift/{code} | " + str(datetime.now()))

client.run(token, bot = False)