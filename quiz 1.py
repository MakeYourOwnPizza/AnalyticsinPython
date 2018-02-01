x = 1
def change(x):
        x = 2
x = 3
change(x)
print(x)


def func(a, b=1, c=3):
    print(a, b, c)
func(1, 2) 
func(5, c = 6)

def func(x):
  return x
print(func(1))
