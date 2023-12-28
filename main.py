import discord
from ticketsystem import TicketSystem
from discord.ext import commands
import logging
import logging.handlers
import conf




if __name__ == "__main__":
    bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=discord.Intents.all())
    
    # logger = logging.getLogger('[BOT-INFO]')
    # logger.setLevel(logging.DEBUG)
    # logging.getLogger('discord.http').setLevel(logging.INFO)

    # handler = logging.handlers.RotatingFileHandler(
    #     filename='discord.log',
    #     encoding='utf-8',
    #     maxBytes=32 * 1024 * 1024,  # 32 MiB
    #     backupCount=5,  # Rotate through 5 files
    # )
    # dt_fmt = '%Y-%m-%d %H:%M:%S'
    # formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)



    @bot.event
    async def on_ready():
        # logger.info(f"User: {bot.user} ID:{bot.user.id}")
        print(f"Bot is ready for use!")



    @bot.command()
    async def menu(ctx):
        view = TicketSystem(bot)
        await ctx.reply(view=view)


    bot.run(conf.TOKEN)





