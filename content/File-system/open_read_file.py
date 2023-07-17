# get_file    = open('content\File-system\demo2.txt','r')
# get_lines   = get_file.readlines()

get_file    = open('content\File-system\demo.txt','r')
get_lines   = get_file.readlines()
new_string  = ""
print("OLD STRING = ",get_lines,"\n")

for line in get_lines:
    words = line.split(" ")
    for word in words:
        print(word+"#",end= "")
    print(" ")
# for line in get_lines:
#     after_replace   =   line.replace(" ","#")
#     new_string      =   new_string + after_replace
# print("after seperated each word by #: ",new_string)

