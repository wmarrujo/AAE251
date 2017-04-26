from Launch import *

################################################################################
# REFERENCE NUMBERS
################################################################################

# UNIVERSAL CONSTANTS

G = 6.67408e-11 # m^3/(kg*s^2) # universal gravitation constant

# EARTH CONSTANTS

g0 = 9.80665 # m/s^2 # gravitational acceleration at sea level
mEarth = 5.9723e24 # kg # mass of earth
rEarth = 6378137 # m # radius of earth
muEarth = G * mEarth # m^3/s^2

# ATMOSPERE PARAMETERS

airIdealGasConstant = 287.058 # J/(kg*K) # ideal gas constant of air
airHeatCapacityRatio = 1.4 # unitless # ratio of specific heats

# LAUNCH LOSSES

dVdragLoss = dragLossUpToAltitude(0) # m/s
dVgravityLoss = gravityLossUpToAltitude(0) # m/s
dVSteeringLoss = steeringLoss() # m/s

# TRANSFERS

dVfor500 = 195.40362680297374 + dVdragLoss + dVgravityLoss + dVSteeringLoss # m/s
dVforGeoTransfer = 2467.596447585046 + dVdragLoss + dVgravityLoss + dVSteeringLoss # m/s
dVforGeoStatOrbit = 4478.0452652 + dVdragLoss + dVgravityLoss + dVSteeringLoss # m/s

# ROCKET INFORMATION

# [(name of rocket, Isp, mass, fuel capacity)]

#[Stage 1 , Stage 2]

f_inert = [0.08, 0.12] # inert mass fraction 
Isp = [310, 360] # s
dV = [5000, 2000] #m/s
m_pay = 10000 #kg
dV_needed = 9000 # m/s
m_inert = [10000]

f_inert = [.08,.15] # inert mass fraction 
Isp = [360, 360] # s
payload = 5000
fairing = 1000
m_pay = payload+fairing #kg


# PARAFOIL INFORMATION

#Found Cd using m*g = .5*Cd*rho*A*vt**2 (Drag at Terminal Velocity, solved for Cd)
CdChute = 2.510418402

# ORBIT INFORMATION

h1 = 200000 #m
h2 = 500000 #m
delta = 28.474 #Degrees

# TURBOFAN DATA

# [(Model, Bypass (min), Bypass (max), Length (min) (m), Length (max) (m), Fan diameter (min) (m), Fan diameter (max) (m), Weight (min) (kg), Weight (max) (kg), Thrust (min) (N), Thrust (max) (N))]
turbofanData = [
    ("GE GE90", 8.7, 9.9, 5.18, 5.40, 3.12, 3.25, 6858.32, 7819.93, 330000, 510000),
    ("P&W PW4000", 4.8, 6.4, 3.37, 4.95, 2.84, float('nan'), 3792.03, 6785.74, 222000, 436000),
    ("R-R Trent XWB", 9.3, float('nan'), 5.22, float('nan'), 3.00, float('nan'), 6604.31, float('nan'), 330000, 430000),
    ("R-R Trent 800", 5.7, 5.8, 4.37, float('nan'), 2.79, float('nan'), 5406.82, 5424.97, 411000, 425000),
    ("EA GP7000", 8.7, float('nan'), 4.75, float('nan'), 2.95, float('nan'), 5524.76, 6087.21, 311000, 363000),
    ("R-R Trent 900", 8.7, float('nan'), 4.55, float('nan'), 2.95, float('nan'), 5606.40, 5669.91, 340000, 357000),
    ("R-R Trent 1000", 10.8, 11.0, 4.74, float('nan'), 2.85, float('nan'), 5234.46, float('nan'), 265300, 360400),
    ("GE GEnx[36]", 8.0, 9.3, 4.31, 4.69, 2.66, 2.82, 5098.38, 5279.82, 296000, 339000),
    ("R-R Trent 700", 4.9, float('nan'), 3.91, float('nan'), 2.47, float('nan'), 4345.42, float('nan'), 320000, 0),
    ("GE CF6", 4.3, 5.3, 4.00, 4.41, 2.20, 2.79, 3465.45, 4608.50, 222000, 298000),
    ("R-R Trent 500", 8.5, float('nan'), 3.91, float('nan'), 2.47, float('nan'), 4281.91, float('nan'), 252000, 0),
    ("P&W PW1000G[37]", 9.0, 12.5, 3.40, float('nan'), 1.42, 2.06, 2594.55, float('nan'), 67000, 160000),
    ("CFM LEAP[38]", 9.0, 11.0, 3.15, 3.33, 1.76, 1.98, 2521.97, 2857.63, 100000, 146000),
    ("CFM56", 5.0, 6.6, 2.36, 2.52, 1.52, 1.84, 1769.01, 2394.97, 97900, 151000),
    ("IAE V2500", 4.4, 4.9, 3.20, float('nan'), 1.60, float('nan'), 2140.96, 2304.25, 97900, 147000),
    ("P&W PW6000", 4.9, float('nan'), 2.73, float('nan'), 1.44, float('nan'), 2140.96, float('nan'), 100200, 0),
    ("R-R BR700", 4.2, 4.5, 3.41, 3.60, 1.32, 1.58, 1478.71, 1914.16, 68900, 102300),
    ("GE Passport", 5.6, float('nan'), 3.37, float('nan'), 1.30, float('nan'), 1877.87, float('nan'), 78900, 84200),
    ("GE CF34", 5.3, 6.3, 2.62, 3.26, 1.25, 1.32, 671.32, 1016.05, 41000, 82300),
    ("R-R Tay", 3.1, 3.2, 2.41, float('nan'), 1.12, 1.14, 1288.20, 1387.99, 61600, 68500),
    ("Silvercrest", 5.9, float('nan'), 1.90, float('nan'), 1.08, float('nan'), 988.83, float('nan'), 50900, 0),
    ("R-R AE 3007", 5.0, float('nan'), 2.71, float('nan'), 1.11, float('nan'), 653.17, float('nan'), 33700, 0),
    ("P&WC PW300", 3.8, 4.5, 1.92, 2.07, 0.97, float('nan'), 408.23, 426.38, 23400, 35600),
    ("HW HTF7000", 4.4, float('nan'), 2.29, float('nan'), 0.87, float('nan'), 562.45, float('nan'), 28900, 0),
    ("HW TFE731", 2.7, 3.9, 1.52, 2.08, 0.72, 0.78, 308.44, 408.23, 15600, 22200),
    ("Williams FJ44", 3.3, 4.1, 1.36, 2.09, 0.53, 0.57, 190.51, 217.72, 6700, 15600),
    ("P&WC PW500", 3.9, float('nan'), 1.52, float('nan'), 0.70, float('nan'), 254.01, float('nan'), 13300, 0),
    ("GE-H HF120", 4.4, float('nan'), 1.12, float('nan'), 0.54, float('nan'), 163.29, float('nan'), 7400, 0),
    ("P&WC PW600", 1.8, 2.8, 0.67, float('nan'), 0.36, float('nan'), 136.08, float('nan'), 6000, 0)],
