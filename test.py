import os

def use_shell(cmd,targetlist):
    cmd += " " + targetlist[0]
    result = os.popen(cmd).read().replace("\n", "")
    result = result.split(" ")
    print "[+]result : "+ str(result)
    return result


def get_target_name():
    f = open("./target.txt")
    target = f.read().replace("\n","")# remove newline
    target = target.split(",")# split ,
    print "[+]target : " + str(target)
    f.close()
    return target

if __name__ == '__main__':
    #get target pid
    targetlist = get_target_name()    
    pidlist = use_shell("pidof",targetlist)
    
