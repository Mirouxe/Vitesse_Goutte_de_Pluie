**Ce projet a pour objectif de répondre à une question en apparence simple : Quelle est la vitesse de la pluie ?** 

Pour répondre à cette question, nous pouvons la reformuler en supposant que la vitesse de la pluie est la vitesse d'une goutte de pluie.

Afin de résoudre ce problème, il est nécessaire de formuler le problème physique en s'appuyant sur certaines hypothèses de modélisation. 

Voici les différents cas étudiés : 

- **Cas 1** : Goutte de pluie sphérique sans frottement soumise à son poid et à la poussée d'Archimède

- **Cas 2** : Goutte de pluie sphérique avec frottement (loi linéaire) soumise à son poid et à la poussée d'Archimède
 
- **Cas 3** : Goutte de pluie sphérique avec frottement (loi quadratique) soumise à son poid et à la poussée d'Archimède

- **Cas 3bis** : Goutte de pluie sphérique avec frottement (loi quadratique) soumise à son poid en négligeant la poussée d'Archimède

![image](https://github.com/user-attachments/assets/17099c63-b83f-4753-8c69-14f54874ce6f)

**Hypothèse 3.b (Loi de traînée quadratique en négligeant la poussée d'archimède)** :

Le Principe Fondamental de la Dynamique (PFD) s'écrit :

```math
$$
m \vec{a} = \sum \vec{F} 
$$

$$
 m \vec{a} = \vec{F}_g + \vec{F}_t + \vec{F}_a
$$
où :
$$
\vec{F}_g = - mg \, \vec{e}_z = - \frac{4}{3} \pi R_0^3 \rho_{\text{eau}} g \, \vec{e}_z
$$

$$
\vec{F}_t = \frac{1}{2} \rho_{\text{air}} C_x \pi R_0^2 v^2 \, \vec{e}_z
$$

$$
\vec{a} = - a \, \vec{e}_z = - \frac{dv}{dt} \, \vec{e}_z
$$

Ainsi le PFD devient :
$$
- m \frac{dv}{dt} = - \frac{4}{3} \pi R_0^3 \rho_{\text{eau}} g + \frac{1}{2} \rho_{\text{air}} C_x \pi R_0^2 v^2
$$

$$
\frac{dv}{dt} + \beta v^2 = g
$$
avec :
$$
\beta = \frac{3}{8R_0} C_x
$$

