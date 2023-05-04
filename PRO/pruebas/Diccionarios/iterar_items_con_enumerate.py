a = {'a':'p','b':'t'}
for index,(key,value) in enumerate(a.items(),start=1):
    print(f'{index} - {key}: {value}')