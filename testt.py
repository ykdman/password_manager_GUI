f = open("datat.txt", mode="r")
contents = f.read()
print(len(contents))
f.close()

f1 = open("datat.txt", mode="a")
f1.write("\ntest")
f1.close()

