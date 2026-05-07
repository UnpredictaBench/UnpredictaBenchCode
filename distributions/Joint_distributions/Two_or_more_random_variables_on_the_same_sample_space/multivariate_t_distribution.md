# Multivariate t-distribution

Multivariable generalization of the Student's t-distribution

| Multivariate t |
| --- |
| Notation | t p ( μ , Σ , ν ) {\displaystyle t_{p}({\boldsymbol {\mu }},{\boldsymbol {\Sigma }},\nu )} ${\displaystyle t_{p}({\boldsymbol {\mu }},{\boldsymbol {\Sigma }},\nu )}$ |
| Parameters | μ = [ μ 1 , … , μ p ] T {\displaystyle {\boldsymbol {\mu }}=[\mu _{1},\dots ,\mu _{p}]^{\mathsf {T}}} location (real p × 1 {\displaystyle p\times 1} vector) Σ {\displaystyle {\boldsymbol {\Sigma }}} scale matrix (positive-definite real p × p {\displaystyle p\times p} matrix) ν > 0 {\displaystyle \nu >0} (real) represents the degrees of freedom ${\displaystyle {\boldsymbol {\mu }}=[\mu _{1},\dots ,\mu _{p}]^{\mathsf {T}}}$ ${\displaystyle p\times 1}$ ${\displaystyle {\boldsymbol {\Sigma }}}$ ${\displaystyle p\times p}$ ${\displaystyle \nu >0}$ |
| Support | x ∈ R p {\displaystyle \mathbf {x} \in \mathbb {R} ^{p}\!} ${\displaystyle \mathbf {x} \in \mathbb {R} ^{p}\!}$ |
| PDF | Γ [ ( ν + p ) / 2 ] Γ ( ν / 2 ) ν p / 2 π p / 2 \| Σ \| 1 / 2 [ 1 + 1 ν ( x − μ ) T Σ − 1 ( x − μ ) ] − ( ν + p ) / 2 {\displaystyle {\frac {\Gamma \left[(\nu +p)/2\right]}{\Gamma (\nu /2)\nu ^{p/2}\pi ^{p/2}\left\|{\boldsymbol {\Sigma }}\right\|^{1/2}}}\left[1+{\frac {1}{\nu }}({\mathbf {x} }-{\boldsymbol {\mu }})^{\mathsf {T}}{\boldsymbol {\Sigma }}^{-1}({\mathbf {x} }-{\boldsymbol {\mu }})\right]^{-(\nu +p)/2}} ${\displaystyle {\frac {\Gamma \left[(\nu +p)/2\right]}{\Gamma (\nu /2)\nu ^{p/2}\pi ^{p/2}\left\|{\boldsymbol {\Sigma }}\right\|^{1/2}}}\left[1+{\frac {1}{\nu }}({\mathbf {x} }-{\boldsymbol {\mu }})^{\mathsf {T}}{\boldsymbol {\Sigma }}^{-1}({\mathbf {x} }-{\boldsymbol {\mu }})\right]^{-(\nu +p)/2}}$ |
| CDF | No analytic expression, but see text for approximations |
| Mean | μ {\displaystyle {\boldsymbol {\mu }}} if ν > 1 {\displaystyle \nu >1} ; else undefined ${\displaystyle {\boldsymbol {\mu }}}$ ${\displaystyle \nu >1}$ |
| Median | μ {\displaystyle {\boldsymbol {\mu }}} ${\displaystyle {\boldsymbol {\mu }}}$ |
| Mode | μ {\displaystyle {\boldsymbol {\mu }}} ${\displaystyle {\boldsymbol {\mu }}}$ |
| Variance | ν ν − 2 Σ {\displaystyle {\frac {\nu }{\nu -2}}{\boldsymbol {\Sigma }}} (covariance matrix) if ν > 2 {\displaystyle \nu >2} ; else undefined ${\displaystyle {\frac {\nu }{\nu -2}}{\boldsymbol {\Sigma }}}$ ${\displaystyle \nu >2}$ |
| Skewness | 0 if ν > 3 {\displaystyle \nu >3} ; else undefined ${\displaystyle \nu >3}$ |

In statistics, the multivariate t-distribution (or multivariate Student distribution) is a multivariate probability distribution. It is a generalization to random vectors of the Student's t-distribution, which is a distribution applicable to univariate random variables. While the case of a random matrix could be treated within this structure, the matrix t-distribution is distinct and makes particular use of the matrix structure.

Definition[edit]
One common method of construction of a multivariate t-distribution, for the case of 

p

{\displaystyle p}

 dimensions, is based on the observation that if 

y

{\displaystyle \mathbf {y} }
{\displaystyle u}

 are independent and distributed as 
{\displaystyle N({\mathbf {0} },{\boldsymbol {\Sigma }})}
{\displaystyle \chi _{\nu }^{2}}

 (i.e. multivariate normal and chi-squared distributions) respectively, the matrix 

Σ

{\displaystyle \mathbf {\Sigma } \,}

 is a p × p matrix, and 

μ

{\displaystyle {\boldsymbol {\mu }}}

 is a constant vector then the random variable 

x

=

y

/

u

/

ν

+

μ

{\textstyle {\mathbf {x} }={\mathbf {y} }/{\sqrt {u/\nu }}+{\boldsymbol {\mu }}}

 has the density[1]
{\displaystyle {\frac {\Gamma \left[(\nu +p)/2\right]}{\Gamma (\nu /2)\nu ^{p/2}\pi ^{p/2}\left|{\boldsymbol {\Sigma }}\right|^{1/2}}}\left[1+{\frac {1}{\nu }}\left({\mathbf {x} }-{\boldsymbol {\mu }}\right)^{\mathsf {T}}{\boldsymbol {\Sigma }}^{-1}\left({\mathbf {x} }-{\boldsymbol {\mu }}\right)\right]^{-(\nu +p)/2}}

and is said to be distributed as a multivariate t-distribution with parameters 
{\displaystyle {\boldsymbol {\Sigma }},{\boldsymbol {\mu }},\nu }

. Note that 

Σ

{\displaystyle \mathbf {\Sigma } }

 is not the covariance matrix since the covariance is given by 
{\displaystyle \nu /(\nu -2)\mathbf {\Sigma } }

 (for 
{\displaystyle \nu >2}

).
The constructive definition of a multivariate t-distribution simultaneously serves as a sampling algorithm:

Generate 
{\displaystyle u\sim \chi _{\nu }^{2}}
{\displaystyle \mathbf {y} \sim N(\mathbf {0} ,{\boldsymbol {\Sigma }})}

, independently.
Compute 

x

←

y

ν

/

u

+

μ

{\textstyle \mathbf {x} \gets \mathbf {y} {\sqrt {\nu /u}}+{\boldsymbol {\mu }}}

.
This formulation gives rise to the hierarchical representation of a multivariate t-distribution as a scale-mixture of normals: 
{\displaystyle u\sim \mathrm {Ga} (\nu /2,\nu /2)}

 where 
{\displaystyle \mathrm {Ga} (a,b)}

 indicates a gamma distribution with density proportional to 
{\displaystyle x^{a-1}e^{-bx}}

, and 
{\displaystyle \mathbf {x} \mid u}

 conditionally follows 
{\displaystyle N({\boldsymbol {\mu }},u^{-1}{\boldsymbol {\Sigma }})}

.
In the special case 
{\displaystyle \nu =1}

, the distribution is a multivariate Cauchy distribution.

Derivation[edit]
There are in fact many candidates for the multivariate generalization of Student's t-distribution. An extensive survey of the field has been given by Kotz and Nadarajah (2004). The essential issue is to define a probability density function of several variables that is the appropriate generalization of the formula for the univariate case. In one dimension (
{\displaystyle p=1}

), with 
{\displaystyle t=x-\mu }
{\displaystyle \Sigma =1}

, we have the probability density function
{\displaystyle f(t)={\frac {\Gamma [(\nu +1)/2]}{{\sqrt {\nu \pi \,}}\,\Gamma [\nu /2]}}(1+t^{2}/\nu )^{-(\nu +1)/2}}

and one approach is to use a corresponding function of several variables. This is the basic idea of elliptical distribution theory, where one writes down a corresponding function of 

p

{\displaystyle p}

 variables 
{\displaystyle t_{i}}

 that replaces 
{\displaystyle t^{2}}

 by a quadratic function of all the 
{\displaystyle t_{i}}

. It is clear that this only makes sense when all the marginal distributions have the same degrees of freedom 

ν

{\displaystyle \nu }

. With 
{\displaystyle \mathbf {A} ={\boldsymbol {\Sigma }}^{-1}}

, one has a simple choice of multivariate density function
{\displaystyle f(\mathbf {t} )={\frac {\Gamma ((\nu +p)/2)\left|\mathbf {A} \right|^{1/2}}{{\sqrt {\nu ^{p}\pi ^{p}\,}}\,\Gamma (\nu /2)}}\left(1+\sum _{i,j=1}^{p,p}A_{ij}t_{i}t_{j}/\nu \right)^{-(\nu +p)/2}}

which is the standard but not the only choice.
An important special case is the standard bivariate t-distribution, p = 2:
{\displaystyle f(t_{1},t_{2})={\frac {\left|\mathbf {A} \right|^{1/2}}{2\pi }}\left(1+\sum _{i,j=1}^{2,2}A_{ij}t_{i}t_{j}/\nu \right)^{-(\nu +2)/2}}

Note that 
{\displaystyle {\frac {\Gamma {\left({\frac {\nu +2}{2}}\right)}}{\pi \nu \,\Gamma {\left({\frac {\nu }{2}}\right)}}}={\frac {1}{2\pi }}}

.
Now, if 

A

{\displaystyle \mathbf {A} }

 is the identity matrix, the density is
{\displaystyle f(t_{1},t_{2})={\frac {1}{2\pi }}\left(1+(t_{1}^{2}+t_{2}^{2})/\nu \right)^{-(\nu +2)/2}.}

The difficulty with the standard representation is revealed by this formula, which does not factorize into the product of the marginal one-dimensional distributions. When 

Σ

{\displaystyle \Sigma }

 is diagonal the standard representation can be shown to have zero correlation but the marginal distributions are not statistically independent.
A notable spontaneous occurrence of the elliptical multivariate distribution is its formal mathematical appearance when least squares methods are applied to multivariate normal data such as the classical Markowitz minimum variance econometric solution for asset portfolios.[2]

Cumulative distribution function[edit]
The definition of the cumulative distribution function (cdf) in one dimension can be extended to multiple dimensions by defining the following probability (here 

x

{\displaystyle \mathbf {x} }

 is a real vector):

F
(

x

)
=

P

(

X

≤

x

)
,

where
{\displaystyle F(\mathbf {x} )=\mathbb {P} (\mathbf {X} \leq \mathbf {x} ),\quad {\textrm {where}}\;\;\mathbf {X} \sim t_{\nu }({\boldsymbol {\mu }},{\boldsymbol {\Sigma }}).}

There is no simple formula for 
{\displaystyle F(\mathbf {x} )}

, but it can be approximated numerically via Monte Carlo integration.[3][4][5]

Conditional Distribution[edit]
This was developed by Muirhead [6] and Cornish,[7] but later derived using the simpler chi-squared ratio representation above, by Roth[1] and Ding.[8] Let vector 

X

{\displaystyle X}

 follow a multivariate t distribution and partition into two subvectors of 
{\displaystyle p_{1},p_{2}}

 elements:
{\displaystyle X_{p}={\begin{bmatrix}X_{1}\\X_{2}\end{bmatrix}}\sim t_{p}\left(\mu _{p},\Sigma _{p\times p},\nu \right)}

where 
{\displaystyle p_{1}+p_{2}=p}

, the known mean vectors are 
{\displaystyle \mu _{p}={\begin{bmatrix}\mu _{1}\\\mu _{2}\end{bmatrix}}}

 and the scale matrix is 
{\displaystyle \Sigma _{p\times p}={\begin{bmatrix}\Sigma _{11}&\Sigma _{12}\\\Sigma _{21}&\Sigma _{22}\end{bmatrix}}}

.
Roth and Ding find the conditional distribution 
{\displaystyle p(X_{1}|X_{2})}

 to be a new t-distribution with modified parameters. 
{\displaystyle X_{1}|X_{2}\sim t_{p_{1}}\left(\mu _{1|2},\,{\frac {\nu +d_{2}}{\nu +p_{2}}}\Sigma _{11|2},\,\nu +p_{2}\right)}

An equivalent expression in Kotz et. al. is somewhat less concise.
Thus the conditional distribution is most easily represented as a two-step procedure. Form first the intermediate distribution 
{\displaystyle X_{1}|X_{2}\sim t_{p_{1}}\left(\mu _{1|2},\Psi ,{\tilde {\nu }}\right)}

 above then, using the parameters below, the explicit conditional distribution becomes
{\displaystyle f(X_{1}|X_{2})={\frac {\Gamma {\left({\frac {{\tilde {\nu }}+p_{1}}{2}}\right)}}{\Gamma {\left({\frac {\tilde {\nu }}{2}}\right)}\left(\pi \,{\tilde {\nu }}\right)^{p_{1}/2}\left|{\boldsymbol {\Psi }}\right|^{1/2}}}\left[1+{\frac {1}{\tilde {\nu }}}\left(X_{1}-\mu _{1|2}\right)^{\mathsf {T}}{\boldsymbol {\Psi }}^{-1}\left(X_{1}-\mu _{1|2}\right)\right]^{-({\tilde {\nu }}+p_{1})/2}}

where
{\displaystyle {\tilde {\nu }}=\nu +p_{2}}

Effective degrees of freedom, 

ν

{\displaystyle \nu }

 is augmented by the number of disused variables 
{\displaystyle p_{2}}
{\displaystyle \mu _{1|2}=\mu _{1}+\Sigma _{12}\Sigma _{22}^{-1}\left(X_{2}-\mu _{2}\right)}

 is the conditional mean of 
{\displaystyle x_{1}}
{\displaystyle \Sigma _{11|2}=\Sigma _{11}-\Sigma _{12}\Sigma _{22}^{-1}\Sigma _{21}}

 is the Schur complement of 
{\displaystyle \Sigma _{22}{\text{ in }}\Sigma }
{\displaystyle d_{2}=(X_{2}-\mu _{2})^{\mathsf {T}}\Sigma _{22}^{-1}(X_{2}-\mu _{2})}

 is the squared Mahalanobis distance of 
{\displaystyle X_{2}}

 from 
{\displaystyle \mu _{2}}

 with scale matrix 
{\displaystyle \Sigma _{22}}
{\displaystyle \Psi ={\frac {\nu +d_{2}}{\tilde {\nu }}}\Sigma _{11|2}}

 is the conditional scale matrix for 
{\displaystyle {\tilde {\nu }}>0}
{\displaystyle \Sigma _{cov}={\frac {\tilde {\nu }}{{\tilde {\nu }}-2}}\Psi ={\frac {\nu +d_{2}}{{\tilde {\nu }}-2}}\Sigma _{11|2}}

 is the conditional covariance matrix for 
{\displaystyle {\tilde {\nu }}>2}

.

Copulas based on the multivariate t[edit]
The use of such distributions is enjoying renewed interest due to applications in mathematical finance, especially through the use of the Student's t copula.[9]

Elliptical representation[edit]
Constructed as an elliptical distribution,[10] take the simplest centralised case with spherical symmetry and no scaling, 
{\displaystyle \Sigma =\operatorname {I} \,}

, then the multivariate t-PDF takes the form
{\displaystyle f_{X}(X)=g(X^{\mathsf {T}}X)={\frac {\Gamma {\left({\frac {\nu +p}{2}}\right)}}{(\nu \pi )^{\,p/2}\Gamma {\left({\frac {\nu }{2}}\right)}}}\left(1+\nu ^{-1}X^{\mathsf {T}}X\right)^{-(\nu +p)/2}}

where 
{\displaystyle X=(x_{1},\cdots ,x_{p})^{\mathsf {T}}}

 is a 

p

{\displaystyle p}

-vector and 

ν

{\displaystyle \nu }

 is the degrees of freedom as defined in Muirhead[6] section 1.5.  The covariance of 

X

{\displaystyle X}
{\displaystyle \operatorname {E} \left(XX^{\mathsf {T}}\right)=\int _{-\infty }^{\infty }\cdots \int _{-\infty }^{\infty }f_{X}(x_{1},\dots ,x_{p})XX^{\mathsf {T}}\,dx_{1}\dots dx_{p}={\frac {\nu }{\nu -2}}\operatorname {I} }

The aim is to convert the Cartesian PDF to a radial one. Kibria and Joarder,[11] define radial measure 
{\displaystyle r_{2}=R^{2}={\frac {X^{\mathsf {T}}X}{p}}}

 and, noting that the density is dependent only on r2, we get
{\displaystyle \operatorname {E} [r_{2}]=\int _{-\infty }^{\infty }\cdots \int _{-\infty }^{\infty }f_{X}(x_{1},\dots ,x_{p}){\frac {X^{\mathsf {T}}X}{p}}\,dx_{1}\dots dx_{p}={\frac {\nu }{\nu -2}}}

which is equivalent to the variance of 

p

{\displaystyle p}

-element vector 

X

{\displaystyle X}

 treated as a univariate heavy-tail zero-mean random sequence with uncorrelated, yet statistically dependent, elements.
Radial Distribution[edit]
{\displaystyle r_{2}={\frac {X^{\mathsf {T}}X}{p}}}

 follows the Fisher-Snedecor or 

F

{\displaystyle F}

 distribution:
{\displaystyle r_{2}\sim f_{F}(p,\nu )=B{\bigg (}{\frac {p}{2}},{\frac {\nu }{2}}{\bigg )}^{-1}{\bigg (}{\frac {p}{\nu }}{\bigg )}^{p/2}r_{2}^{p/2-1}{\bigg (}1+{\frac {p}{\nu }}r_{2}{\bigg )}^{-(p+\nu )/2}}

having mean value 
{\displaystyle \operatorname {E} [r_{2}]={\frac {\nu }{\nu -2}}}
{\displaystyle F}

-distributions arise naturally in tests of sums of squares of sampled data after normalization by the sample standard deviation.
By a change of random variable to 
{\displaystyle y={\frac {p}{\nu }}r_{2}={\frac {X^{\mathsf {T}}X}{\nu }}}

 in the equation above, retaining 

p

{\displaystyle p}

-vector 

X

{\displaystyle X}

, we have 
{\displaystyle \operatorname {E} [y]=\int _{-\infty }^{\infty }\cdots \int _{-\infty }^{\infty }f_{X}(X){\frac {X^{\mathsf {T}}X}{\nu }}\,dx_{1}\dots dx_{p}={\frac {p}{\nu -2}}}

 and probability distribution 
{\displaystyle {\begin{aligned}f_{Y}(y|\,p,\nu )&=\left|{\frac {p}{\nu }}\right|^{-1}B\left({\frac {p}{2}},{\frac {\nu }{2}}\right)^{-1}\left({\frac {p}{\nu }}\right)^{p/2}\left({\frac {p}{\nu }}\right)^{-p/2-1}y^{\,p/2-1}{\bigl (}1+y{\bigr )}^{-(p+\nu )/2}\\[2ex]&=B\left({\frac {p}{2}},{\frac {\nu }{2}}\right)^{-1}y^{\,p/2-1}{\bigl (}1+y{\bigr )}^{-(\nu +p)/2}\end{aligned}}}

which is a regular Beta-prime distribution 
{\displaystyle y\sim \beta \,'{\bigg (}y;{\frac {p}{2}},{\frac {\nu }{2}}{\bigg )}}

 having mean value 
{\displaystyle {\frac {{\frac {1}{2}}p}{{\frac {1}{2}}\nu -1}}={\frac {p}{\nu -2}}}

.

Cumulative Radial Distribution[edit]
Given the Beta-prime distribution, the radial cumulative distribution function of 

y

{\displaystyle y}

 is known:
{\displaystyle F_{Y}(y)\sim I{\bigg (}{\frac {y}{1+y}};\,{\frac {p}{2}},{\frac {\nu }{2}}{\bigg )}\,B{\bigg (}{\frac {p}{2}},{\frac {\nu }{2}}{\bigg )}^{-1}}

where 

I

{\displaystyle I}

 is the incomplete Beta function and applies with a spherical 

Σ

{\displaystyle \Sigma }

 assumption.
In the scalar case, 
{\displaystyle p=1}

, the distribution is equivalent to Student-t with the equivalence 
{\displaystyle t^{2}=y^{2}\sigma ^{-1}}

, the variable t having double-sided tails for CDF purposes, i.e. the "two-tail-t-test".
The radial distribution can also be derived via a straightforward coordinate transformation from Cartesian to spherical.  A constant radius surface at 

R
=

(

X

T

X

)

1

/

2

{\textstyle R=\left(X^{\mathsf {T}}X\right)^{1/2}}

 with PDF 

p

X

(
X
)
∝

(

1
+

ν

−
1

R

2

)

−
(
ν
+
p
)

/

2

{\textstyle p_{X}(X)\propto \left(1+\nu ^{-1}R^{2}\right)^{-(\nu +p)/2}}

 is an iso-density surface.  Given this density value, the quantum of probability on a shell of surface area 
{\displaystyle A_{R}}

 and thickness 
{\displaystyle \delta R}
{\displaystyle R}
{\displaystyle \delta P=p_{X}(R)\,A_{R}\delta R}

.
The enclosed 

p

{\displaystyle p}

-sphere of radius 

R

{\displaystyle R}

 has surface area 
{\displaystyle A_{R}={\frac {2\pi ^{p/2}R^{\,p-1}}{\Gamma (p/2)}}}

.  Substitution into 
{\displaystyle \delta P}

 shows that the shell has element of probability 
{\displaystyle \delta P=p_{X}(R){\frac {2\pi ^{p/2}R^{p-1}}{\Gamma (p/2)}}\delta R}

 which is equivalent to radial density function
{\displaystyle f_{R}(R)={\frac {\Gamma {\big (}{\frac {1}{2}}(\nu +p)\,{\big )}}{\nu ^{\,p/2}\pi ^{\,p/2}\Gamma {\big (}{\frac {1}{2}}\nu {\big )}}}{\frac {2\pi ^{p/2}R^{p-1}}{\Gamma (p/2)}}{\bigg (}1+{\frac {R^{2}}{\nu }}{\bigg )}^{-(\nu +p)/2}}

which further simplifies to 
{\displaystyle f_{R}(R)={\frac {2}{\nu ^{1/2}B{\big (}{\frac {1}{2}}p,{\frac {1}{2}}\nu {\big )}}}{\bigg (}{\frac {R^{2}}{\nu }}{\bigg )}^{(p-1)/2}{\bigg (}1+{\frac {R^{2}}{\nu }}{\bigg )}^{-(\nu +p)/2}}

 where 
{\displaystyle B(*,*)}

 is the Beta function.
Changing the radial variable to 
{\displaystyle y=R^{2}/\nu }

 returns the previous Beta Prime distribution
{\displaystyle f_{Y}(y)={\frac {1}{B{\left({\frac {1}{2}}p,{\frac {1}{2}}\nu \right)}}}y^{\,p/2-1}\left(1+y\right)^{-(\nu +p)/2}}

To scale the radial variables without changing the radial shape function, define scale matrix 
{\displaystyle \Sigma =\alpha \operatorname {I} }

, yielding a 3-parameter Cartesian density function, ie. the probability 
{\displaystyle \Delta _{P}}

 in volume element 
{\displaystyle dx_{1}\dots dx_{p}}
{\displaystyle \Delta _{P}{\big (}f_{X}(X\,|\alpha ,p,\nu ){\big )}={\frac {\Gamma {\left({\frac {1}{2}}(\nu +p)\,\right)}}{(\nu \pi )^{\,p/2}\alpha ^{\,p/2}\Gamma {\left({\frac {1}{2}}\nu \right)}}}\left(1+{\frac {X^{\mathsf {T}}X}{\alpha \nu }}\right)^{-(\nu +p)/2}\;dx_{1}\dots dx_{p}}

or, in terms of scalar radial variable 

R

{\displaystyle R}
{\displaystyle f_{R}(R\,|\alpha ,p,\nu )={\frac {2}{\alpha ^{1/2}\;\nu ^{1/2}B{\big (}{\frac {1}{2}}p,{\frac {1}{2}}\nu {\big )}}}{\bigg (}{\frac {R^{2}}{\alpha \,\nu }}{\bigg )}^{(p-1)/2}{\bigg (}1+{\frac {R^{2}}{\alpha \,\nu }}{\bigg )}^{-(\nu +p)/2}}

Radial Moments[edit]
The moments of all the radial variables , with the spherical distribution assumption, can be derived from the Beta Prime distribution.  If 
{\displaystyle Z\sim \beta '(a,b)}

 then 
{\displaystyle \operatorname {E} (Z^{m})={\frac {B(a+m,b-m)}{B(a,b)}}}

, a known result. Thus, for variable 
{\displaystyle y={\frac {p}{\nu }}R^{2}}

 we have 
{\displaystyle \operatorname {E} (y^{m})={\frac {B({\frac {1}{2}}p+m,{\frac {1}{2}}\nu -m)}{B({\frac {1}{2}}p,{\frac {1}{2}}\nu )}}={\frac {\Gamma {\big (}{\frac {1}{2}}p+m{\big )}\;\Gamma {\big (}{\frac {1}{2}}\nu -m{\big )}}{\Gamma {\big (}{\frac {1}{2}}p{\big )}\;\Gamma {\big (}{\frac {1}{2}}\nu {\big )}}},\;\nu /2>m}

The moments of 
{\displaystyle r_{2}=\nu \,y}
{\displaystyle \operatorname {E} (r_{2}^{m})=\nu ^{m}\operatorname {E} (y^{m})}

while introducing the scale matrix 
{\displaystyle \alpha \operatorname {I} }

 yields
{\displaystyle \operatorname {E} (r_{2}^{m}|\alpha )=\alpha ^{m}\nu ^{m}\operatorname {E} (y^{m})}

Moments relating to radial variable 

R

{\displaystyle R}

 are found by setting 
{\displaystyle R=(\alpha \nu y)^{1/2}}
{\displaystyle M=2m}

 whereupon
{\displaystyle {\begin{aligned}\operatorname {E} (R^{M})&=\operatorname {E} \!\left((\alpha \nu y)^{1/2}\right)^{2m}=(\alpha \nu )^{M/2}\operatorname {E} (y^{M/2})\\[1ex]&=(\alpha \nu )^{M/2}{\frac {B{\big (}{\frac {1}{2}}(p+M),{\frac {1}{2}}(\nu -M){\big )}}{B{\left({\frac {p}{2}},{\frac {\nu }{2}}\right)}}}\end{aligned}}}

Linear Combinations and Affine Transformation[edit]
Full Rank Transform[edit]
This closely relates to the multivariate normal method and is described in Kotz and Nadarajah, Kibria and Joarder, Roth, and Cornish.  Starting from a somewhat simplified version of the central MV-t pdf: 
{\displaystyle f_{X}(X)={\frac {\mathrm {K} }{\left|\Sigma \right|^{1/2}}}\left(1+\nu ^{-1}X^{\mathsf {T}}\Sigma ^{-1}X\right)^{-\left(\nu +p\right)/2}}

, where 

K

{\displaystyle \mathrm {K} }

 is a constant and 

ν

{\displaystyle \nu }

 is arbitrary but fixed, let 
{\displaystyle \Theta \in \mathbb {R} ^{p\times p}}

 be a full-rank matrix and form vector 
{\displaystyle Y=\Theta X}

.  Then, by straightforward change of variables
{\displaystyle f_{Y}(Y)={\frac {\mathrm {K} }{\left|\Sigma \right|^{1/2}}}\left(1+\nu ^{-1}Y^{\mathsf {T}}\Theta ^{-{\mathsf {T}}}\Sigma ^{-1}\Theta ^{-1}Y\right)^{-\left(\nu +p\right)/2}\left|{\frac {\partial Y}{\partial X}}\right|^{-1}}

The matrix of partial derivatives is 
{\displaystyle {\frac {\partial Y_{i}}{\partial X_{j}}}=\Theta _{i,j}}

 and the Jacobian becomes 
{\displaystyle \left|{\frac {\partial Y}{\partial X}}\right|=\left|\Theta \right|}

.  Thus
{\displaystyle f_{Y}(Y)={\frac {\mathrm {K} }{\left|\Sigma \right|^{1/2}\left|\Theta \right|}}\left(1+\nu ^{-1}Y^{\mathsf {T}}\Theta ^{-{\mathsf {T}}}\Sigma ^{-1}\Theta ^{-1}Y\right)^{-\left(\nu +p\right)/2}}

The denominator reduces to 
{\displaystyle \left|\Sigma \right|^{1/2}\left|\Theta \right|=\left|\Sigma \right|^{1/2}\left|\Theta \right|^{1/2}\left|\Theta ^{\mathsf {T}}\right|^{1/2}=\left|\Theta \Sigma \Theta ^{\mathsf {T}}\right|^{1/2}}

In full:
{\displaystyle f_{Y}(Y)={\frac {\Gamma \left[(\nu +p)/2\right]}{\Gamma (\nu /2)\,(\nu \,\pi )^{\,p/2}\left|\Theta \Sigma \Theta ^{\mathsf {T}}\right|^{1/2}}}\left(1+\nu ^{-1}Y^{\mathsf {T}}\left(\Theta \Sigma \Theta ^{\mathsf {T}}\right)^{-1}Y\right)^{-\left(\nu +p\right)/2}}

which is a regular MV-t distribution.
In general if 
{\displaystyle X\sim t_{p}(\mu ,\Sigma ,\nu )}
{\displaystyle \Theta ^{p\times p}}

 has full rank 

p

{\displaystyle p}

 then
{\displaystyle \Theta X+c\sim t_{p}(\Theta \mu +c,\Theta \Sigma \Theta ^{\mathsf {T}},\nu )}

Marginal Distributions[edit]
This is a special case of the rank-reducing linear transform below.  Kotz defines marginal distributions as follows.  Partition 
{\displaystyle X\sim t(p,\mu ,\Sigma ,\nu )}

 into two subvectors of 
{\displaystyle p_{1},p_{2}}

 elements:
{\displaystyle X_{p}={\begin{bmatrix}X_{1}\\X_{2}\end{bmatrix}}\sim t\left(p_{1}+p_{2},\mu _{p},\Sigma _{p\times p},\nu \right)}

with 
{\displaystyle p_{1}+p_{2}=p}

, means 
{\displaystyle \mu _{p}={\begin{bmatrix}\mu _{1}\\\mu _{2}\end{bmatrix}}}

, scale matrix 
{\displaystyle \Sigma _{p\times p}={\begin{bmatrix}\Sigma _{11}&\Sigma _{12}\\\Sigma _{21}&\Sigma _{22}\end{bmatrix}}}

then 
{\displaystyle X_{1}\sim t\left(p_{1},\mu _{1},\Sigma _{11},\nu \right)}
{\displaystyle X_{2}\sim t\left(p_{2},\mu _{2},\Sigma _{22},\nu \right)}

 such that
{\displaystyle f(X_{1})={\frac {\Gamma \left[(\nu +p_{1})/2\right]}{\Gamma (\nu /2)\,(\nu \,\pi )^{\,p_{1}/2}\left|{{\boldsymbol {\Sigma }}_{11}}\right|^{1/2}}}\left[1+{\frac {1}{\nu }}({\mathbf {X} _{1}}-{{\boldsymbol {\mu }}_{1}})^{\mathsf {T}}{\boldsymbol {\Sigma }}_{11}^{-1}({\mathbf {X} _{1}}-{{\boldsymbol {\mu }}_{1}})\right]^{-(\nu \,+\,p_{1})/2}}
{\displaystyle f(X_{2})={\frac {\Gamma \left[(\nu +p_{2})/2\right]}{\Gamma (\nu /2)\,(\nu \,\pi )^{\,p_{2}/2}\left|{{\boldsymbol {\Sigma }}_{22}}\right|^{1/2}}}\left[1+{\frac {1}{\nu }}({\mathbf {X} _{2}}-{{\boldsymbol {\mu }}_{2}})^{\mathsf {T}}{\boldsymbol {\Sigma }}_{22}^{-1}({\mathbf {X} _{2}}-{{\boldsymbol {\mu }}_{2}})\right]^{-(\nu \,+\,p_{2})/2}}

If a transformation is constructed in the form
{\displaystyle \Theta _{p_{1}\times \,p}={\begin{bmatrix}1&\cdots &0&\cdots &0\\0&\ddots &0&\cdots &0\\0&\cdots &1&\cdots &0\end{bmatrix}}}

then vector 
{\displaystyle Y=\Theta X}

, as discussed below, has the same distribution as the marginal distribution of 
{\displaystyle X_{1}}

.

Rank-Reducing Linear Transform[edit]
In the linear transform case, if 

Θ

{\displaystyle \Theta }

 is a rectangular matrix 
{\displaystyle \Theta \in \mathbb {R} ^{m\times p},m<p}

, of rank 

m

{\displaystyle m}

 the result is dimensionality reduction. Here, Jacobian 
{\displaystyle \left|\Theta \right|}

 is seemingly rectangular but the value 
{\displaystyle \left|\Theta \Sigma \Theta ^{\mathsf {T}}\right|^{1/2}}

 in the denominator pdf is nevertheless correct. There is a discussion of rectangular matrix product determinants in Aitken.[12] In general if 
{\displaystyle X\sim t(p,\mu ,\Sigma ,\nu )}
{\displaystyle \Theta ^{m\times p}}

 has full rank 

m

{\displaystyle m}

 then
{\displaystyle Y=\Theta X+c\sim t(m,\Theta \mu +c,\Theta \Sigma \Theta ^{\mathsf {T}},\nu )}
{\displaystyle f_{Y}(Y)={\frac {\Gamma \left[(\nu +m)/2\right]}{\Gamma (\nu /2)\,(\nu \,\pi )^{\,m/2}\left|\Theta \Sigma \Theta ^{\mathsf {T}}\right|^{1/2}}}\left[1+{\frac {1}{\nu }}(Y-c_{1})^{\mathsf {T}}(\Theta \Sigma \Theta ^{\mathsf {T}})^{-1}(Y-c_{1})\right]^{-(\nu \,+\,m)/2},\;c_{1}=\Theta \mu +c}

In extremis, if m = 1 and 

Θ

{\displaystyle \Theta }

 becomes a row vector, then scalar Y follows a univariate double-sided Student-t distribution defined by 
{\displaystyle t^{2}=Y^{2}/\sigma ^{2}}

 with the same 

ν

{\displaystyle \nu }

 degrees of freedom.  Kibria et. al. use the affine transformation to find the marginal distributions which are also MV-t.

During affine transformations of variables with elliptical distributions all vectors must ultimately derive from one initial isotropic spherical vector 

Z

{\displaystyle Z}

 whose elements remain 'entangled' and are not statistically independent.
A vector of independent student-t samples is not consistent with the multivariate t distribution.
Adding two sample multivariate t vectors generated with independent Chi-squared samples and different 

ν

{\displaystyle \nu }

 values: 

1

/

u

1

/

ν

1

,

1

/

u

2

/

ν

2

{\textstyle {1}/{\sqrt {u_{1}/\nu _{1}}},\;\;{1}/{\sqrt {u_{2}/\nu _{2}}}}

 will not produce internally consistent distributions, though they will yield a Behrens-Fisher problem.[13]
Taleb compares many examples of fat-tail elliptical vs non-elliptical multivariate distributions
Related concepts[edit]
In univariate statistics, the Student's t-test makes use of Student's t-distribution
The elliptical multivariate-t distribution arises spontaneously in linearly constrained least squares solutions involving multivariate normal source data, for example the Markowitz global minimum variance solution in financial portfolio analysis.[14][15][2] which addresses an ensemble of normal random vectors or a random matrix.  It does not arise in ordinary least squares (OLS) or multiple regression with fixed dependent and independent variables which problem tends to produce well-behaved normal error probabilities.
Hotelling's T-squared distribution is a distribution that arises in multivariate statistics.
The matrix t-distribution is a distribution for random variables arranged in a matrix structure.
This article includes a list of general references, but it lacks sufficient corresponding inline citations. Please help to improve this article by introducing more precise citations. (May 2012) (Learn how and when to remove this message)
