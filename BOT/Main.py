import discord
import timeit
from discord import app_commands
from discord.ext import commands
from config import TOKEN

class MyClient(discord.Client):
	prefix = "-"
	async def on_ready(self):
		print(f'Logged on as {self.user}!')

	async def on_message(self, message):
		print(f'Message from {message.author}: {message.content}')
		if message.content == self.prefix + "help":
			#start = timeit.timeit()
			await message.channel.send("ayuda: para cambiar el prefijo el comando es: " + self.prefix + "prefix")
			#end = timeit.timeit()
			#totTime = end - start
			#print("el timepo de ejecucion fue de  " + str(totTime) + "S")
		else:
			command, *args = message.content.split(' ', 1)
			if command == self.prefix + "prefix":
				if args:
					MyClient.prefix = args[0]
					await message.channel.send(f"Prefijo cambiado a: {MyClient.prefix}")
				else:
					await message.channel.send("Faltan argumentos")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('TOKEN')