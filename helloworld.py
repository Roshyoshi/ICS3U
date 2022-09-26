from itertools import accumulate

def check(*a):
  valid = lambda x : x > 0 and x <= 15
  accumulate((lambda x y x and y), map(valid, a))

def main():
  values = list("length", "width", )
  
