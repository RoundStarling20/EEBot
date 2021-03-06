import os

import discord
from discord import file
from discord.ext import commands
from discord.flags import Intents

import custom
from custom import directoryPath

client = commands.Bot(command_prefix = custom.getPrefix, intents=Intents.all(), description="A bot programmed by RoundStarling20")

@client.event
async def on_guild_join(guild):
    prefixes = custom.get_db(filePath=directoryPath["serverPrefixdb"])
    prefixes[str(guild.id)] = '.'
    custom.save_db(db=prefixes, filePath=directoryPath["serverPrefixdb"])

@client.event
async def on_guild_remove(guild):
    prefixes = custom.get_db(filePath=directoryPath["serverPrefixdb"])
    prefixes.pop(str(guild.id))
    custom.save_db(db=prefixes, filePath=directoryPath["serverPrefixdb"])

@client.event
async def on_member_join(member):
    await member.guild.system_channel.send(f'Welcome <@{member.id}>, check out <#899548270454513734>!')

@client.event
async def on_member_remove(member):
    await member.guild.system_channel.send(f'Goodbye DooDoo Head <@{member.id}>!')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandNotFound):
        await ctx.send("Thats not a command")

@client.command(help= "send a member's profile picture")
async def av(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    embed = discord.Embed(
        title = f'{member.name}',
        url = f'{member.avatar_url}'
    )
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')


with open("token.txt", 'r', encoding="utf-8") as fp:
    client.run(f"{fp.read()}")

#rotate images