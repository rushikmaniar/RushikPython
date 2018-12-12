import traceback
def temp_cnv(var):
    try:
        return int(var)
    except :
        print('Trackback: \n',traceback.format_exc())

temp_cnv('AB')