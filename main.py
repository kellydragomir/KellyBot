import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())


@bot.slash_command()
async def mason(interaction: disnake.AppCmdInter):
    await interaction.send("Mason Helper лох")

@bot.slash_command()
async def swaston(interaction: disnake.AppCmdInter):
    await interaction.send("Свастон, кидай зигу")
    await interaction.send("https://i.imgur.com/QJi2304.jpg")

@bot.slash_command()
async def zahar(interaction: disnake.AppCmdInter):
    await interaction.send("<@385775087636447232> ты пидорас")

@bot.slash_command()
async def maksim(interaction: disnake.AppCmdInter):
    await interaction.send("Усики - пропуск в трусики")
    await interaction.send("https://i.imgur.com/W2XgJid.jpg")

@bot.slash_command()
async def semo4ka(interaction: disnake.AppCmdInter):
    await interaction.send("https://i.imgur.com/uN5ToD3.jpg")
    await interaction.send("Хуи люблю и на хуе вертелся, правда <@526231090541756418>?")

@bot.slash_command()
async def lesbian(interaction: disnake.AppCmdInter):
    await interaction.send("https://media.tenor.com/ad3PA3NIS8gAAAAd/mencia-rebeka.gif")

@bot.slash_command()
async def salt(interaction: disnake.AppCmdInter):
    await interaction.send("<@385775087636447232> заебал со своей солью, долбоеб")
    await interaction.send("https://media.tenor.com/JoKsQILIIpAAAAAd/cat-kamaru.gif")

bot.run("MTA2MTI2MzQ2NDE5NjIxMDY4OA.GAm5p5.puSpCPZ9-CpvtmuIUqlYFTbmd5Xn9aeWG3N3Ac")