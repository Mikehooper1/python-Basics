#Simple program to calculate age 

print('Answer the Question to Know how long you have lived in your life..')
name = input('Nmae:')
print('what is your age',(name),'?')
age = int(input('Age:'))

#Years, Days, hours, min, sec...

days =age*365
minutes = age*525948
seconds = age*31556926

print(name,'has been alive for',days,'days',minutes,'minutes',seconds,'seconds')
print('Thank you',name)