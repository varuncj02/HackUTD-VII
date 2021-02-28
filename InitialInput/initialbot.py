import discord
import os
import requests
import json
import datetime

client = discord.Client()
                 
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send("Hello World!")

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  


  #if message.content.startswith('!startofweek'):
   # input1 = get_schedule()

    #await message.channel.send("Have to Fill in with something")


@client.event
async def on_message(message):
    if message.content.startswith('!startofweek'):
        channel = message.channel
        await channel.send('Enter Day of Exam (If none enter zero): ')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        examDate = await client.wait_for('message', check=check)
        await message.channel.send(examDate)



def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


def get_schedule():
  day_of_week = []
  valid = 1
  while valid != 0:
    dayInput = input("Enter Day of Exam (If none enter zero).")
    dayInput = datetime.datetime.strptime(dayInput,"%m/%d/%Y").date()
    print('Datetime is ', dayInput)
  return dayInput

client.run(('tokens'))

