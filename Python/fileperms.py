
import stat, os, subprocess
#Getting search pattern from the user and assigning it to a list

#use try/excpet for error catching
try:
    #run a 'find' command and assign results to a variable
    pattern = input("Enter the file pattern to search for:\n")
    commandstring = "find " + pattern
    commandoutput = subprocess.getoutput(commandstring)
    findresults = commandoutput.split("\n")

    #output find results, along with permissions
    print("Files:")
    print(commandoutput)
    print("================================")
    for file in findresults:
        #S_IMODE -> file permissions
        # retrieves the linux file perm values for user,group, and other
        mode=stat.S_IMODE(os.lstat(file)[stat.ST_MODE])
        print("\nPermissions for file ", file, ":")
        for level in "USR", "GRP", "OTH":
            for perm in "R", "W", "X":
                if mode & getattr(stat,"S_I"+perm+level):
                    print(level, " has ", perm, " permission")
                else:
                    print(level, " does NOT have ", perm, " permission")
#print error if any errors aris
except:
    print("There was a problem - check the message above")