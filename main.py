from discord.ext import commands
import discord
from os import getenv
from dotenv import load_dotenv
import logging
import requests
import json
import ast
import pandas

# Set the logging level
logging.basicConfig(level=logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# .env
load_dotenv()

# Intents
intents = discord.Intents.default()
intents.message_content = True

# bot instances
bot = commands.Bot(command_prefix="!", intents=intents.all())


# second server
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel_id = getenv("CHANNEL_ID")

    # Attempt to convert channel_id to integer
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


def getquote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


@bot.command(name="quote", help="Get a random inspirational quote")
async def get_quote(ctx):
    random_quote = getquote()
    await ctx.send(random_quote)


# !animeshow command randomize show recommendations

@bot.command(name="animeshow", help="Shows recommendation of a randomized anime show")
async def anime_show(ctx):
    # Read the CSV file and extract the desired columns
    data = pandas.read_csv("./data/animes.csv")
    extracted_column = data[["title", "desc"]]

    # Sample a random row
    random_row = extracted_column.sample(n=1)

    # Extract the title and description from the random row
    title = random_row.iloc[0]["title"]
    desc = random_row.iloc[0]["desc"]

    # Send the formatted message to the Discord channel
    await ctx.send(f"Random Anime Show Recommendation:\nTitle: {title}\nDescription: {desc}")


@bot.command(name="animeshowv2", help="Shows recommendation of a randomized anime show")
async def anime_show(ctx):
    while True:
        # Read the CSV file and extract the desired columns
        data = pandas.read_csv("./data/animesv2.csv")
        extracted_column = data[["title", "synopsis", "genre", "aired", "episodes", "popularity", "ranked", "score",
                                 "img_url", "link"]]

        # Sample a random row
        random_row = extracted_column.sample(n=1)

        # Extract information from the random row and convert genres to a list using ast
        genres_list = ast.literal_eval(random_row.iloc[0]["genre"])
        genre = ', '.join(genres_list)  # Join the list back to a string for display
        title = random_row.iloc[0]["title"]
        desc = random_row.iloc[0]["synopsis"]
        aired = random_row.iloc[0]["aired"]
        episodes = random_row.iloc[0]["episodes"]
        popularity = random_row.iloc[0]["popularity"]
        ranked = random_row.iloc[0]["ranked"]
        score = random_row.iloc[0]["score"]
        img_url = random_row.iloc[0]["img_url"]
        link = random_row.iloc[0]["link"]

        # Check if "Hentai" is not in the genres list
        if "Hentai" not in genres_list:
            # Send the formatted message to the Discord channel
            message = f"Random Anime Show Recommendation:\n" \
                      f"Title: {title}\n" \
                      f"Description: {desc}\n" \
                      f"Genre: {genre}\n" \
                      f"Aired: {aired}\n" \
                      f"Episodes: {episodes}\n" \
                      f"Popularity: {popularity}\n" \
                      f"Ranked: {ranked}\n" \
                      f"Score: {score}\n" \
                      f"Image URL: {img_url}\n" \
                      f"More Info: {link}"
            await ctx.send(message)
            break  # Exit the loop once a recommendation is sent


# !tip command. Tip Calculator
@bot.command(name="tip", help="Add bill and tip. Split amount is optional")
async def tip_calculator(ctx, bill: float, tip: float, split: int = 1):
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


# !add command. Addition
@bot.command(name="add", help="input as much numbers you want separated by spaces to add them")
async def add(ctx, *arr):
    result = 0
    for number in arr:
        result += int(number)
    await ctx.send(f"Result: {result}")


# !subtract command. Subtraction
@bot.command(name="subtract", help="input as much numbers you want separated by spaces to subtract")
async def subtract(ctx, *arr):
    result = int(arr[0])
    for number in arr[1:]:
        result -= int(number)
    await ctx.send(f"Result: {result}")


# !multiply command. multiplication
@bot.command(name="multiply", help="input as much numbers you want separated by spaces to multiply")
async def multiply(ctx, *arr):
    result = 1  # Initialize with 1
    for number in arr:
        result *= int(number)
    await ctx.send(f"Result: {result}")


# !divide command. Division
@bot.command(name="divide", help="input as much numbers you want separated by spaces to divide")
async def divide(ctx, *arr):
    result = 1  # Initialize with a non-zero value
    for number in arr:
        if int(number) == 0:
            await ctx.send("Cannot divide by zero!")
            return
        result /= int(number)
    await ctx.send(f"Result: {result}")


# handle errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.send(f"Error: {error}")


# runs the bot
bot.run(getenv('DISCORD_TOKEN'), log_handler=handler)
