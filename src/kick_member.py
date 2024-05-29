import discord
from discord.ext import commands

async def kick(ctx,member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} был исключен')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("У тебя недостаточно прав для кика участниковф :(")