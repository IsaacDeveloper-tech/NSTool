from models.Machines import Machines

machines = Machines()

machines.createMachine({
    "name"          : "TMC",
    "ip_direction"  : "172.19.145.67"
})

machines.createMachine({
    "name"          : "TRAM",
    "ip_direction"  : "172.19.145.68"
})

print(machines.getMachinesByName("TM"))
