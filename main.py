# permission needed are: Manage Roles, Manage Channels, Read Text Channels & See Voice Channels, Manage Messages, Read Message History

import os
import discord
from dotenv import load_dotenv

# TODO readme


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# TODO make it so the first message is only sent once
# TODO make it so that the owner can remove roles and add roles



async def first_message():
    for ch in client.get_all_channels():
        if ch.name == "role" and ch.type.name == "text":
            
             async for msg in ch.history(limit=200):
                 await msg.delete()

            message = await ch.send('Welcome to the **' + ch.guild.name + '** server, \n \n There are many hidden channels here that we dont want you to be bothered with, but if you so choose just ping the topic you are interested in down here and enjoy ! \n :smile:')
            msg_id = ch.last_message_id
            message = await ch.fetch_message(msg_id)
            for emoji in client.emojis:
                if emoji.name.startswith("ec_"):
                    await message.add_reaction(emoji)



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    await first_message()

@client.event
async def on_reaction_add(reaction,user):
    reaction
# TODO make it so that on reaction and on removal of one the roles are added to the people
client.run(TOKEN)