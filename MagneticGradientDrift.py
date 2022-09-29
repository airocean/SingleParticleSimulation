from cmath import sin
import matplotlib.pyplot as plt
x_data=[]
y_data=[]
z_data=[]
t_0=0
v_x=0.1
v_y=0
v_z=0
x=0
y=0
z=0
d_t=1e-10
m=9.1e-31
q=-1.6e-19
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(x,y,z,label='Initial Position')
for t_0 in range(1,5000000):
    # 时间使用t
    t=d_t*t_0
    b_x=0
    b_y=0
    b_z=1e-6+y*0.1
    e_x=0
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
    # figure = ax.plot(x_data, y_data, z_data, c='r')
    # plt.pause(1e-100) #利用时间切片解决这个问题，十分机械、智障的方式
# print(v_y)
# plt.plot(x_data,y_data)

figure = ax.plot(x_data, y_data, z_data, label='Trajectory', c='r')
ax.set_xlabel("X/m")
ax.set_ylabel("Y/m")
ax.set_zlabel("Z/m")

plt.grid()
plt.legend()
plt.show()
    