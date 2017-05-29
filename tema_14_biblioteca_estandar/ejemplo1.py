import os 
for variable, valor in os.environ.items(): 
    print("%s: %s" % (variable, valor))