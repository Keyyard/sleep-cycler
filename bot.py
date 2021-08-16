import datetime
import discord
token = "ODc2OTY1MTc3NjA0NTk1NzYy.YRrvdw.b9kIlwD08BkLPYeRK6wXRFi7aCk"
bot = commands.Bot(command_prefix=".",intents=discord.Intents.all())
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    async def on_message(self, message):
        
        if message.author.id == self.user.id:
            return
            
        if message.content.startswith('im sleepy'):
            await message.reply("Hi there, you should set your alarm at: \n", datetime.datetime.now()+ datetime.timedelta(minutes=15)+ datetime.timedelta(minutes=90) datetime.datetime.now()+ datetime.timedelta(minutes=15)+ datetime.timedelta(minutes=180), "\n",datetime.datetime.now()+ datetime.timedelta(minutes=15)+ datetime.timedelta(minutes=270), "\n",datetime.datetime.now()+ datetime.timedelta(minutes=15)+ datetime.timedelta(minutes=360), "\n",datetime.datetime.now()+ datetime.timedelta(minutes=15)+ datetime.timedelta(minutes=450), "\n",datetime.datetime.now()+ datetime.timedelta(minutes=15)+ datetime.timedelta(minutes=540), "\n", mention_author=True)
client = MyClient()
client.run('token')
