from discord.ext import commands
from os import getenv

class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Bot intro
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'We have logged in as {bot.user}')
        
        # Attempt to convert channel_id to integer
        channel_id = getenv("CHANNEL_ID")
        try:
            channel_id = int(channel_id)
        except ValueError:
            print("Error: channel_id is not a valid integer.")
            return

        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send("Hello! Bot is ready!")
        else:
            print(f"Error: Could not find the channel with ID {channel_id}")

    # handle errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            await ctx.send(f"Error: {error}")

async def setup(bot):
    await bot.add_cog(EventsCog(bot))
