#    Homework 2

![](https://i.imgur.com/TazlsO5.png)

Let us obtain positions of all points:
$$O_1 = (0,0)$$
$$A = (O_1Acos(\omega_{O_1A}\phi),O_1Asin(\omega_{O_1A}\phi))$$

We can get point B from the following system:

\begin{equation}
\begin{cases}

(x_B - x_A)^2 + (y_B - y_A)^2 = AB^2
\\
x_B = 0

\end{cases}\.
\end{equation}
We will get 2 solutions for this system, we will take the one with the higher $y_B$
This system can be solved numerically using libraries in Python like Sympy

We can obtain C from the following equation:
$$\vec{AC} = \vec{AB}\frac{AC}{AB}$$
$$O_2 = (a+b,-d)$$
We can get point D from the following system:


\begin{cases}
(x_D - x_A)^2 + (y_D - y_A)^2 = AD^2
\\
(x_D - x_{O_2})^2 + (y_D - y_{O_2})^2 = O_2D^2
\end{cases}

We will get 2 solutions for this system, we will take the one with the higher $y_D$.
This system can be solved numerically.

$$O_3 = (a+b+c,e)$$
We can get point E from the following system:


\begin{cases}
(x_D - x_E)^2 + (y_D - y_E)^2 = DE^2
\\
(x_E - x_{O_3})^2 + (y_D - y_{O_3})^2 = O_2D^2
\end{cases}

We will get 2 solutions for this system, we will take the one with the higher $y_E$.
This system can be solved numerically.

We can obtain F from the following equation:
$$\vec{DF} = \frac{3}{5}\vec{DE}$$

$$O_4 = (a,e)$$

We can get point G from the following system:


\begin{cases}
(x_G - x_F)^2 + (y_G - y_F)^2 = FG^2
\\
(x_G - x_{O_4})^2 + (y_G - y_{O_4})^2 = O_3G^2
\end{cases}

We will get 2 solutions for this system, we will take the one with the higher $y_G$.
This system can be solved numerically.

Finally,
We can get point H from the following system:


\begin{cases}
(x_H - x_F)^2 + (y_H - y_F)^2 = FH^2
\\
(x_G - x_H)^2 + (y_G - y_H)^2 = HG^2
\end{cases}

We will get 2 solutions for this system, we will take the one with the higher $y_H$.
This system can be solved numerically.

Since we have functions of coordinates for all points, we will find the velocities of these points by derivating these functions numerically.


