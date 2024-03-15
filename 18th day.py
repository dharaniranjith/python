#dict kula dict
'''new={"emp1":{"name":"arun","dep":"python"},
     "emp2":{"name":"balaji","dep":"java"},
     "emp3":{"name":"divi","dep":"cobal"}}
     "emp4":{"name":"sagar","dep":"cobal"}}
for i,j in new.items():
         print(i)
         for key,val in j.items():
             print(key,val)'''
#emply name and salary
'''new={"a":30,"b":40,"c":25,"d":60}
max_salary=max(new.values())
print(f"the highest salary:{max_salary}")'''
'''new={"a":30,"b":40,"c":25,"d":60}
b=max(new,key=new.get)
c=new[b]
for d in b,c:
      print(d)'''
#second duplicate value
'''a={"a":4,"b":5,"c":7,"d":5,"e":9,"f":8,"g":9}
b=[]
c=[]
for i,j in a.items():
    if j not in b:
        b.append(j)
    else:
        c.append(j)
output=c[-2]
for i,j in a.items():
    if j==output:
        print(i,j)'''
# print in dict any key i type means value should be print
c= {'glossary':[
    {'title':'example glossary','Glossdiv':
    {'title':'s','Glosslist':
     {'GlossEntry':
                {'ID':'SGML','SortAS':'SGML','GlossTerm':'Standard Generalized Markup Language',
                 'Acronym':"SGML",'Abbrev':'ISO 8879:1986','GlossDEf':
                     {'para':'A meta-markup language,used to create markup languages such as Docbook.',
                          'GlossSeeAlso':['GML','XML']},'GlossSee':'markup'}}}}]} 

'''for key, value in c.items():
    print(f"{key}: {value}")
for i,j in c.items():
    print(i)
    for k in j:
        for k,l in k.items():'''
            
keys_to_extract = ['title', 'GlossTerm', 'Acronym', 'GlossDEf', 'GlossSeeAlso']
values = [c['glossary'][0]['Glossdiv']['Glosslist']['GlossEntry'][key] for key in keys_to_extract]

# Printing the results
for key, value in zip(keys_to_extract, values):
    print(f'{key}: {value}')
