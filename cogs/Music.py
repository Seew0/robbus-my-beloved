import discord
from discord import voice_client
from discord.ext import commands
from discord.ext.commands.core import command
import youtube_dl
from youtube_dl.YoutubeDL import YoutubeDL

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Music.py Ready!")

    @commands.command()
    async def join(self, ctx): 
        vc = ctx.voice_client
        if ctx.author.voice is None:
            await ctx.send("Vc toh join karle")
        voice_channel = ctx.author.voice.channel
        if vc is None:
            await voice_channel.connect()
        else:
            await vc.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx): 
        vc = ctx.voice_client
        await vc.disconnect()

    @commands.command()
    async def play(self, ctx, url): 
        vc = ctx.voice_client
        vc.stop()
        FFFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFFMPEG_OPTIONS)
            vc.play(source)
            await ctx.send("Play!")

    @commands.command()
    async def pause(self, ctx):
        vc = ctx.voice_client
        await vc.pause()
        await ctx.send("kya dikkat ho gyi?")

    @commands.command() 
    async def resume(self, ctx):
        vc = ctx.voice_client
        await vc.resume()
        await ctx.send("chalooooooooooo")

def setup(bot):
    bot.add_cog(Music(bot))
