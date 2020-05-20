import discord
from discord.ext import commands
import random
import time
import datetime
import threading

client = commands.Bot(command_prefix = '.')
TOKEN = open("token.txt","r").readline()

client.remove_command('help')

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')

@client.command(pass_context=True)
async def help(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : Countdown ')
    embed.add_field(name='.count', value='Counts down, arguments needed are month, day, hour (all in digits, UTC/GMT), minutes(optional), name of event(optional). Separate them by spaces. Make sure bot is allowed to post in channel an pin messages (under Managa Messages)', inline=False)
    await channel.send(embed=embed)

@client.command()
async def count(ctx, arg1, arg2, arg3, arg4=0, arg5='Raid'):
    now = datetime.datetime.utcnow().replace(second=0, microsecond=0)
    #horodate = datetime.datetime.strptime(horodate)
    #horodate = horodate.replace(second=0, microsecond=0)
    year = int(now.strftime("%Y"))
    month = int(now.strftime("%m"))
    day = int(now.strftime("%d"))
    hour = int(now.strftime("%H"))
    minute = int(now.strftime("%H"))
    print(f'now {now}')
    print(f'arg1 {arg1}')
    target_month = int(arg1)
    target_day = int(arg2)
    target_hour = int(arg3)
    target_minute = int(arg4)
    global target
    target = datetime.datetime(year, target_month, target_day, target_hour, target_minute, 0, 0)
    print(f'target {target}')
    diff = target - now
    print(f'diff {diff}')
    random.seed()
    color = discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    embed = discord.Embed(title=f'Countdown to  {arg5}', colour=color)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name='Time remaining :', value=diff, inline=False)
    msg = await ctx.send(embed=embed)
    await msg.pin()
    #diff = countdown(target)
    #now = datetime.utcnow()
    #now = now.replace(second=0, microsecond=0)
    while now < target:
        time.sleep(60)
        now = datetime.datetime.utcnow().replace(second=0, microsecond=0)
        #now = now.replace(second=0, microsecond=0)
        diff = (target - now)
        new_embed = discord.Embed(title=f'Countdown to  {arg5}', colour=color)
        new_embed.set_thumbnail(url=ctx.guild.icon_url)
        new_embed.add_field(name='Time remaining :', value=diff, inline=False)
        await msg.edit(embed=new_embed)

client.run(TOKEN)