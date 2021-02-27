import discord
import os
import requests
import json

client = discord.Client()
                 
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

client.run(os.getenv('ODE1MzQ4MjcxNjk4MjgwNDQ4.YDrGQA.LgFBNLym7yuExLvCLwlnyAc1REY'))