import discord
from discord.ext import commands
async def ban(ctx,member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} был забанен')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("У тебя недостаточно прав для бана участников :(")