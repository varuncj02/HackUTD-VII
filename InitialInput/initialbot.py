import discord
import os
import requests
import json
import datetime

class Scheduler:
  def __init__(self, date, activity_type ):
    self.date = date
    self.activity_type = activity_type

schedules_list = []

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
  
  if message.content.startswith('$today'):
        #channel = message.channel
        #val = message.content
        #val = val[val.find(',')+1:]
        #val = val.strip()
        #val = val.isDigit()
        print(message.content)
        #day_tuple = check_match_day(message.content)
        # output = 'Your Nearest Activity is ', schedules_list[0][1]
        out = schedules_list[0][1]
        await message.channel.send('The Nearest Activity is {}'.format(out))
  if message.content.startswith('$entry'):
      channel = message.channel
      # await channel.send('Enter Day of Exam (If none enter zero): ')
      val = message.content
      newval = val[6:val.find(',')]
      assessment = val[val.find(',')+1:] 
      def check(m):
        return m.content == 'add' and m.channel == channel
      print(val)
      examDate = await client.wait_for('message', check=check)
      sched = Scheduler(newval, assessment) 
      temp_list = [sched.date, sched.activity_type]
      schedules_list.append(temp_list)
      output_list = [newval, assessment]
      await message.channel.send(schedules_list)
  


  #if message.content.startswith('!startofweek'):
   # input1 = get_schedule()

    #await message.channel.send("Have to Fill in with something")

'''
@client.event
async def on_message(message):
    if message.content.startswith('!entry'):
        channel = message.channel
        # await channel.send('Enter Day of Exam (If none enter zero): ')
        val = message.content
        newval = val[6:val.find(',')]
        assessment = val[val.find(',')+1:] 
        def check(m):
            return m.content == 'Append' and m.channel == channel
        print(val)
        examDate = await client.wait_for('message', check=check)
        sched = Scheduler(newval, assessment) 
        temp_list = [sched.date, sched.activity_type]
        schedules_list.append(temp_list)
        output_list = [newval, assessment]
        await message.channel.send(schedules_list)


@client.event
async def on_message(message):
    if message.content.startswith('!today'):
        #channel2 = message.channel
        val = message.content
        val = val[val.find(',')+1:]
        val = val.strip()
        val = val.isDigit()
       # day_tuple = check_match_day(val)
        await message.channel.send("Hello")

        # await channel.send('Enter Day of Exam (If none enter zero): ')
        

        
        val = message.content
        newval = val[13:val.find(',')]
        assessment = val[val.find(',')+1:] 
        def check(m):
            return m.content == 'Append' and m.channel == channel
        print(val)
        examDate = await client.wait_for('message', check=check)
        sched = Scheduler(datetime.datetime.strptime(newval,"%m/%d/%Y").date(), assessment) 
        temp_list = [sched.date, sched.activity_type]
        schedules_list.append(temp_list)
        output_list = [newval, assessment]
        await message.channel.send(schedules_list)'''


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


def check_match_day(day):
  day = day[day.find(',')+1:]
  day = day.strip()
  day = day.isDigit()
  days_list = []
  for schedule in schedules_list:
    compareDate = schedule.date[schedule.date.find('\\'):schedule.date.find('\\')+2]
    if day == int(compareDate):
      days_list.append(schedule)
  day_tup = tuple(days_list)
  return day_tup


def get_schedule():
  day_of_week = []
  valid = 1
  while valid != 0:
    dayInput = input("Enter Day of Exam (If none enter zero).")
    dayInput = datetime.datetime.strptime(dayInput,"%m/%d/%Y").date()
    print('Datetime is ', dayInput)
  return dayInput

client.run(("ODE1MzQ4MjcxNjk4MjgwNDQ4.YDrGQA.mVweAv6PGHavxRzvib_taTNGU3c"))

