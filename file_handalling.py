__author__ = 'Asmit'
# Open a file
fo = open("if_statements.py", "r")
str = fo.read(1000)
print ("Read String is : ", str)
# Close opend file
fo.close()