import discord
from dotenv import load_dotenv
from generator import *

load_dotenv()
TOKEN = 'MTEwNjMzOTk4OTA2NDc5NDEzMg.GTfhgm.SqSuwhfe8FpTHipNiAvKsY1gvrBVXG13uN4bTQ'
GUILD = os.getenv('Itineraro')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

plans = []

@client.event
async def on_ready():
    guild_count = 0
    for guild in client.guilds:
        guild_count = guild_count + 1
    print("Itineraro is in " + str(guild_count) + " guilds.")

client.run(TOKEN)