import discord
import os
my_secret = os.environ['TOKEN']
#add your token in commands -> environment-variables and make the key TOKEN and the secret is your bot token

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
#this says your logged in

@client.event
async def on_message(message):
  if message.author == client.user:
    return
#returns the statement below

  if message.content.startswith('add your trigger command here'):
    await message.channel.send('add what you want it to say or do')
#sends the message you put above in the channel it was triggered in

client.run(my_secret)
#runs the bot
