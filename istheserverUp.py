#Python script to check if the minecraft log.lck file exists

server_loc = "./minecraft.txt"
server_file = "/server.log.lck"
#try to read the location of the server off a .txt file.
try:
    loc_file = open(server_loc, 'r')
    loc_text = loc_file.read()
except:     #if it does not exist, propmt for the location, and save it.
    new_file = open(server_loc, 'w')
    loc_text = input("Please enter the location of you server: ")
    new_file.write(loc_text)
    new_file.close()
    
loc_text = loc_text + server_file

#attempt to open the .lck file in the server dir.
exists = True
try:
    open(loc_text)
except:
    exists = False
    #if it does not exist set false
print exists
