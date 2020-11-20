import discord
from discord.ext import commands
import random
import aiohttp

class MiscCommands(commands.Cog, name = 'Fun Commands'):
    '''Fun Commands'''

    def __init__(self, bot):
      self.bot = bot 

    @commands.command()
    async def quote(self, ctx):
      response = [
        "It’s just pathetic to give up on something before you even give it a shot.”",
        "Knowing you’re different is only the beginning. If you accept these differences you’ll be able to get past them and grow even closer.” – Miss Kobayashi",
        "JOJO POSE!",
        "If you don\'t know what you should hold dear, then your life is just a journey without a destination. - Hisano Kuroda",
        "If you waste time fiddling with a new humanity and evolution, you'll never make it. Human strength lies in the ability to change yourself. - Saitama",
        "Give up! On making me give up! - Naruto",
        "The difference between the novice and the master is that the master has failed more than the novice has tried. - Koro-sensei",
        "If you win, you live. If you lose, you die. If you don't fight, you can't win! - Eren Jaeger",
        "How can you move forward if you keep regretting the past. - Edward Elric",
        "“If you don’t take risks, you can’t create a future!” - Luffy",
        "“People’s lives don’t end when they die, it ends when they lose faith.” - Itachi",
        "“If you don’t like your destiny, don’t accept it.” - Naruto",
        "“If you don’t share someone’s pain, you can never understand them.” - Nagato",
        "“There’s no shame in falling down! True shame is to not stand up again!” - Shintarō Midorima",
        "“People become stronger because they have memories they can’t forget.” - Tsunade",
        "“If you really want to be strong… Stop caring about what your surrounding thinks of you!” - Saitama",
        "“Hard work is worthless for those that don’t believe in themselves.” - Naruto",
        "“It is at the moment of death that humanity has value.” - Archer"  ]

      await ctx.send(f'{ctx.author.mention}\nQuote: `{random.choice(response)}`')

    @commands.command(aliases=['8ball', 'kk'])
    async def magikball(self, ctx, *, question):
        response = [
            "It is certain. :8ball:", "It is decidedly so. :8ball:",
            "Without a doubt. :8ball:", "Yes - definitely. :8ball:",
            "You may rely on it. :8ball:", "As I see it, yes. :8ball:",
            "Most likely. :8ball:", "Outlook good. :8ball: ", "Yes. :8ball:",
            "Signs point to yes. :8ball: ", "Reply hazy, try again. :8ball:",
            "Ask again later. :8ball:", "Better not tell you now. :8ball:",
            "Cannot predict now. :8ball:", "Concentrate and ask again. :8ball:",
            "Don't count on it. :8ball:", "My reply is no. :8ball: ",
            "My sources say no. :8ball: ", "Outlook not so good. :8ball:",
            "Very doubtful. :8ball:", "Idc, Idk :8ball:", "Wise words... Did you know that you have to ask a question?"
        ]

        await ctx.send(
            f'Question: {question}\n {ctx.author.mention}\nAnswer: {random.choice(response)}'
        )

    @commands.command()
    async def kiss(self, ctx, user: discord.Member):
          gifs = [
              "https://media1.tenor.com/images/558f63303a303abfdddaa71dc7b3d6ae/tenor.gif?itemid=12879850",
              "https://i.gifer.com/PCUi.gif",
              "https://cdn.weeb.sh/images/B13D2aOwW.gif",
              "https://cdn.weeb.sh/images/B1yv36_PZ.gif",
              "https://cdn.weeb.sh/images/Sk5P2adDb.gif",
              "https://media.discordyui.net/reactions/kiss/234082934.gif"
          ]
          embed = discord.Embed(
              title="Kiss",
              description=
              f"Woah {ctx.author.mention} stop kissing {user.mention} so passionately ...",
              color=discord.Color.blue())
          embed.set_image(url=f"{random.choice(gifs)}")
          await ctx.send(embed=embed)


    @commands.command()
    async def lick(self, ctx, user: discord.Member):
          gifs = [
              "https://images-ext-2.discordapp.net/external/AqmvPrnwsYvvxn5kgJH9Bd-J7mKkl3ka-jpVCwOiMyQ/https/cdn.weeb.sh/images/Sk15iVlOf.gif",
              "https://media1.tenor.com/images/6b701503b0e5ea725b0b3fdf6824d390/tenor.gif?itemid=12141727",
              "https://cdn.weeb.sh/images/ryGpGsnAZ.gif"
          ]
          embed = discord.Embed(
              title="Lick",
              description=
              f"Woah {ctx.author.mention} stop licking {user.mention} like he/she is icecream ...",
              color=discord.Color.blue())
          embed.set_image(url=f"{random.choice(gifs)}")
          await ctx.send(embed=embed)


    @commands.command()
    async def hug(self, ctx, user: discord.Member):
          gifs = [
              "https://cdn.weeb.sh/images/H1ui__XDW.gif",
              "https://cdn.weeb.sh/images/B11CDkhqM.gif",
              "https://cdn.weeb.sh/images/rJv2H5adf.gif",
              "https://cdn.weeb.sh/images/SywetdQvZ.gif",
              "https://cdn.weeb.sh/images/BJCCd_7Pb.gif"
          ]
          embed = discord.Embed(
              title="Hug",
              description=f" {ctx.author.mention} hugs you {user.mention}  ...",
              color=discord.Color.blue())
          embed.set_image(url=f"{random.choice(gifs)}")
          await ctx.send(embed=embed)


    @commands.command()
    async def kill(self, ctx, user: discord.Member, *, reason = "Killing someone without any reason, understandable."):
          gifs = [
              "https://cdn.weeb.sh/images/r11as1tvZ.gif",
              "https://cdn.weeb.sh/images/BJO2j1Fv-.gif",
          ]
          embed = discord.Embed(
              title="kill",
              description=
              f" {ctx.author.mention} brutally kills {user.mention} for {reason}",
              color=discord.Color.blue())
          embed.set_image(url=f"{random.choice(gifs)}")
          await ctx.send(embed=embed)


    @commands.command()
    async def pat(self, ctx, user: discord.Member):
          gifs = [
              "https://media.tenor.com/images/ad8357e58d35c1d63b570ab7e587f212/tenor.gif",
              "https://media.tenor.com/images/a671268253717ff877474fd019ef73e9/tenor.gif"
          ]
          embed = discord.Embed(
              title="pat",
              description=f"{ctx.author.mention} pats {user.mention}",
              color=discord.Color.blue())
          embed.set_image(url=f"{random.choice(gifs)}")
          await ctx.send(embed=embed)


    @commands.command()
    async def slap(self, ctx, user: discord.Member, *, reason = f"Feels good boi"):
          gifs = [
              "https://media1.tenor.com/images/b6d8a83eb652a30b95e87cf96a21e007/tenor.gif?itemid=10426943",
              "https://media1.tenor.com/images/e8f880b13c17d61810ac381b2f6a93c3/tenor.gif?itemid=17897236"
          ]
          embed = discord.Embed(
              title="Slap",
              description=
              f"Woah {ctx.author.mention} chill... You slapped {user.mention} for {reason}, so hard they are now in hospital...",
              color=discord.Color.blue())
          embed.add_field(name = f"{ctx.author.name} onii/onee-channn!", value =  "*screams loudly*", inline = False)
          embed.set_image(url=f"{random.choice(gifs)}")
          await ctx.send(embed=embed)

    @commands.command(aliases=["meemee"])
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"https://www.reddit.com/r/memes/top.json") as response:
                j = await response.json()

        data = j["data"]["children"][random.randint(0, 50)]["data"]
        image_url = data["url"]
        title = data["title"]
        em = discord.Embed(
            description=f"[**{title}**]({image_url})", color=ctx.author.color)
        em.set_image(url=image_url)
        em.set_footer(
            icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
        await ctx.send(embed=em)

    @commands.command()
    async def character(self, ctx):
        images = ["https://th.bing.com/th/id/OIP.KGg9LxyyPQHMYTzf2QE8oAHaHa?w=179&h=180&c=7&o=5&pid=1.7",
      "https://th.bing.com/th/id/OIP.IEqeBi1qGnolmbAv60P8gwHaNK?w=115&h=186&c=7&o=5&pid=1.7",
      "https://th.bing.com/th/id/OIP.pk1ZNsA-B-xGn8e3D9OaDwHaJ4?w=200&h=267&c=7&o=5&pid=1.7",
      "https://th.bing.com/th/id/OIP.D-9__yO-oIdrhB80Sk1cXwHaEK?w=274&h=180&c=7&o=5&pid=1.7",
      "https://th.bing.com/th/id/OIP.rBhuIDtPtKKISPYGnM3xTwHaEK?w=294&h=180&c=7&o=5&pid=1.7",
      "https://th.bing.com/th/id/OIP.XbU-RJBMFdIHG0P3IQV5FAHaEK?w=286&h=180&c=7&o=5&pid=1.7",
      "https://th.bing.com/th/id/OIP.PH9PgbdurulZI5MGTszT2QHaEK?w=321&h=180&c=7&o=5&pid=1.7",
      "https://vignette.wikia.nocookie.net/fma/images/d/d3/Avatar_edward.png/revision/latest?cb=20180406214254",
      "https://th.bing.com/th/id/OIP.Byg_SbpZ8k_EPuYdLvS8OAHaHa?w=200&h=200&c=7&o=5&pid=1.7"]

        em = discord.Embed(
              title="Anime",
              description=
              "A cool character",
              color=discord.Color.blue())
        em.set_image(url=f"{random.choice(images)}")

        await ctx.send(embed = em)

    @commands.command(
          name='say',
          description='The say command',
          aliases=['repeat', 'parrot'],
          usage='<text>'
      )
    async def say_command(self, ctx):
          # The 'usage' only needs to show the parameters
          # As the rest of the format is generated automatically
          
          # Lets see what the parameters are: -
          # The self is just a regular reference to the class
          # ctx - is the Context related to the command
          # For more reference - https://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#context

          # Next we get the message with the command in it.
          msg = ctx.message.content

          # Extracting the text sent by the user
          # ctx.invoked_with gives the alias used
          # ctx.prefix gives the prefix used while invoking the command
          prefix_used = ctx.prefix
          alias_used = ctx.invoked_with
          text = msg[len(prefix_used) + len(alias_used):]
          
          # Next, we check if the user actually passed some text
          if text == '':
              # User didn't specify the text
              
              await ctx.send(content='You need to specify the text!')            

              pass
          else:
              # User specified the text.
              
              await ctx.send(content=f"**{text}**")
              
              pass

          return

def setup(bot):
    bot.add_cog(MiscCommands(bot))