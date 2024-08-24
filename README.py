import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def atık(ctx):
    await ctx.send("meyve atıkları, atık yağlar, kağıt ve cam gibi geri dönüştürülebilen atıklar")
@bot.command()
async def çözüm(ctx):
    await ctx.send("1- Evdeki atıkları belirle  2- En çok hangi tür atığın olduğunu bul  3- Her atığı kendi içinde gruplandırarak farklı poşetlere koy  4- Geri dönüştürmek istediğin atığın ismini yaz")
@bot.command()
async def meyve (ctx):
    await ctx.send("Meyve atıkları geri dönüştürülemez, sokaktaki hayvanlara verebilirsin!")   
@bot.command()
async def cam (ctx):
    await ctx.send("Cam geri dönüştürülebilir. Cam için ayırdığın poşeti sokaktaki cam için olan geri dönüşüm kutusuna koyabilirsin.")
@bot.command()
async def yağ (ctx): 
    await ctx.send("Atık yağlar doğayı kirlettiğinden ve borularını tıkadığı için lavaboya ve toprağa dökülmesi oldukça zararlıdır. Bu sebeple yağları bir torbada biriktirip sonrasında çöpe atmak daha yararlıdır.")

bot.run("your token")
