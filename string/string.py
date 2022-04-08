class basic:
    def copy_str(self, x, y):
      a1 = basic()
      if len(y) == 0:
        print(x)
      else:
        c = a1.copy_str(x, (y)[1:-1])
        print(c)

lsbasic = basic()
x = input('enter a first name here:')
y = input('enter a second name here:')
lsbasic.copy_str(x, y)        
