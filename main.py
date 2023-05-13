

# https://discord.com/api/oauth2/authorize?client_id=1106339989064794132&permissions=274877974528&scope=bot



import discord
from dotenv import load_dotenv
from generator import *

load_dotenv()
TOKEN = 'TOKEN'
GUILD = os.getenv('Itineraro')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

plans = []

@client.event
async def on_ready():
    print('Itineraro is ready ;)')
    guild_count = 0
    for guild in client.guilds:
        guild_count = guild_count + 1
    print("Itineraro is in " + str(guild_count) + " guilds.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '&itineraro':
        await message.reply("Hey! What's Up! \nIf you would like help with commands just type - ' **&help** '")

    if message.content == '&help':
        await message.channel.send("Understood, I'm here to help \n\n I’m Itineraro and I make trip planning with friends a breeze."+
                            " Just let me know your interests, preferences, travel dates, destinations, and must-see sights."+
                            " I’ll create a personalized itinerary for you that even takes into account any dietary restrictions or allergies"+
                             "\n\n\n To Start a new trip just type - ' **&new_trip** '")

    if message.content == '&end':
        await message.reply("Understood! I'll always be here to help out!")

    if message.content == '&new_trip':
        await message.channel.send("🛩️ Ready to plan? (You can always exit with **&end**) \n\n **Make sure you're clear for the best experience possible**\n"
                                   +"First, enter where you would like to be going, when, and for how many?\n\n"
                                   +"Then,your interest and hobbies, what do you like to do when you travel and when you're at home \n\n"
                                    +"Next, any dietary restrictions you might have, be as broad or specific as you would like \n\n"
                                     +"So, what are some things you definitely have to do while you're there, feel free to include links and be as specific as you would like\n\n"
                                      +"You're so close to your trip!\n\n Lastly, How busy do you want to be while there (If you want to be more busy then we will plan more for you)"
                                       +" \n\nOnce your message is over, just type **&finish**")
        while message.content != '&done':
            msg = await client.wait_for("message")
            plans.append(msg.content+'. ')

    if message.content == '&finish':
        await message.channel.send("All set, your personalized itinerary is coming..")
        await message.channel.send("Loading...")
        final_plans = convo(''.join(plans))
        await message.channel.send(final_plans[:2000])
        plans.clear()

client.run(TOKEN)
