import discord
import custom
from discord.ext import commands


class role(commands.Cog, name="RoleAdder", description="Adds roles on reaction"):
    def __init__(self, client):
        self.client = client

    @commands.command(help= "send a message for people to react to")
    @commands.check(custom.isItme)
    async def prompt(self, ctx):
        embed = discord.Embed(
            title = 'Add Roles!',
            description="React to this message to self-assign roles",
            color = 0xd8815e
    )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Majors",value="Degrees offered by our school", inline=False)
        embed.add_field(name="🔌", value="Electrical Engineering", inline=True)
        embed.add_field(name="💻", value="Computer Engineering", inline=True)
        embed.add_field(name="Degree Tracks",value="Specialization tracks offered by our school", inline=False)
        embed.add_field(name="🤖", value="Robotics Track", inline=True)
        embed.add_field(name="👾", value="Space Track", inline=True)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction(emoji='🔌')
        await msg.add_reaction(emoji='💻')
        await msg.add_reaction(emoji='🤖')
        await msg.add_reaction(emoji='👾')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.message_id == 899550874051940362:
            guild = self.client.get_guild(id=payload.guild_id)
            role = False
            if not(payload.user_id == 896677611340701726):
                if payload.emoji.name == '🤖':
                    role = discord.utils.get(iterable=guild.roles, name="Robotics Track")
                elif payload.emoji.name == '👾':
                    role = discord.utils.get(iterable=guild.roles, name="Space Track")
                elif payload.emoji.name == '🔌':
                    role = discord.utils.get(iterable=guild.roles, name="Electrical Engineering")
                elif payload.emoji.name == '💻':
                    role = discord.utils.get(iterable=guild.roles, name="Computer Engineering")
                if role:
                    await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if payload.message_id == 899550874051940362:
            guild = self.client.get_guild(id=payload.guild_id)
            member = guild.get_member(payload.user_id)
            role = False
            if not(payload.user_id == 896677611340701726):
                if payload.emoji.name == '🤖':
                    role = discord.utils.get(iterable=guild.roles, name="Robotics Track")
                elif payload.emoji.name == '👾':
                    role = discord.utils.get(iterable=guild.roles, name="Space Track")
                elif payload.emoji.name == '🔌':
                    role = discord.utils.get(iterable=guild.roles, name="Electrical Engineering")
                elif payload.emoji.name == '💻':
                    role = discord.utils.get(iterable=guild.roles, name="Computer Engineering")
                if role:
                    await member.remove_roles(role)


def setup(client):
    client.add_cog(role(client))
