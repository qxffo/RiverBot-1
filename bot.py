import discord
from discord.ext import commands
import random
import json

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)
client.remove_command('help')

@client.event
async def on_ready():
  print('Logged into {0.user}'.format(client))
  await client.change_presence(status=discord.Status.online, activity=discord.Game('PICKLE RICK!!! | ;help'))
#Change Prefix
@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = ';'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    embed = discord.Embed(
        colour = discord.Colour.purple()
    )

    embed.set_author(name='Prefix changed to: {prefix}')

    await ctx.send(embed=embed)



#Clear Command
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

#Kick Command
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

#Kick Error
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        
        embed = discord.Embed(
        colour = discord.Colour.blue()
    )

        embed.set_author(name='You do not have permision to use this command!')

        await ctx.send(embed=embed)

#Ban Command
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

#Ban Error
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        
        embed = discord.Embed(
        colour = discord.Colour.blue()
    )

        embed.set_author(name='You do not have permision to use this command!')

        await ctx.send(embed=embed)

#Help Command
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.channel

    embed = discord.Embed(
        colour = discord.Colour.dark_green()
    )

    embed.set_author(name='Source Code')
    embed.add_field(name=';kick', value='Kicks mentioned user', inline=False)
    embed.add_field(name=';ban', value='Bans mentioned user', inline=False)
    embed.add_field(name=';clear', value='Deletes messages.', inline=False)
    
    await author.send(embed=embed)
#Source Command
@client.command(pass_context=True)
async def source(ctx):
    author = ctx.message.channel

    embed = discord.Embed(
        colour = discord.Colour.dark_green()
    )

    embed.set_author(name='Source Code')
    embed.add_field(name='Source', value='https://github.com/qxffo/RiverBot-1', inline=False)
    
    await author.send(embed=embed)

#8ball Command
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes – definitely.',
                 'Signs point to yes.',
                 'Outlook good.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.',
                 'Better not tell you now']
    await ctx.send(f'Question: {question}\nAsnwer: {random.choice(responses)}')

client.run('TOKEN')
