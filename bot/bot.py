import discord
from discord import option
from discord.ext import commands
import os

# Pega o token direto do Codespaces Environment Secrets
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.slash_command(name="ping", description="Responde com pong!")
async def ping(ctx):
    await ctx.respond("Pong!")

@bot.slash_command(name="userinfo", description="Mostra informações do usuário.")
async def userinfo(ctx, user: discord.User = None):
    user = user or ctx.author
    await ctx.respond(f"Usuário: {user.name}\nID: {user.id}")

@bot.slash_command(name="serverinfo", description="Mostra informações do servidor.")
async def serverinfo(ctx):
    guild = ctx.guild
    await ctx.respond(f"Servidor: {guild.name}\nMembros: {guild.member_count}")

@bot.slash_command(name="help", description="Mostra comandos disponíveis.")
async def help_command(ctx):
    await ctx.respond("Comandos disponíveis: /ping, /userinfo, /serverinfo, /help, /status")

@bot.slash_command(name="status", description="Mostra status do bot.")
async def status(ctx):
    await ctx.respond("Estou online e funcional!")

bot.run(TOKEN)
