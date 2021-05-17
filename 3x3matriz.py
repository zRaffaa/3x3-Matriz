matriz = []

somaMaior10 = 0

for li in range(0,3):

  linha = []

  for co in range(0,3):

    linha.append(int(input(f'Digite numero lin={li} col={co}')))

  matriz.append(linha)



for li in range(0,3):

  for co in range(0,3):

    if (matriz[li][co] > 10):

      somaMaior10 += 1



    print (f'[{matriz[li][co]:^4}]',end='')

  print ()



print ("A quantidade maior que 10 ",somaMaior10)



 
 
   
   
   
