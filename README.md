# householder-givens

Let 
$x \in \mathbb{R}^2$
be a random vector then its rotation by
$ \theta $
degrees is computed by Givens rotation method:
$ \vec{x'} = \begin{pmatrix} c & -s\\ s & c \end{pmatrix} \vec{x}$
, where
$ c = \cos{\theta} $
and 
$s = \sin{\theta} $
and its reflection over a subspace orthogonal to a given unit vector 
$ v \in \mathbb{R}^2 $
is 
$ \vec{x''} = \vec{x}-2[(\vec{x} \cdot \vec{v}) \vec{v}] $.

## Prerequisites
  
  To run the application you need to have installed the python packages from *requirements.txt*.
  
## Application
   Application starts by running the *app.py* script.
   
   ![housholder screenshot](https://github.com/lucianodainic/householder-givens/blob/main/assets/householder.png)
   ![givens screenshot](https://github.com/lucianodainic/householder-givens/blob/main/assets/givens.png)
   * :large_blue_circle: : x
   * :green_circle: : x' / x'' (rotation/ reflection)
   * :red_circle: : orthogonal subspace
