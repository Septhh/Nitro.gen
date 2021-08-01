import random, string
import webbrowser
import time
import requests

print("""

Lagi loading
loading bergantung pada internet

■□□□□

■■□□□

■■■□□

■■■■□

■■■■■

Lagi running⊙

opening property Protocol.open.discordapp

opening ProcessLookupError.ProxyType

made by: Asep(th)
""")

num=input('tolong tunggu hingga generate selesai,Berapa banyak yang mau generate: ')

f=open("Nitro Codes.txt", "w", encoding='utf-8')

print("Tunggu sayang tolong untuk di lihat seksama jika jackpot dapat valid code!")

for n in range(int(num)):
    y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    f.write('https://discord.gift/')
    f.write(y)
    f.write("\n")

f.close()

#checker#

with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitelemnts/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Selamat kamu dapat nitro | {} ".format(line.strip("\n")))
            break
        else:
            print(" Invalid code | {}".format(line.strip("\n")))
input("Sudah done kak klik enter 5x atau tombol pojok kanan di android.")
input("4")
input("3")
input("2")
input("Jangan lupa beli di peach shop lagi, pencet sekali lagi untuk close")
print("""
closing Protocol.end.discordapp

closing Runend.ProcessLookupError.ProxyType""")