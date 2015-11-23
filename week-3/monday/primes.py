num = int(input("Enter a number: "))

if num < 0:
  print('we dont define negative prime number.')
elif num == 1:
  print('not prime, it is one')
elif num == 0:
  print('not prime, it is zero')


else:
  a = 2

  while a <= num ** 0.5:
      if (num % a == 0):
          print('not prime')
          break
      a += 1

  else:
      print('prime')

# en ezt loptam!!
