name = input("请输入名字带后缀")
a = open(name,"r")
coutent = a.read()

s = name.rfind(".")
name[0:s]









b = open(name+"复制","w")
b.write(contet)

a.close
b.close
