import  re

pattern = r"(0|\+91)\d{10}"
if re.match(pattern,"09898989898"):
    print('Match')
else:
    print('Not Match')

print('use of Reg Symbol : \\w  \\s . ^  $ *')
print(re.search(r"^\w\s{2}H*el+l.", "a \nHellllllo$").group())


print("findall()")
seq = "reg@gmail.com,rus@ymail.com"
pattern = "r[\w\.-]+@[\w\.-]+"
address = re.findall(pattern,seq)
print(address)

print("sub()")
address = re.sub(pattern,seq,"mail")
print(address)