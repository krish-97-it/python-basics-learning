create_file = open('content\File-system\demo2.txt','x')     # file creation by selcting method 'x'
list_lines  = ["I am Groot.\n", "I am Iron Man.\n", "I am Captain America.\n", "I am Hulk\n", "I am Black Widow.\n", "I am Captain Marvel.\n", "I am Hakwaye.\n"]
file        = open('content\File-system\demo2.txt','w')     # write something on the created
file.write("Hello world!!\n")   # single line write a single string
file.writelines(list_lines)     # multiple linses as a lists
file.close()                    # save/done

get_file    = open('content\File-system\demo2.txt','r')     # open the file with read mode, r+ for read-write both
get_lines   = get_file.readlines()      # to read multiple lines
new_string  = ""
print("OLD STRING = ",get_lines,"\n")

for line in get_lines:
    after_replace   =   line.replace(" ","#")
    new_string      =   new_string + after_replace
print("after seperated each word by #: ",new_string)