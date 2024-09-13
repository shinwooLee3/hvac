import math

def enthalpy_given_dbt_rh(t, rh, P_atm=14.7):

    # Step 1: Convert Temperature to Rankine
    r = t + 459.67

    # ASHRAE Fundamentals 2017 CH1 eq.6
    c8 = -1.044039*10000 # -1.044039*math.pow(10,4)
    c9 = -1.129465*10 # -1.129465*10
    c10 = -2.7022355*0.01 # -2.7022355*math.pow(10,-2)
    c11 = 1.2890360*0.00001 # 1.2890360*math.pow(10,-5)
    c12 = -2.4780681*0.000000001 # -2.4780681*math.pow(10,-9)
    c13 = 6.5459673 # 6.5459673

    # Step 2: Calculate Saturation Vapor Pressure (P_ws) using empirical formula
    P_ws = math.exp(c8/r + c9 + c10*r + c11*r*r + c12*r*r*r + c13*math.log(r)) # ASHRAE Fundamentals 2017 CH1 eq.6

    # Step 3: Calculate Actual Vapor Pressure (P_w)
    P_w = (rh / 100) * P_ws

    # Step 4: Calculate Humidity Ratio (W)
    w = 0.621945 * (P_w / (P_atm - P_w)) # ASHRAE Fundamentals 2017 CH1 eq.20

    # Step 5: Calculate Enthalpy (h)
    h = 0.24 * t + w * (1061 + 0.444 * t) # ASHRAE Fundamentals 2017 CH1 eq.30

    return h

'''
# Example calculation
t = 80  # Temperature in Fahrenheit
rh = 50  # Relative Humidity in %

enthalpy = enthalpy_given_dbt_rh(t, rh)

print(f"Enthalpy of moist air: {enthalpy:.2f} BTU/lb")
'''