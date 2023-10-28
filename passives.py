# Module for passive component algorithms 
# https://en.wikipedia.org/wiki/Electrical_reactance#Inductive_reactance
# https://en.wikipedia.org/wiki/Electrical_reactance#Capacitive_reactance

import math

def ind_reactance(inductance: float, frequency: float, reactance: float):
    """
    Calculate inductive reactance, frequency or inductance from two given electrical
    properties then return name/value pair of the zero value in a Python dict.

    Parameters
    ----------
    inductance : float with units in Henries
    frequency : float with units in Hertz
    reactance : float with units in Ohms

    >>> ind_reactance(-35e-6, 1e3, 0)
    Traceback (most recent call last):
        ...
    ValueError: Inductance cannot be negative

    >>> ind_reactance(35e-6, -1e3, 0)
    Traceback (most recent call last):
        ...
    ValueError: Frequency cannot be negative

    >>> ind_reactance(35e-6, 0, -1)
    Traceback (most recent call last):
        ...
    ValueError: Reactance cannot be negative

    """

    if (inductance, frequency, reactance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if inductance < 0:
        raise ValueError("Inductance cannot be negative")
    if frequency < 0:
        raise ValueError("Frequency cannot be negative")
    if reactance < 0:
        raise ValueError("Reactance cannot be negative")
    if inductance == 0:
        return {"inductance": reactance / (2*math.pi*frequency)}
    elif frequency == 0:
        return {"frequency": reactance / (2*math.pi*inductance)}
    elif reactance == 0:
        return {"reactance": 2*math.pi*frequency*inductance}
    else:
        raise ValueError("Exactly one argument must be 0")

    
def cap_reactance(capacitance: float, frequency: float, reactance: float):
    """
    Calculate capacitive reactance, frequency or inductance from two given electrical
    properties then return name/value pair of the zero value in a Python dict.

    Parameters
    ----------
    capacitance : float with units in Farads
    frequency : float with units in Hertz
    reactance : float with units in Ohms

    >>> cap_reactance(-35e-6, 1e3, 0)
    Traceback (most recent call last):
        ...
    ValueError: Capacitance cannot be negative

    >>> cap_reactance(35e-6, -1e3, 0)
    Traceback (most recent call last):
        ...
    ValueError: Frequency cannot be negative

    >>> cap_reactance(35e-6, 0, -1)
    Traceback (most recent call last):
        ...
    ValueError: Reactance cannot be negative

    """

    if (capacitance, frequency, reactance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if capacitance < 0:
        raise ValueError("Capacitance cannot be negative")
    if frequency < 0:
        raise ValueError("Frequency cannot be negative")
    if reactance < 0:
        raise ValueError("Reactance cannot be negative")
    if capacitance == 0:
        return {"capacitance": 1 / (2*math.pi*frequency*reactance)}
    elif frequency == 0:
        return {"frequency": 1 / (2*math.pi*capacitance*reactance)}
    elif reactance == 0:
        return {"reactance": 1 / (2*math.pi*frequency*capacitance)}
    else:
        raise ValueError("Exactly one argument must be 0")
    

def resonance(capacitance: float, inductance: float, frequency: float):
    """
    Calculate capacitance, inductance or resonance frequency.

    Parameters
    ----------
    capacitance : float with units in Farads
    inductance : float with units in Henries
    frequency : float with units in Hertz
    """
        
    if (capacitance, inductance, frequency).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    elif inductance == 0:
        return {"inductance": 1 / (pow(2*math.pi*frequency,2)*capacitance)}
    elif capacitance == 0:
        return {"capacitance": 1 / (pow(2*math.pi*frequency,2)*inductance)}
    elif frequency == 0:
        return {"frequency": math.sqrt(1/(4*pow(math.pi,2)*capacitance*inductance))}
    else:
        raise ValueError("Exactly one argument must be 0")
    

def ohms_law(voltage: float, current: float, resistance: float):
    """
    Calculate resistance, voltage or current by Ohms Law.

    Parameters
    ----------
    current : float with units in amps
    volts : float with units in volts
    resistance : float with units in Ohms
    """
    if (voltage, current, resistance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")  
    elif voltage == 0:
        return {"voltage": current*resistance}
    elif current == 0:
        return {"current": voltage/resistance}
    elif resistance == 0:
        return {"resistance": voltage/current}
    else:
        raise ValueError("Exactly one argument must be 0")


def power(voltage: float, current: float, resistance: float):
    """
    Calculate power from resistance, voltage or current by Ohms Law.

    Parameters
    ----------
    current : float with units in amps
    volts : float with units in volts
    resistance : float with units in Ohms
    
    Returns
    ----------
    power : float in Watts
    """
    if (voltage, current, resistance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")  
    elif voltage == 0:
        return {"power": pow(current,2)*resistance}
    elif current == 0:
        return {"power": pow(voltage,2)/resistance}
    elif resistance == 0:
        return {"power": voltage*current}
    else:
        raise ValueError("Exactly one argument must be 0")


def impedance(resistance: float, ind_reactance: float, cap_reactance: float):
    if (resistance, ind_reactance, cap_reactance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")  
    elif resistance == 0:   
        return math.sqrt(pow(ind_reactance + cap_reactance))
    elif ind_reactance == 0:   
        return 0
    elif cap_reactance == 0:
        return 0
    else:
        raise ValueError("Exactly one argument must be 0")


def divider(res_high: float, res_low, v_in: float, v_out):
    if (res_high,res_low,v_in,v_out).count(0) != 1:
        raise ValueError("One and only one argument must be 0")  
    elif v_in == 0:
        return v_out*(res_low+res_high)/res_low
    elif v_out == 0:
        return res_low/(res_high + res_low)*v_in
    elif res_high == 0:
        return ((res_low*v_in)/v_out) - res_low
    elif res_low == 0:
        return (res_high*v_out)/(v_in - v_out)
    else:
        raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
