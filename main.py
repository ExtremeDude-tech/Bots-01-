import discord
from discord.ext import commands
import asyncio 
import os
logo = """• ▌ ▄ ·.              ▐ ▄     ▄▄▄▄▄            ▄▄▌  .▄▄ · 
·██ ▐███▪▪     ▪     •█▌▐█    •██  ▪     ▪     ██•  ▐█ ▀. 
▐█ ▌▐▌▐█· ▄█▀▄  ▄█▀▄ ▐█▐▐▌     ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  ▄▀▀▀█▄
██ ██▌▐█▌▐█▌.▐▌▐█▌.▐▌██▐█▌     ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█
▀▀  █▪▀▀▀ ▀█▄▀▪ ▀█▄▀▪▀▀ █▪     ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀ """



with open('prefix.txt') as f:
    content = f.readlines()
    prefix = content
    client = commands.Bot(command_prefix=prefix)
    client.remove_command('help')




def ready():
    os.system('title Token login')
    print(logo)
    print()
    print('Coded by ExtremeDev#0001')
    print()
    print('What is your token?')
    token = input('->')
    client.run(token)
    print()
    os.system('cls')

@client.command()
@commands.has_permissions(administrator=True)
async def status(ctx, message, *args):
    mesg = ' '.join(args)
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(mesg))
    status1122 = ('Status changed to:' + f"**{mesg}**")
    await ctx.send(status1122)

@client.event
async def on_ready():
    os.system('title Bot is on!')
    os.system('cls')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('pornhub'))
    print()
    print(logo)
    print()
    print('Coded by ExtremeDev#0001')
    print()
    print('Bot for administrate')



@client.command()
async def prefix(ctx):
    await ctx.send('My prefis is:' + f"**{content}**")





@client.event
async def on_command_error(ctx, error):
    if not isinstance(error, commands.CheckFailure): 
        embed = discord.Embed(title="Invalid command", color=0x00ff00)
        await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.kick()
    await ctx.send(f"{member.mention} got kicked")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to kick people")

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Who wanna ban? https://i.imgur.com/RkIfjMP.gif")
        return
    await member.ban()
    await ctx.send(f"{member.mention} got banned. https://i.imgur.com/RkIfjMP.gif")
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to ban people nigward")

@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    await ctx.send('Member muted! https://gph.is/2bDfI0R')
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to mute people")


@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.remove_roles(role)
    await ctx.send('Member unmuted!')

@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to unmute people")

@client.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await ctx.send(mesg)




@client.command(pass_context = True)
async def embed(ctx, *args):
    mesg = ' '.join(args)
    embed = discord.Embed(description=mesg, color=0x50bdfe)
    await ctx.send(embed=embed)    

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", description="coded by ExtremeDev#0001", color=0x00ff00)
    embed.add_field(name="help", value="Showing this command", inline=False)
    embed.add_field(name="ban", value="Ban a member", inline=False)
    embed.add_field(name="mute", value="Mute a member", inline=False)
    embed.add_field(name="unmute", value="Unmute a member", inline=False)
    embed.add_field(name="say", value="Say a message", inline=False)
    embed.add_field(name="embed", value="Say a embed message", inline=False)
    embed.add_field(name="prefix", value="Showing the current prefix", inline=False)
    embed.add_field(name="status", value="Change the bot status", inline=False)
    await ctx.send(embed=embed)





ready()

