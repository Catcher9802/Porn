import discord
import os
from discord.ext import commands

token = input("โทเค็นบอท : ")
channel = input("ไอดีห้อง : ")

bot = commands.Bot(command_prefix="/")
@bot.event
async def on_ready():
	print(bot.user)
	os.system("clear")
	print("คำสั่ง /gif")
	
@bot.command()
async def gif(ctx):
	if (str(ctx.message.channel.id) == f"{channel}"):
		data = ['https://wetgif.com/wp-content/uploads/gifs-girls-masturbate-81.gif','https://wetgif.com/wp-content/uploads/gifs-girls-masturbate-96.gif','https://wetgif.com/wp-content/uploads/gif-passionate-sex-84.gif','https://wetgif.com/wp-content/uploads/2020/12/slender-girl-porno-8.gif','https://wetgif.com/wp-content/uploads/gifs-girls-masturbate-53.gif','https://wetgif.com/wp-content/uploads/2021/02/morning-sex-11.gif','https://wetgif.com/wp-content/uploads/2021/02/morning-sex-92.gif','https://wetgif.com/wp-content/uploads/2020/10/penisinvagina-69.gif','https://wetgif.com/wp-content/uploads/gif-passionate-sex-81.gif','https://wetgif.com/wp-content/uploads/gentle-sex-57.gif','https://wetgif.com/wp-content/uploads/mouth-cumshot-sperm-3.gif','https://wetgif.com/wp-content/uploads/gifs-girls-masturbate-91.gif','https://wetgif.com/wp-content/uploads/big-tits-45.gif','https://wetgif.com/wp-content/uploads/2021/02/morning-sex-76.gif','https://wetgif.com/wp-content/uploads/gentle-sex-10.gif','https://wetgif.com/wp-content/uploads/gentle-sex-60.gif','https://wetgif.com/wp-content/uploads/porno-gifs-double-penetration-86.gif','https://wetgif.com/wp-content/uploads/gentle-sex-3.gif']
		show = str(random.choice(data))
		await ctx.channel.send(show)
		
bot.run(token)
