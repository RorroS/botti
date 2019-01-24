# Work with Python 3.6
import discord
import json

# Get token
with open('auth.json') as f:
    TOKEN = json.load(f)['token']

client = discord.Client()

@client.event
async def on_message(message):
    # Prevent from replying to self
    if message.author == client.user:
        return

    # Assign the user to the role they request
    if message.content.startswith('!role'):
        msg_list = message.content.split(' ')
        if len(msg_list) > 1:
            requested_role = ' '.join(msg_list[1:])
            role = discord.utils.get(message.server.roles, name=requested_role)

            if role != None:
                try:
                    await client.add_roles(message.author, role)
                    msg = '{0.author.mention}, you joined '.format(message) + '**' + requested_role + '**'
                except discord.errors.Forbidden:
                    msg = 'Cannot assign that role!'
            else:
                msg = 'Role does not exist (Roles are case-sensitive)'
        else:
            msg = 'Role was left blank!'
        await client.send_message(message.channel, msg)

    # Remove user from the role requested
    if message.content.startswith('!leave'):
        msg_list = message.content.split(' ')
        if len(msg_list) > 1:
            requested_role = ' '.join(msg_list[1:])
            role = discord.utils.get(message.server.roles, name=requested_role)

            if role != None:
                try:
                    await client.remove_roles(message.author, role)
                    msg = '{0.author.mention}, you left '.format(message) + '**' + requested_role + '**'
                except discord.errors.Forbidden:
                    msg = 'Cannot remove that role!'
            else:
                msg = 'Role does not exist (Roles are case-sensitive)'
        else:
            msg = 'Role was left blank!'
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
