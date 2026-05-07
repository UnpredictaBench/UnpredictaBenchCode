# Log-normal distribution

Probability distribution

| Log-normal distribution |
| --- |
| Probability density functionIdentical parameter μ {\displaystyle \mu } but differing parameters σ {\displaystyle \sigma } ${\displaystyle \mu }$ ${\displaystyle \sigma }$ |
| Cumulative distribution function μ = 0 {\displaystyle \mu =0} ${\displaystyle \mu =0}$ |
| Notation | Lognormal ⁡ ( μ , σ 2 ) {\displaystyle \operatorname {Lognormal} \left(\mu ,\,\sigma ^{2}\right)} ${\displaystyle \operatorname {Lognormal} \left(\mu ,\,\sigma ^{2}\right)}$ |
| Parameters | μ ∈ ( − ∞ , + ∞ ) {\displaystyle \mu \in (-\infty ,+\infty )} (logarithm of location), σ > 0 {\displaystyle \sigma >0} (logarithm of scale) ${\displaystyle \mu \in (-\infty ,+\infty )}$ ${\displaystyle \sigma >0}$ |
| Support | x ∈ ( 0 , + ∞ ) {\displaystyle x\in (0,+\infty )} ${\displaystyle x\in (0,+\infty )}$ |
| PDF | 1 x σ 2 π exp ⁡ ( − ( ln ⁡ x − μ ) 2 2 σ 2 ) {\displaystyle {\frac {1}{x\sigma {\sqrt {2\pi }}}}\exp \left(-{\frac {\left(\ln x-\mu \right)^{2}}{2\sigma ^{2}}}\right)} ${\displaystyle {\frac {1}{x\sigma {\sqrt {2\pi }}}}\exp \left(-{\frac {\left(\ln x-\mu \right)^{2}}{2\sigma ^{2}}}\right)}$ |
| CDF | 1 2 [ 1 + erf ⁡ ( ln ⁡ x − μ σ 2 ) ] = Φ ( ln ⁡ x − μ σ ) {\displaystyle {\begin{aligned}&{\frac {1}{2}}\left[1+\operatorname {erf} \left({\frac {\ln x-\mu }{\sigma {\sqrt {2}}}}\right)\right]\\[1ex]&=\Phi {\left({\frac {\ln x-\mu }{\sigma }}\right)}\end{aligned}}} ${\displaystyle {\begin{aligned}&{\frac {1}{2}}\left[1+\operatorname {erf} \left({\frac {\ln x-\mu }{\sigma {\sqrt {2}}}}\right)\right]\\[1ex]&=\Phi {\left({\frac {\ln x-\mu }{\sigma }}\right)}\end{aligned}}}$ |
| Quantile | exp ⁡ ( μ + 2 σ 2 erf − 1 ⁡ ( 2 p − 1 ) ) = exp ⁡ ( μ + σ Φ − 1 ( p ) ) {\displaystyle {\begin{aligned}&\exp \left(\mu +{\sqrt {2\sigma ^{2}}}\operatorname {erf} ^{-1}(2p-1)\right)\\[1ex]&=\exp(\mu +\sigma \Phi ^{-1}(p))\end{aligned}}} ${\displaystyle {\begin{aligned}&\exp \left(\mu +{\sqrt {2\sigma ^{2}}}\operatorname {erf} ^{-1}(2p-1)\right)\\[1ex]&=\exp(\mu +\sigma \Phi ^{-1}(p))\end{aligned}}}$ |
| Mean | exp ⁡ ( μ + σ 2 2 ) {\displaystyle \exp \left(\mu +{\frac {\sigma ^{2}}{2}}\right)} ${\displaystyle \exp \left(\mu +{\frac {\sigma ^{2}}{2}}\right)}$ |
| Median | exp ⁡ ( μ ) {\displaystyle \exp(\mu )} ${\displaystyle \exp(\mu )}$ |
| Mode | exp ⁡ ( μ − σ 2 ) {\displaystyle \exp \left(\mu -\sigma ^{2}\right)} ${\displaystyle \exp \left(\mu -\sigma ^{2}\right)}$ |
| Variance | [ exp ⁡ ( σ 2 ) − 1 ] exp ⁡ ( 2 μ + σ 2 ) {\displaystyle \left[\exp(\sigma ^{2})-1\right]\exp \left(2\mu +\sigma ^{2}\right)} ${\displaystyle \left[\exp(\sigma ^{2})-1\right]\exp \left(2\mu +\sigma ^{2}\right)}$ |
| Skewness | [ exp ⁡ ( σ 2 ) + 2 ] exp ⁡ ( σ 2 ) − 1 {\displaystyle \left[\exp \left(\sigma ^{2}\right)+2\right]{\sqrt {\exp(\sigma ^{2})-1}}} ${\displaystyle \left[\exp \left(\sigma ^{2}\right)+2\right]{\sqrt {\exp(\sigma ^{2})-1}}}$ |
| Excess kurtosis | exp ⁡ ( 4 σ 2 ) + 2 exp ⁡ ( 3 σ 2 ) + 3 exp ⁡ ( 2 σ 2 ) − 6 {\displaystyle \exp \left(4\sigma ^{2}\right)+2\exp \left(3\sigma ^{2}\right)+3\exp \left(2\sigma ^{2}\right)-6} ${\displaystyle \exp \left(4\sigma ^{2}\right)+2\exp \left(3\sigma ^{2}\right)+3\exp \left(2\sigma ^{2}\right)-6}$ |
| Entropy | log 2 ⁡ ( 2 π e σ e μ ) {\displaystyle \log _{2}\left({\sqrt {2\pi e}}\,\sigma e^{\mu }\right)} ${\displaystyle \log _{2}\left({\sqrt {2\pi e}}\,\sigma e^{\mu }\right)}$ |
| MGF | defined only for numbers with a non-positive real part, see text |
| CF | representation ∑ n = 0 ∞ ( i t ) n n ! e n μ + n 2 σ 2 / 2 {\displaystyle \sum _{n=0}^{\infty }{\frac {{\left(it\right)}^{n}}{n!}}e^{n\mu +n^{2}\sigma ^{2}/2}} is asymptotically divergent, but adequate for most numerical purposes ${\displaystyle \sum _{n=0}^{\infty }{\frac {{\left(it\right)}^{n}}{n!}}e^{n\mu +n^{2}\sigma ^{2}/2}}$ |
| Fisher information | 1 σ 2 ( 1 0 0 2 ) {\displaystyle {\frac {1}{\sigma ^{2}}}{\begin{pmatrix}1&0\\0&2\end{pmatrix}}} ${\displaystyle {\frac {1}{\sigma ^{2}}}{\begin{pmatrix}1&0\\0&2\end{pmatrix}}}$ |
| Method of moments | μ = ln ⁡ E ⁡ [ X ] − 1 2 ln ⁡ ( Var ⁡ [ X ] E ⁡ [ X ] 2 + 1 ) , {\displaystyle \mu =\ln \operatorname {E} [X]-{\frac {1}{2}}\ln \left({\frac {\operatorname {Var} [X]}{\operatorname {E} [X]^{2}}}+1\right),} σ = ln ⁡ ( Var ⁡ [ X ] E ⁡ [ X ] 2 + 1 ) {\displaystyle \sigma ={\sqrt {\ln \left({\frac {\operatorname {Var} [X]}{\operatorname {E} [X]^{2}}}+1\right)}}} ${\displaystyle \mu =\ln \operatorname {E} [X]-{\frac {1}{2}}\ln \left({\frac {\operatorname {Var} [X]}{\operatorname {E} [X]^{2}}}+1\right),}$ ${\displaystyle \sigma ={\sqrt {\ln \left({\frac {\operatorname {Var} [X]}{\operatorname {E} [X]^{2}}}+1\right)}}}$ |
| Expected shortfall | e μ + σ 2 2 2 p [ 1 + erf ⁡ ( σ 2 + erf − 1 ⁡ ( 2 p − 1 ) ) ] = e μ + σ 2 2 1 − p [ 1 − Φ ( Φ − 1 ( p ) − σ ) ] {\displaystyle {\begin{aligned}&{\frac {e^{\mu +{\frac {\sigma ^{2}}{2}}}}{2p}}\left[1+\operatorname {erf} \left({\frac {\sigma }{\sqrt {2}}}+\operatorname {erf} ^{-1}(2p-1)\right)\right]\\[0.5ex]&={\frac {e^{\mu +{\frac {\sigma ^{2}}{2}}}}{1-p}}\left[1-\Phi (\Phi ^{-1}(p)-\sigma )\right]\end{aligned}}} [1] ${\displaystyle {\begin{aligned}&{\frac {e^{\mu +{\frac {\sigma ^{2}}{2}}}}{2p}}\left[1+\operatorname {erf} \left({\frac {\sigma }{\sqrt {2}}}+\operatorname {erf} ^{-1}(2p-1)\right)\right]\\[0.5ex]&={\frac {e^{\mu +{\frac {\sigma ^{2}}{2}}}}{1-p}}\left[1-\Phi (\Phi ^{-1}(p)-\sigma )\right]\end{aligned}}}$ |

In probability theory, a log-normal (or lognormal) distribution is a continuous probability distribution of a random variable whose logarithm is normally distributed. Thus, if the random variable X is log-normally distributed, then Y = ln X has a normal distribution.[2][3] Equivalently, if Y has a normal distribution, then the exponential function of Y, X = exp(Y), has a log-normal distribution. A random variable which is log-normally distributed takes only positive real values. It is a convenient and useful model for measurements in exact and engineering sciences, as well as medicine, economics and other topics (e.g., energies, concentrations, lengths, prices of financial instruments, and other metrics).

The distribution is occasionally referred to as the Galton distribution or Galton's distribution, after Francis Galton.[4] The log-normal distribution has also been associated with other names, such as McAlister, Gibrat and Cobb–Douglas.[4]

A log-normal process is the statistical realization of the multiplicative product of many independent random variables, each of which is positive. This is justified by considering the central limit theorem in the log domain (sometimes called Gibrat's law). The log-normal distribution is the maximum entropy probability distribution for a random variate X—for which the mean and variance of ln X are specified.[5]

Definitions[edit]
Generation and parameters[edit]
{\displaystyle Z}

 be a standard normal variable, and let 

μ

{\displaystyle \mu }
{\displaystyle \sigma }

 be two real numbers, with 
{\displaystyle \sigma >0}

. Then, the distribution of the random variable
{\displaystyle X=e^{\mu +\sigma Z}}

is called the log-normal distribution with parameters 

μ

{\displaystyle \mu }
{\displaystyle \sigma }

. These are the expected value (or mean) and standard deviation of the variable's natural logarithm, 
{\displaystyle \ln X}

, not the expectation and standard deviation of 

X

{\displaystyle X}

 itself.

Relation between normal and log-normal distribution. If 
{\displaystyle Y=\mu +\sigma Z}

 is normally distributed, then 
{\displaystyle X\sim e^{Y}}

 is log-normally distributed.
This relationship is true regardless of the base of the logarithmic or exponential function: If 
{\displaystyle \log _{a}X}

 is normally distributed, then so is 
{\displaystyle \log _{b}X}

 for any two positive numbers 
{\displaystyle a,b\neq 1}

. Likewise, if 
{\displaystyle e^{Y}}

 is log-normally distributed, then so is 
{\displaystyle a^{Y}}

, where 
{\displaystyle 0<a\neq 1}

.
In order to produce a distribution with desired mean 
{\displaystyle \mu _{X}}

 and variance 
{\displaystyle \sigma _{X}^{2}}

, one uses 
{\displaystyle \mu =\ln {\frac {\mu _{X}^{2}}{\sqrt {\mu _{X}^{2}+\sigma _{X}^{2}}}}}
{\displaystyle \sigma ^{2}=\ln \left(1+{\frac {\sigma _{X}^{2}}{\mu _{X}^{2}}}\right)}

.
Alternatively, the "multiplicative" or "geometric" parameters 
{\displaystyle \mu ^{*}=e^{\mu }}
{\displaystyle \sigma ^{*}=e^{\sigma }}

 can be used. They have a more direct interpretation: 
{\displaystyle \mu ^{*}}

 is the median of the distribution, and 
{\displaystyle \sigma ^{*}}

 is useful for determining "scatter" intervals, see below.

Probability density function[edit]
A positive random variable 

X

{\displaystyle X}

 is log-normally distributed (i.e., 

X
∼
Lognormal
⁡

(

μ
,

σ

2

)

{\textstyle X\sim \operatorname {Lognormal} \left(\mu ,\sigma ^{2}\right)}

), if the natural logarithm of 

X

{\displaystyle X}

 is normally distributed with mean 

μ

{\displaystyle \mu }

 and variance 
{\displaystyle \sigma ^{2}}
{\displaystyle \ln X\sim {\mathcal {N}}(\mu ,\sigma ^{2})}
{\displaystyle \Phi }
{\displaystyle \varphi }

 be respectively the cumulative probability distribution function and the probability density function of the 
{\displaystyle {\mathcal {N}}(0,1)}

 standard normal distribution, then we have that[2][4] the probability density function of the log-normal distribution is given by:
{\displaystyle {\begin{aligned}f_{X}(x)&={\frac {d}{dx}}\Pr \nolimits _{X}\left[X\leq x\right]\\[6pt]&={\frac {d}{dx}}\Pr \nolimits _{X}\left[\ln X\leq \ln x\right]\\[6pt]&={\frac {d}{dx}}\Phi {\left({\frac {\ln x-\mu }{\sigma }}\right)}\\[6pt]&=\varphi {\left({\frac {\ln x-\mu }{\sigma }}\right)}{\frac {d}{dx}}\left({\frac {\ln x-\mu }{\sigma }}\right)\\[6pt]&=\varphi {\left({\frac {\ln x-\mu }{\sigma }}\right)}{\frac {1}{\sigma x}}\\[6pt]&={\frac {1}{x\sigma {\sqrt {2\pi }}}}\exp \left(-{\frac {(\ln x-\mu )^{2}}{2\sigma ^{2}}}\right)~.\end{aligned}}}

Cumulative distribution function[edit]
The cumulative distribution function is
{\displaystyle F_{X}(x)=\Phi {\left({\frac {\ln x-\mu }{\sigma }}\right)}}

where 

Φ

{\displaystyle \Phi }

 is the cumulative distribution function of the standard normal distribution (i.e., 
{\displaystyle \operatorname {\mathcal {N}} (0,1)}

).
This may also be expressed as follows:[2]

1
2

[

1
+
erf
⁡

(

ln
⁡
x
−
μ

σ

2

)

]

=

1
2

erfc
{\displaystyle {\frac {1}{2}}\left[1+\operatorname {erf} \left({\frac {\ln x-\mu }{\sigma {\sqrt {2}}}}\right)\right]={\frac {1}{2}}\operatorname {erfc} \left(-{\frac {\ln x-\mu }{\sigma {\sqrt {2}}}}\right)}

where erfc is the complementary error function.

Multivariate log-normal[edit]
{\displaystyle {\boldsymbol {X}}\sim {\mathcal {N}}({\boldsymbol {\mu }},\,{\boldsymbol {\Sigma }})}

 is a multivariate normal distribution, then 
{\displaystyle Y_{i}=\exp(X_{i})}

 has a multivariate log-normal distribution.[6][7] The exponential is applied element-wise to the random vector 

X

{\displaystyle {\boldsymbol {X}}}

. The mean of 

Y

{\displaystyle {\boldsymbol {Y}}}
{\displaystyle \operatorname {E} [{\boldsymbol {Y}}]_{i}=e^{\mu _{i}+{\frac {1}{2}}\Sigma _{ii}},}

and its covariance matrix is
{\displaystyle \operatorname {Var} [{\boldsymbol {Y}}]_{ij}=e^{\mu _{i}+\mu _{j}+{\frac {1}{2}}(\Sigma _{ii}+\Sigma _{jj})}\left(e^{\Sigma _{ij}}-1\right).}

Since the multivariate log-normal distribution is not widely used, the rest of this entry only deals with the univariate distribution.

Characteristic function and moment generating function[edit]
All moments of the log-normal distribution exist and
{\displaystyle \operatorname {E} [X^{n}]=e^{n\mu +n^{2}\sigma ^{2}/2}}

This can be derived by letting 

z
=

ln
⁡
x
−
μ

σ

−
n
σ

{\textstyle z={\tfrac {\ln x-\mu }{\sigma }}-n\sigma }

 within the integral. However, the log-normal distribution is not determined by its moments.[8] This implies that it cannot have a defined moment generating function in a neighborhood of zero.[9] Indeed, the expected value 
{\displaystyle \operatorname {E} [e^{tX}]}

 is not defined for any positive value of the argument 

t

{\displaystyle t}

, since the defining integral diverges.
The characteristic function 
{\displaystyle \operatorname {E} [e^{itX}]}

 is defined for real values of t, but is not defined for any complex value of t that has a negative imaginary part, and hence the characteristic function is not analytic at the origin. Consequently, the characteristic function of the log-normal distribution cannot be represented as an infinite convergent series.[10] In particular, its Taylor formal series diverges:
{\displaystyle \sum _{n=0}^{\infty }{\frac {{\left(it\right)}^{n}}{n!}}e^{n\mu +n^{2}\sigma ^{2}/2}}

However, a number of alternative divergent series representations have been obtained.[10][11][12][13]
A closed-form formula for the characteristic function 
{\displaystyle \varphi (t)}

 with 

t

{\displaystyle t}

 in the domain of convergence is not known. A relatively simple approximating formula is available in closed form, and is given by[14]
{\displaystyle \varphi (t)\approx {\frac {\exp \left(-{\frac {W^{2}(-it\sigma ^{2}e^{\mu })+2W(-it\sigma ^{2}e^{\mu })}{2\sigma ^{2}}}\right)}{\sqrt {1+W{\left(-it\sigma ^{2}e^{\mu }\right)}}}}}

where 

W

{\displaystyle W}

 is the Lambert W function. This approximation is derived via an asymptotic method, but it stays sharp all over the domain of convergence of 

φ

{\displaystyle \varphi }

.

Properties[edit]
Geometric or multiplicative moments[edit]
The geometric or multiplicative mean of the log-normal distribution is 
{\displaystyle \operatorname {GM} [X]=e^{\mu }=\mu ^{*}}

. It equals the median. The geometric or multiplicative standard deviation is 
{\displaystyle \operatorname {GSD} [X]=e^{\sigma }=\sigma ^{*}}

.[15][16]
By analogy with the arithmetic statistics, one can define a geometric variance, 

GVar
{\displaystyle \operatorname {GVar} [X]=e^{\sigma ^{2}}}

, and a geometric coefficient of variation,[15] 
{\displaystyle \operatorname {GCV} [X]=e^{\sigma }-1}

, has been proposed. This term was intended to be analogous to the coefficient of variation, for describing multiplicative variation in log-normal data, but this definition of GCV has no theoretical basis as an estimate of 

CV

{\displaystyle \operatorname {CV} }

 itself (see also Coefficient of variation).
Note that the geometric mean is smaller than the arithmetic mean. This is due to the AM–GM inequality and is a consequence of the logarithm being a concave function. In fact,[17]

E
⁡
[
X
]
=

e

μ
+

1
2

σ

2

=

e

μ

⋅

e

σ

2

=
GM
⁡
[
X
]
⋅

GVar
{\displaystyle \operatorname {E} [X]=e^{\mu +{\frac {1}{2}}\sigma ^{2}}=e^{\mu }\cdot {\sqrt {e^{\sigma ^{2}}}}=\operatorname {GM} [X]\cdot {\sqrt {\operatorname {GVar} [X]}}.}

In finance, the term 
{\displaystyle e^{-\sigma ^{2}/2}}

 is sometimes interpreted as a convexity correction. From the point of view of stochastic calculus, this is the same correction term as in Itō's lemma for geometric Brownian motion.

Arithmetic moments[edit]
For any real or complex number n, the n-th moment of a log-normally distributed variable X is given by[4]
{\displaystyle \operatorname {E} [X^{n}]=e^{n\mu +{\frac {1}{2}}n^{2}\sigma ^{2}}.}

Specifically, the arithmetic mean, expected square, arithmetic variance, and arithmetic standard deviation of a log-normally distributed variable X are respectively given by:[2]
{\displaystyle {\begin{aligned}\operatorname {E} [X]&=e^{\mu +{\tfrac {1}{2}}\sigma ^{2}},\\[4pt]\operatorname {E} [X^{2}]&=e^{2\mu +2\sigma ^{2}},\\[4pt]\operatorname {Var} [X]&=\operatorname {E} [X^{2}]-\operatorname {E} [X]^{2}={\left(\operatorname {E} [X]\right)}^{2}\left(e^{\sigma ^{2}}-1\right)\\[2pt]&=e^{2\mu +\sigma ^{2}}\left(e^{\sigma ^{2}}-1\right),\\[4pt]\operatorname {SD} [X]&={\sqrt {\operatorname {Var} [X]}}=\operatorname {E} [X]{\sqrt {e^{\sigma ^{2}}-1}}\\[2pt]&=e^{\mu +{\tfrac {1}{2}}\sigma ^{2}}{\sqrt {e^{\sigma ^{2}}-1}},\end{aligned}}}

The arithmetic coefficient of variation 
{\displaystyle \operatorname {CV} [X]}

 is the ratio 
{\displaystyle {\tfrac {\operatorname {SD} [X]}{\operatorname {E} [X]}}}

. For a log-normal distribution it is equal to[3]
{\displaystyle \operatorname {CV} [X]={\sqrt {e^{\sigma ^{2}}-1}}.}

This estimate is sometimes referred to as the "geometric CV" (GCV),[18][19] due to its use of the geometric variance. Contrary to the arithmetic standard deviation, the arithmetic coefficient of variation is independent of the arithmetic mean.
The parameters μ and σ can be obtained, if the arithmetic mean and the arithmetic variance are known:
{\displaystyle {\begin{aligned}\mu &=\ln {\frac {\operatorname {E} [X]^{2}}{\sqrt {\operatorname {E} [X^{2}]}}}=\ln {\frac {\operatorname {E} [X]^{2}}{\sqrt {\operatorname {Var} [X]+\operatorname {E} [X]^{2}}}},\\[1ex]\sigma ^{2}&=\ln {\frac {\operatorname {E} [X^{2}]}{\operatorname {E} [X]^{2}}}=\ln \left(1+{\frac {\operatorname {Var} [X]}{\operatorname {E} [X]^{2}}}\right).\end{aligned}}}

A probability distribution is not uniquely determined by the moments E[Xn] = enμ + ⁠1/2⁠n2σ2 for n ≥ 1. That is, there exist other distributions with the same set of moments.[4] In fact, there is a whole family of distributions with the same moments as the log-normal distribution.[citation needed]

Mode, median, quantiles[edit]
Comparison of mean, median and mode of two log-normal distributions with different skewness.
The mode is the point of global maximum of the probability density function. In particular, by solving the equation 
{\displaystyle (\ln f)'=0}

, we get that:

Mode
{\displaystyle \operatorname {Mode} [X]=e^{\mu -\sigma ^{2}}.}

Since the log-transformed variable 
{\displaystyle Y=\ln X}

 has a normal distribution, and quantiles are preserved under monotonic transformations, the quantiles of 

X

{\displaystyle X}
{\displaystyle q_{X}(\alpha )=\exp \left[\mu +\sigma q_{\Phi }(\alpha )\right]=\mu ^{*}(\sigma ^{*})^{q_{\Phi }(\alpha )},}

where 
{\displaystyle q_{\Phi }(\alpha )}

 is the quantile of the standard normal distribution.
Specifically, the median of a log-normal distribution is equal to its multiplicative mean,[20]
{\displaystyle \operatorname {Med} [X]=e^{\mu }=\mu ^{*}~.}

Partial expectation[edit]
The partial expectation of a random variable 

X

{\displaystyle X}

 with respect to a threshold 

k

{\displaystyle k}

 is defined as
{\displaystyle g(k)=\int _{k}^{\infty }x\,f_{X}(x)\,dx.}

Alternatively, by using the definition of conditional expectation, it can be written as 
{\displaystyle g(k)=\operatorname {E} [X\mid X>k]\Pr(X>k)}

. For a log-normal random variable, the partial expectation is given by:
{\displaystyle {\begin{aligned}g(k)&=\int _{k}^{\infty }xf_{X}(x)\,dx\\[1ex]&=e^{\mu +{\tfrac {1}{2}}\sigma ^{2}}\,\Phi {\left({\frac {\mu -\ln k}{\sigma }}+\sigma \right)}\end{aligned}}}

where 

Φ

{\displaystyle \Phi }

 is the normal cumulative distribution function. The derivation of the formula is provided in the Talk page. The partial expectation formula has applications in insurance and economics, it is used in solving the partial differential equation leading to the Black–Scholes formula.

Conditional expectation[edit]
The conditional expectation of a log-normal random variable 

X

{\displaystyle X}

—with respect to a threshold 

k

{\displaystyle k}

—is its partial expectation divided by the cumulative probability of being in that range:
{\displaystyle {\begin{aligned}\operatorname {E} [X\mid X<k]&=e^{\mu +{\frac {\sigma ^{2}}{2}}}\cdot {\frac {\Phi {\left[{\frac {\ln k-\mu }{\sigma }}-\sigma \right]}}{\Phi {\left[{\frac {\ln k-\mu }{\sigma }}\right]}}}\\[8pt]\operatorname {E} [X\mid X\geq k]&=e^{\mu +{\frac {\sigma ^{2}}{2}}}\cdot {\frac {\Phi {\left[{\frac {\mu -\ln k}{\sigma }}+\sigma \right]}}{1-\Phi {\left[{\frac {\ln k-\mu }{\sigma }}\right]}}}\\[8pt]\operatorname {E} [X\mid X\in [k_{1},k_{2}]]&=e^{\mu +{\frac {\sigma ^{2}}{2}}}\cdot {\frac {\Phi {\left[{\frac {\ln k_{2}-\mu }{\sigma }}-\sigma \right]}-\Phi {\left[{\frac {\ln k_{1}-\mu }{\sigma }}-\sigma \right]}}{\Phi \left[{\frac {\ln k_{2}-\mu }{\sigma }}\right]-\Phi \left[{\frac {\ln k_{1}-\mu }{\sigma }}\right]}}\end{aligned}}}

Alternative parameterizations[edit]
In addition to the characterization by 
{\displaystyle \mu ,\sigma }
{\displaystyle \mu ^{*},\sigma ^{*}}

, here are multiple ways how the log-normal distribution can be parameterized. ProbOnto, the knowledge base and ontology of probability distributions[21][22] lists seven such forms: Overview of parameterizations of the log-normal distributions.
LogNormal1(μ,σ) with mean, μ, and standard deviation, σ, both on the log-scale [23] 
{\displaystyle P(x;{\boldsymbol {\mu }},{\boldsymbol {\sigma }})={\frac {1}{x\sigma {\sqrt {2\pi }}}}\exp \left[-{\frac {(\ln x-\mu )^{2}}{2\sigma ^{2}}}\right]}

LogNormal2(μ,υ) with mean, μ, and variance, υ, both on the log-scale 
{\displaystyle P(x;{\boldsymbol {\mu }},{\boldsymbol {v}})={\frac {1}{x{\sqrt {v}}{\sqrt {2\pi }}}}\exp \left[-{\frac {(\ln x-\mu )^{2}}{2v}}\right]}

LogNormal3(m,σ) with median, m, on the natural scale and standard deviation, σ, on the log-scale[23] 
{\displaystyle P(x;{\boldsymbol {m}},{\boldsymbol {\sigma }})={\frac {1}{x\sigma {\sqrt {2\pi }}}}\exp \left[-{\frac {\ln ^{2}(x/m)}{2\sigma ^{2}}}\right]}

LogNormal4(m,cv) with median, m, and coefficient of variation, cv, both on the natural scale 
{\displaystyle P(x;{\boldsymbol {m}},{\boldsymbol {cv}})={\frac {1}{x{\sqrt {\ln(cv^{2}+1)}}{\sqrt {2\pi }}}}\exp \left[-{\frac {\ln ^{2}(x/m)}{2\ln(cv^{2}+1)}}\right]}

LogNormal5(μ,τ) with mean, μ, and precision, τ, both on the log-scale[24] 
{\displaystyle P(x;{\boldsymbol {\mu }},{\boldsymbol {\tau }})={\sqrt {\frac {\tau }{2\pi }}}{\frac {1}{x}}\exp \left[-{\frac {\tau }{2}}(\ln x-\mu )^{2}\right]}

LogNormal6(m,σg) with median, m, and geometric standard deviation, σg, both on the natural scale[25] 
{\displaystyle P(x;{\boldsymbol {m}},{\boldsymbol {\sigma _{g}}})={\frac {1}{x{\sqrt {2\pi }}\,\ln \sigma _{g}}}\exp \left[-{\frac {\ln ^{2}(x/m)}{2\ln ^{2}(\sigma _{g})}}\right]}

LogNormal7(μN,σN) with mean, μN, and standard deviation, σN, both on the natural scale[26] 
{\displaystyle P(x;{\boldsymbol {\mu _{N}}},{\boldsymbol {\sigma _{N}}})={\frac {1}{x{\sqrt {2\pi \ln \left(1+\sigma _{N}^{2}/\mu _{N}^{2}\right)}}}}\exp \left[-{\frac {\left(\ln x-\ln {\frac {\mu _{N}}{\sqrt {1+\sigma _{N}^{2}/\mu _{N}^{2}}}}\right)^{2}}{2\ln \left(1+{\frac {\sigma _{N}^{2}}{\mu _{N}^{2}}}\right)}}\right]}

Examples for re-parameterization[edit]
Consider the situation when one would like to run a model using two different optimal design tools, for example PFIM[27] and PopED.[28] The former supports the LN2, the latter LN7 parameterization, respectively. Therefore, the re-parameterization is required, otherwise the two tools would produce different results.
For the transition 
{\displaystyle \operatorname {LN2} (\mu ,v)\to \operatorname {LN7} (\mu _{N},\sigma _{N})}

 following formulas hold 

μ

N

=
exp
⁡
(
μ
+
v

/

2
)

{\textstyle \mu _{N}=\exp(\mu +v/2)}

 and 

σ

N

=
exp
⁡
(
μ
+
v

/

2
)

exp
⁡
(
v
)
−
1

{\textstyle \sigma _{N}=\exp(\mu +v/2){\sqrt {\exp(v)-1}}}

.
For the transition 
{\displaystyle \operatorname {LN7} (\mu _{N},\sigma _{N})\to \operatorname {LN2} (\mu ,v)}

 following formulas hold 

μ
=
ln
⁡

μ

N

−

1
2

v

{\textstyle \mu =\ln \mu _{N}-{\frac {1}{2}}v}

 and 

v
=
ln
⁡
(
1
+

σ

N

2

/

μ

N

2

)

{\textstyle v=\ln(1+\sigma _{N}^{2}/\mu _{N}^{2})}

.
All remaining re-parameterisation formulas can be found in the specification document on the project website.[29]

Multiple, reciprocal, power[edit]
Multiplication by a constant: If 

X
∼
Lognormal
{\displaystyle X\sim \operatorname {Lognormal} (\mu ,\sigma ^{2})}

 then 

a
X
∼
Lognormal
{\displaystyle aX\sim \operatorname {Lognormal} (\mu +\ln a,\sigma ^{2})}
{\displaystyle a>0.}

Reciprocal: If 

X
∼
Lognormal
{\displaystyle X\sim \operatorname {Lognormal} (\mu ,\sigma ^{2})}

 then 

1
X

∼
Lognormal
{\displaystyle {\tfrac {1}{X}}\sim \operatorname {Lognormal} (-\mu ,\sigma ^{2}).}

Power: If 

X
∼
Lognormal
{\displaystyle X\sim \operatorname {Lognormal} (\mu ,\sigma ^{2})}

 then 

X

a

∼
Lognormal
{\displaystyle X^{a}\sim \operatorname {Lognormal} (a\mu ,a^{2}\sigma ^{2})}
{\displaystyle a\neq 0.}

Multiplication and division of independent, log-normal random variables[edit]
If two independent, log-normal variables 
{\displaystyle X_{1}}
{\displaystyle X_{2}}

 are multiplied [divided], the product [ratio] is again log-normal, with parameters 
{\displaystyle \mu =\mu _{1}+\mu _{2}}
{\displaystyle \mu =\mu _{1}-\mu _{2}}

] and 

σ

{\displaystyle \sigma }

, where 
{\displaystyle \sigma ^{2}=\sigma _{1}^{2}+\sigma _{2}^{2}}

.
More generally, if 

X

j

∼
Lognormal
{\displaystyle X_{j}\sim \operatorname {Lognormal} (\mu _{j},\sigma _{j}^{2})}
{\displaystyle n}

 independent, log-normally distributed variables, then 

Y
=

∏

j
=
1

n

X

j

∼
Lognormal
⁡

(

∑

j
=
1

n

μ

j

,

∑

j
=
1

n

σ

j

2

)

.

{\textstyle Y=\prod _{j=1}^{n}X_{j}\sim \operatorname {Lognormal} {\Big (}\sum _{j=1}^{n}\mu _{j},\sum _{j=1}^{n}\sigma _{j}^{2}{\Big )}.}

Multiplicative central limit theorem[edit]
See also: Gibrat's law
The geometric or multiplicative mean of 

n

{\displaystyle n}

 independent, identically distributed, positive random variables 
{\displaystyle X_{i}}

 shows, for 
{\displaystyle n\to \infty }

, approximately a log-normal distribution with parameters 
{\displaystyle \mu =\operatorname {E} [\ln X_{i}]}
{\displaystyle \sigma ^{2}=\operatorname {var} [\ln X_{i}]/n}

, assuming 
{\displaystyle \sigma ^{2}}

 is finite.
In fact, the random variables do not have to be identically distributed. It is enough for the distributions of 
{\displaystyle \ln X_{i}}

 to all have finite variance and satisfy the other conditions of any of the many variants of the central limit theorem.
This is commonly known as Gibrat's law.

Heavy-tailness of the Log-Normal[edit]
Whether a Log-Normal can be considered or not a true heavy-tail distribution is still debated. The main reason is that its variance is always finite, differently from what happen with certain Pareto distributions, for instance. However a recent study has shown how it is possible to create a Log-Normal distribution with infinite variance using Robinson Non-Standard Analysis.[30]

Other[edit]
A set of data that arises from the log-normal distribution has a symmetric Lorenz curve (see also Lorenz asymmetry coefficient).[31]
The harmonic 

H

{\displaystyle H}

, geometric 

G

{\displaystyle G}

 and arithmetic 

A

{\displaystyle A}

 means of this distribution are related;[32] such relation is given by
{\displaystyle H={\frac {G^{2}}{A}}.}

Log-normal distributions are infinitely divisible,[33] but they are not stable distributions, which can be easily drawn from.[34]

Related distributions[edit]
{\displaystyle X\sim {\mathcal {N}}(\mu ,\sigma ^{2})}

 is a normal distribution, then 

exp
⁡
(
X
)
∼
Lognormal
{\displaystyle \exp(X)\sim \operatorname {Lognormal} (\mu ,\sigma ^{2}).}

If 

X
∼
Lognormal
{\displaystyle X\sim \operatorname {Lognormal} (\mu ,\sigma ^{2})}

 is distributed log-normally, then 
{\displaystyle \ln X\sim {\mathcal {N}}(\mu ,\sigma ^{2})}

 is a normal random variable.
Let 

X

j

∼
Lognormal
{\displaystyle X_{j}\sim \operatorname {Lognormal} (\mu _{j},\sigma _{j}^{2})}

 be independent log-normally distributed variables with possibly varying 

σ

{\displaystyle \sigma }
{\displaystyle \mu }

 parameters, and 

Y
=

∑

j
=
1

n

X

j

{\textstyle Y=\sum _{j=1}^{n}X_{j}}

. The distribution of 

Y

{\displaystyle Y}

 has no closed-form expression, but can be reasonably approximated by another log-normal distribution 

Z

{\displaystyle Z}

 at the right tail.[35] Its probability density function at the neighborhood of 0 has been characterized[34] and it does not resemble any log-normal distribution. A commonly used approximation due to L.F. Fenton (but previously stated by R.I. Wilkinson and mathematically justified by Marlow[36]) is obtained by matching the mean and variance of another log-normal distribution: 
{\displaystyle {\begin{aligned}\sigma _{Z}^{2}&=\ln \!\left[{\frac {\sum _{j}e^{2\mu _{j}+\sigma _{j}^{2}}\left(e^{\sigma _{j}^{2}}-1\right)}{{\left(\sum _{j}e^{\mu _{j}+\sigma _{j}^{2}/2}\right)}^{2}}}+1\right],\\[1ex]\mu _{Z}&=\ln \!\left[\sum _{j}e^{\mu _{j}+\sigma _{j}^{2}/2}\right]-{\frac {\sigma _{Z}^{2}}{2}}.\end{aligned}}}

 In the case that all 
{\displaystyle X_{j}}

 have the same variance parameter 
{\displaystyle \sigma _{j}=\sigma }

, these formulas simplify to 
{\displaystyle {\begin{aligned}\sigma _{Z}^{2}&=\ln \!\left[\left(e^{\sigma ^{2}}-1\right){\frac {\sum _{j}e^{2\mu _{j}}}{{\left(\sum _{j}e^{\mu _{j}}\right)}^{2}}}+1\right],\\[1ex]\mu _{Z}&=\ln \!\left[\sum _{j}e^{\mu _{j}}\right]+{\frac {\sigma ^{2}}{2}}-{\frac {\sigma _{Z}^{2}}{2}}.\end{aligned}}}

For a more accurate approximation, one can use the Monte Carlo method to estimate the cumulative distribution function, the pdf and the right tail.[37][38] The cdf and pdf of the sum of correlated log-normally distributed random variables can also be approximated by Monte Carlo simulation.[39]

If 

X
∼
Lognormal
{\displaystyle X\sim \operatorname {Lognormal} (\mu ,\sigma ^{2})}

 then 
{\displaystyle X+c}

 is said to have a Three-parameter log-normal distribution with support 
{\displaystyle x\in (c,+\infty )}
{\displaystyle \operatorname {E} [X+c]=\operatorname {E} [X]+c}
{\displaystyle \operatorname {Var} [X+c]=\operatorname {Var} [X]}

.
The log-normal distribution is a special case of the semi-bounded Johnson's SU-distribution.[41]
If 

X
∣
Y
∼
Rayleigh
{\displaystyle X\mid Y\sim \operatorname {Rayleigh} (Y)}

 with 

Y
∼
Lognormal
{\displaystyle Y\sim \operatorname {Lognormal} (\mu ,\sigma ^{2})}

, then 

X
∼
Suzuki
{\displaystyle X\sim \operatorname {Suzuki} (\mu ,\sigma )}

 (Suzuki distribution).
A substitute for the log-normal whose integral can be expressed in terms of more elementary functions[42] can be obtained based on the logistic distribution to get an approximation for the CDF 
{\displaystyle F(x;\mu ,\sigma )=\left[\left({\frac {e^{\mu }}{x}}\right)^{\pi /(\sigma {\sqrt {3}})}+1\right]^{-1}.}

 This is a log-logistic distribution.
Statistical inference[edit]
Estimation of parameters[edit]
Maximum likelihood estimator[edit]
For determining the maximum likelihood estimators of the log-normal distribution parameters μ and σ, we can use the same procedure as for the normal distribution. Note that
{\displaystyle L(\mu ,\sigma )=\prod _{i=1}^{n}{\frac {1}{x_{i}}}\varphi _{\mu ,\sigma }(\ln x_{i}),}

where 

φ

{\displaystyle \varphi }

 is the density function of the normal distribution 
{\displaystyle {\mathcal {N}}(\mu ,\sigma ^{2})}

. Therefore, the log-likelihood function is
{\displaystyle \ell (\mu ,\sigma \mid x_{1},x_{2},\ldots ,x_{n})=-\sum _{i}\ln x_{i}+\ell _{N}(\mu ,\sigma \mid \ln x_{1},\ln x_{2},\dots ,\ln x_{n}).}

Since the first term is constant with regard to μ and σ, both logarithmic likelihood functions, 

ℓ

{\displaystyle \ell }
{\displaystyle \ell _{N}}

, reach their maximum with the same 

μ

{\displaystyle \mu }
{\displaystyle \sigma }

. Hence, the maximum likelihood estimators are identical to those for a normal distribution for the observations 
{\displaystyle \ln x_{1},\ln x_{2},\dots ,\ln x_{n})}
{\displaystyle {\widehat {\mu }}={\frac {\sum _{i}\ln x_{i}}{n}},\qquad {\widehat {\sigma }}^{2}={\frac {\sum _{i}{\left(\ln x_{i}-{\widehat {\mu }}\right)}^{2}}{n}}.}

For finite n, the estimator for 

μ

{\displaystyle \mu }

 is unbiased, but the one for 

σ

{\displaystyle \sigma }

 is biased. As for the normal distribution, an unbiased estimator for 

σ

{\displaystyle \sigma }

 can be obtained by replacing the denominator n by n−1 in the equation for 
{\displaystyle {\widehat {\sigma }}^{2}}

.
From this, the MLE for the expectancy of x is:[43]
{\displaystyle {\widehat {\theta }}_{\text{MLE}}={\widehat {\operatorname {E} [X]}}_{\text{MLE}}=e^{{\hat {\mu }}+{{\hat {\sigma }}^{2}}/{2}}}

Method of moments[edit]
When the individual values 
{\displaystyle x_{1},x_{2},\ldots ,x_{n}}

 are not available, but the sample's mean 
{\displaystyle {\bar {x}}}

 and standard deviation s is, then the method of moments can be used. The corresponding parameters are determined by the following formulas, obtained from solving the equations for the expectation 
{\displaystyle \operatorname {E} [X]}

 and variance 
{\displaystyle \operatorname {Var} [X]}
{\displaystyle \mu }
{\displaystyle \sigma }
{\displaystyle {\begin{aligned}\mu &=\ln {\frac {\bar {x}}{\sqrt {1+{\widehat {\sigma }}^{2}/{\bar {x}}^{2}}}},\\[1ex]\sigma ^{2}&=\ln \left(1+{{\widehat {\sigma }}^{2}}/{\bar {x}}^{2}\right).\end{aligned}}}

Other estimators[edit]
Other estimators also exist, such as Finney's UMVUE estimator,[45] the "Approximately Minimum Mean Squared Error Estimator", the "Approximately Unbiased Estimator" and "Minimax Estimator",[46] also "A Conditional Mean Squared Error Estimator",[47] and other variations as well.[48][49]

Interval estimates[edit]
Further information: Reference range § Log-normal distribution
The most efficient way to obtain interval estimates when analyzing log-normally distributed data consists of applying the well-known methods based on the normal distribution to logarithmically transformed data and then to back-transform results if appropriate.

Prediction intervals[edit]
A basic example is given by prediction intervals: For the normal distribution, the interval 
{\displaystyle [\mu -\sigma ,\mu +\sigma ]}

 contains approximately two thirds (68%) of the probability (or of a large sample), and 
{\displaystyle [\mu -2\sigma ,\mu +2\sigma ]}

 contain 95%. Therefore, for a log-normal distribution,
{\displaystyle [\mu ^{*}/\sigma ^{*},\mu ^{*}\cdot \sigma ^{*}]=[\mu ^{*}{}^{\times }\!\!/\sigma ^{*}]}

 contains 2/3, and
{\displaystyle [\mu ^{*}/(\sigma ^{*})^{2},\mu ^{*}\cdot (\sigma ^{*})^{2}]=[\mu ^{*}{}^{\times }\!\!/(\sigma ^{*})^{2}]}

 contains 95% of the probability. Using estimated parameters, then approximately the same percentages of the data should be contained in these intervals.
Confidence interval for eμ[edit]
Using the principle, note that a confidence interval for 

μ

{\displaystyle \mu }
{\displaystyle [{\widehat {\mu }}\pm q\cdot {\widehat {\mathop {se} }}]}

, where 
{\displaystyle \mathop {se} ={\widehat {\sigma }}/{\sqrt {n}}}

 is the standard error and q is the 97.5% quantile of a t distribution with n-1 degrees of freedom. Back-transformation leads to a confidence interval for 
{\displaystyle \mu ^{*}=e^{\mu }}

 (the median), is:
{\displaystyle [{\widehat {\mu }}^{*}{}^{\times }\!\!/(\operatorname {sem} ^{*})^{q}]}

 with 
{\displaystyle \operatorname {sem} ^{*}=({\widehat {\sigma }}^{*})^{1/{\sqrt {n}}}}

Confidence interval for E(X)[edit]
The literature discusses several options for calculating the confidence interval for 

μ

{\displaystyle \mu }

 (the mean of the log-normal distribution). These include bootstrap as well as various other methods.[50][51]
The Cox Method[a] proposes to plug-in the estimators 
{\displaystyle {\widehat {\mu }}={\frac {\sum _{i}\ln x_{i}}{n}},\qquad S^{2}={\frac {\sum _{i}\left(\ln x_{i}-{\widehat {\mu }}\right)^{2}}{n-1}}}

and use them to construct approximate confidence intervals in the following way:
{\displaystyle \mathrm {CI} (\operatorname {E} (X)):\exp \left({\hat {\mu }}+{\frac {S^{2}}{2}}\pm z_{1-{\frac {\alpha }{2}}}{\sqrt {{\frac {S^{2}}{n}}+{\frac {S^{4}}{2(n-1)}}}}\right)}

[Proof]
We know that 
{\displaystyle \operatorname {E} (X)=e^{\mu +{\frac {\sigma ^{2}}{2}}}}

. Also, 
{\displaystyle {\widehat {\mu }}}

 is a normal distribution with parameters: 
{\displaystyle {\widehat {\mu }}\sim N\left(\mu ,{\frac {\sigma ^{2}}{n}}\right)}
{\displaystyle S^{2}}

 has a chi-squared distribution, which is approximately normally distributed (via CLT), with parameters: 
{\displaystyle S^{2}{\dot {\sim }}N\left(\sigma ^{2},{\frac {2\sigma ^{4}}{n-1}}\right)}

. Hence, 
{\displaystyle {\frac {S^{2}}{2}}{\dot {\sim }}N\left({\frac {\sigma ^{2}}{2}},{\frac {\sigma ^{4}}{2(n-1)}}\right)}

.
Since the sample mean and variance are independent, and the sum of normally distributed variables is also normal, we get that:
{\displaystyle {\widehat {\mu }}+{\frac {S^{2}}{2}}{\dot {\sim }}N\left(\mu +{\frac {\sigma ^{2}}{2}},{\frac {\sigma ^{2}}{n}}+{\frac {\sigma ^{4}}{2(n-1)}}\right)}

Based on the above, standard confidence intervals for 
{\displaystyle \mu +{\frac {\sigma ^{2}}{2}}}

 can be constructed (using a Pivotal quantity) as: 
{\displaystyle {\hat {\mu }}+{\frac {S^{2}}{2}}\pm z_{1-{\frac {\alpha }{2}}}{\sqrt {{\frac {S^{2}}{n}}+{\frac {S^{4}}{2(n-1)}}}}}

And since confidence intervals are preserved for monotonic transformations, we get that:
{\displaystyle \mathrm {CI} \left(\operatorname {E} [X]=e^{\mu +{\frac {\sigma ^{2}}{2}}}\right):\exp \left({\hat {\mu }}+{\frac {S^{2}}{2}}\pm z_{1-{\frac {\alpha }{2}}}{\sqrt {{\frac {S^{2}}{n}}+{\frac {S^{4}}{2(n-1)}}}}\right)}

As desired.

Olsson 2005, proposed a "modified Cox method" by replacing 
{\displaystyle z_{1-{\frac {\alpha }{2}}}}

 with 
{\displaystyle t_{n-1,1-{\frac {\alpha }{2}}}}

, which seemed to provide better coverage results for small sample sizes.[50]: Section 3.4 

Confidence interval for comparing two log normals[edit]
Comparing two log-normal distributions can often be of interest, for example, from a treatment and control group (e.g., in an A/B test). We have samples from two independent log-normal distributions with parameters 
{\displaystyle (\mu _{1},\sigma _{1}^{2})}
{\displaystyle (\mu _{2},\sigma _{2}^{2})}

, with sample sizes 
{\displaystyle n_{1}}
{\displaystyle n_{2}}

 respectively.
Comparing the medians of the two can easily be done by taking the log from each and then constructing straightforward confidence intervals and transforming it back to the exponential scale.
{\displaystyle \mathrm {CI} (e^{\mu _{1}-\mu _{2}}):\exp \left({\hat {\mu }}_{1}-{\hat {\mu }}_{2}\pm z_{1-{\frac {\alpha }{2}}}{\sqrt {{\frac {S_{1}^{2}}{n}}+{\frac {S_{2}^{2}}{n}}}}\right)}

These CI are what are often used in epidemiology for calculation of the CI for relative-risk and odds-ratio.[54] The way it is done there is that we have two approximately Normal distributions (e.g., p1 and p2, for RR), and we wish to calculate their ratio.[b]
However, the ratio of the expectations (means) of the two samples might also be of interest, while requiring more work to develop. The ratio of their means is:
{\displaystyle {\frac {\operatorname {E} (X_{1})}{\operatorname {E} (X_{2})}}={\frac {e^{\mu _{1}+\sigma _{1}^{2}/2}}{e^{\mu _{2}+\sigma _{2}^{2}/2}}}=e^{(\mu _{1}-\mu _{2})+{\frac {1}{2}}\left(\sigma _{1}^{2}-\sigma _{2}^{2}\right)}}

Plugin in the estimators to each of these parameters yields also a log normal distribution, which means that the Cox Method, discussed above, could similarly be used for this use-case:
{\displaystyle \mathrm {CI} \left({\frac {\operatorname {E} (X_{1})}{\operatorname {E} (X_{2})}}={\frac {e^{\mu _{1}+\sigma _{1}^{2}/2}}{e^{\mu _{2}+\sigma _{2}^{2}/2}}}\right):\exp \left(\left({\hat {\mu }}_{1}-{\hat {\mu }}_{2}+{\tfrac {1}{2}}S_{1}^{2}-{\tfrac {1}{2}}S_{2}^{2}\right)\pm z_{1-{\frac {\alpha }{2}}}{\sqrt {{\frac {S_{1}^{2}}{n_{1}}}+{\frac {S_{2}^{2}}{n_{2}}}+{\frac {S_{1}^{4}}{2(n_{1}-1)}}+{\frac {S_{2}^{4}}{2(n_{2}-1)}}}}\right)}

[Proof]
To construct a confidence interval for this ratio, we first note that 
{\displaystyle {\hat {\mu }}_{1}-{\hat {\mu }}_{2}}

 follows a normal distribution, and that both 
{\displaystyle S_{1}^{2}}
{\displaystyle S_{2}^{2}}

 has a chi-squared distribution, which is approximately normally distributed (via CLT, with the relevant parameters).
This means that
{\displaystyle ({\hat {\mu }}_{1}-{\hat {\mu }}_{2}+{\frac {1}{2}}S_{1}^{2}-{\frac {1}{2}}S_{2}^{2})\sim N\left((\mu _{1}-\mu _{2})+{\frac {1}{2}}(\sigma _{1}^{2}-\sigma _{2}^{2}),{\frac {\sigma _{1}^{2}}{n_{1}}}+{\frac {\sigma _{2}^{2}}{n_{2}}}+{\frac {\sigma _{1}^{4}}{2(n_{1}-1)}}+{\frac {\sigma _{2}^{4}}{2(n_{2}-1)}}\right)}

Based on the above, standard confidence intervals can be constructed (using a Pivotal quantity) as: 
{\displaystyle ({\hat {\mu }}_{1}-{\hat {\mu }}_{2}+{\frac {1}{2}}S_{1}^{2}-{\frac {1}{2}}S_{2}^{2})\pm z_{1-{\frac {\alpha }{2}}}{\sqrt {{\frac {S_{1}^{2}}{n_{1}}}+{\frac {S_{2}^{2}}{n_{2}}}+{\frac {S_{1}^{4}}{2(n_{1}-1)}}+{\frac {S_{2}^{4}}{2(n_{2}-1)}}}}}

And since confidence intervals are preserved for monotonic transformations, we get that:
{\displaystyle CI\left({\frac {\operatorname {E} (X_{1})}{\operatorname {E} (X_{2})}}={\frac {e^{\mu _{1}+{\frac {\sigma _{1}^{2}}{2}}}}{e^{\mu _{2}+{\frac {\sigma _{2}^{2}}{2}}}}}\right):e^{\left(({\hat {\mu }}_{1}-{\hat {\mu }}_{2}+{\frac {1}{2}}S_{1}^{2}-{\frac {1}{2}}S_{2}^{2})\pm z_{1-{\frac {\alpha }{2}}}{\sqrt {{\frac {S_{1}^{2}}{n_{1}}}+{\frac {S_{2}^{2}}{n_{2}}}+{\frac {S_{1}^{4}}{2(n_{1}-1)}}+{\frac {S_{2}^{4}}{2(n_{2}-1)}}}}\right)}}

As desired.

It is worth noting that naively using the MLE in the ratio of the two expectations to create a ratio estimator will lead to a consistent, yet biased, point-estimation (we use the fact that the estimator of the ratio is a log normal distribution):[c][citation needed]
{\displaystyle {\begin{aligned}\operatorname {E} \left[{\frac {{\widehat {\operatorname {E} }}(X_{1})}{{\widehat {\operatorname {E} }}(X_{2})}}\right]&=\operatorname {E} \left[\exp \left(\left({\widehat {\mu }}_{1}-{\widehat {\mu }}_{2}\right)+{\tfrac {1}{2}}\left(S_{1}^{2}-S_{2}^{2}\right)\right)\right]\\&\approx \exp \left[{(\mu _{1}-\mu _{2})+{\frac {1}{2}}(\sigma _{1}^{2}-\sigma _{2}^{2})+{\frac {1}{2}}\left({\frac {\sigma _{1}^{2}}{n_{1}}}+{\frac {\sigma _{2}^{2}}{n_{2}}}+{\frac {\sigma _{1}^{4}}{2(n_{1}-1)}}+{\frac {\sigma _{2}^{4}}{2(n_{2}-1)}}\right)}\right]\end{aligned}}}

Extremal principle of entropy to fix the free parameter σ[edit]
In applications, 

σ

{\displaystyle \sigma }

 is a parameter to be determined. For growing processes balanced by production and dissipation, the use of an extremal principle of Shannon entropy shows that[55]
{\displaystyle \sigma ={\frac {1}{\sqrt {6}}}}

This value can then be used to give some scaling relation between the inflexion point and maximum point of the log-normal distribution.[55] This relationship is determined by the base of natural logarithm, 

e
=
2.718
…

{\displaystyle e=2.718\ldots }

, and exhibits some geometrical similarity to the minimal surface energy principle.
These scaling relations are useful for predicting a number of growth processes (epidemic spreading, droplet splashing, population growth, swirling rate of the bathtub vortex, distribution of language characters, velocity profile of turbulences, etc.).
For example, the log-normal function with such 

σ

{\displaystyle \sigma }

 fits well with the size of secondarily produced droplets during droplet impact [56] and the spreading of an epidemic disease.[57]
The value 

σ
=
1

/

6

{\textstyle \sigma =1{\big /}{\sqrt {6}}}

 is used to provide a probabilistic solution for the Drake equation.[58]

Occurrence and applications[edit]
The log-normal distribution is important in the description of natural phenomena. Many natural growth processes are driven by the accumulation of many small percentage changes which become additive on a log scale. Under appropriate regularity conditions, the distribution of the resulting accumulated changes will be increasingly well approximated by a log-normal, as noted in the section above on "Multiplicative Central Limit Theorem". This is also known as Gibrat's law, after Robert Gibrat (1904–1980) who formulated it for companies.[59] If the rate of accumulation of these small changes does not vary over time, growth becomes independent of size. Even if this assumption is not true, the size distributions at any age of things that grow over time tends to be log-normal.[citation needed] Consequently, reference ranges for measurements in healthy individuals are more accurately estimated by assuming a log-normal distribution than by assuming a symmetric distribution about the mean.[citation needed]
A second justification is based on the observation that fundamental natural laws imply multiplications and divisions of positive variables. Examples are the simple gravitation law connecting masses and distance with the resulting force, or the formula for equilibrium concentrations of chemicals in a solution that connects concentrations of educts and products. Assuming log-normal distributions of the variables involved leads to consistent models in these cases.
Specific examples are given in the following subsections.[60] contains a review and table of log-normal distributions from geology, biology, medicine, food, ecology, and other areas.[61] is a review article on log-normal distributions in neuroscience, with annotated bibliography.

Human behavior[edit]
The length of comments posted in Internet discussion forums follows a log-normal distribution.[62]
Users' dwell time on online articles (jokes, news etc.) follows a log-normal distribution.[63]
The length of chess games tends to follow a log-normal distribution.[64]
Onset durations of acoustic comparison stimuli that are matched to a standard stimulus follow a log-normal distribution.[17]
Biology and medicine[edit]
Measures of size of living tissue (length, skin area, weight).[65]
Incubation period of diseases.[66]
Diameters of banana leaf spots, powdery mildew on barley.[60]
For highly communicable epidemics, such as SARS in 2003, if public intervention control policies are involved, the number of hospitalized cases is shown to satisfy the log-normal distribution with no free parameters if an entropy is assumed and the standard deviation is determined by the principle of maximum rate of entropy production.[67]
The length of inert appendages (hair, claws, nails, teeth) of biological specimens, in the direction of growth.[citation needed]
The normalised RNA-Seq readcount for any genomic region can be well approximated by log-normal distribution.
The PacBio sequencing read length follows a log-normal distribution.[68]
Certain physiological measurements, such as blood pressure of adult humans (after separation on male/female subpopulations).[69]
Several pharmacokinetic variables, such as Cmax, elimination half-life and the elimination rate constant.[70]
In neuroscience, the distribution of firing rates across a population of neurons is often approximately log-normal. This has been first observed in the cortex and striatum [71] and later in hippocampus and entorhinal cortex,[72] and elsewhere in the brain.[61][73] Also, intrinsic gain distributions and synaptic weight distributions appear to be log-normal[74] as well.
Neuron densities in the cerebral cortex, due to the noisy cell division process during neurodevelopment.[75]
In operating-rooms management, the distribution of surgery duration.
In the size of avalanches of fractures in the cytoskeleton of living cells, showing log-normal distributions, with significantly higher size in cancer cells than healthy ones.[76]
Chemistry[edit]
Particle size distributions and molar mass distributions.
The concentration of rare elements in minerals.[77]
Diameters of crystals in ice cream, oil drops in mayonnaise, pores in cocoa press cake.[60]
Fitted cumulative log-normal distribution to annually maximum 1-day rainfalls, see distribution fitting 
Physical sciences[edit]
In hydrology, the log-normal distribution is used to analyze extreme values of such variables as monthly and annual maximum values of daily rainfall and river discharge volumes.[78]
The image on the right illustrates an example of fitting the log-normal distribution to ranked annually maximum one-day rainfalls showing also the 90% confidence belt based on the binomial distribution.
The rainfall data are represented by plotting positions as part of a cumulative frequency analysis.
In physical oceanography, the sizes of icebergs in the midwinter Southern Atlantic Ocean were found to follow a log-normal size distribution. The iceberg sizes, measured visually and by radar from the F.S. Polarstern in 1986, were thought to be controlled by wave action in heavy seas causing them to flex and break.[79]
In atmospheric science, log-normal distributions (or distributions made by combining multiple log-normal functions) have been used to characterize both measurements and models of the sizes and concentrations of many different types of particles, from volcanic ash, to clouds and rain, to airborne microbes.[80][81][82][83] The log-normal distribution is strictly empirical, so more physically based distributions have been adopted to better understand processes controlling size distributions of particles such as volcanic ash.[84]
Social sciences and demographics[edit]
In economics, there is evidence that the income of 97–99% of the population is distributed log-normally.[85] (The distribution of higher-income individuals follows a Pareto distribution).[86]
If an income distribution follows a log-normal distribution with standard deviation 

σ

{\displaystyle \sigma }

, then the Gini coefficient, commonly used to evaluate income inequality, can be computed as 
{\displaystyle G=\operatorname {erf} \left({\frac {\sigma }{2}}\right)}

 where 

erf

{\displaystyle \operatorname {erf} }

 is the error function, since 
{\displaystyle G=2\Phi {\left({\frac {\sigma }{\sqrt {2}}}\right)}-1}

, where 
{\displaystyle \Phi (x)}

 is the cumulative distribution function of a standard normal distribution.
In finance, in particular the Black–Scholes model, changes in the logarithm of exchange rates, price indices, and stock market indices are assumed normal[87] (these variables behave like compound interest, not like simple interest, and so are multiplicative). However, some mathematicians such as Benoit Mandelbrot have argued [88] that log-Lévy distributions, which possess heavy tails, would be a more appropriate model, in particular for the analysis for stock market crashes. Indeed, stock price distributions typically exhibit a fat tail.[89] The fat tailed distribution of changes during stock market crashes invalidate the assumptions of the central limit theorem.
In scientometrics, the number of citations to journal articles and patents follows a discrete log-normal distribution.[90][91]
City sizes (population) satisfy Gibrat's Law.[92] The growth process of city sizes is proportionate and invariant with respect to size. From the central limit theorem therefore, the log of city size is normally distributed.
The number of sexual partners appears to be best described by a log-normal distribution.[93]
Technology[edit]
In reliability analysis, the log-normal distribution is often used to model times to repair a maintainable system.[94]
In wireless communication, "the local-mean power expressed in logarithmic values, such as dB or neper, has a normal (i.e., Gaussian) distribution."[95] Also, the random obstruction of radio signals due to large buildings and hills, called shadowing, is often modeled as a log-normal distribution.
Particle size distributions produced by comminution with random impacts, such as in ball milling.[96]
The file size distribution of publicly available audio and video data files (MIME types) follows a log-normal distribution over five orders of magnitude.[97]
File sizes of 140 million files on personal computers running the Windows OS, collected in 1999.[98][62]
Sizes of text-based emails (1990s) and multimedia-based emails (2000s).[62]
In computer networks and Internet traffic analysis, log-normal is shown as a good statistical model to represent the amount of traffic per unit time. This has been shown by applying a robust statistical approach on a large groups of real Internet traces. In this context, the log-normal distribution has shown a good performance in two main use cases: (1) predicting the proportion of time traffic will exceed a given level (for service level agreement or link capacity estimation) i.e. link dimensioning based on bandwidth provisioning and (2) predicting 95th percentile pricing.[99]
in physical testing when the test produces a time-to-failure of an item under specified conditions, the data is often best analyzed using a lognormal distribution.[100][101]
