import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands
from discord.utils import get
import asyncio
import random
from random import choice
import sqlite3
import datetime

client = commands.Bot(command_prefix="$")

x = datetime.datetime.now()
print(x)

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

sad_starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!"
]

roast = [
  "https://image.scoopwhoop.com/w620/s3.scoopwhoop.com/anj/wdkusd/56e77205-7614-4eac-a80f-4131113db56a.jpg.webp",
  "https://image.scoopwhoop.com/w620/s4.scoopwhoop.com/anj/wdkusd/1e0f91f0-dfa6-4634-bd45-ea48b3b2f67e.jpg.webp",
  "https://image.scoopwhoop.com/w620/s4.scoopwhoop.com/anj/wdkusd/c47ebb95-250c-449c-a2a2-ab60acb1e329.jpg.webp",
  "https://image.scoopwhoop.com/w620/s4.scoopwhoop.com/anj/wdkusd/5f3a1870-8451-491c-8ef0-e863af289e11.jpg.webp",
  "https://image.scoopwhoop.com/w620/s4.scoopwhoop.com/anj/wdkusd/573b1657-7a43-49fd-b2b4-695b9fa029a6.jpg.webp",
  "https://image.scoopwhoop.com/w620/s3.scoopwhoop.com/anj/wdkusd/4d4e09d5-3fcb-454f-a936-9cead91a4efb.jpg.webp",
  "https://image.scoopwhoop.com/w620/s4.scoopwhoop.com/anj/wdkusd/7f37bd7c-3622-466b-bfd1-7d4f86bcb21d.jpg.webp",
  "https://image.scoopwhoop.com/w620/s4.scoopwhoop.com/anj/wdkusd/ae60e1ef-8160-4e4e-bb63-11de62736671.jpg.webp",
  "https://image.scoopwhoop.com/w620/s3.scoopwhoop.com/anj/wdkusd/e5744625-9197-4ad3-86d4-cfe62fd8b89f.jpg.webp",
  "https://image.scoopwhoop.com/w620/s4.scoopwhoop.com/anj/wdkusd/f09cc7cb-bc82-49ed-9f1a-c3012bac5725.jpg.webp",
  "https://image.scoopwhoop.com/w620/s3.scoopwhoop.com/anj/jjs/92a59cac-0237-4c8f-8998-c19d5af04914.jpg.webp",
]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

ROLE = "Is a bot?"

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_joke():
  response = requests.get("http://api.icndb.com/jokes/random")
  json_data = json.loads(response.text)
  joke = json_data[0]['q'] + " -" + json_data[0]['a']
  return(joke)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="$help"))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    unverified = discord.utils.get(member.guild.roles, name="Is a bot?") #finds the unverified role in the guild
    await member.add_roles(unverified) #adds the unverified role to the member
    

def is_channel(ctx):
    return ctx.channel.id == 811292105891643442


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "「🙌」welcome-logs":
            await channel.send_message(f"""Welcome to the server {member.mention}""")

@client.command()
async def whoAmI(ctx):
  await ctx.send(f'You are {ctx.message.author}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if msg.startswith('$joke'):
    joke = get_joke()
    await message.channel.send(joke)

  if db["responding"]:
    options = sad_starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))
  
  if message.content.startswith('$application'):
    await message.channel.send('http://techy-code.github.io/application')
  
  if message.content.startswith("$roast"):
    await message.channel.send(random.choice(roast))
  
  if message.content.startswith('$invite'):
    await message.channel.send('https://discord.gg/kZmGPBtw5n')

  if message.content.startswith('$ping'):
    await message.channel.send(f'<@&808216317186408479> {message.content}')
  
  if message.content.startswith('$sugestion'):
    user = f"<@{message.author.id}>"
    channel = client.get_channel(818542458342211634)
    embed=discord.Embed(title="New Suggetion", color=0x00ff00, description=f'{message.content}')
    embed.add_field(name="User Suggested", value=user)
    await channel.send(embed=embed)
  
  if message.content.startswith('$startcfheads'):
    numbers = [1,2]
    choice = random.choice(numbers)
    conn = sqlite3.connect('score.db')
    print ("Opened database successfully");
    if choice == 1:
      conn.execute(f'''INSERT INTO SCORE (ID,NAME,GAME)
      VALUES ({x}, <@!{message.author.id}>,CoinFlip)''');
      conn.commit()
      print("Values Added")
      await message.channel.send('It was Heads! You won')
    else:
      await message.channel.send('It was Tails! You lost')
  
  if message.content.startswith('$startcftails'):
    numbers = [1,2]
    choice = random.choice(numbers)
    if choice == 2:
      await message.channel.send('It was Tails! You won')
    else:
      await message.channel.send('It was Heads! You lost')
  
  if message.content.startswith('$roll'):
    await message.channel.send(random.choice(numbers))
  
  if message.content.startswith('$website'):
    await message.channel.send('https://techy-code.github.io')

  if message.content.startswith('$members.admin'):
    embed=discord.Embed(title="Admins:", color=0x00ff00)
    embed.set_thumbnail(url="https://i.imgur.com/Pjl8Kqj.png")
    embed.add_field(name="Admins", value='''<@504296094793072641>
    <@554827199249907732> 
    ''', inline=False)
    embed.add_field(name="Moderators", value='''<@750877677103349850>''', inline=False)
    embed.set_footer(text="Looking for mods. Plz dm admins to take an interview!")
    await message.channel.send(embed=embed)
  
  if message.content.startswith('$members.company'):
    embed=discord.Embed(title="Company members", color=0x00ff00)
    embed.set_thumbnail(url="https://i.imgur.com/Pjl8Kqj.png")
    embed.add_field(name="CEO/Founder", value="<@504296094793072641>", inline=False)
    embed.add_field(name="COO", value="<@554827199249907732>", inline=False)
    await message.channel.send(embed=embed)
  
  if message.content.startswith('$help'):
    embed=discord.Embed(title="Help Comands", color=0x00ff00)
    embed.set_thumbnail(url="https://i.imgur.com/Pjl8Kqj.png")
    embed.add_field(name="Prefix", value="$", inline=False)
    embed.add_field(name="$help", value="Help command", inline=False)
    embed.add_field(name="$inspire", value="Get a quote", inline=False)
    embed.add_field(name="$roast", value="Want to roast someone, use this command", inline=False)
    embed.add_field(name="$members", value=".admin to get admins or .company to get company members", inline=False)
    embed.add_field(name="$website", value="Get the website for Techy", inline=False)
    await message.channel.send(embed=embed)

keep_alive()
client.run(os.getenv('TOKEN'))