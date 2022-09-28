from cmath import sin
import matplotlib.pyplot as plt
x_data=[0]
y_data=[0]
z_data=[0]
t_0=0
v_x=1
v_y=0
v_z=0
x=0
y=0
z=0
d_t=0.001
m=1
q=1
for t_0 in range(1,50000):
    # 时间使用t
    t=d_t*t_0
    b_x=0
    b_y=0
    b_z=1
    e_x=1
    e_y=0
    e_z=0
    x+=(v_x*d_t)
    y+=(v_y*d_t)
    z+=(v_z*d_t)
    x_data.append(x)
    y_data.append(y)
    z_data.append(z)
    f_x=(e_x*q)+q*(v_y*b_z-v_z*b_y)
    f_y=(e_y*q)+q*(v_z*b_x-v_x*b_z)
    f_z=(e_z*q)+q*(v_x*b_y-v_y*b_x)
    v_x+=(f_x*d_t/m)
    v_y+=(f_y*d_t/m)
    v_z+=(f_z*d_t/m)
# print(v_y)
# plt.plot(x_data,y_data)
fig = plt.figure()
ax = fig.gca(projection='3d')

figure = ax.plot(x_data, y_data, z_data, c='r')
ax.set_xlabel("X/m")
ax.set_ylabel("Y/m")
ax.set_zlabel("Z/m")

plt.grid()
plt.legend()
plt.show()
    