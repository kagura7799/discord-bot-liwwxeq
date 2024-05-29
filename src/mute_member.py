import discord
import asyncio
from discord.ext import commands

async def mute(ctx, member: discord.Member = None, time: int = 1, *, reason=None):
    role_id = 970660008838721547
    role = discord.utils.get(ctx.guild.roles, id=role_id)

    if role is None:
        await ctx.send("Роль для мута не найдена. Проверьте правильность ID роли.")
        return

    elif member is None:
        await ctx.send("Вы не указали пользователя дл замьюта.")
        return

    emb = discord.Embed()
    emb.set_author(name=member.display_name)
    emb.set_footer(text=f'Был замучен администратором {ctx.author.display_name} на {time} минут')

    await ctx.send(embed=emb)
    await member.add_roles(role)
    await asyncio.sleep(int(time) * 60)
    await member.remove_roles(role)

@mute.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("У тебя недостаточно прав для мута участников :(")