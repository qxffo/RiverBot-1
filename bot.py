import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = ';')
client.remove_command('help')

@client.event
async def on_ready():
  print('Logged into RiverBot')
  await client.change_presence(status=discord.Status.online, activity=discord.Game('PICKLE RICK!!! | ;help'))
#Clear Command
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
#Help Command
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.channel

    embed = discord.Embed(
        colour = discord.Colour.dark_green()
    )

    embed.set_author(name='All commands for RiverBot')
    embed.add_field(name=';kick', value='Kicks mentioned member', inline=False)
    embed.add_field(name=";Ban", value="Bans mentioned member", inline=False)
    embed.add_field(name=";unban", value="Bans mentioned member", inline=False)
    
    await author.send(embed=embed)
#Kick Command
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')
#Ban Command
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
#Unban Command
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
#Source Command
@client.command(pass_context=True)
async def source(ctx):
    author = ctx.message.channel

    embed = discord.Embed(
        colour = discord.Colour.dark_green()
    )

    embed.set_author(name='Source Code')
    embed.add_field(name='Source', value='https://github.com/qxffo/RiverBot-Version-0.0.6', inline=False)
    
    await author.send(embed=embed)

client.run('TOKEN')
