import json 
import os 
import platform 
import random 
import sys
from datetime import time  

import disnake 
from disnake.ext import commands
from disnake import ApplicationCommandInteraction  
from disnake.ext.commands import Bot
from disnake.ext.commands import Context 


from config import Config 



class Cache_Bot(commands.Bot):
    
    config = Config()
    

    intents = disnake.Intents.default()

    intents.dm_messages = True 
    intents.dm_reactions = True
    intents.members = True 
    intents.guild_typing = True 
    intents.typing = False
    intents.presences = False
    intents.reactions = True
    intents.message_content = True
    
    def __init__(self,config = config, intents = intents):
        
        self.config = config
        
        
        super().__init__(command_prefix = commands.when_mentioned_or(config['command_pref']),
                         intents = intents, 
                         case_insensitive = True )
        
        self.autoload_extensions('cache_command')
        
       
    
    # bu klasördeki tüm py dosyalarını main'e aktarmak için bir fonksiyon
    def autoload_extensions(self, command_type):
        for file in os.listdir(f'./{command_type}'):
           extension = file[:-3]
           end = file[-3:]
           
           if end == '.py':
               try:
                   self.load_extension(f"{command_type}.{extension}")
                   print(f" {extension} dosyası oluşturuldu !")
               except Exception as e:
                   exception = f"{type(e).__name__}: {e}"
                   print(f" {exception} yüzünden {extension} dosyası yüklenemedi")
           else:
                print(f' {file} dosyası reddedildi')
    
if __name__ == '__main__':
    bot = Cache_Bot()
    token = bot.config['token']
    #bot.remove_command('help')
    #bot.autoload_extensions('help')
    
    if token is not None:
        bot.run(token)
        print("Bot Bağlandı")
    else:
        print('Bot bağlanamadı !')