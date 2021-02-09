import discord
import sqlite3

# Add Member intents
intents = discord.Intents.default()
intents.members = True

# Create the client with the new intents
client = discord.Client(intents=intents)

# Define birthday database location
Tanjodb = 'birthdays.db'

# Initialize DB if it's not available
# Connect to DB with birthday passed in
    # If new, add to table
    # Update Bday if needed
# Delete bday from table (maybe later? Might need more permissions)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    elif message.content.startswith('$debug'):
        await message.channel.send('Info:')
        await message.channel.send(f'Channel: {message.channel}')
        await message.channel.send(f'Guild: {message.guild}')
        await message.channel.send(f'Guild Members: {message.guild.members}')

    elif message.content.startswith('$users'):
        await message.channel.send('Here are all visible users: ')
        for member in message.guild.members:
            await message.channel.send(member.display_name)

    elif message.content.startswith('$bd'):
        # BD Commands here
        # Split the message by space, then start peeling back the layers
        # We know to skip the first part due to it being $bd
        words_list = message.content.split()[1:]
        command = words_list[0]
        # Regardless of command, peel off the top word once more
        params = words_list[1:]
        if command == 'register':
            await add_birthday(message.channel, params)
        elif command == 'edit':
            await edit_birthday(message.channel, params)
        elif command == 'delete':
            await delete_birthday(message.channel, params)
        else:
            await message.channel.send('Invalid Tanjobot command.')
            await print_help(message.channel)

async def print_help(channel):
    await channel.send('''
    Valid commands for Tanjobot are:
\t- register:\tRegister a new birthday.
\t\t*Requires birthday date.
\t\t*Optionally, provide a name (will otherwise use the username)
\t- edit:\tProvide a new date for your birthday (in case you got it wrong).
\t\t*Requires new date
\t- delete:\tRemove your birthday from the list.
''')

# Birthday bot commands:
async def add_birthday(channel, param_list)

client.run('Insert Token Here')