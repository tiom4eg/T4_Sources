import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="t4!")
channels2users = {}
id2users = {}


@bot.event
async def on_ready():
    print("Connected!")


# OK
@bot.command()
async def create_channel(ctx, member: discord.Member):
    if (ctx.author.id, member.id) not in channels2users.get(ctx.guild.id, []):
        await ctx.guild.create_text_channel(f"{ctx.author.id}_{member.id}_{ctx.guild.id}")
        if ctx.guild.id not in channels2users.get(ctx.guild.id, []):
            channels2users[ctx.guild.id] = [(ctx.author.id, member.id)]
        else:
            channels2users[ctx.guild.id].append((ctx.author.id, member.id))
        ID = discord.utils.get(ctx.guild.text_channels, name=f"{ctx.author.id}_{member.id}_{ctx.guild.id}").id
        id2users[ID] = (ctx.author.id, member.id)
        await ctx.send("Channel successfully created!")
    else:
        await ctx.send("You're already have channel in this guild!")


@bot.command()
async def guild_channels(ctx):
    if channels2users.get(ctx.guild.id, []):
        channels = []
        for el in channels2users[ctx.guild.id]:
            channels.append(f"{channels2users[ctx.guild.id][el[0]]}_{channels2users[ctx.guild.id][el[1]]}_{ctx.guild.id}")
        await ctx.send("List of this guild's channels:")
        await ctx.send("\n".join(map(str, channels)))
    else:
        await ctx.send("There's no channels in this guild, that were created by me!")


@bot.command()
async def my_channels(ctx):
    channels = []
    for el in id2users:
        if ctx.author.id in id2users[el]:
            channels.append(el)
    if channels:
        await ctx.send("List of your channels:")
        await ctx.send("\n".join(map(str, channels)))
    else:
        await ctx.send("You haven't created any channels!")


@bot.command()
async def delete_channel(ctx, channel: discord.TextChannel):
    if channel.id in id2users:
        del id2users[channel.id]
        del channels2users[channel.guild.id][channels2users[channel.guild.id].index((int(channel.name.split("_")[0]), int(channel.name.split("_")[1])))]
        await channel.delete()
        await ctx.send("Channel was successfully deleted!")
    else:
        await ctx.send("This channel doesn't exist or wasn't created by me!")


@bot.command()
async def debug(ctx):
    await ctx.send(channels2users)
    await ctx.send(id2users)

bot.run("**********************") # your secret token
