import sys, time, os

from pystyle import Colors, Colorate

def slow_write(text):
    for x in text: print('' + x, end="");sys.stdout.flush();time.sleep(0.005)

slow_write("\u001b[38;5;159m-> Token: ")
token = input()

import random, discord

with open("pack.txt", "r") as x:
    options = x.readlines()


slow_write("\u001b[38;5;156m-> Loading..")


os.system("cls")
os.system(f'title [PACKER]')
os.system(f'mode 30,15')


class PackBot(discord.Client):
    async def on_ready(self):
        slow_write('logged in as {0}'.format(self.user))
        self.packing = False
    
    async def on_message(self, message):
        if message.author == self.user and ".pack" in message.content:
            self.packing = True
            while self.packing == True:
                pack = random.choice(options)
                await message.channel.send(f"<@{message.mentions[0].id}> {pack} ")
        
        if message.author == self.user and ".stop" in message.content:
            self.packing = False

client = PackBot()

client.run(token, bot=False)
