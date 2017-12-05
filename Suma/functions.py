"""JUAN PABLO RAMIREZ IBARRA
GITI9072-E

SUMA DE DOS NUMEROS"""
def vent_net(vent_tot: float, dev: float, desc: float) -> float:
    """This program calculate the net sales."""
    vents_nets = vent_tot - (dev + desc)
    return vents_nets


def comp_tot(num1: float, num2: float) -> float:
    """This program calculate the total sales."""
    tot = num1 + num2
    return tot
