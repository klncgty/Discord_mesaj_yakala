#goals:
# generate a csv of every single member on the LabDAO discord with these fields:
#ID, Nickname, discord name, roles (maybe separated at some point), date joined, sorted by order joined

import disnake 
from disnake.ext import commands
from disnake.ext.commands import Context
import pandas as pd 
import datetime



class Member_CSV(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot 
        self.category = 'Backend'

    @commands.command(
        name = 'üyeCSV',
        description  = 'herbir üye için rolü ve mesajlarını içeren csv listeler'
    )
    @commands.has_permissions(administrator=True)
    async def memberCSV(self, context: Context) -> None:
        columns = ['Kullanıcı adı', 'Nickname', 'Discriminator','Rol','Katılma Tarihi']
        df = pd.DataFrame(columns = columns)
        guild = context.guild
        members = guild.members

        for member in members:
            if member.nick == None:
                nick = member.name
            else:
                nick = member.nick
            user = member.name 
            d_id = member.id
            disc = member.discriminator
            roles = []
            for role in member.roles[1::]:
                roles += [str(role)]
            joined = member.joined_at
            temp_df = pd.DataFrame(data = {'Kullanıcı adı': [user],
                                    'Nickname' : [nick],
                                    'Discriminator': [disc],
                                    'Rol': [roles],
                                    'Katılma Tarihi' : [joined.strftime("%m/%d/%Y, %H:%M:%S")]})
            df = pd.concat([df, temp_df], ignore_index = True)

        df.sort_values(by = ['Nickname']).reset_index
        df.to_csv(f'{self.bot.config["output_url"]}/{guild.name}_members.csv', sep = ',')
        print('Finished Running')      

def setup(bot):
    bot.add_cog(Member_CSV(bot))      