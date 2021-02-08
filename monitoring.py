import pandas as pd
import time
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
    print("map : " + str(ordermap))        
    return ordermap

def get_static_data(pid, columnslist):
    data = {pid:{}} 

    for targetdir in columnsmap.keys():
        location = "/proc/"+pid+"/"
        location += targetdir # set target location	
	# get data
        result = os.popen("cat "+location).read()

        if targetdir == "status":
	    result = result.replace("\t","").split("\n")
            for index,val in enumerate(result):
                result[index] = val.split(":")
            for column in columnsmap[targetdir]:
                for item in result: # ex) ["Ppid","4232"]
                    if column == "CMD1": # CMD1 == Name
                        if "NAME" == item[0].upper():
                            data[pid][column] = item[1]
                            continue
                    if column == item[0].upper():
                        data[pid][column] = item[1]
        elif targetdir == "cmdline":
            data[pid]["CMD2"] = result.replace("\x00","")
    print(data)
    return data


def start_parsing(targetlist, columnslist, pidlist):
    # make map
    ordermap = make_map(columnslist)
    # start parsing by pid
    rows = {}
    for pid in pidlist:
	# get static data
	rows.update(get_static_data(pid, columnslist))
    # get dinamic data  ex) cpu usage
    print(rows)
    
    # Fit order with columnlist
    total = []
    for key in rows:
        tmp = [0]*len(rows[key])
        print(rows[key])
        print(tmp)
        for column in rows[key]:
            index = columnslist.index(column) 
            tmp[index] = rows[key][column]
        total.append(tmp)
    
    columnslist.insert(0,"TIME")
    for row in total:
        row.insert(0,int(time.time()))
    t = pd.DataFrame(total, columns=columnslist, index=None)
    print(t)
    t.to_csv("static.csv")
        
   
if __name__ == '__main__':
    #get target pid
    targetlist = get_target_name()    
    columnslist = get_columns()    
    pidlist = use_shell("pidof",targetlist)

    #start parsing
    start_parsing(targetlist, columnslist, pidlist)
    
