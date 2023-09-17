def fatorial(num):
 if(num == 1):
  return 1
 else:
    return num * fatorial(num-1)

def fatorial_ternario(num):
 return 1 if num ==1 else num * fatorial(num -1)

print(fatorial_ternario(5))
print(fatorial(5))
