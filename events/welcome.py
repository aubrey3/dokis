import asyncio, discord, random
import discord.ext.commands as client

class Welcome(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_support_server(self, id):
        return id == json.loads(open("config.json",'r').read())["support server"]["invite"]

    @client.Cog.listener()
    async def on_member_join(self, member):
        if not member.bot or not self.is_support_server(ctx.guild.id):
            return
        tampered = True if self.bot.globalCursor.execute(f"SELECT * FROM tampered WHERE bot = '{self.bot.name}' AND (type = 'guild' AND id = {member.guild.id if member.guild else 0}) OR (type = 'user' AND id = {member.author.id})").fetchone() is not None else False
        self.bot.globalCursor.execute(f"INSERT INTO 'currentWelcomer' ('bot','id') SELECT '{random.choice([i['name'] for i in characters])}',{config['support server']['id']} WHERE NOT EXISTS(SELECT bot FROM currentWelcomer WHERE id = {member.guild.id}) LIMIT 1")
        currentWelcomer = self.bot.globalCursor.execute(f"SELECT bot FROM currentWelcomer WHERE id = {member.guild.id}").fetchone()
        if currentWelcomer.lower() == self.bot.name.lower():
            reply = self.bot.character.welcome(tamper=tampered, member=member)
            await self.bot.send(member.channel, reply)

def setup(bot):
    bot.add_cog(Welcome(bot))