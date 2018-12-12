def temp_cnv(var):
    try:
        return int(var)
    except Exception as e:
        print('General Exception: \n',e.args)

temp_cnv('AB')