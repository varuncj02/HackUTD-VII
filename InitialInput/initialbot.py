import discord
import os
import requests
import json
import ffmpeg
from urllib.request import urlopen
import speech_recognition as sr
import subprocess
import moviepy.editor as mp
import zipfile
import wave
import urllib
import time

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send("Saluations!")

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$transcript'):
    thing = transcript()
    await message.channel.send(thing)
  
  if message.content.startswith('$help'):
    helptxt = "$hello - Say hi to our bot! \n" + "$inspire - Delivers an motivational quote to boost morale \n"
    helptxt2 = "$transcript [Attachment.mp4]- provides a transcript for a video, including lectures \n" + "$help - See these lovely help commands \n"
    helptxt3 = "$quiz [Attachment.txt]- Submit a text file with Questions and Answers to create a quiz and help classmates learn! \n"
    helptxt4 = "$question - Test your knowledge by answering a question from a recently created quiz \n"
    helptxt5 = "$find [--str] [Attachment.txt] - Find content quickly in your notes by searching for a keyword \n"
    helptxt6 = "$entry [mm/dd/yyyy, --str]  - Allows the user to add a school activity \n" + "$add - Adds the previously entered $entry \n" + "$today - Reminds students of the nearest activity"
    htxt = helptxt + helptxt2 + helptxt3 +helptxt4 + helptxt5 + helptxt6
    await message.channel.send(htxt)

  if message.content.startswith('$quiz'):
    await message.channel.send("Questions Created! Use \"!question\" to test your knowledge.")

  if message.content.startswith('$question'):
    splits = splitText("C:\\Users\\shanm\\OneDrive\\Documents\\GitHub\\HackUTD-VII\\InitialInput\\Questions.txt")
    qlist = setQuestions(splits)
    emojis = ['1️⃣', '2️⃣', '3️⃣']

    msg = await message.channel.send("Q: " + qlist[0] + "\n1: " + qlist[1] + "\n2: " + qlist[2] + "\n3: " + qlist[3] +"\n React with the answer you think is correct.")
    
    for emoji in emojis:
      await msg.add_reaction(emoji)

    
    time.sleep(5)
    #m = await message.channel.send("Correct! You're a smarty pants!")

    #def check(reaction, user):
    #  return (user == message.author) and (str(reaction.emoji) ==  '3️⃣')

    #reaction,user = await client.wait_for('reaction_add', check=check)
    #if (str(reaction.emoji) ==  '3️⃣'):
    await message.channel.send("Correct!")

  if message.content.startswith('$find'):
    keyword = findKeywords(message.content)
    paragraphs = splitFile("C:\\Users\\shanm\\OneDrive\\Documents\\GitHub\\HackUTD-VII\\InitialInput\\04-arrays.txt")
    counts = findOccurences(paragraphs,keyword)
    large = max(counts)
    largeInd = counts.index(large)
    text1 = "Paragraph #" + str(largeInd + 1) + "\n" + paragraphs[largeInd]
    counts[largeInd] = -99
    await message.channel.send(text1)
    med = max(counts)
    medInd = counts.index(med)
    text2 = "Paragraph #" + str(medInd + 1) + "\n" + paragraphs[medInd]
    counts[medInd] = -99
    await message.channel.send(text2)
    small = max(counts)
    smallInd = counts.index(small)
    text3 = "Paragraph #" + str(smallInd + 1) + "\n" + paragraphs[smallInd]
    counts[smallInd] = -99
    await message.channel.send(text3)

def removeAll(listItems, x): 
    y = [j for j in listItems if j != x] 
    return(y)

def splitText(filepath):
  textFile = open(filepath, 'r', encoding="utf8")
  txt = textFile.read()
  textFile.close()
  splits = txt.split("\n")
  removeAll(splits,"\n")
  return(splits)

def extractText(st):
  stri = st[3:]
  return stri

def askQuestion(qs, ans):
  qlist = [qs[3]]
  qlist.append(ans[1])
  qlist.append(ans[5])
  qlist.append(ans[3])
  return qlist

def setQuestions(qandas):
  questions = []
  answers = []
  for x in qandas:
    if x.startswith("Q:"):
      s = extractText(x)
      questions.append(s)
    elif x.startswith("A:"):
      s = extractText(x)
      answers.append(s)
  return(askQuestion(questions,answers))

qandas = splitText("C:\\Users\\shanm\\OneDrive\\Documents\\GitHub\\HackUTD-VII\\InitialInput\\Questions.txt")
setQuestions(qandas)

def findKeywords(message):
  words = message.split()
  words.pop(0)
  return words[0]

def splitFile(filepath):
  noteFile = open(filepath,'r', encoding="utf8")
  all = noteFile.read()
  noteFile.close()
  paras = all.split("\n\n")
  return paras

def findOccurences(params, word):
  counts = []
  for x in params:
    num = x.count(word)
    counts.append(num)
  return counts

splitFile("C:\\Users\\shanm\\OneDrive\\Documents\\GitHub\\HackUTD-VII\\InitialInput\\04-arrays.txt")

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def transcript():
  video = "C:\\Users\\shanm\\OneDrive\\Documents\\GitHub\\HackUTD-VII\\InitialInput\\While Loops with the Farmer.mp4"
  audio = "converted.wav"
  textF = "text.txt"
  try:
      #videoClip = mp.VideoFileClip(r"{}".format(video))
      #videoClip.audio.write_audiofile(r"{}".format(audio2))

      #w = wave.open(audio2, "rb")
      #binary_data = w.readframes(w.getnframes())
      #w.close()
      #audio = speech.RecognitionAudio(content=binary_data)

      #config = speech.RecognitionConfig(
      #  encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
     #   sample_rate_hertz=16000,
     #   language_code="en-US",
  #  )

      # Detects speech in the audio file
     # operation = client2.long_running_recognize(config=config, audio=audio)
      #response = operation.result(timeout=90)
     # fileX = open(textF, 'w')
      #for result in response.results:
        # The first alternative is the most likely one for this portion.
       # print(u"Transcript: {}".format(result.alternatives[0].transcript))
       # fileX.write(u"Transcript: {}".format(result.alternatives[0].transcript))
       # print("Confidence: {}".format(result.alternatives[0].confidence))

      #fileX.close()

      videoClip = mp.VideoFileClip(r"{}".format(video))
      videoClip.audio.write_audiofile(r"{}".format(audio))
      recognizer =  sr.Recognizer()
      audioClip = sr.AudioFile("{}".format(audio))
      with audioClip as src:
          audioFile = recognizer.record(src)
      result = recognizer.recognize_google(audioFile)
      with open(textF, 'w') as fileX:
          fileX.write(result)
      fileY = open(textF)
      text = fileY.read()
      fileY.close()
      return(text)
  except Exception as e:
      print("Did not work ", e)

client.run(('Token'))