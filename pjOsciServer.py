import visa 

rm = visa.ResourceManager('@py')                      #opens the resource manager for the Raspberry Pi
rm.list_resources()                                                 #lists all available connections on your device
inst = rm.open_resource('<your resource>')     #opens your connection
print(inst.query("*IDN?"))                                    #returns the identification of your device


    
