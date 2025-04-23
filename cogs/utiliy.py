from discord.ext import commands

# Tip Calculator
class UtilityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # !tip command. Tip Calculator
    @commands.command(name="tip", help="Add bill and tip. Split amount is optional")
    async def tip_calculator(self, ctx, bill: float, tip: float, split: int = 1):
        # input validations
        if bill <= 0 or tip < 0 or split <= 0:
            await ctx.send("Invalid input values. Please provide positive values for bill, tip, and split.")
            return
        # calculations
        tip_amount = bill * (tip / 100)
        # results
        total_amount = round(bill + tip_amount, 2)
        split_amount = round(total_amount / split, 2)

        # response
        await ctx.send(f"Bill Amount: {bill:.2f}. Tip Percentage: {tip:.2f}%. Total Amount: {total_amount:.2f}")
        if split_amount > 1:
            await ctx.send(f"{split} people is paying ${split_amount:.2f} each")


# Setup
async def setup(bot):
    await bot.add_cog(UtilityCog(bot))