# permission needed are: Manage Roles, Manage Channels, Read Text Channels & See Voice Channels, Manage Messages, Read Message History

import os
import discord
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
emojis = []
client = discord.Client()



async def clean_channel(ch):
    """
    This function gets a channel and removes all the messages that were sent from users other than the client
    """
    async for msg in ch.history(limit=200):
        if msg.author.id != client.user.id:
            await msg.delete()


async def first_message():
    """
    This function checks if there is an appropriate channel, cleans it from user messages, checks if the message that is required to be sent is there and updates the emojis on the message.

    """
    for ch in client.get_all_channels():
        # checks if there is an appropriate channel 
        if ch.name == "role" and ch.type.name == "text":
            
            # removes messages from other users
            await clean_channel(ch)


            # sends a message so that the next function wont fail and also lets the users know the bot is starting.
            starting_message = await ch.send('starting...')
            message = None
            
            # goes through the messages on the channel to get the role message
            async for msg in ch.history(limit=2):
                if msg.clean_content != starting_message.clean_content:
                    message = msg
            
            
            # if there is no role message send it (create it)
            if message == None:
                message = await ch.send('Welcome to the **' + ch.guild.name + '** server, \n \n There are many hidden channels here that we dont want you to be bothered with, but if you so choose just ping the topic you\'re interested in down here and enjoy ! \n :smile:')


            # delete the starting message
            await starting_message.delete()
            


            # add the current emojis to a list
            for current_reaction in message.reactions:
                if current_reaction.emoji.name.startswith("role_"):
                    
                    emojis.append(current_reaction.emoji)



            # add emoji to the role message
            for emoji in client.emojis:
                if emoji.name.startswith("role_"):
                    await message.add_reaction(emoji)
 
        

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    await first_message()

@client.event
async def on_reaction_add(reaction,user):
    reaction
client.run(TOKEN)