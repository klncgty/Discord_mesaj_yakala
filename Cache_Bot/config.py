import os

def Config():
    config={
            "token":'MTIwNjkwNjQ4MTM0MjAyNTc2OQ.GGy_-F.Kd8qxdG46m5Vksglx9vUORzuKsbbc3Y83KCpF4',
            "command_pref":"!!",
            "permissions":66560,
            "output_url" : f'{os.path.dirname(os.path.realpath(__name__))}/Output_CSVs'
            }
    return config