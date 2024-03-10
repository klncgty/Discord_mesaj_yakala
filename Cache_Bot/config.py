import os

def Config():
    config={
            "token":'buraya_discord_token_gelecek',
            "command_pref":"!!",
            "permissions":66560,
            "output_url" : f'{os.path.dirname(os.path.realpath(__name__))}/Output_CSVs'
            }
    return config
