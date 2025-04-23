import ast
import pandas
from discord.ext import commands

# Helper Function
def get_random_anime():
        try:
            # Read the CSV file
            data = pandas.read_csv("./data/animesv2.csv")

            while True:
                # Sample a random row
                random_row = data.sample(n=1)

                # Extract random row
                genres_list = ast.literal_eval(random_row.iloc[0]["genre"])  # evaluate string into list

                # Filtering method
                if "Hentai" in genres_list:
                    continue

                # Extract data
                anime_info = {
                    "title": random_row.iloc[0]["title"],
                    "description": random_row.iloc[0]["synopsis"],
                    "genre": ', '.join(genres_list),
                    "aired": random_row.iloc[0]["aired"],
                    "episodes": random_row.iloc[0]["episodes"],
                    "popularity": random_row.iloc[0]["popularity"],
                    "ranked": random_row.iloc[0]["ranked"],
                    "score": random_row.iloc[0]["score"],
                    "img_url": random_row.iloc[0]["img_url"],
                    "link": random_row.iloc[0]["link"]
                    }

                return anime_info

        except (FileNotFoundError, pd.errors.EmptyDataError, KeyError, ValueError) as e:
            return {"error": f"Error fetching anime data: {e}"}


class AnimeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # !animeshow command randomize show recommendations
    @commands.command(name="animeshow", help="Shows recommendation of a randomized anime show")
    async def anime_show(self, ctx):
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
    
    # !animeshowv2 command randomize show recommendations with more detail.
    @commands.command(name="animeshowv2", help="Shows recommendation of a randomized anime show")
    async def anime_show_v2(self, ctx):
        anime = get_random_anime()

        # Send the formatted message to the Discord channel
        message = f"Random Anime Show Recommendation:\n" \
                    f"Title: {anime['title']}\n" \
                    f"Description: {anime['description']}\n" \
                    f"Genre: {anime['genre']}\n" \
                    f"Aired: {anime['aired']}\n" \
                    f"Episodes: {anime['episodes']}\n" \
                    f"Popularity: {anime['popularity']}\n" \
                    f"Ranked: {anime['ranked']}\n" \
                    f"Score: {anime['score']}\n" \
                    f"Image URL: {anime['img_url']}\n" \
                    f"More Info: {anime['link']}"

        await ctx.send(message)


# Setup
async def setup(bot):
    await bot.add_cog(AnimeCog(bot))
