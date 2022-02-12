import random, discord

token = input("Enter Token: ")

with open("pack.txt", "r") as x:
    options = x.readlines()

class PackBot(discord.Client):
    async def on_ready(self):
        print('logged in as {0}'.format(self.user))
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
