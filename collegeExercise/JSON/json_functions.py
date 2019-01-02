'''
json functions
'''
import  json
data = {
    'people':[
        {
            'name':'Scott',
            'Website':'google.com',
            'from':'India'
        }
    ]
}

a = json.dumps(data,indent=4)
print(a)

person = json.loads(a)
print(a)

with open('data.json','w') as json_file:
    json.dump(a,json_file)

with open ('data.json','r') as file1:
    a = json.load(file1)
    print(a)
