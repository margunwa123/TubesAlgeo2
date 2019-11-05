
# KAMUS
# var v : array of integer
# var w : array of integer

# MAIN PROGRAM
import array as arr
x = int(input("Masukkan jumlah unit vektor: "))
w = arr.array('i',[0])
v = arr.array('i',[0])

for i in range (1,x+1):
    y = int(input("Masukkan unit vektor v ke-" + str(i)+":" ))
    v.insert(i+1,y)
    w.insert(i+1,i)

sum = 0
for i in range (1,x+1):
    sum = sum + ((v[i] - w[i])**2)
total = sum ** (1/2)
print(total)


