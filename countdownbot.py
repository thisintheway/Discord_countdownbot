import discord
from discord.ext import commands
import random
import time
import datetime
import threading

client = commands.Bot(command_prefix = '.')
TOKEN = open("token.txt","r").readline()

@client.command()
async def count(ctx, arg1, arg2, arg3, arg4=0, arg5='Raid'):
    horodate = ctx.message.created_at
    year = int(horodate.strftime("%Y"))
    month = int(horodate.strftime("%m"))
    day = int(horodate.strftime("%d"))
    hour = int(horodate.strftime("%H"))
    minute = int(horodate.strftime("%H"))
    print(f'horodate {horodate}')
    print(f'arg1 {arg1}')
    target_month = int(arg1)
    target_day = int(arg2)
    target_hour = int(arg3)
    target_minute = int(arg4)
    global target
    target = datetime.datetime(year, target_month, target_day, target_hour, target_minute)
    print(f'target {target}')
    diff = target - horodate
    print(f'diff {diff}')
    random.seed()
    color = discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    embed = discord.Embed(title=f'Countdown to  {arg5}', colour=color)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name='Time remaining :', value=diff, inline=False)
    msg = await ctx.send(embed=embed)
    #diff = countdown(target)
    while datetime.datetime.now() < target:
        time.sleep(5)
        diff = (target - datetime.datetime.now())
        new_embed = discord.Embed(title=f'Countdown to  {arg5}', colour=color)
        new_embed.set_thumbnail(url=ctx.guild.icon_url)
        new_embed.add_field(name='Time remaining :', value=diff, inline=False)
        await msg.edit(embed=new_embed)

client.run(TOKEN)