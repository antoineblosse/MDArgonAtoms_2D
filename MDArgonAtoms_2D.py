import pandas as pd

t = 0  # initial time
dt = 0.1  # time-step of integration
t_total = 100  # duration of simulation
N_atoms = 10  # total number of atoms
m = 1  # mass of a single Argon atom
k = 0.2  # Spring constant for molecule
x0 = 1  # Equilibrium length of the spring

x = []                      # initial x_positions
for i in range(10):
    for j in range(10):
        x.append(j)

y = []                      # initial y_positions
count = 0
for i in range(10):
    for j in range(10):
        y.append(count)
    count += 1

Vx = [0] * 100              # initial velocities
Vy = [0] * 100

Fx_0 = []
Fx_sum = 0
Fx = []                     # Each element is the sum of x_forces acting on that particle (index number)

for i in range(N_atoms):
    for j in range(N_atoms):
        Fx_0.append(k * (x[i] - x[j] - x0))
        Fx_sum = sum(Fx_0)
    Fx.append(Fx_sum)
    Fx_0 = []

# print (Fx)

Fy_0 = []
Fy_sum = 0
Fy = []

for i in range(N_atoms):
    for j in range(N_atoms):
        Fy_0.append(k * (y[i] - y[j] - x0))
        Fy_sum = sum(Fy_0)
    Fy.append(Fy_sum)
    Fy_0 = []

# print (Fy)


while t <= t_total:
    x_new = []
    y_new = []
    for i in range(N_atoms):
        x_new.append(x[i] + dt * Vx[i] + (0.5 * (dt * dt) * (Fx[i] / m)))
        y_new.append(y[i] + dt * Vy[i] + (0.5 * (dt * dt) * (Fy[i] / m)))
    x = x_new
    y = y_new
    Fx_new = []
    Fy_new = []
    for i in range(N_atoms):  # calculate new forces Fx
        for j in range(N_atoms):
            Fx_0.append(k * (x[i] - x[j] - x0))
            Fx_sum = sum(Fx_0)
        # print(Fx_0)
        Fx_new.append(Fx_sum)
        Fx_0 = []
    for i in range(N_atoms):  # calculate new forces Fy
        for j in range(N_atoms):
            Fy_0.append(k * (y[i] - y[j] - x0))
            Fy_sum = sum(Fy_0)
        # print(Fx_0)
        Fy_new.append(Fy_sum)
        Fy_0 = []
    for i in range(N_atoms):
        Vx.append(Vx[i] + 0.5 * dt * (Fx_new[i] + Fx[i]) / m)
        Vy.append(Vy[i] + 0.5 * dt * (Fy_new[i] + Fy[i]) / m)
    t = t + dt
    raw_data = {'X positions': x, 'Y positions': y}
    df = pd.DataFrame(raw_data)
    df.to_csv('Particle positions.csv', mode='a', index=False, header=False)
    df.columns = ['X positions', 'Y positions']
    print(df)
