import discord, discord.ext.commands, discord.ext.tasks, asyncio #Discord API Wrapper, Commands Framework, Background loop Framework and Asyncio library
import configparser, pathlib, random #Other stuff
import cogs.rakbotbase #Base cog

if __name__ == "__main__": #Must be main file
    ini = configparser.ConfigParser()
    ini.read(pathlib.Path(__file__).parent.absolute()/"rakbot.ini") #Open ini

    RAKBOT = discord.ext.commands.Bot(ini.get("General", "CommandPrefix")) #Decare the bot         
    RAKBOT.add_cog(cogs.rakbotbase.RakBotBase(RAKBOT))
    
    RAKBOT.run(ini.get("General", "Token")) #Login