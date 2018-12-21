import  re
pattern = r"(0|\+91)\d{10}"
if re.match(pattern,"09898989898"):
    print('Match')
else:
    print('Not Match')
