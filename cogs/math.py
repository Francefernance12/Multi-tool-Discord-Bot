from discord.ext import commands

class MathCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # !add command. Addition
    @commands.command(name="add", help="input as much numbers you want separated by spaces to add them")
    async def add(self, ctx, *arr):
        try:
            result = 0
            for number in arr:
                result += int(number)
            await ctx.send(f"Result: {result}")
        except ValueError:
            await ctx.send("Please provide valid numbers.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")


    # !subtract command. Subtraction
    @commands.command(name="subtract", help="input as much numbers you want separated by spaces to subtract")
    async def subtract(self, ctx, *arr):
        try:
            result = int(arr[0])
            for number in arr[1:]:
                result -= int(number)
            await ctx.send(f"Result: {result}")
        except ValueError:
            await ctx.send("Please provide valid numbers.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")


    # !multiply command. multiplication
    @commands.command(name="multiply", help="input as much numbers you want separated by spaces to multiply")
    async def multiply(self, ctx, *arr):
        try:
            result = 1  # Initialize with 1
            for number in arr:
                result *= int(number)
            await ctx.send(f"Result: {result}")
        except ValueError:
            await ctx.send("Please provide valid numbers.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    # !divide command. Division
    @commands.command(name="divide", help="input as much numbers you want separated by spaces to divide")
    async def divide(self, ctx, *arr):
        try:
            numbers = [float(num) for num in arr]  # Convert inputs to floats
            result = numbers[0]  # Start with the first number
            
            for num in numbers[1:]:
                if num == 0:
                    await ctx.send("Cannot divide by zero!")
                    return
                result /= num

            await ctx.send(f"Result: {result}")
        except ValueError:
            await ctx.send("Please provide valid numbers.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

# Setup
async def setup(bot):
    await bot.add_cog(MathCog(bot))
