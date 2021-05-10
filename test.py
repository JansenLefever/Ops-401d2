import logging, os
# Main
logging.basicConfig(filename="./example.log", level=logging.ERROR, format="%(asctime)s:%(levelname)s:%(message)s")
print("Begin logging...")
try:
  verification() # Intentional error
except Exception as msg:
  print(msg)
  logging.exception(msg)
print("Logging finished.")