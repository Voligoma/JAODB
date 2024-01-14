import discord
import timeit

class MyClient(discord.Client):
	async def on_ready(self):
		print(f'Logged on as {self.user}!')

	async def on_message(self, message):
		print(f'Message from {message.author}: {message.content}')
		if message.content == "hello":
			#start = timeit.timeit()
			await message.channel.send("World")
			#end = timeit.timeit()
			#totTime = end - start
			#print("el timepo de ejecucion fue de  " + str(totTime) + "S")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTA1Mjc1ODA4NTUzNTUzOTI1Mg.GKzulT.qldetCkzqz66V_iFDEcJf7uckdvAi0AGW4VIRY')