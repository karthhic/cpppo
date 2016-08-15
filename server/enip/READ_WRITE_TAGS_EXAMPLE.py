#------PLC Tag Read and Write Code using CPPPO-----------
#------Author:Karthhic Mukil-----------------------------
from cpppo.server.enip import client
import sys

print(" ")
print("Output:")
timeout=1
port=44818
def TagData(mode,tag_name, plc_addr):								                                                #Building a function
    with client.connector( host = plc_addr, port = 44818, timeout = timeout ) as conn:     				                        #Creates a UDP connection
        operations              = client.parse_operations( [tag_name] )
        if (mode == "wr"):
            failures,transactions   = conn.process(operations=operations, depth=2, multiple=0,fragment=False, printing=False, timeout=timeout ) #Write Tag             
        elif (mode == "rd"):
            for index,descr,op,reply,status,value in conn.pipeline(operations = operations, depth = 2 ):                                        #Read tag
                pass
            if value is None:
                print("None returned while reading %s from PLC %s " % (tag_name, plc_addr))
            return index,descr,op,reply,status,value[0]

#---------------------------Sample inputs----------------------------------
#TagData("rd","Tag_Name", "192.168.0.1")
#output = TagData("rd","Tag_Name", "192.168.0.2")
#print (output[5])
#TagData("wr","Tag_Name=(DINT)%i" % (output[5]), "192.168.0.3")
