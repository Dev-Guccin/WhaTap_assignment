import os

columnsmap = {"status":["PID","PPID","CMD1"],"cmdline":["CMD2"]}

def use_shell(cmd,targetlist):
    cmd += " " + targetlist[0]
    result = os.popen(cmd).read().replace("\n", "")
    result = result.split(" ")
    print "[+]cmd $ "+cmd+": "+ str(result)
    return result


def get_target_name():
    f = open("./target.txt")
    target = f.read().replace("\n","")# remove newline
    target = target.split(",")# split ,
    print "[+]target : " + str(target)
    f.close()
    return target

def get_columns():
    f = open("./columns.txt")
    columns = f.read().replace("\n", "")
    columns = columns.split(",")
    print "[+]columns : "+str(columns)
    f.close()
    return columns

def make_map(columnslist):
    print("[+]make map")
    ordermap = {}
    for filename in columnsmap.keys():
        for column in columnslist:
            
            for column2 in columnsmap[filename]:
                if column == column2:
                    if not ordermap.get(filename):# if not defined
            	        ordermap[filename]=[]#set list
                    ordermap[filename].append(column)
                    break
                else:
                    continue
    print(ordermap)            
    return ordermap

def start_parsing(targetlist, columnslist, pidlist):
    # make map
    ordermap = make_map(columnslist)
    # start parsing by ordermap
    
        
   
if __name__ == '__main__':
    #get target pid
    targetlist = get_target_name()    
    columnslist = get_columns()    
    pidlist = use_shell("pidof",targetlist)

    #start parsing
    start_parsing(targetlist, columnslist, pidlist)
    
