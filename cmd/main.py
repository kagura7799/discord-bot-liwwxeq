import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from config.config import token
import src.kick_member
import src.ban_member
import src.mute_member

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(pass_context=True, aliases=['кикни', 'кик', 'кикнуть'])
@has_permissions(kick_members=True)
async def kick_members(ctx, member: discord.Member, *, reason=None):
    await src.kick_member.kick(ctx, member, reason)

@bot.command(pass_context=True, aliases=['забань', 'бан', 'забанить'])
@has_permissions(kick_members=True)
async def ban_members(ctx, member: discord.Member, *, reason=None):
    await src.ban_member.ban(ctx, member, reason)

@bot.command(pass_context=True, aliases=['замуть', 'мут', 'мьют', 'вмьют', 'вмут'])
@commands.has_permissions(administrator=True)
async def mute_members(ctx, member: discord.Member, *, reason=None):
    await src.mute_member.mute(ctx, member, reason)

if __name__ == '__main__':
    bot.run(token)
