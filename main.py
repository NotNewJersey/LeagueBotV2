import discord
from discord.ext import commands
from my_commands import MyCommands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Load the MyCommands cog from my_commands.py
bot.add_cog(MyCommands(bot))

@bot.event
async def on_ready():
    print(f'Bot is ready and connected as {bot.user.name}')

bot.run('blank')
