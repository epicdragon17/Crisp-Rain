import discord
from discord.ext import commands

bot + commands.Bot(command_prefix+'$')

@bot.event
async def on_ready ():
print('LOgged in as')
print(bot.user.name)
print('------')
@bot.command()
async def greet(ctx)
    await ctx.send(":smiley: :wave: Hello, there!")
    
bot.run('<YOUR_TOKEN_HERE>')
