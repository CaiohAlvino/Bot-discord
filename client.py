from math import e
import discord
from discord.ext.commands.core import _CaseInsensitiveDict
from Token import token
from discord.ext import commands

#prefixo
Prefix = "."
client = commands.Bot(command_prefix=Prefix, case_insensitive = True)

#eventos
@client.event
async def on_ready():
    activity = discord.Game(name="| Em BETA |", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Estou pronto para a jornada!")
    print(client.user)

#todos os comandos
@client.command()
async def comandos(ctx):
    embed = discord.Embed(
        title = "**COMANDOS**",
        description = "Esses são todos os comandos",
        color = discord.Colour.green()
    )
    
    embed.set_author(name="Guilda", icon_url="https://www.tibiawiki.com.br/images/e/e2/Adamant_Shield.gif")

    embed.set_thumbnail(url="https://www.tibiawiki.com.br/images/a/a6/Gingerbread_Recipe.gif")

    embed.add_field(name = ".ola", value ="Olá!", inline = False)
    embed.add_field(name = ".inforank", value ="Uma breve informações dos ranks", inline = False)
    #embed.add_field(name = ".rankp", value ="Mostra os ranks de Party", inline = False)
    embed.add_field(name = ".inforankp", value ="Mostra as reconpensas de cada _ranks de Party_", inline = False)
    #embed.add_field(name = ".ranki", value ="Mostra os _ranks individuais_", inline = False)
    embed.add_field(name = ".inforanki", value ="Uma breve descrição do rank", inline = False)
    embed.add_field(name = ".meuranki", value = "Vai vir ainda, n terminei o codigo", inline = False)
    await ctx.send(embed = embed)

#comando informativo sobre os ranks em geral
@client.command()
async def inforank(ctx):
    embed = discord.Embed(
        title = "**UMA CURTA INFORMAÇÃO DOS RANKS**",
        description = "Existem dois tipos de ranks, os Individuais e o da Party, cada um com seus ranks e divisões determinadas. Para subir de rank é necessário pontos de guilda que vem de missões completas. Esses pontos são pontos Individuais que com eles vocês sobem de rank, e juntando seus pontos individuais do Grupo vocês tem o rank da Party.",
        color = discord.Colour.purple()
    )

    embed.set_author(name="Guilda", icon_url="https://www.tibiawiki.com.br/images/e/e2/Adamant_Shield.gif")

    embed.set_thumbnail(url="https://www.tibiawiki.com.br/images/e/ee/Arcane_Insignia.gif")
    await ctx.send(embed = embed)


#ranks de party
@client.command()
async def rankp(ctx):
    embed = discord.Embed(
        title = "**RANK da PARTY**",
        description = "Esses são todos os _ranks_ de party",
        color = discord.Colour.red()
    )
    
    embed.set_author(name="Guilda", icon_url="https://www.tibiawiki.com.br/images/e/e2/Adamant_Shield.gif")

    embed.set_thumbnail(url="https://www.tibiawiki.com.br/images/e/ee/Arcane_Insignia.gif")

    embed.add_field(name = "**S+**", value ="Heroico", inline = False)
    embed.add_field(name = "**S**", value = "Lendario", inline = False)
    embed.add_field(name = "**A**", value ="Diamante", inline = False)
    embed.add_field(name = "**B**", value ="Platina", inline = False)
    embed.add_field(name = "**C**", value ="Ouro", inline = False)
    embed.add_field(name = "**D**", value ="Prata", inline = False)
    embed.add_field(name = "**E**", value ="Bronze", inline = False)
    await ctx.send(embed = embed)


#comandos de informativos dos ranks de party

@client.command()
async def inforankp(ctx):
    embed = discord.Embed(
        title = "**RANK da PARTY**",
        description = "Esses são todos os _ranks_ de party",
        color = discord.Colour.red()
    )
    
    embed.set_author(name="Guilda", icon_url="https://www.tibiawiki.com.br/images/e/e2/Adamant_Shield.gif")

    embed.set_thumbnail(url="https://www.tibiawiki.com.br/images/e/ee/Arcane_Insignia.gif")

    embed.add_field(name = "**S+ ou Heroico**", value ="certificado de grupo rank **Heroico** ganha 1 platina extra cartão guilda **Heroico**", inline = False)
    embed.add_field(name = "**S ou Lendario**", value = "certificado de grupo rank **Lendario**, ganha 50 de ouro extra e os gastos de viagens(entrada para outros reinos, hospedagens, etc) sobe missões são nulas", inline = False)
    embed.add_field(name = "**A ou Diamante**", value ="certificado de grupo rank **Diamante**, ganha 50 de prata extra e as taxas de entradas para outros reinos são nulas", inline = False)
    embed.add_field(name = "**B ou Platina**", value ="certificado de grupo rank **Platina**, ganha 5 de prata extra e as taxas de entradas para outros reinos são nulas", inline = False)
    embed.add_field(name = "**C ou Ouro**", value ="certificado de grupo rank **Ouro** além de ganha 50 de cobre extra", inline = False)
    embed.add_field(name = "**D ou Prata**", value ="certificado de grupo rank **Prata** além de ganhar 5 de cobre extra ", inline = False)
    embed.add_field(name = "**E ou Bronze**", value ="Certificado de grupo rank **Bronze**.", inline = False)
    await ctx.send(embed = embed)

#ranks individuais
@client.command()
async def ranki(ctx):
    embed = discord.Embed(
        title = "**RANK INDIVIDUAL**",
        description = "Esses são todos os _ranks_ individuais",
        color = discord.Colour.red()
    )
    
    embed.set_author(name="Guilda", icon_url="https://www.tibiawiki.com.br/images/e/e2/Adamant_Shield.gif")

    embed.set_thumbnail(url="https://www.tibiawiki.com.br/images/e/ee/Arcane_Insignia.gif")

    embed.add_field(name = "**S+**", value ="Maior Que Santo", inline = False)
    embed.add_field(name = "**S**", value = "Santo", inline = False)
    embed.add_field(name = "**A+**", value ="Maior Que Anjo", inline = False)
    embed.add_field(name = "**A**", value ="Anjo", inline = False)
    embed.add_field(name = "**R**", value ="Rei", inline = False)
    embed.add_field(name = "**E**", value ="Explorador", inline = False)
    embed.add_field(name = "**I**", value ="Iniciante", inline = False)
    await ctx.send(embed = embed)

#comandos informatifos dos ranks individuais

@client.command()
async def inforanki(ctx):
    embed = discord.Embed(
        title = "**RANK INDIVIDUAL**",
        description = "Uma breve descrição dos _**ranks individuais**_",
        color = discord.Colour.red()
    )
    
    embed.set_author(name="Guilda", icon_url="https://www.tibiawiki.com.br/images/e/e2/Adamant_Shield.gif")

    embed.set_thumbnail(url="https://www.tibiawiki.com.br/images/e/ee/Arcane_Insignia.gif")

    embed.add_field(name = "**S+ ou MAIO que SANTO**", value ="Precisa de ? Xp da guilda, s(Apito para combate com criaturas classificadas com o rank S+ e contem viagem para outros continentes)", inline = False)
    embed.add_field(name = "**S ou SANTO**", value = "Precisa de ? Xp da guilda, (Apito para combate com criaturas classificadas com o rank S e podem conter viagens para outros continentes)", inline = False)
    embed.add_field(name = "**A+ ou MAIOR que ANJO**", value ="Precisa de ? Xp da guilda, (Apito para combate com criaturas classificadas de A+ e contem viagens para outros reinos)", inline = False)
    embed.add_field(name = "**A ou ANJO**", value ="Precisa de ? Xp da guilda, (Apito para combate com criaturas de rank A e podem conter viagens para outros reinos)", inline = False)
    embed.add_field(name = "**R ou REI**", value ="Precisa de ? Xp da guilda, (Apito para viagens longas e Combate com criaturas de rank R)", inline = False)
    embed.add_field(name = "**E ou EXPLORADOR**", value ="Precisa de ? Xp da guilda, (Apito para explorações simples e combate com criaturas de rank E)", inline = False)
    embed.add_field(name = "**I ou INICIANTE**", value ="Precisa de 0 Xp da guilda, (Sem combate)", inline = False)
    await ctx.send(embed = embed)

#fim dos comandos informativos dos ranks individuais

#comandos normais
@client.command()
async def ola(ctx):
    msg = (f"Olá, {ctx.author.mention} como posso ajudar?")
    await ctx.send(msg)

#comandos missões
@client.command()
async def missoes(ctx):
    msg = (f"No momento não temos missões, volte mais tarde.")
    await ctx.send(msg)



client.run(token)