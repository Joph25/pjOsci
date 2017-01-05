import visa
rm = visa.ResourceManager('pjSim.yaml@sim')
rm.list_resources()
inst = rm.open_resource('ASRL1::INSTR', read_termination='\n')
print(inst.query("?IDN"))
