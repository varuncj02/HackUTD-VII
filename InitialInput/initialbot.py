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

  if message.content.startswith('$transcript'):
    thing = transcript()
    await message.channel.send(thing)

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

#CHANGE TO TOKENS YOU DIMWIT THEN TAKE THIS OUT BEFORE SUBMISSION IDIOT
client.run(('Token'))