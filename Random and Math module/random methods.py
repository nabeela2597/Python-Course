import random as r

#random() method
print(r.random())

#randint()
print(r.randint(0, 10))

#choice ()
print(r.choice('Hello'))

#seed()
r.seed(10)
print(r.random())