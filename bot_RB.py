import discord
from discord.ext import commands
import requests
import re

with open('Bot_token.txt', 'r') as f:
    token = f.read()
with open('RB_API_key.txt', 'r') as f:
    RB_api_key = f.read()

# Enable necessary intents
intents = discord.Intents.default()
intents.message_content = True  # Enable Message Content Intent

# Initialize the bot client with commands.Bot
bot = commands.Bot(command_prefix='bot ', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Event: Print received messages
@bot.event
async def on_message(message):
    print(f"Received a message: {message.content}")
    await bot.process_commands(message)

# Command: Respond with "Hello!"
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Command: Respond with "Pong!"
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Echo the user's message
@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

# Command to search for a LEGO set on Rebrickable
@bot.command()
async def rebrickable(ctx, set_number: int):
    api_key = RB_api_key
    set_number = f"{set_number}-1"
    url = f'https://rebrickable.com/api/v3/lego/sets/{set_number}/'
    
    headers = {
        'Authorization': f'key {api_key}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if response.status_code == 200:
        # Extract information from the response
        set_name = data['name']
        set_link = data['set_url']
        set_year = data['year']
        message = f"{set_name} ({set_number}) from {set_year}, link: {set_link}"
    else:
        message = f"Error retrieving data from Rebrickable API: {response.status_code}"
    
    await ctx.send(message)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Use regex to find a 4 or 5 digit number in the message
    match = re.search(r'\b\d{4,5}\b', message.content)
    if match and match.group() not in ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', 
                               '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']:
        set_number = int(match.group(0))
        ctx = await bot.get_context(message)
        await rebrickable(ctx, set_number)
        
    await bot.process_commands(message)

# Run the bot with your token
bot.run(token)