import random

def primary():
  print("Keep it logically awesome.")

  f = open('C:/Users/borre/github/python-random-quote/quotes.txt')
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd_quote_index = random.randint(0, last)
  print(quotes[rnd_quote_index])

if __name__== "__main__":
  primary()
