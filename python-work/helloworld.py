def main():
  print "hello, world!"

def duck_typing(a, b):
  print a+b
 
if __name__ == "__main__":
  main()
  duck_typing(5, 4)
  duck_typing("5", "4")
  try:
    duck_typing(5, "4")
  except:
    print "+ isn't defined for int+str"
  finally:
    print "ciao world!"
