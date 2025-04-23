from discord.ext import commands
import requests
import json

class QuoteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # command
    @commands.command(name="quote", help="Get a random inspirational quote")
    async def get_quote(self, ctx):
        try:
            response = requests.get("https://zenquotes.io/api/random")
            response.raise_for_status()  # Raises HTTPError for bad status codes
            json_data = json.loads(response.text)
            random_quote = json_data[0]['q'] + " -" + json_data[0]['a']
        
        except requests.exceptions.HTTPError as e:
            return f"HTTP error: {e}"

        await ctx.send(random_quote)

# Setup
async def setup(bot):
    await bot.add_cog(QuoteCog(bot))
