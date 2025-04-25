from discord.ext import commands
import discord

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="help")
    async def help(self, ctx):
        embed = discord.Embed(title="Bot Commands", color=discord.Color.blurple())
        embed.add_field(name="🔧 !prefix(W.I.P)", value="**Inputs**: [Prefix]\r\n**Current Prefix**: !.\r\n**Description**: Change the prefix for the bot", inline=False)
        embed.add_field(name="🗬 !quote", value="**Description**: Get a random inspirational quote", inline=False)
        embed.add_field(name="📺 !animeshow / !animeshowv2", value="**Description**: Get a random anime show recommendations", inline=False)
        embed.add_field(name="🫙 !tip", value="**Inputs**: [Bill] [Tip Percentage] [Split Amount(Optional)]\r\n**Description**: Calculate tips and split bills.", inline=False)
        embed.add_field(name="🧮 !add / !subtract / !multiply / !divide", value="**Inputs**: [Number1] [Number2] [Number3]... And so on.\r\n**Description**: Basic calculator commands.", inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))