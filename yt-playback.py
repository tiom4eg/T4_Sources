import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import asyncio

bot = commands.Bot(command_prefix=<command_prefix>)

server_channel = {}
channel_queue = {}


@bot.command()
async def play(ctx, track: str):
    user = ctx.message.author
    if user.voice:  # check if user in ANY voice channel
        if not server_channel.get(ctx.guild, 0):  # if this guild hasn't vc with bot
            server_channel[ctx.guild] = user.voice.channel.id  # set this VoiceChannel as guild's vc
            # getting url with youtube_dl
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(track, download=False)
            url = info['formats'][0]['url']
            channel_queue[user.voice.channel.id] = [(url, track)]
            # let music make you lose control!
            vc = await user.voice.channel.connect()
            while channel_queue[user.voice.channel.id]:
                # executable takes path to ffmpeg.exe as argument
                vc.play(discord.FFmpegPCMAudio(executable=r"<path>\ffmpeg.exe", source=channel_queue[user.voice.channel.id][0][0]))
                while vc.is_playing():
                    await asyncio.sleep(3)
                channel_queue[user.voice.channel.id].pop(0)
            # bye-bye!
            del server_channel[ctx.guild]
            del channel_queue[user.voice.channel.id]
            await ctx.send("Thank you for listening!")
            await vc.disconnect()
        else:  # otherwise, check if this user joined to vc our bot in
            if user.voice.channel.id != server_channel[ctx.guild]:
                await ctx.send("You're not allowed to use bot commands, if you're not joined voice channel with bot.")
            else:  # everything is all right, let's add to queue
                # getting url...
                with YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(track, download=False)
                url = info['formats'][0]['url']
                channel_queue[user.voice.channel.id].append((url, track))
    else:  # if not, he is not allowed to use .play()
        await ctx.send("You're not in voice channel on this server.")
        
        
@bot.command()
async def queue(ctx):
    if server_channel.get(ctx.guild, 0):
        await ctx.send("\n".join(map(lambda x: f"{x[0]}. {x[1][1]}", enumerate(channel_queue[server_channel[ctx.guild]], 1))))
        
        
bot.run(<token>)
