import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


#Conditions initiales ,paramètres:
N= 10 #nb_planetes
G=1
dt=0.05 #meilleur paramètre qu'on a trouvé
masse =np.random.uniform(1,5,N)
pos = np.random.uniform(0,100, (N, 2))
vit = np.zeros((N,2))

fig, ax = plt.subplots()

def distance(pos):
    diff = pos[np.newaxis, :, :] - pos[:, np.newaxis, :]
    norme = np.clip(10**(-5),np.sqrt(np.sum(diff**2, axis=2)))
    np.fill_diagonal(norme, np.inf)
    return diff, norme

def calcul_acceleration(pos,masse):
    diff, norme = distance(pos)
    m = masse[np.newaxis, :, np.newaxis]
    a=G*np.sum((m*diff)/(norme[:, :, np.newaxis])**3, axis=1)
    return a


#ax.axis('equal')
ax.set(xlim=[-100, 100], ylim=[-100,100])


def get_new_position(pos, masse):
    global vit
    At=calcul_acceleration(pos,masse)
    vit=vit + At*dt
    pos= pos + vit*dt
    return pos

scat = ax.scatter(pos[:,0], pos[:,1])


def animate(t):

    global pos

    for _ in range(10):
        pos = get_new_position(pos,masse)

    
    scat.set_offsets(pos)
    return scat,

ani = animation.FuncAnimation(
    fig=fig,
    func=animate,
    interval=20,
    cache_frame_data=False,
)
plt.show()