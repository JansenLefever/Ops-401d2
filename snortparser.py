#!/usr/bin/python3

def scanner():
  file_name = input("Please input a file to scan. \n:")
  f = open(file_name)
  results1 = f.read().splitlines()

  searching = True
  while searching:
    parser = input("What would you like to search for? \n:")
    results1 = list(filter(lambda x: parser in x, results1))
    for line in results1:
      print(line)
    search_more = input("would you like to search further y/n? \n:")
    if (search_more != 'y'): searching = False

looping = True
while looping:
  print("""What would you like to do:
  1) Scan snort file
  2) exit""")
  choice = input(":")
  if (choice == "1"):
    scanner()
    looping = False
  elif (choice == "2"):
    print("Exiting program")
    looping = False
  else:
    print("Incorrect input")  