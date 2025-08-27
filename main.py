# by pan$i ==> guns.lol/x0202s
import discord
from discord.ext import commands 
import asyncio 
import os 
 
intents = discord.Intents.default() 
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents) 
@bot.event 
async def on_ready(): 
    print(f'ready') 
    
    try: 
        synced = await bot.tree.sync() 
        print(f"comandos slash sincronizados: {len(synced)}") 
    except Exception as e: 
        print(f"error synchronizing commands: {e}") 
     
     
@bot.tree.command(name='spamiza', description='spam the current channel') 
async def spam(interaction: discord.Interaction): 
    message = ( "# JOIN KHS\n" 
               "https://discord.gg/M4bbNhPY\n" 
               "https://youtu.be/9CAWNeYrohU?si=WiFb8iHZd8dkpfjy\n" # replace this with your spam message 
            ) 
    await interaction.response.send_message("iniciando xd...", ephemeral=True) 
    for _ in range(10): 
        await interaction.followup.send(message) 
    await asyncio.sleep(0.1) 
 
bot.run("") # put ur bot token between the quotation marks
