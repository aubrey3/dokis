import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Hug(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def hug(self,ctx, *, message=None): 
        member = ctx.message.content.split(" ")[0]
        if message is None: #No argument? Just assume it's you
            user = ctx.author
            hug_list = [f"F-fine, but only because I'll look like a jerk if I don't! *hugs <@{user.id}>*", f"I guess a quick hug never hurt anyone... *hugs {user.name}*"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(hug_list))

        elif message == '@everyone' or message == '@here':
            await ctx.send(conf.everyone_tag)
            
        if message == f'<@{self.b.user.id}>': # Oh noes it's me!
            hug_list = [f"...fine. *hugs myself*", "Well, if you say so... *hugs myself*", "*hugs myself* Huh. Now I see why you guys like my hugs so much."]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(hug_list))

        else: # Argument, okay let's spit whatever the user just said
            hug_list = [f"F-fine, but only because I'll look like a jerk if I don't! *hugs {message}*", f"I guess a quick hug never hurt anyone... *hugs {message}*"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(hug_list))


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Hug(bot))
