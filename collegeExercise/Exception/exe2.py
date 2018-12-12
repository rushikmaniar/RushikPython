import sys
def temp_cnv(var):
    try:
        return int(var)
    except:
        print('System Error : \n',sys.exc_info())

temp_cnv('AB')