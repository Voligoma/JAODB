import discord
import timeit

class MyClient(discord.Client):
	async def on_ready(self):
		print(f'Logged on as {self.user}!')

	async def on_message(self, message):
		prefix = "-"
		print(f'Message from {message.author}: {message.content}')
		if message.content == prefix + "help":
			#start = timeit.timeit()
			await message.channel.send("ayuda: para cambiar el prefijo el comando es: " + prefix + "prefix")
			#end = timeit.timeit()
			#totTime = end - start
			#print("el timepo de ejecucion fue de  " + str(totTime) + "S")
		else:
			command, *args = message.content.split(' ', 1)
			if command == prefix + "prefix":
				if args:
					prefix = args[0]
					await message.channel.send(f"Prefijo cambiado a: {prefix}")
				else:
					await message.channel.send("Faltan argumentos")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTA1Mjc1ODA4NTUzNTUzOTI1Mg.GKzulT.qldetCkzqz66V_iFDEcJf7uckdvAi0AGW4VIRY')