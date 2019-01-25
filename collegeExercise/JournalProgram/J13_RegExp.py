'''
    13.Write a regular expression program for validating mobile number(10 digits,starting with 8or9) and validating email id.
'''
import  re

#Validating mobile starting with 8 or 9
print("Mobile Validation MobileNo : 7898989898")
pattern = r"(8|9)\d{9}"
if re.match(pattern,"7898989898"):
    print('Match')
else:
    print('Not Match')

#email validating

print("Email Validation email:rus@gmail.com")
pattern = "r[\w\.-]+@[\w\.-]+"
if re.match(pattern,"rus@gmail.com"):
    print('Match')
else:
    print('Not Match')
