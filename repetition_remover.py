import os

try:
    os.remove("output/repetition_remover_output.txt")
except:
    pass

obj = open("My Clippings.txt","r")
contents = obj.read()
obj.close()

newContents = contents.split("==========\n")
#print len(newContents)
newContents = newContents[0:int(len(newContents))-1]
#newContents = list(set(newContents)) #not used here as tuple method can remove the duplicated elements but destroy the order.

temp_set = ()
temp_newContents = []

for i in newContents:
    if i not in temp_set:
        temp_newContents.append(i)
        temp_set += (str(i),)

newContents = temp_newContents

glue = "==========\n"
newContents = glue.join(newContents) + "=========="

obj = open("output/repetition_remover_output.txt", "w")
obj.writelines(newContents)
obj.close()

print "done."
