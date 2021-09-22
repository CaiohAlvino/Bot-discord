import discord #importações do bot
from Token import token
from discord.ext import commands

Prefix = '!' #prefixo do bot / variavel client
client = commands.Bot(command_prefix=Prefix)

#comando para saber se está funncionando

@client.event #definimos um evento
async def on_ready():
    activity = discord.Game(name="Em manutenção", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Estou acordado!, Pronto para uso!")       #.dnd
    print(client.user)                               #.online

#comandos dos membros
@client.command() # definimos um comando
async def acorda(ctx):
    msg = f"Acordei!, bom dia {ctx.author.mention} "
    await ctx.send(msg)

#comandos de moderação
@client.command()
async def kick(ctx, membro : discord.Member, *,motivo=None):
    canal = client.get_channel(id=862679861943336990)
    msg = f"{ctx.author.mention} expulsou {membro.mention} por {motivo}"
    await membro.kick()
    await canal.send(msg)

@client.command()
async def ban(ctx, membro : discord.Member, *,motivo=None):
    canal = client.get_channel(id=862679861943336990)
    msg = f"{ctx.author.mention} baniu {membro.mention} por {motivo}"
    await membro.ban()
    await canal.send(msg)

client.run(token) #token do bot
