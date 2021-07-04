
from os import write


lines =  []
write_lines= []
with open("indian_liver_1.csv","r") as fp:
    lines =  fp.readlines()
    for line in lines:
        splitovano =  line.strip().split(",")
        if "" in splitovano or len(splitovano)!=11:
            continue
        if(splitovano[-1]=="1"):
            splitovano[-1]="0"
        if(splitovano[-1]=="2"):
            print("usao")
            splitovano[-1]="1"
        write_lines.append( ",".join(splitovano)+"\n")


with open("indian_liver_1.csv","w") as fp:
    fp.writelines(write_lines)