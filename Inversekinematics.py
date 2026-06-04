import numpy as np  
import matplotlib.pyplot as plt

l1 = 6  # fixed arm lengths
l2 = 5

def on_click(event):
    plt.clf() 
    x = event.xdata 
    y = event.ydata
    d = (x**2) + (y**2)
    a2 = np.arccos((d - (l1**2) - (l2**2)) / (2*l1*l2))
    a1 = np.arctan2(y, x) - np.arctan2(l2 * np.sin(a2), l1 + l2 * np.cos(a2))
    angle1 = np.degrees(a1)
    angle2 = np.degrees(a2)
    x1 = l1 * np.cos(a1)
    y1 = l1 * np.sin(a1)
    x2 = l2 * np.cos(a2 + a1)
    y2 = l2 * np.sin(a1 + a2)
    A = x1 + x2
    B = y1 + y2
    plt.plot([0,x1],[0,y1])
    plt.plot([x1,A],[y1,B])
    plt.plot(0.0,'o')
    plt.plot(x1,y1,'o')
    plt.plot(A, B, 'o')
    plt.axis('equal')
    plt.grid(True)
    plt.draw()  

fig, ax = plt.subplots()
fig.canvas.mpl_connect('button_press_event', on_click)
plt.axis('equal')
plt.grid(True)
plt.xlim(-15, 15)  # set screen size
plt.ylim(-15, 15)
plt.show()       