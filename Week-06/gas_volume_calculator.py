GAS_CONSTANT = 8.3144621

def compute_gas_volume(pressure, temperature, moles):
    return (moles * GAS_CONSTANT * temperature) / pressure

pressure = float(input())
moles = float(input())
temperature = float(input())

print(compute_gas_volume(
    pressure,
    temperature,
    moles
))
