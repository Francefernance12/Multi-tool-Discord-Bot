from discord.ext import commands


class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Bot intro
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'We have logged in as {self.bot.user}')  

        for guild in self.bot.guilds:  # Loop through servers
            for channel in guild.text_channels:  # Loop through text channels
                if channel.permissions_for(guild.me).send_messages:
                    await channel.send("Hello! I'm online and ready to go! 🎉")
                    break  # Only send to the first available channel


    # handle errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            await ctx.send(f"Error: {error}")

async def setup(bot):
    await bot.add_cog(EventsCog(bot))
