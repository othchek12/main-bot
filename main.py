import discord
import os

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
     print("Bot is ready to use")

@client.event
async def on_message(message):

     if message.author == client.user:
          return

     if str(message.content) == 'pepega1':
          await message.channel.send('If you take a break your luck will improve🐵')
     
     if str(message.content) == 'pepega2':
          await message.channel.send('when you lose a lot, just take a break man... It helped me when I was stuck in silver 4, Im now happy to say that with this de-tilt techjnique Im not closing up silver 2 with less than 200 lp to go!')
     
     if str(message.content) == 'pet the mbabe':
          await message.channel.send('https://tenor.com/view/mbanbi-gif-26573925')
     
     if str(message.content) == 'pepega':
          await message.channel.send('https://tenor.com/view/pepega-pepe-meme-reddit-twitch-gif-16295852')
     if str(message.content) == 'pepega3':
          await message.channel.send('T9sr match mora lmatch')
     
     if str(message.content) == 'solo duo':
          await message.channel.send('https://media.discordapp.net/attachments/753670017991573515/878422441448333313/nn_msahba.PNG')
     if str(message.content) == 'khouribga':
          await message.channel.send('https://media.discordapp.net/attachments/753670017991573515/865302873789431909/ZomboMeme_15072021192234.jpg')
     if str(message.content) == 'mbabe':
          await message.channel.send('https://media.discordapp.net/attachments/753670017991573515/882563238728970280/13_Reasons_Why_That_Smile_Meme_Template.jpeg?width=591&height=676')
     if str(message.content) == 'sindab':
          await message.channel.send('https://tenor.com/view/stupid-patrick-spongebob-fish-rambling-gif-12797920')
     
     if str(message.content) == 'niggay':
          await message.channel.send('https://yt3.ggpht.com/ytc/AKedOLSznoN-4YcQ5SumdQAD-hRzsfMf6l1wrjVGFb1Kig=s900-c-k-c0x00ffffff-no-rj')
      


     


client.run(os.environ["DISCORD_TOKEN"])

