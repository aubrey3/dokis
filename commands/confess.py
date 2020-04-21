import discord, json, re, rstr
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Confess(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def confess(self,ctx):
        if await self.bot.detectEveryoneMention(ctx):
            return
        target = ctx.message.content.partition(' ')[2]
        if not target:
            target = f"<@{ctx.author.id}>"

        monika = next( (c for c in self.bot.chrs if c["name"].lower() == "monika"), None)
        monikaID = monika["character"].id
        sayori = next( (c for c in self.bot.chrs if c["name"].lower() == "sayori"), None)
        sayoriID = sayori["character"].id
        yuri = next( (c for c in self.bot.chrs if c["name"].lower() == "yuri"), None)
        yuriID = yuri["character"].id
        natsuki = next( (c for c in self.bot.chrs if c["name"].lower() == "natsuki"), None)
        natsukiID = natsuki["character"].id

        if re.search(f"^(monika|<@!?436351740787294208>)", target, re.IGNORECASE):
            await self.bot.send(ctx, self.bot.character.confess(target="monika", targetName=f"<@{monikaID}>"))
        elif re.search(f"^(sayori|<@!?425696108455657472>)", target, re.IGNORECASE):
            await self.bot.send(ctx, self.bot.character.confess(target="sayori", targetName=f"<@{sayoriID}>"))
        elif re.search(f"^(yuri|<@!?436350586670153730>)", target, re.IGNORECASE):
            await self.bot.send(ctx, self.bot.character.confess(target="yuri", targetName=f"<@{yuriID}>"))
        elif re.search(f"^(natsuki|<@!?433834936450023424>)", target, re.IGNORECASE):
            await self.bot.send(ctx, self.bot.character.confess(target="natsuki", targetName=f"<@{natsukiID}>"))
        else:
            await self.bot.send(ctx, self.bot.character.confess(target="", targetName=target))

def setup(bot):
    bot.add_cog(Confess(bot))

def check(character):
    return hasattr(character, "confess")