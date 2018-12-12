def temp_cnv(var):
    try:
        return int(var)
    except ValueError as ve:
        print('The Argument Does Not contain Number',ve.args)

temp_cnv('AB')