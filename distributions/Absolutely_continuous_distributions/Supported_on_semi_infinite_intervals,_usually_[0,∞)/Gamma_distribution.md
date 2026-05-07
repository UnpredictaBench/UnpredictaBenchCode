# Gamma distribution

Probability distribution

| Gamma |
| --- |
| Probability density function |
| Cumulative distribution function |
| Parameters | α > 0 shape θ > 0 scale | α > 0 shapeλ > 0 rate |
| Support | x ∈ [ 0 , ∞ ) {\displaystyle x\in [0,\infty )} ${\displaystyle x\in [0,\infty )}$ | x ∈ [ 0 , ∞ ) {\displaystyle x\in [0,\infty )} ${\displaystyle x\in [0,\infty )}$ |
| PDF | f ( x ) = 1 Γ ( α ) θ α x α − 1 e − x / θ {\displaystyle f(x)={\frac {1}{\Gamma (\alpha )\theta ^{\alpha }}}x^{\alpha -1}e^{-x/\theta }} ${\displaystyle f(x)={\frac {1}{\Gamma (\alpha )\theta ^{\alpha }}}x^{\alpha -1}e^{-x/\theta }}$ | f ( x ) = λ α Γ ( α ) x α − 1 e − λ x {\displaystyle f(x)={\frac {\lambda ^{\alpha }}{\Gamma (\alpha )}}x^{\alpha -1}e^{-\lambda x}} ${\displaystyle f(x)={\frac {\lambda ^{\alpha }}{\Gamma (\alpha )}}x^{\alpha -1}e^{-\lambda x}}$ |
| CDF | F ( x ) = 1 Γ ( α ) γ ( α , x θ ) {\displaystyle F(x)={\frac {1}{\Gamma (\alpha )}}\gamma \left(\alpha ,{\frac {x}{\theta }}\right)} ${\displaystyle F(x)={\frac {1}{\Gamma (\alpha )}}\gamma \left(\alpha ,{\frac {x}{\theta }}\right)}$ | F ( x ) = 1 Γ ( α ) γ ( α , λ x ) {\displaystyle F(x)={\frac {1}{\Gamma (\alpha )}}\gamma (\alpha ,\lambda x)} ${\displaystyle F(x)={\frac {1}{\Gamma (\alpha )}}\gamma (\alpha ,\lambda x)}$ |
| Mean | α θ {\displaystyle \alpha \theta } ${\displaystyle \alpha \theta }$ | α λ {\displaystyle {\frac {\alpha }{\lambda }}} ${\displaystyle {\frac {\alpha }{\lambda }}}$ |
| Median | Simple closed form does not exist | Simple closed form does not exist |
| Mode | ( α − 1 ) θ for α ≥ 1 {\displaystyle (\alpha -1)\theta {\text{ for }}\alpha \geq 1} , 0 for α < 1 {\displaystyle 0{\text{ for }}\alpha <1} ${\displaystyle (\alpha -1)\theta {\text{ for }}\alpha \geq 1}$ ${\displaystyle 0{\text{ for }}\alpha <1}$ | α − 1 λ for α ≥ 1 , 0 for α < 1 {\displaystyle {\frac {\alpha -1}{\lambda }}{\text{ for }}\alpha \geq 1{\text{, }}0{\text{ for }}\alpha <1} ${\displaystyle {\frac {\alpha -1}{\lambda }}{\text{ for }}\alpha \geq 1{\text{, }}0{\text{ for }}\alpha <1}$ |
| Variance | α θ 2 {\displaystyle \alpha \theta ^{2}} ${\displaystyle \alpha \theta ^{2}}$ | α λ 2 {\displaystyle {\frac {\alpha }{\lambda ^{2}}}} ${\displaystyle {\frac {\alpha }{\lambda ^{2}}}}$ |
| Skewness | 2 α {\displaystyle {\frac {2}{\sqrt {\alpha }}}} ${\displaystyle {\frac {2}{\sqrt {\alpha }}}}$ | 2 α {\displaystyle {\frac {2}{\sqrt {\alpha }}}} ${\displaystyle {\frac {2}{\sqrt {\alpha }}}}$ |
| Excess kurtosis | 6 α {\displaystyle {\frac {6}{\alpha }}} ${\displaystyle {\frac {6}{\alpha }}}$ | 6 α {\displaystyle {\frac {6}{\alpha }}} ${\displaystyle {\frac {6}{\alpha }}}$ |
| Entropy | α + ln ⁡ θ + ln ⁡ Γ ( α ) + ( 1 − α ) ψ ( α ) {\displaystyle {\begin{aligned}\alpha &+\ln \theta +\ln \Gamma (\alpha )\\&+(1-\alpha )\psi (\alpha )\end{aligned}}} ${\displaystyle {\begin{aligned}\alpha &+\ln \theta +\ln \Gamma (\alpha )\\&+(1-\alpha )\psi (\alpha )\end{aligned}}}$ | α − ln ⁡ λ + ln ⁡ Γ ( α ) + ( 1 − α ) ψ ( α ) {\displaystyle {\begin{aligned}\alpha &-\ln \lambda +\ln \Gamma (\alpha )\\&+(1-\alpha )\psi (\alpha )\end{aligned}}} ${\displaystyle {\begin{aligned}\alpha &-\ln \lambda +\ln \Gamma (\alpha )\\&+(1-\alpha )\psi (\alpha )\end{aligned}}}$ |
| MGF | ( 1 − θ t ) − α for t < 1 θ {\displaystyle (1-\theta t)^{-\alpha }{\text{ for }}t<{\frac {1}{\theta }}} ${\displaystyle (1-\theta t)^{-\alpha }{\text{ for }}t<{\frac {1}{\theta }}}$ | ( 1 − t λ ) − α for t < λ {\displaystyle \left(1-{\frac {t}{\lambda }}\right)^{-\alpha }{\text{ for }}t<\lambda } ${\displaystyle \left(1-{\frac {t}{\lambda }}\right)^{-\alpha }{\text{ for }}t<\lambda }$ |
| CF | ( 1 − θ i t ) − α {\displaystyle (1-\theta it)^{-\alpha }} ${\displaystyle (1-\theta it)^{-\alpha }}$ | ( 1 − i t λ ) − α {\displaystyle \left(1-{\frac {it}{\lambda }}\right)^{-\alpha }} ${\displaystyle \left(1-{\frac {it}{\lambda }}\right)^{-\alpha }}$ |
| Fisher information | I ( α , θ ) = ( ψ ( 1 ) ( α ) θ − 1 θ − 1 α θ − 2 ) {\displaystyle I(\alpha ,\theta )={\begin{pmatrix}\psi ^{(1)}(\alpha )&\theta ^{-1}\\\theta ^{-1}&\alpha \theta ^{-2}\end{pmatrix}}} ${\displaystyle I(\alpha ,\theta )={\begin{pmatrix}\psi ^{(1)}(\alpha )&\theta ^{-1}\\\theta ^{-1}&\alpha \theta ^{-2}\end{pmatrix}}}$ | I ( α , λ ) = ( ψ ( 1 ) ( α ) − λ − 1 − λ − 1 α λ − 2 ) {\displaystyle I(\alpha ,\lambda )={\begin{pmatrix}\psi ^{(1)}(\alpha )&-\lambda ^{-1}\\-\lambda ^{-1}&\alpha \lambda ^{-2}\end{pmatrix}}} ${\displaystyle I(\alpha ,\lambda )={\begin{pmatrix}\psi ^{(1)}(\alpha )&-\lambda ^{-1}\\-\lambda ^{-1}&\alpha \lambda ^{-2}\end{pmatrix}}}$ |
| Method of moments | α = E [ X ] 2 V [ X ] , {\displaystyle \alpha ={\frac {E[X]^{2}}{V[X]}},} θ = V [ X ] E [ X ] {\displaystyle \theta ={\frac {V[X]}{E[X]}}\quad \quad } ${\displaystyle \alpha ={\frac {E[X]^{2}}{V[X]}},}$ ${\displaystyle \theta ={\frac {V[X]}{E[X]}}\quad \quad }$ | α = E [ X ] 2 V [ X ] , {\displaystyle \alpha ={\frac {E[X]^{2}}{V[X]}},} λ = E [ X ] V [ X ] {\displaystyle \lambda ={\frac {E[X]}{V[X]}}} ${\displaystyle \alpha ={\frac {E[X]^{2}}{V[X]}},}$ ${\displaystyle \lambda ={\frac {E[X]}{V[X]}}}$ |

In probability theory and statistics, the gamma distribution is a versatile two-parameter family of continuous probability distributions.[1]  The exponential distribution, Erlang distribution, and chi-squared distribution are special cases of the gamma distribution.[2]  There are two equivalent parameterizations in common use:

1. With a shape parameter α and a scale parameter θ
2. With a shape parameter 

α

{\displaystyle \alpha }

 and a rate parameter ⁠
{\displaystyle \lambda =1/\theta }

⁠ ${\displaystyle \alpha }$ ${\displaystyle \lambda =1/\theta }$

In each of these forms, both parameters are positive real numbers.

The distribution has important applications in various fields, including econometrics, Bayesian statistics, and life testing.[3] In econometrics, the (α, θ) parameterization is common for modeling waiting times, such as the time until death, where it often takes the form of an Erlang distribution for integer α values. Bayesian statisticians prefer the (α,λ) parameterization, utilizing the gamma distribution as a conjugate prior for several inverse scale parameters, facilitating analytical tractability in posterior distribution computations.

The gamma distribution is the maximum entropy probability distribution (both with respect to a uniform base measure and a 
{\displaystyle 1/x}

 base measure) for a random variable X for which E[X] = αθ = α/λ is fixed and greater than zero, and E[ln X] = ψ(α) + ln θ = ψ(α) − ln λ is fixed (ψ is the digamma function).[4] ${\displaystyle 1/x}$

Definitions[edit]
The parameterization with α and θ appears to be more common in econometrics and other applied fields, where the gamma distribution is frequently used to model waiting times. For instance, in life testing, the waiting time until death is a random variable that is frequently modeled with a gamma distribution. See Hogg and Craig[5]  for an explicit motivation.
The parameterization with α and λ is more common in Bayesian statistics, where the gamma distribution is used as a conjugate prior distribution for various types of inverse scale (rate) parameters, such as the λ of an exponential distribution or a Poisson distribution[6] – or for that matter, the λ of the gamma distribution itself. The closely related inverse-gamma distribution is used as a conjugate prior for scale parameters, such as the variance of a normal distribution.
If α is a positive integer, then the distribution represents an Erlang distribution; i.e., the sum of α independent exponentially distributed random variables, each of which has a mean of θ.

Characterization using shape α and rate λ[edit]
The gamma distribution can be parameterized in terms of a shape parameter α and an inverse scale parameter λ = 1/θ, called a rate parameter. A random variable X that is gamma-distributed with shape α and rate λ is denoted

X
∼
Γ
(
α
,
λ
)
≡
Gamma
{\displaystyle X\sim \Gamma (\alpha ,\lambda )\equiv \operatorname {Gamma} (\alpha ,\lambda )}

The corresponding probability density function in the shape-rate parameterization is
{\displaystyle {\begin{aligned}f(x;\alpha ,\lambda )&={\frac {x^{\alpha -1}e^{-\lambda x}\lambda ^{\alpha }}{\Gamma (\alpha )}}\quad {\text{ for }}x>0\quad \alpha ,\lambda >0,\\[6pt]\end{aligned}}}

where 
{\displaystyle \Gamma (\alpha )}

 is the gamma function.
For all positive integers, 
{\displaystyle \Gamma (\alpha )=(\alpha -1)!}

.
The cumulative distribution function is the regularized gamma function:
{\displaystyle F(x;\alpha ,\lambda )=\int _{0}^{x}f(u;\alpha ,\lambda )\,du={\frac {\gamma (\alpha ,\lambda x)}{\Gamma (\alpha )}},}

where 
{\displaystyle \gamma (\alpha ,\lambda x)}

 is the lower incomplete gamma function.
If α is a positive integer (i.e., the distribution is an Erlang distribution), the cumulative distribution function has the following series expansion:[7]
{\displaystyle {\begin{aligned}F(x;\alpha ,\lambda )&=1-\sum _{i=0}^{\alpha -1}{\frac {\left(\lambda x\right)^{i}}{i!}}e^{-\lambda x}\\[1ex]&=e^{-\lambda x}\sum _{i=\alpha }^{\infty }{\frac {\left(\lambda x\right)^{i}}{i!}}.\end{aligned}}}

Characterization using shape α and scale θ[edit]
A random variable X that is gamma-distributed with shape α and scale θ is denoted by

X
∼
Γ
(
α
,
θ
)
≡
Gamma
{\displaystyle X\sim \Gamma (\alpha ,\theta )\equiv \operatorname {Gamma} (\alpha ,\theta )}

Illustration of the gamma PDF for parameter values over α and x with θ set to 1, 2, 3, 4, 5, and 6. One can see each θ layer by itself here [2] as well as by α [3] and x. [4].
The probability density function using the shape-scale parametrization is
{\displaystyle f(x;\alpha ,\theta )={\frac {x^{\alpha -1}e^{-x/\theta }}{\theta ^{\alpha }\Gamma (\alpha )}}\quad {\text{ for }}x>0{\text{ and }}\alpha ,\theta >0.}

Here Γ(α) is the gamma function evaluated at α.
The cumulative distribution function is the regularized gamma function:
{\displaystyle F(x;\alpha ,\theta )=\int _{0}^{x}f(u;\alpha ,\theta )\,du={\frac {\gamma {\left(\alpha ,{\frac {x}{\theta }}\right)}}{\Gamma (\alpha )}},}

where 

γ

(

α
,

x
θ

)

{\textstyle \gamma {\left(\alpha ,{\frac {x}{\theta }}\right)}}

 is the lower incomplete gamma function.
It can also be expressed as follows, if α is a positive integer (i.e., the distribution is an Erlang distribution):[7]
{\displaystyle F(x;\alpha ,\theta )=1-\sum _{i=0}^{\alpha -1}{\frac {1}{i!}}\left({\frac {x}{\theta }}\right)^{i}e^{-x/\theta }=e^{-x/\theta }\sum _{i=\alpha }^{\infty }{\frac {1}{i!}}\left({\frac {x}{\theta }}\right)^{i}.}

Both parametrizations are common because either can be more convenient depending on the situation.

Properties[edit]
Mean and variance[edit]
The mean of gamma distribution is given by the product of its shape and scale parameters:
{\displaystyle \mu =\alpha \theta =\alpha /\lambda }

The variance is:
{\displaystyle \sigma ^{2}=\alpha \theta ^{2}=\alpha /\lambda ^{2}}

The square root of the inverse shape parameter gives the coefficient of variation:
{\displaystyle \sigma /\mu =\alpha ^{-0.5}=1/{\sqrt {\alpha }}}

Skewness[edit]
The skewness of the gamma distribution only depends on its shape parameter, α, and it is equal to 
{\displaystyle 2/{\sqrt {\alpha }}.}

Higher moments[edit]
The r-th raw moment is given by:
{\displaystyle \mathrm {E} [X^{r}]=\theta ^{r}{\frac {\Gamma (\alpha +r)}{\Gamma (\alpha )}}=\theta ^{r}\alpha ^{\overline {r}}}

with 
{\displaystyle \alpha ^{\overline {r}}}

 the rising factorial.

Median approximations and bounds[edit]
Bounds and asymptotic approximations to the median of the gamma distribution.  The cyan-colored region indicates the large gap between published lower and upper bounds before 2021.
Unlike the mode and the mean, which have readily calculable formulas based on the parameters, the median does not have a closed-form equation. The median for this distribution is the value 

ν

{\displaystyle \nu }

 such that
{\displaystyle {\frac {1}{\Gamma (\alpha )\theta ^{\alpha }}}\int _{0}^{\nu }x^{\alpha -1}e^{-x/\theta }dx={\frac {1}{2}}.}

A rigorous treatment of the problem of determining an asymptotic expansion and bounds for the median of the gamma distribution was handled first by Chen and Rubin, who proved that (for 
{\displaystyle \theta =1}
{\displaystyle \alpha -{\tfrac {1}{3}}<\nu (\alpha )<\alpha ,}

where 
{\displaystyle \mu (\alpha )=\alpha }

 is the mean and 
{\displaystyle \nu (\alpha )}

 is the median of the 

Gamma
{\displaystyle {\text{Gamma}}(\alpha ,1)}

 distribution.[8]  For other values of the scale parameter, the mean scales to 
{\displaystyle \mu =\alpha \theta }

, and the median bounds and approximations would be similarly scaled by θ.
K. P. Choi found the first five terms in a Laurent series asymptotic approximation of the median by comparing the median to Ramanujan's 

θ

{\displaystyle \theta }

 function.[9]  Berg and Pedersen found more terms:[10]

ν
(
α
)
=
α

−

1
3

+

8
405

α

−
1

+

184

25

515

α

−
2

+

2248
{\displaystyle {\begin{aligned}\nu (\alpha )=\alpha &-{\frac {1}{3}}+{\frac {8}{405}}\alpha ^{-1}+{\frac {184}{25\,515}}\alpha ^{-2}+{\frac {2248}{3\,444\,525}}\alpha ^{-3}\\[1ex]&-{\frac {19\,006\,408}{15\,345\,358\,875}}\alpha ^{-4}-{\mathcal {O}}{\left(\alpha ^{-5}\right)}+\cdots \end{aligned}}}

 Two gamma distribution median asymptotes which were proved in 2023 to be bounds (upper solid red and lower dashed red), of the from 
{\displaystyle \nu (\alpha )\approx 2^{-1/\alpha }(A+\alpha )}

, and an interpolation between them that makes an approximation (dotted red) that is exact at α = 1 and has maximum relative error of about 0.6%. The cyan shaded region is the remaining gap between upper and lower bounds (or conjectured bounds), including these new bounds and the bounds in the previous figure.
Log–log plot of upper (solid) and lower (dashed) bounds to the median of a gamma distribution and the gaps between them.  The green, yellow, and cyan regions represent the gap before the Lyon 2021 paper.  The green and yellow narrow that gap with the lower bounds that Lyon proved.  Lyon's bounds proved in 2023 further narrow the yellow.  Mostly within the yellow, closed-form rational-function-interpolated conjectured bounds are plotted along with the numerically calculated median (dotted) value.  Tighter interpolated bounds exist but are not plotted, as they would not be resolved at this scale.
Partial sums of these series are good approximations for high enough α; they are not plotted in the figure, which is focused on the low-α region that is less well approximated.
Berg and Pedersen also proved many properties of the median, showing that it is a convex function of α,[11] and that the asymptotic behavior near 
{\displaystyle \alpha =0}
{\displaystyle \nu (\alpha )\approx e^{-\gamma }2^{-1/\alpha }}

 (where γ is the Euler–Mascheroni constant), and that for all 
{\displaystyle \alpha >0}

 the median is bounded by 
{\displaystyle \alpha 2^{-1/\alpha }<\nu (\alpha )<ke^{-1/3k}}

.[10]
A closer linear upper bound, for 
{\displaystyle \alpha \geq 1}

 only, was provided in 2021 by Gaunt and Merkle,[12] relying on the Berg and Pedersen result that the slope of 
{\displaystyle \nu (\alpha )}

 is everywhere less than 1:
{\displaystyle \nu (\alpha )\leq \alpha -1+\log 2~~}
{\displaystyle \alpha \geq 1}

 (with equality at 
{\displaystyle \alpha =1}

)
which can be extended to a bound for all 
{\displaystyle \alpha >0}

 by taking the max with the chord shown in the figure, since the median was proved convex.[11]
An approximation to the median that is asymptotically accurate at high α and reasonable down to 
{\displaystyle \alpha =0.5}

 or a bit lower follows from the Wilson–Hilferty transformation:
{\displaystyle \nu (\alpha )=\alpha \left(1-{\frac {1}{9\alpha }}\right)^{3}}

which goes negative for 
{\displaystyle \alpha <1/9}

.
In 2021, Lyon proposed several approximations of the form 
{\displaystyle \nu (\alpha )\approx 2^{-1/\alpha }(A+B\alpha )}

.  He conjectured values of A and B for which this approximation is an asymptotically tight upper or lower bound for all 
{\displaystyle \alpha >0}

.[13]  In particular, he proposed these closed-form bounds, which he proved in 2023:[14]
{\displaystyle \nu _{L\infty }(\alpha )=2^{-1/\alpha }\left(\log 2-{\tfrac {1}{3}}+\alpha \right)}

 is a lower bound, asymptotically tight as 
{\displaystyle \alpha \to \infty }
{\displaystyle \nu _{U}(\alpha )=2^{-1/\alpha }(e^{-\gamma }+\alpha )\quad }

 is an upper bound, asymptotically tight as 
{\displaystyle \alpha \to 0}

Lyon also showed (informally in 2021, rigorously in 2023) two other lower bounds that are not closed-form expressions, including this one involving the gamma function, based on solving the integral expression substituting 1 for 
{\displaystyle e^{-x}}
{\displaystyle \nu (\alpha )>\left({\frac {2}{\Gamma (\alpha +1)}}\right)^{-1/\alpha }}

 (approaching equality as 
{\displaystyle k\to 0}

)
and the tangent line at 
{\displaystyle \alpha =1}

 where the derivative was found to be 

ν

′

(
1
)
≈
0.9680448

{\displaystyle \nu ^{\prime }(1)\approx 0.9680448}
{\displaystyle \nu (\alpha )\geq \nu (1)+(\alpha -1)\nu ^{\prime }(1)\quad }

 (with equality at 
{\displaystyle k=1}
{\displaystyle \nu (\alpha )\geq \log 2+(\alpha -1)\left[\gamma -2\operatorname {Ei} (-\log 2)-\log \log 2\right]}

where Ei is the exponential integral.[13][14]
Additionally, he showed that interpolations between bounds could provide excellent approximations or tighter bounds to the median, including an approximation that is exact at 
{\displaystyle \alpha =1}

 (where 
{\displaystyle \nu (1)=\log 2}

) and has a maximum relative error less than 0.6%.  Interpolated approximations and bounds are all of the form
{\displaystyle \nu (\alpha )\approx {\tilde {g}}(\alpha )\nu _{L\infty }(\alpha )+(1-{\tilde {g}}(\alpha ))\nu _{U}(\alpha )}

where 
{\displaystyle {\tilde {g}}}

 is an interpolating function running monotonially from 0 at low α to 1 at high α, approximating an ideal, or exact, interpolator 
{\displaystyle g(\alpha )}
{\displaystyle g(\alpha )={\frac {\nu _{U}(\alpha )-\nu (\alpha )}{\nu _{U}(\alpha )-\nu _{L\infty }(\alpha )}}}

For the simplest interpolating function considered, a first-order rational function
{\displaystyle {\tilde {g}}_{1}(\alpha )={\frac {\alpha }{b_{0}+\alpha }}}

the tightest lower bound has

b

0

=

8
405

+

e

−
γ

log
⁡
2
−

log

2

⁡
2

2

e

−
γ

−
log
⁡
2
+

1
3

−
log
⁡
2
≈
0.143472

{\displaystyle b_{0}={\frac {{\frac {8}{405}}+e^{-\gamma }\log 2-{\frac {\log ^{2}2}{2}}}{e^{-\gamma }-\log 2+{\frac {1}{3}}}}-\log 2\approx 0.143472}

and the tightest upper bound has

b

0

=

e

−
γ

−
log
⁡
2
+

1
3

1
−

e

−
γ

π

2

12

≈
0.374654

{\displaystyle b_{0}={\frac {e^{-\gamma }-\log 2+{\frac {1}{3}}}{1-{\frac {e^{-\gamma }\pi ^{2}}{12}}}}\approx 0.374654}

The interpolated bounds are plotted (mostly inside the yellow region) in the log–log plot shown.  Even tighter bounds are available using different interpolating functions, but not usually with closed-form parameters like these.[13]

Summation[edit]
If Xi has a Gamma(αi, θ) distribution for i = 1, 2, ..., N (i.e., all distributions have the same scale parameter θ), then
{\displaystyle \sum _{i=1}^{N}X_{i}\sim \mathrm {Gamma} \left(\sum _{i=1}^{N}\alpha _{i},\theta \right)}

provided all Xi are independent.
For the cases where the Xi are independent but have different scale parameters, see Mathai [15] or Moschopoulos.[16]
The gamma distribution exhibits infinite divisibility.

Scaling[edit]
{\displaystyle X\sim \mathrm {Gamma} (\alpha ,\theta ),}

then, for any c > 0,
{\displaystyle cX\sim \mathrm {Gamma} (\alpha ,c\,\theta ),}

 by moment generating functions,
or equivalently, if
{\displaystyle X\sim \mathrm {Gamma} \left(\alpha ,\lambda \right)}

 (shape-rate parameterization)
{\displaystyle cX\sim \mathrm {Gamma} \left(\alpha ,{\frac {\lambda }{c}}\right),}

Indeed, we know that if X is an exponential r.v. with rate λ, then cX is an exponential r.v. with rate λ/c; the same thing is valid with Gamma variates (and this can be checked using the moment-generating function, see, e.g.,these notes, 10.4-(ii)): multiplication by a positive constant c divides the rate (or, equivalently, multiplies the scale).

Exponential family[edit]
The gamma distribution is a two-parameter exponential family with natural parameters α − 1 and −1/θ (equivalently, α − 1 and −λ), and natural statistics X and ln X.
If the shape parameter α is held fixed, the resulting one-parameter family of distributions is a natural exponential family.

Logarithmic expectation and variance[edit]
One can show that
{\displaystyle \operatorname {E} [\ln X]=\psi (\alpha )-\ln \lambda }

or equivalently,
{\displaystyle \operatorname {E} [\ln X]=\psi (\alpha )+\ln \theta }

where ψ is the digamma function.  Likewise,
{\displaystyle \operatorname {var} [\ln X]=\psi ^{(1)}(\alpha )}

where 
{\displaystyle \psi ^{(1)}}

 is the trigamma function.
This can be derived using the exponential family formula for the moment generating function of the sufficient statistic, because one of the sufficient statistics of the gamma distribution is ln x.

Information entropy[edit]
The information entropy is
{\displaystyle {\begin{aligned}\operatorname {H} (X)&=\operatorname {E} [-\ln p(X)]\\[4pt]&=\operatorname {E} [-\alpha \ln \lambda +\ln \Gamma (\alpha )-(\alpha -1)\ln X+\lambda X]\\[4pt]&=\alpha -\ln \lambda +\ln \Gamma (\alpha )+(1-\alpha )\psi (\alpha ).\end{aligned}}}

In the α, θ parameterization, the information entropy is given by
{\displaystyle \operatorname {H} (X)=\alpha +\ln \theta +\ln \Gamma (\alpha )+(1-\alpha )\psi (\alpha ).}

Kullback–Leibler divergence[edit]
Illustration of the Kullback–Leibler (KL) divergence for two gamma PDFs. Here λ = λ0 + 1 which are set to 1, 2, 3, 4, 5, and 6. The typical asymmetry for the KL divergence is clearly visible.
The Kullback–Leibler divergence (KL-divergence), of Gamma(αp,  λp) ("true" distribution) from Gamma(αq, λq) ("approximating" distribution) is given by[17]
{\displaystyle {\begin{aligned}D_{\mathrm {KL} }(\alpha _{p},\lambda _{p};\alpha _{q},\lambda _{q})={}&(\alpha _{p}-\alpha _{q})\psi (\alpha _{p})-\log {\frac {\Gamma (\alpha _{p})}{\Gamma (\alpha _{q})}}\\&{}+\alpha _{q}\log {\frac {\lambda _{p}}{\lambda _{q}}}+\alpha _{p}\left({\frac {\lambda _{q}}{\lambda _{p}}}-1\right).\end{aligned}}}

Written using the α, θ parameterization, the KL-divergence of Gamma(αp,  θp) from Gamma(αq,  θq) is given by
{\displaystyle {\begin{aligned}D_{\mathrm {KL} }(\alpha _{p},\theta _{p};\alpha _{q},\theta _{q})={}&(\alpha _{p}-\alpha _{q})\psi (\alpha _{p})-\log {\frac {\Gamma (\alpha _{p})}{\Gamma (\alpha _{q})}}\\&{}+\alpha _{q}\log {\frac {\theta _{q}}{\theta _{p}}}+\alpha _{p}\left({\frac {\theta _{p}}{\theta _{q}}}-1\right).\end{aligned}}}

Laplace transform[edit]
The Laplace transform of the gamma PDF, which is the moment-generating function of the gamma distribution, is
{\displaystyle F(s)=\operatorname {E} \left[e^{-sX}\right]={\frac {1}{\left(1+\theta s\right)^{\alpha }}}=\left({\frac {\lambda }{\lambda +s}}\right)^{\alpha }}

(where 

X

{\textstyle X}

 is a random variable with that distribution).

Related distributions[edit]
General[edit]
{\displaystyle X_{1},X_{2},\ldots ,X_{n}}
{\displaystyle n}

 independent and identically distributed random variables following an exponential distribution with rate parameter λ, then 

∑

i

X

i

∼
Gamma
⁡
(
n
,
λ
)

{\textstyle \sum _{i}X_{i}\sim \operatorname {Gamma} (n,\lambda )}

 where n is the shape parameter and λ is the rate, and 

X
¯

=

1
n

∑

i

X

i

∼
Gamma
⁡
(
n
,
n
λ
)

{\textstyle {\bar {X}}={\frac {1}{n}}\sum _{i}X_{i}\sim \operatorname {Gamma} (n,n\lambda )}

.
If X ~ Gamma(1, λ) (in the shape–rate parametrization), then X has an exponential distribution with rate parameter λ. In the shape-scale parametrization, X ~ Gamma(1, θ) has an exponential distribution with rate parameter 1/θ.
If X ~ Gamma(ν/2, 2) (in the shape–scale parametrization), then X is identical to χ2(ν), the chi-squared distribution with ν degrees of freedom. Conversely, if Q ~ χ2(ν) and c is a positive constant, then cQ ~ Gamma(ν/2, 2c).
If θ = 1/α, one obtains the Schulz-Zimm distribution, which is most prominently used to model polymer chain lengths.
If α is an integer, the gamma distribution is an Erlang distribution and is the probability distribution of the waiting time until the α-th "arrival" in a one-dimensional Poisson process with intensity 1/θ. If

X
∼
Γ
(
α
∈

Z

,
θ
)
,

Y
∼
Pois
{\displaystyle X\sim \Gamma (\alpha \in \mathbb {Z} ,\theta ),\qquad Y\sim \operatorname {Pois} \left({\frac {x}{\theta }}\right),}

then
{\displaystyle \Pr(X>x)=\Pr(Y<\alpha ).}

If X has a Maxwell–Boltzmann distribution with parameter a, then
{\displaystyle X^{2}\sim \Gamma {\left({\tfrac {3}{2}},2a^{2}\right)}.}

If X ~ Gamma(α, θ), then 

exp
⁡
X

{\textstyle \exp X}

 follows a log-gamma distribution.[18]
If X ~ Gamma(α, θ), then 

log
⁡
X

{\textstyle \log X}

 follows an exponential-gamma (abbreviated exp-gamma) distribution.[19] It is sometimes incorrectly referred to as the log-gamma distribution.[20] Formulas for its mean and variance are in the section #Logarithmic expectation and variance.
If X ~ Gamma(α, θ), then 

X

{\displaystyle {\sqrt {X}}}

 follows a generalized gamma distribution with parameters p = 2, d = 2α, and 
{\displaystyle a={\sqrt {\theta }}}

.[citation needed]
More generally, if X ~ Gamma(α,θ), then 
{\displaystyle X^{q}}
{\displaystyle q>0}

 follows a generalized gamma distribution with parameters p = 1/q, d = α/q, and 
{\displaystyle a=\theta ^{q}}

.
If X ~ Gamma(α, θ) with shape α and scale θ, then 1/X ~ Inv-Gamma(α, θ−1) (see Inverse-gamma distribution for derivation).
Parametrization 1: If 
{\displaystyle X_{k}\sim \Gamma (\alpha _{k},\theta _{k})\,}

 are independent, then 
{\displaystyle {\frac {\alpha _{2}\theta _{2}X_{1}}{\alpha _{1}\theta _{1}X_{2}}}\sim \mathrm {F} (2\alpha _{1},2\alpha _{2})}

, or equivalently, 
{\displaystyle {\frac {X_{1}}{X_{2}}}\sim \lambda '\left(\alpha _{1},\alpha _{2},1,{\frac {\theta _{1}}{\theta _{2}}}\right)}

Parametrization 2: If 
{\displaystyle X_{k}\sim \Gamma (\alpha _{k},\lambda _{k})\,}

 are independent, then 
{\displaystyle {\frac {\alpha _{2}\lambda _{1}X_{1}}{\alpha _{1}\lambda _{2}X_{2}}}\sim \mathrm {F} (2\alpha _{1},2\alpha _{2})}

, or equivalently, 
{\displaystyle {\frac {X_{1}}{X_{2}}}\sim \lambda '\left(\alpha _{1},\alpha _{2},1,{\frac {\lambda _{2}}{\lambda _{1}}}\right)}

If X ~ Gamma(α, θ) and Y ~ Gamma(λ, θ) are independently distributed, then X/(X + Y) has a beta distribution with parameters α and λ, and X/(X + Y) is independent of X + Y, which is Gamma(α + λ, θ)-distributed.
If 

X

n

∼

Beta
{\displaystyle X_{n}\sim {\text{Beta}}(\alpha ,n\lambda )\,}
{\displaystyle Y_{n}=nX_{n}}

, then 
{\displaystyle Y_{n}}

 converges in distribution to 

Gamma
{\displaystyle {\text{Gamma}}(\alpha ,\lambda )}

 defined under parametrization 2.
If Xi ~ Gamma(αi, 1) are independently distributed, then the vector (X1/S, ..., Xn/S), where S = X1 + ... + Xn, follows a Dirichlet distribution with parameters α1, ..., αn.
For large α the gamma distribution converges to normal distribution with mean μ = αθ and variance σ2 = αθ2.
The gamma distribution is the conjugate prior for the precision of the normal distribution with known mean.
The matrix gamma distribution and the Wishart distribution are multivariate generalizations of the gamma distribution (samples are positive-definite matrices rather than positive real numbers).
The gamma distribution is a special case of the generalized gamma distribution, the generalized integer gamma distribution, and the generalized inverse Gaussian distribution.
Among the discrete distributions, the negative binomial distribution is sometimes considered the discrete analog of the gamma distribution.
Tweedie distributions – the gamma distribution is a member of the family of Tweedie exponential dispersion models.
Modified Half-normal distribution – the Gamma distribution is a member of the family of Modified half-normal distribution.[21] The corresponding density is 
{\displaystyle f(x\mid \alpha ,\lambda ,\gamma )={\frac {2\lambda ^{\frac {\alpha }{2}}x^{\alpha -1}\exp(-\lambda x^{2}+\gamma x)}{\Psi {\left({\frac {\alpha }{2}},{\frac {\gamma }{\sqrt {\lambda }}}\right)}}}}

, where 
{\displaystyle \Psi (\alpha ,z)={}_{1}\Psi _{1}{\left({\begin{matrix}\left(\alpha ,{\frac {1}{2}}\right)\\(1,0)\end{matrix}};z\right)}}

 denotes the Fox–Wright Psi function.
For the shape-scale parameterization 
{\displaystyle x|\theta \sim \Gamma (\alpha ,\theta )}

, if the scale parameter 
{\displaystyle \theta \sim IG(b,1)}

 where 
{\displaystyle IG}

 denotes the Inverse-gamma distribution, then the marginal distribution 
{\displaystyle x\sim \lambda '(\alpha ,b)}

 where 
{\displaystyle \lambda '}

 denotes the Beta prime distribution.
Compound gamma[edit]
If the shape parameter of the gamma distribution is known, but the inverse-scale parameter is unknown, then a gamma distribution for the inverse scale forms a conjugate prior. The compound distribution, which results from integrating out the inverse scale, has a closed-form solution known as the compound gamma distribution.[22]
If, instead, the shape parameter is known but the mean is unknown, with the prior of the mean being given by another gamma distribution, then it results in K-distribution.

Statistical inference[edit]
Parameter estimation[edit]
Maximum likelihood estimation[edit]
The likelihood function for N iid observations (x1, ..., xN) is
{\displaystyle L(\alpha ,\theta )=\prod _{i=1}^{N}f(x_{i};\alpha ,\theta )}

from which we calculate the log-likelihood function
{\displaystyle \ell (\alpha ,\theta )=(\alpha -1)\sum _{i=1}^{N}\ln x_{i}-\sum _{i=1}^{N}{\frac {x_{i}}{\theta }}-N\alpha \ln \theta -N\ln \Gamma (\alpha )}

Finding the maximum with respect to θ by taking the derivative and setting it equal to zero yields the maximum likelihood estimator of the θ parameter, which equals the sample mean 
{\displaystyle {\bar {x}}}

 divided by the shape parameter α:
{\displaystyle {\hat {\theta }}={\frac {1}{\alpha N}}\sum _{i=1}^{N}x_{i}={\frac {\bar {x}}{\alpha }}}

Substituting this into the log-likelihood function gives
{\displaystyle \ell (\alpha )=(\alpha -1)\sum _{i=1}^{N}\ln x_{i}-N\alpha -N\alpha \ln {\frac {\sum _{i}x_{i}}{\alpha N}}-N\ln \Gamma (\alpha )}

We need at least two samples: 
{\displaystyle N\geq 2}

, because for 
{\displaystyle N=1}

, the function 
{\displaystyle \ell (\alpha )}

 increases without bounds as 
{\displaystyle \alpha \to \infty }

. For 
{\displaystyle \alpha >0}

, it can be verified that 
{\displaystyle \ell (\alpha )}

 is strictly concave, by using inequality properties of the polygamma function. Finding the maximum with respect to α by taking the derivative and setting it equal to zero yields
{\displaystyle {\begin{aligned}\ln \alpha -\psi (\alpha )&=\ln \left({\frac {1}{N}}\sum _{i=1}^{N}x_{i}\right)-{\frac {1}{N}}\sum _{i=1}^{N}\ln x_{i}\\[1ex]&=\ln {\bar {x}}-{\overline {\ln x}}\end{aligned}}}

where ψ is the digamma function and 
{\displaystyle {\overline {\ln x}}}

 is the sample mean of ln x. There is no closed-form solution for α. The function is numerically very well behaved, so if a numerical solution is desired, it can be found using, for example, Newton's method. An initial value of k can be found either using the method of moments, or using the approximation
{\displaystyle \ln \alpha -\psi (\alpha )\approx {\frac {1}{2\alpha }}\left(1+{\frac {1}{6\alpha +1}}\right)}

If we let
{\displaystyle {\begin{aligned}s&=\ln \left({\frac {1}{N}}\sum _{i=1}^{N}x_{i}\right)-{\frac {1}{N}}\sum _{i=1}^{N}\ln x_{i}\\[1ex]&=\ln {\bar {x}}-{\overline {\ln x}}\end{aligned}}}

then α is approximately
{\displaystyle k\approx {\frac {3-s+{\sqrt {\left(s-3\right)^{2}+24s}}}{12s}}}

which is within 1.5% of the correct value.[23] An explicit form for the Newton–Raphson update of this initial guess is:[24]
{\displaystyle \alpha \leftarrow \alpha -{\frac {\ln \alpha -\psi (k)-s}{{\frac {1}{\alpha }}-\psi \prime (\alpha )}}.}

At the maximum-likelihood estimate 
{\displaystyle ({\hat {\alpha }},{\hat {\theta }})}

, the expected values for x and 
{\displaystyle \ln x}

 agree with the empirical averages:
{\displaystyle {\begin{aligned}{\hat {\alpha }}{\hat {\theta }}&={\bar {x}}&&{\text{and}}&\psi ({\hat {\alpha }})+\ln {\hat {\theta }}&={\overline {\ln x}}.\end{aligned}}}

Caveat for small shape parameter[edit]
For data, 
{\displaystyle (x_{1},\ldots ,x_{N})}

, that is represented in a floating point format that underflows to 0 for values smaller than 

ε

{\displaystyle \varepsilon }

, the logarithms that are needed for the maximum-likelihood estimate will cause failure if there are any underflows. If we assume the data was generated by a gamma distribution with cdf 
{\displaystyle F(x;\alpha ,\theta )}

, then the probability that there is at least one underflow is:

Pr
(

underflow
{\displaystyle \Pr({\text{underflow}})=1-(1-F(\varepsilon ;\alpha ,\theta ))^{N}}

This probability will approach 1 for small α and  large N. For example, at 
{\displaystyle \alpha =10^{-2}}
{\displaystyle N=10^{4}}

 and 

ε
=
2.25
{\displaystyle \varepsilon =2.25\times 10^{-308}}

, 

Pr
(

underflow

)
≈
0.9998

{\displaystyle \Pr({\text{underflow}})\approx 0.9998}

. A workaround is to instead have the data in logarithmic format.
In order to test an implementation of a maximum-likelihood estimator that takes logarithmic data as input, it is useful to be able to generate non-underflowing logarithms of random gamma variates, when 
{\displaystyle \alpha <1}

. Following the implementation in scipy.stats.loggamma, this can be done as follows:[25] sample 

Y
∼

Gamma
{\displaystyle Y\sim {\text{Gamma}}(\alpha +1,\theta )}

 and 

U
∼

Uniform

{\displaystyle U\sim {\text{Uniform}}}

 independently. Then the required logarithmic sample is 
{\displaystyle Z=\ln(Y)+\ln(U)/\alpha }

, so that 

exp
⁡
(
Z
)
∼

Gamma
{\displaystyle \exp(Z)\sim {\text{Gamma}}(k,\theta )}

.

Closed-form estimators[edit]
There exist consistent closed-form estimators of α and θ that are derived from the likelihood of the generalized gamma distribution.[26]
The estimate for the shape α is
{\displaystyle {\hat {\alpha }}={\frac {N\sum \limits _{i=1}^{N}x_{i}}{N\sum \limits _{i=1}^{N}x_{i}\ln x_{i}-\sum \limits _{i=1}^{N}x_{i}\sum \limits _{i=1}^{N}\ln x_{i}}}}

and the estimate for the scale θ is
{\displaystyle {\hat {\theta }}={\frac {1}{N^{2}}}\left(N\sum _{i=1}^{N}x_{i}\ln x_{i}-\sum _{i=1}^{N}x_{i}\sum _{i=1}^{N}\ln x_{i}\right)}

Using the sample mean of x, the sample mean of ln x, and the sample mean of the product x·ln x simplifies the expressions to:
{\displaystyle {\hat {\alpha }}={\frac {\bar {x}}{\hat {\theta }}}}
{\displaystyle {\hat {\theta }}={\overline {x\ln x}}-{\bar {x}}{\overline {\ln x}}.}

If the rate parameterization is used, the estimate of 
{\displaystyle {\hat {\lambda }}=1/{\hat {\theta }}}

.
These estimators are not strictly maximum likelihood estimators, but are instead referred to as mixed type log-moment estimators. They have however similar efficiency as the maximum likelihood estimators.
Although these estimators are consistent, they have a small bias. A bias-corrected variant of the estimator for the scale θ is
{\displaystyle {\tilde {\theta }}={\frac {N}{N-1}}{\hat {\theta }}}

A bias correction for the shape parameter α is given as[27]
{\displaystyle {\tilde {\alpha }}={\hat {\alpha }}-{\frac {1}{N}}\left(3{\hat {\alpha }}-{\frac {2}{3}}\left({\frac {\hat {\alpha }}{1+{\hat {\alpha }}}}\right)-{\frac {4}{5}}{\frac {\hat {\alpha }}{(1+{\hat {\alpha }})^{2}}}\right)}

Bayesian minimum mean squared error[edit]
With known α and unknown θ, the posterior density function for theta (using the standard scale-invariant prior for θ) is
{\displaystyle \Pr(\theta \mid \alpha ,x_{1},\dots ,x_{N})\propto {\frac {1}{\theta }}\prod _{i=1}^{N}f(x_{i};\alpha ,\theta )}

Denoting
{\displaystyle y\equiv \sum _{i=1}^{N}x_{i},\qquad \Pr(\theta \mid \alpha ,x_{1},\dots ,x_{N})=C(x_{i})\theta ^{-N\alpha -1}e^{-y/\theta }}

where the C (integration) constant does not depend on θ. The form of the posterior density reveals that 1 / θ is gamma-distributed with shape parameter Nα + 2 and rate parameter y. Integration with respect to θ can be carried out using a change of variables to find the integration constant
{\displaystyle {\begin{aligned}\int _{0}^{\infty }\theta ^{-N\alpha -1+m}e^{-y/\theta }\,d\theta &=\int _{0}^{\infty }x^{N\alpha -1-m}e^{-xy}\,dx\\&=y^{-(N\alpha -m)}\Gamma (N\alpha -m)\!\end{aligned}}}

The moments can be computed by taking the ratio (m by m = 0)
{\displaystyle \operatorname {E} [x^{m}]={\frac {\Gamma (N\alpha -m)}{\Gamma (N\alpha )}}y^{m}}

which shows that the mean ± standard deviation estimate of the posterior distribution for θ is
{\displaystyle {\frac {y}{N\alpha -1}}\pm {\sqrt {\frac {y^{2}}{\left(N\alpha -1\right)^{2}(N\alpha -2)}}}.}

Bayesian inference[edit]
Conjugate prior[edit]
In Bayesian inference, the gamma distribution is the conjugate prior to many likelihood distributions: the Poisson, exponential, normal (with known mean), Pareto, gamma with known shape σ, inverse gamma with known shape parameter, and Gompertz with known scale parameter. 
The gamma distribution's conjugate prior is:[28]
{\displaystyle p(\alpha ,\theta \mid p,q,r,s)={\frac {1}{Z}}{\frac {p^{\alpha -1}e^{-\theta ^{-1}q}}{\Gamma (\alpha )^{r}\theta ^{\alpha s}}},}

where Z is the normalizing constant with no closed-form solution.
The posterior distribution can be found by updating the parameters as follows:
{\displaystyle {\begin{aligned}p'&=p\prod \nolimits _{i}x_{i},\\q'&=q+\sum \nolimits _{i}x_{i},\\r'&=r+n,\\s'&=s+n,\end{aligned}}}

where n is the number of observations, and xi is the i-th observation from the gamma distribution.

Occurrence and applications[edit]
Consider a sequence of events, with the waiting time for each event being an exponential distribution with rate λ. Then the waiting time for the n-th event to occur is the gamma distribution with integer shape 
{\displaystyle \alpha =n}

. This construction of the gamma distribution allows it to model a wide variety of phenomena where several sub-events, each taking time with exponential distribution, must happen in sequence for a major event to occur.[29] Examples include the waiting time of cell-division events,[30] number of compensatory mutations for a given mutation,[31] waiting time until a repair is necessary for a hydraulic system,[32] and so on.
In biophysics, the dwell time between steps of a molecular motor like ATP synthase is nearly exponential at constant ATP concentration, revealing that each step of the motor takes a single ATP hydrolysis. If there were n ATP hydrolysis events, then it would be a gamma distribution with degree n.[33]
The gamma distribution has been used to model the size of insurance claims[34] and rainfalls.[35] This means that aggregate insurance claims and the amount of rainfall accumulated in a reservoir are modelled by a gamma process – much like the exponential distribution generates a Poisson process.
The gamma distribution is also used to model errors in multi-level Poisson regression models because a mixture of Poisson distributions with gamma-distributed rates has a known closed form distribution, called negative binomial.
In wireless communication, the gamma distribution is used to model the multi-path fading of signal power;[citation needed] see also Rayleigh distribution and Rician distribution.
In oncology, the age distribution of cancer incidence often follows the gamma distribution, wherein the shape and scale parameters predict, respectively, the number of driver events and the time interval between them.[36][37]
In neuroscience, the gamma distribution is often used to describe the distribution of inter-spike intervals.[38][39]
In bacterial gene expression where protein production can occur in bursts, the copy number of a given protein often follows the gamma distribution, where the shape and scale parameters are, respectively, the mean number of bursts per cell cycle and the mean number of protein molecules produced per burst.[40]
In genomics, the gamma distribution was applied in peak calling step (i.e., in recognition of signal) in ChIP-chip[41] and ChIP-seq[42] data analysis.
In Bayesian statistics, the gamma distribution is widely used as a conjugate prior. It is the conjugate prior for the precision (i.e. inverse of the variance) of a normal distribution. It is also the conjugate prior for the exponential distribution.
In phylogenetics, the gamma distribution is the most commonly used approach to model among-sites rate variation[43] when maximum likelihood, Bayesian, or distance matrix methods are used to estimate phylogenetic trees. Phylogenetic analyzes that use the gamma distribution to model rate variation estimate a single parameter from the data because they limit consideration to distributions where α = λ. This parameterization means that the mean of this distribution is 1 and the variance is 1/α. Maximum likelihood and Bayesian methods typically use a discrete approximation to the continuous gamma distribution.[44][45]

Random variate generation[edit]
Given the scaling property above, it is enough to generate gamma variables with θ = 1, as we can later convert to any value of λ with a simple division.
Suppose we wish to generate random variables from Gamma(n + δ, 1), where n is a non-negative integer and 0 < δ < 1. Using the fact that a Gamma(1, 1) distribution is the same as an Exp(1) distribution, and noting the method of generating exponential variables, we conclude that if U is uniformly distributed on (0, 1], then −ln U is distributed Gamma(1, 1) (i.e. inverse transform sampling). Now, using the "α-addition" property of gamma distribution, we expand this result:
{\displaystyle -\sum _{k=1}^{n}\ln U_{k}\sim \Gamma (n,1)}

where Uk are all uniformly distributed on (0, 1] and independent. All that is left now is to generate a variable distributed as Gamma(δ, 1) for 0 < δ < 1 and apply the "α-addition" property once more. This is the most difficult part.
Random generation of gamma variates is discussed in detail by Devroye,[46]: 401–428  noting that none are uniformly fast for all shape parameters. For small values of the shape parameter, the algorithms are often not valid.[46]: 406  For arbitrary values of the shape parameter, one can apply the Ahrens and Dieter[47] modified acceptance-rejection method Algorithm GD (shape α ≥ 1), or transformation method[48] when 0 < α < 1. Also see Cheng and Feast Algorithm GKM 3[49] or Marsaglia's squeeze method.[50]
The following is a version of the Ahrens-Dieter acceptance–rejection method:[47]

Generate U, V and W as iid uniform (0, 1] variates.
{\displaystyle U\leq {\frac {e}{e+\delta }}}

 then 
{\displaystyle \xi =V^{1/\delta }}
{\displaystyle \eta =W\xi ^{\delta -1}}

. Otherwise, 
{\displaystyle \xi =1-\ln V}
{\displaystyle \eta =We^{-\xi }}
{\displaystyle \eta >\xi ^{\delta -1}e^{-\xi }}

 then go to step 1.
ξ is distributed as Γ(δ, 1).
A summary of this is
{\displaystyle \theta \left(\xi -\sum _{i=1}^{\lfloor \alpha \rfloor }\ln U_{i}\right)\sim \Gamma (\alpha ,\theta )}

where 
{\displaystyle \scriptstyle \lfloor \alpha \rfloor }

 is the integer part of α, ξ is generated via the algorithm above with δ = {α} (the fractional part of α) and the Uk are all independent.
While the above approach is technically correct, Devroye notes that it is linear in the value of α and generally is not a good choice. Instead, he recommends using either rejection-based or table-based methods, depending on context.[46]: 401–428 
For example, Marsaglia's simple transformation-rejection method relying on one normal variate X and one uniform variate U:[25]
{\displaystyle d=a-{\frac {1}{3}}}
{\displaystyle c={\frac {1}{\sqrt {9d}}}}
{\displaystyle v=(1+cX)^{3}}
{\displaystyle v>0}
{\displaystyle \ln U<{\frac {X^{2}}{2}}+d-dv+d\ln v}

 return 
{\displaystyle dv}

, else go back to step 2.
With 
{\displaystyle 1\leq a=\alpha }

 generates a gamma distributed random number in time that is approximately constant with α.  The acceptance rate does depend on α, with an acceptance rate of 0.95, 0.98, and 0.99 for α = 1, 2, and 4.  For α < 1, one can use 
{\displaystyle \gamma _{\alpha }=\gamma _{1+\alpha }U^{1/\alpha }}

 to boost k to be usable with this method.
In Matlab numbers can be generated using the function gamrnd(), which uses the α, θ representation.
