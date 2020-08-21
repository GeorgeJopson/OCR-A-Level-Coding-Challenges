#Solution (1 line):
print("\n".join([((str(bottles)+" bottles sitting on the wall,\n")*2+"And if one green bottle should accidentally fall,\n"+"There’ll be "+str(bottles-1)+" green bottles sitting on the wall.\n") for bottles in range(10,0,-1)]))
