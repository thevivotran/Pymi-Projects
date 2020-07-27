n = int(input("Nhập số n: "))

def oddeven(n):
  res = 0
  for i in range (1,n+1):
    if i % 2 != 0:
      print(i," là một số lẻ")
      res += 1
  print("Có",res,"số lẻ")

def snt(n):
  for i in range (2,round(n**(1/2))):
    if n % i == 0:
      return True
  return False

snt(n)