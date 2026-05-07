# Rectified Gaussian distribution

Mixture of discrete and continuous distributions

Not to be confused with truncated Gaussian distribution.

In probability theory, the rectified Gaussian distribution is a modification of the Gaussian distribution when its negative elements are reset to 0 (analogous to an electronic rectifier). It is essentially a mixture of a discrete distribution (constant 0) and a continuous distribution (a truncated Gaussian distribution with interval 
{\displaystyle (0,\infty )}

) as a result of censoring. ${\displaystyle (0,\infty )}$

Density function[edit]
The probability density function of a rectified Gaussian distribution, for which random variables X having this distribution, derived from the normal distribution 
{\displaystyle {\mathcal {N}}(\mu ,\sigma ^{2}),}

 are displayed as  
{\displaystyle X\sim {\mathcal {N}}^{\textrm {R}}(\mu ,\sigma ^{2})}

,   is given by
{\displaystyle f(x;\mu ,\sigma ^{2})=\Phi {\left(-{\frac {\mu }{\sigma }}\right)}\delta (x)+{\frac {1}{\sqrt {2\pi \sigma ^{2}}}}\;e^{-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}}{\textrm {U}}(x).}

A comparison of Gaussian distribution, rectified Gaussian distribution, and truncated Gaussian distribution.
Here, 
{\displaystyle \Phi (x)}

 is the cumulative distribution function (cdf) of the standard normal distribution:
{\displaystyle \Phi (x)={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{x}e^{-t^{2}/2}\,dt\quad x\in \mathbb {R} ,}
{\displaystyle \delta (x)}

 is the Dirac delta function
{\displaystyle \delta (x)={\begin{cases}+\infty ,&x=0\\0,&x\neq 0\end{cases}}}

and, 
{\displaystyle {\textrm {U}}(x)}

 is the unit step function:
{\displaystyle {\textrm {U}}(x)={\begin{cases}0,&x\leq 0,\\1,&x>0.\end{cases}}}

Mean and variance[edit]
Since the unrectified normal distribution has mean 

μ

{\displaystyle \mu }

 and since in transforming it to the rectified distribution some probability mass has been shifted to a higher value (from negative values to 0), the mean of the rectified distribution is greater than 
{\displaystyle \mu .}

Since the rectified distribution is formed by moving some of the probability mass toward the rest of the probability mass, the rectification is a mean-preserving contraction combined with a mean-changing rigid shift of the distribution, and thus the variance is decreased; therefore the variance of the rectified distribution is less than 
{\displaystyle \sigma ^{2}.}

Generating values[edit]
To generate values computationally, one can use
{\displaystyle s\sim {\mathcal {N}}(\mu ,\sigma ^{2}),\quad x={\textrm {max}}(0,s),}

and then
{\displaystyle x\sim {\mathcal {N}}^{\textrm {R}}(\mu ,\sigma ^{2}).}

Application[edit]
A rectified Gaussian distribution is semi-conjugate to the Gaussian likelihood, and it has been recently applied to factor analysis, or particularly, (non-negative) rectified factor analysis.
Harva[1] proposed a variational learning algorithm for the rectified factor model, where the factors follow a mixture of rectified Gaussian; and later Meng[2] proposed an infinite rectified factor model coupled with its Gibbs sampling solution, where the factors follow a Dirichlet process mixture of rectified Gaussian distribution, and applied it in computational biology for reconstruction of gene regulatory networks.

Extension to general bounds[edit]
An extension to the rectified Gaussian distribution was proposed by Palmer et al.,[3] allowing rectification between arbitrary lower and upper bounds. For lower and upper bounds 

a

{\displaystyle a}
{\displaystyle b}

 respectively, the cdf, 
{\displaystyle F_{R}(x|\mu ,\sigma ^{2})}

 is given by:
{\displaystyle F_{R}(x|\mu ,\sigma ^{2})={\begin{cases}0,&x<a,\\\Phi (x|\mu ,\sigma ^{2}),&a\leq x<b,\\1,&x\geq b,\\\end{cases}}}

where 
{\displaystyle \Phi (x|\mu ,\sigma ^{2})}

 is the cdf of a normal distribution with mean 

μ

{\displaystyle \mu }

 and variance 
{\displaystyle \sigma ^{2}}

. The mean and variance of the rectified distribution is calculated by first transforming the constraints to be acting on a standard normal distribution:
{\displaystyle c={\frac {a-\mu }{\sigma }},\qquad d={\frac {b-\mu }{\sigma }}.}

Using the transformed constraints, the mean and variance, 
{\displaystyle \mu _{R}}
{\displaystyle \sigma _{R}^{2}}

 respectively, are then given by:
{\displaystyle \mu _{t}={\frac {1}{\sqrt {2\pi }}}\left(e^{\left(-{\frac {c^{2}}{2}}\right)}-e^{\left(-{\frac {d^{2}}{2}}\right)}\right)+{\frac {c}{2}}\left(1+{\textrm {erf}}\left({\frac {c}{\sqrt {2}}}\right)\right)+{\frac {d}{2}}\left(1-{\textrm {erf}}\left({\frac {d}{\sqrt {2}}}\right)\right),}
{\displaystyle {\begin{aligned}\sigma _{t}^{2}&={\frac {\mu _{t}^{2}+1}{2}}\left({\textrm {erf}}\left({\frac {d}{\sqrt {2}}}\right)-{\textrm {erf}}\left({\frac {c}{\sqrt {2}}}\right)\right)-{\frac {1}{\sqrt {2\pi }}}\left(\left(d-2\mu _{t}\right)e^{\left(-{\frac {d^{2}}{2}}\right)}-\left(c-2\mu _{t}\right)e^{\left(-{\frac {c^{2}}{2}}\right)}\right)\\&+{\frac {\left(c-\mu _{t}\right)^{2}}{2}}\left(1+{\textrm {erf}}\left({\frac {c}{\sqrt {2}}}\right)\right)+{\frac {\left(d-\mu _{t}\right)^{2}}{2}}\left(1-{\textrm {erf}}\left({\frac {d}{\sqrt {2}}}\right)\right),\end{aligned}}}
{\displaystyle \mu _{R}=\mu +\sigma \mu _{t},}
{\displaystyle \sigma _{R}^{2}=\sigma ^{2}\sigma _{t}^{2},}

where erf is the error function. This distribution was used by Palmer et al. for modelling physical resource levels, such as the quantity of liquid in a vessel, which is bounded by both 0 and the capacity of the vessel.
