import discord
from discord.ext import commands, bridge

from dbotbase import BotConfig
from arcacog.logs import *

info("Starting application...")

bot_config = BotConfig(name="Arca", config_files=["bot_config.yaml"])

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=bot_config.log_level)

# intents = discord.Intents.default()
# intents.message_content = True
# intents.members = True
intents = discord.Intents(messages=True, members=True, guilds=True)
bot = bridge.Bot(command_prefix=bot_config.prefix, intents=intents)
formatter = commands.HelpCommand(show_check_failure=False)

extensions = []

with open("cog_list.txt", "r") as f:
    for line in f.readlines():
        extensions.append(f"cogs.{line.strip()}.cog")


@bot.event
async def on_ready():
    info(f'\n\nLogged in as : {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game(
                                  name=f'Making lists, checking them twice | {bot_config.prefix}'))
    info(f'Successfully logged in and booted...!\n')


if __name__ == '__main__':
    info("Connecting to Discord...")
    for ext in extensions:
        bot.load_extension(ext)
    bot.run(bot_config.token)
