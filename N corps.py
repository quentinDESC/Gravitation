import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


#Conditions initiales ,paramètres:
N= 10 #nb_planetes
G=1
dt=0.05 #meilleur paramètre qu'on a trouvé
masse =np.random.uniform(1,5,N)
pos = np.random.uniform(-100,100, (N, 2))
vit = np.zeros((N,2))

fig, ax = plt.subplots()

def distance(pos):
    #fonction utile pour préparer la suivante 
    diff = pos[np.newaxis, :, :] - pos[:, np.newaxis, :] #on crée la matrice à 3 dimensions des distances selon x et y entre toutes les planètes
    norme = np.sqrt(np.sum(diff**2, axis=2))
    np.fill_diagonal(norme, np.inf) # distance d'une planète à elle même =+ infini pour pas de pb de force 
    return diff, norme

def calcul_acceleration(pos,masse):
    #on calcule l'accélération pour préparer l'Euler
    diff, norme = distance(pos)
    m = masse[np.newaxis, :, np.newaxis] # je change la forme pour que la ligne suivante fonctionne
    a=G*np.sum((m*diff)/(norme[:, :, np.newaxis])**3+10**(-8), axis=1)# on rajoute un élément négligeable( 10**-8) pour éviter les divisions par 0
    return a


#ax.axis('equal')
ax.set(xlim=[-100, 100], ylim=[-100,100])


def get_new_position(pos, masse):
    global vit #doit être maj
    At=calcul_acceleration(pos,masse)
    vit=vit + At*dt #méthode d'euler
    pos= pos + vit*dt #méthode d'euler
    return pos

rayon = masse**(1/3)
surface=20*(rayon**2) #bonus: on adapte les tailles des planètes en fonction de leurs masses ( 20 adapté à notre affichage après test)
scat = ax.scatter(pos[:,0], pos[:,1], surface)



### modifié avec un LLM pour adapter à notre code 
def animate(t):

    global pos #doit être maj

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