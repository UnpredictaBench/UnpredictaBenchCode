# Gumbel distribution

Particular case of the generalized extreme value distribution

| Gumbel |
| --- |
| Probability density function |
| Cumulative distribution function |
| Notation | Gumbel ( μ , β ) {\displaystyle {\text{Gumbel}}(\mu ,\beta )} ${\displaystyle {\text{Gumbel}}(\mu ,\beta )}$ |
| Parameters | μ , {\displaystyle \mu ,} location (real) β > 0 , {\displaystyle \beta >0,} scale (real) ${\displaystyle \mu ,}$ ${\displaystyle \beta >0,}$ |
| Support | x ∈ R {\displaystyle x\in \mathbb {R} } ${\displaystyle x\in \mathbb {R} }$ |
| PDF | 1 β e − ( z + e − z ) {\displaystyle {\frac {1}{\beta }}e^{-(z+e^{-z})}} (maximum case) where z = x − μ β {\displaystyle z={\frac {x-\mu }{\beta }}} ${\displaystyle {\frac {1}{\beta }}e^{-(z+e^{-z})}}$ ${\displaystyle z={\frac {x-\mu }{\beta }}}$ |
| CDF | e − e − ( x − μ ) / β {\displaystyle e^{-e^{-(x-\mu )/\beta }}} (maximum case) ${\displaystyle e^{-e^{-(x-\mu )/\beta }}}$ |
| Quantile | μ − β ln ⁡ ( − ln ⁡ ( p ) ) {\displaystyle \mu -\beta \ln(-\ln(p))} ${\displaystyle \mu -\beta \ln(-\ln(p))}$ |
| Mean | μ + β γ {\displaystyle \mu +\beta \gamma } where γ {\displaystyle \gamma } is the Euler–Mascheroni constant ${\displaystyle \mu +\beta \gamma }$ ${\displaystyle \gamma }$ |
| Median | μ − β ln ⁡ ( ln ⁡ 2 ) {\displaystyle \mu -\beta \ln(\ln 2)} ${\displaystyle \mu -\beta \ln(\ln 2)}$ |
| Mode | μ {\displaystyle \mu } ${\displaystyle \mu }$ |
| Variance | π 2 6 β 2 {\displaystyle {\frac {\pi ^{2}}{6}}\beta ^{2}} ${\displaystyle {\frac {\pi ^{2}}{6}}\beta ^{2}}$ |
| Skewness | 12 6 ζ ( 3 ) π 3 ≈ 1.14 {\displaystyle {\frac {12{\sqrt {6}}\,\zeta (3)}{\pi ^{3}}}\approx 1.14} ${\displaystyle {\frac {12{\sqrt {6}}\,\zeta (3)}{\pi ^{3}}}\approx 1.14}$ |
| Excess kurtosis | 12 5 {\displaystyle {\frac {12}{5}}} ${\displaystyle {\frac {12}{5}}}$ |
| Entropy | ln ⁡ ( β ) + γ + 1 {\displaystyle \ln(\beta )+\gamma +1} ${\displaystyle \ln(\beta )+\gamma +1}$ |
| MGF | Γ ( 1 − β t ) e μ t {\displaystyle \Gamma (1-\beta t)e^{\mu t}} ${\displaystyle \Gamma (1-\beta t)e^{\mu t}}$ |
| CF | Γ ( 1 − i β t ) e i μ t {\displaystyle \Gamma (1-i\beta t)e^{i\mu t}} ${\displaystyle \Gamma (1-i\beta t)e^{i\mu t}}$ |

In probability theory and statistics, the Gumbel distribution (also known as the type-I generalized extreme value distribution) is used to model the distribution of the maximum (or the minimum) of a number of samples of various distributions.

This distribution might be used to represent the distribution of the maximum level of a river in a particular year if there was a list of maximum values for the past ten years. It is useful in predicting the chance that an extreme earthquake, flood or other natural disaster will occur. The potential applicability of the Gumbel distribution to represent the distribution of maxima relates to extreme value theory, which indicates that it is likely to be useful if the distribution of the underlying sample data is of the normal or exponential type.[a]

The Gumbel distribution is a particular case of the generalized extreme value distribution (also known as the Fisher–Tippett distribution). It is also known as the log-Weibull distribution and the double exponential distribution (a term that is alternatively sometimes used to refer to the Laplace distribution). It is related to the Gompertz distribution: when its density is first reflected about the origin and then restricted to the positive half line, a Gompertz function is obtained.

In the latent variable formulation of the multinomial logit model — common in discrete choice theory — the errors of the latent variables follow a Gumbel distribution. This is useful because the difference of two Gumbel-distributed random variables has a logistic distribution.

The Gumbel distribution is named after Emil Julius Gumbel (1891–1966), based on his original papers describing the distribution.[1][2]

Definitions[edit]
The cumulative distribution function of the Gumbel distribution (maximum case) is
{\displaystyle F(x;\mu ,\beta )=e^{-e^{-(x-\mu )/\beta }}\,}

Standard Gumbel distribution[edit]
The standard Gumbel distribution is the case where 
{\displaystyle \mu =0}
{\displaystyle \beta =1}

 with cumulative distribution function
{\displaystyle F(x)=e^{-e^{-x}}\,}

and probability density function  
{\displaystyle f(x)=e^{-(x+e^{-x})}.}

In this case the mode is 0, the median is 

−
ln
⁡
(
ln
⁡
(
2
)
)
≈
0.3665

{\displaystyle -\ln(\ln(2))\approx 0.3665}

, the mean is 

γ
≈
0.5772

{\displaystyle \gamma \approx 0.5772}

 (the Euler–Mascheroni constant), and the standard deviation is 

π

/

6

≈
1.2825.

{\displaystyle \pi /{\sqrt {6}}\approx 1.2825.}

The cumulants, for n > 1, are given by 
{\displaystyle \kappa _{n}=(n-1)!\zeta (n).}

Properties[edit]
The mode is μ, while the median is 
{\displaystyle \mu -\beta \ln \left(\ln 2\right),}

 and the mean is given by
{\displaystyle \operatorname {E} (X)=\mu +\gamma \beta }

,
where 

γ

{\displaystyle \gamma }

 is the Euler–Mascheroni constant.
The standard deviation 

σ

{\displaystyle \sigma }
{\displaystyle \beta \pi /{\sqrt {6}}}

 hence 

β
=
σ

6

/

π
≈
0.78
σ
.

{\displaystyle \beta =\sigma {\sqrt {6}}/\pi \approx 0.78\sigma .}

 [3]
At the mode, where 
{\displaystyle x=\mu }

, the value of 
{\displaystyle F(x;\mu ,\beta )}

 becomes 

e

−
1

≈
0.37

{\displaystyle e^{-1}\approx 0.37}

, irrespective of the value of 
{\displaystyle \beta .}
{\displaystyle G_{1},...,G_{k}}

 are iid Gumbel random variables with parameters 
{\displaystyle (\mu ,\beta )}

 then 
{\displaystyle \max\{G_{1},...,G_{k}\}}

 is also a Gumbel random variable with parameters 
{\displaystyle (\mu +\beta \ln k,\beta )}
{\displaystyle G_{1},G_{2},...}

 are iid random variables such that 
{\displaystyle \max\{G_{1},...,G_{k}\}-\beta \ln k}

 has the same distribution as 
{\displaystyle G_{1}}

 for all natural numbers 

k

{\displaystyle k}

, then 
{\displaystyle G_{1}}

 is necessarily Gumbel distributed with scale parameter 

β

{\displaystyle \beta }

 (actually it suffices to consider just two distinct values of k>1 which are coprime).

Other related distributions[edit]
The discrete Gumbel distribution[edit]
Many problems in discrete mathematics involve the study of an extremal parameter that follows a discrete version of the Gumbel distribution.[4][5] This discrete version is the law of 
{\displaystyle Y=\lceil X\rceil }

, where 

X

{\displaystyle X}

 follows the continuous Gumbel distribution 
{\displaystyle \mathrm {Gumbel} (\mu ,\beta )}

.
Accordingly, this gives 
{\displaystyle P(Y\leq h)=\exp(-\exp(-(h-\mu )/\beta ))}

 for any 
{\displaystyle h\in \mathbb {Z} }

.
Denoting 
{\displaystyle \mathrm {DGumbel} (\mu ,\beta )}

 as the discrete version, one has 
{\displaystyle \lceil X\rceil \sim \mathrm {DGumbel} (\mu ,\beta )}
{\displaystyle \lfloor X\rfloor \sim \mathrm {DGumbel} (\mu -1,\beta )}

.
There is no known closed form for the mean, variance (or higher-order moments) of the discrete Gumbel distribution, but it is easy to obtain high-precision numerical evaluations via rapidly converging infinite sums. For example, this yields 

E

[

D
G
u
m
b
e
l

(
0
,
1
)
]
=
1.077240905953631072609...

{\displaystyle {\mathbb {E} }[\mathrm {DGumbel} (0,1)]=1.077240905953631072609...}

, but it remains an open problem to find a closed form for this constant (it is plausible there is none).
Aguech, Althagafi, and Banderier[4] provide various bounds linking the discrete and continuous versions of the Gumbel distribution and explicitly detail (using methods from Mellin transform) the oscillating phenomena that appear when one has a sequence of random variables 
{\displaystyle \lfloor Y_{n}-c\ln n\rfloor }

 converging to a discrete Gumbel distribution.

Continuous distributions[edit]
{\displaystyle X}

 has a Gumbel distribution, then the conditional distribution of 
{\displaystyle Y=-X}

 given that 

Y

{\displaystyle Y}

 is positive, or equivalently given that 

X

{\displaystyle X}

 is negative, has a Gompertz distribution. The cdf 

G

{\displaystyle G}
{\displaystyle Y}

 is related to 

F

{\displaystyle F}

, the cdf of 

X

{\displaystyle X}

, by the formula 
{\displaystyle G(y)=P(Y\leq y)=P(X\geq -y\mid X\leq 0)=(F(0)-F(-y))/F(0)}
{\displaystyle y>0}

. Consequently, the densities are related by 
{\displaystyle g(y)=f(-y)/F(0)}

: the Gompertz density is proportional to a reflected Gumbel density, restricted to the positive half-line.[6]
{\displaystyle X\sim \mathrm {Exponential} (1)}

 is an exponentially distributed variable with mean 1, then 
{\displaystyle \mu -\beta \log(X)\sim \mathrm {Gumbel} (\mu ,\beta )}
{\displaystyle U\sim \mathrm {Uniform} (0,1)}

 is a uniformly distributed variable on the unit interval, then 
{\displaystyle \mu -\beta \log(-\log(U))\sim \mathrm {Gumbel} (\mu ,\beta )}
{\displaystyle X\sim \mathrm {Gumbel} (\alpha _{X},\beta )}
{\displaystyle Y\sim \mathrm {Gumbel} (\alpha _{Y},\beta )}

 are independent, then 
{\displaystyle X-Y\sim \mathrm {Logistic} (\alpha _{X}-\alpha _{Y},\beta )\,}

 (see Logistic distribution).
Despite this, if 
{\displaystyle X,Y\sim \mathrm {Gumbel} (\alpha ,\beta )}

 are independent, then 
{\displaystyle X+Y\nsim \mathrm {Logistic} (2\alpha ,\beta )}

. This can easily be seen by noting that 
{\displaystyle \mathbb {E} (X+Y)=2\alpha +2\beta \gamma \neq 2\alpha =\mathbb {E} \left(\mathrm {Logistic} (2\alpha ,\beta )\right)}

 (where 

γ

{\displaystyle \gamma }

 is the Euler-Mascheroni constant). Instead, the distribution of linear combinations of independent Gumbel random variables can be approximated by GNIG and GIG distributions.[7]
Theory related to the generalized multivariate log-gamma distribution provides a multivariate version of the Gumbel distribution.

Occurrence and applications[edit]
Applications of the continuous Gumbel distribution[edit]
Distribution fitting with confidence band of a cumulative Gumbel distribution to maximum one-day October rainfalls. 
Gumbel has shown that the maximum value (or last order statistic) in a sample of random variables following an exponential distribution minus the natural logarithm of the sample size [8]  approaches the Gumbel distribution as the sample size increases.[9]
Concretely, let 
{\displaystyle \rho (x)=e^{-x}}

 be the probability distribution of 

x

{\displaystyle x}
{\displaystyle Q(x)=1-e^{-x}}

 its cumulative distribution. Then the maximum value out of 

N

{\displaystyle N}

 realizations of 

x

{\displaystyle x}

 is smaller than 

X

{\displaystyle X}

 if and only if all realizations are smaller than 

X

{\displaystyle X}

. So the cumulative distribution of the maximum value 
{\displaystyle {\tilde {x}}}

 satisfies
{\displaystyle P({\tilde {x}}-\log(N)\leq X)=P({\tilde {x}}\leq X+\log(N))=[Q(X+\log(N))]^{N}=\left(1-{\frac {e^{-X}}{N}}\right)^{N},}

and, for large 

N

{\displaystyle N}

, the right-hand-side converges to 
{\displaystyle e^{-e^{(-X)}}.}

In hydrology, therefore, the Gumbel distribution is used to analyze such variables as monthly and annual maximum values of daily rainfall and river discharge volumes,[3] and also to describe droughts.[10]
Gumbel has also shown that the estimator r⁄(n+1) for the probability of an event — where r is the rank number of the observed value in the data series and n is the total number of observations — is an unbiased estimator of the cumulative probability around the mode of the distribution. Therefore, this estimator is often used as a plotting position.

Prediction[edit]
It is often of interest to predict probabilities out-of-sample data under the assumption that both the training data and the out-of-sample data follow a Gumbel distribution.
Predictions of probabilities generated by substituting maximum likelihood estimates of the Gumbel parameters into the cumulative distribution function ignore parameter uncertainty. As a result, the probabilities are not well calibrated, do not reflect the frequencies of out-of-sample events, and, in particular, underestimate the probabilities of out-of-sample tail events.[11]
Predictions generated using the objective Bayesian approach of calibrating prior prediction completely eliminate this underestimation. The Gumbel distribution is one of a number of statistical distributions with group structure, which arises because the Gumbel is a location-scale model. As a result of the group structure, the Gumbel has associated left and right Haar measures. The use of the right Haar measure as the prior (known as the right Haar prior) in a Bayesian prediction gives probabilities that are perfectly calibrated, for any underlying true parameter values.[12][11][13] Calibrating prior prediction for the Gumbel using the appropriate right Haar prior is implemented in the R software package fitdistcp.[14]
Occurrences of the discrete Gumbel distribution[edit]
In combinatorics, the discrete Gumbel distribution appears as a limiting distribution for the hitting time in the coupon collector's problem. This result was first established by Laplace in 1812 in his Théorie analytique des probabilités, marking the first historical occurrence of what would later be called the Gumbel distribution.
In number theory, the Gumbel distribution approximates the number of terms in a random partition of an integer[15] as well as the trend-adjusted sizes of maximal prime gaps and maximal gaps between prime constellations.[16]
In probability theory, it appears as the distribution of the maximum height reached by discrete walks (on the lattice 
{\displaystyle {\mathbb {N} }^{2}}

), where the process can be reset to its starting point at each step.[4]
In analysis of algorithms, it appears, for example, in the study of the maximum carry propagation in base-

b

{\displaystyle b}

 addition algorithms.[17]

Random variate generation[edit]
Further information: Non-uniform random variate generation
Since the quantile function (inverse cumulative distribution function), 
{\displaystyle Q(p)}

, of a Gumbel distribution is given by
{\displaystyle Q(p)=\mu -\beta \ln(-\ln(p)),}

the variate 
{\displaystyle Q(U)}

 has a Gumbel distribution with parameters 

μ

{\displaystyle \mu }
{\displaystyle \beta }

 when the random variate 

U

{\displaystyle U}

 is drawn from the uniform distribution on the interval 
{\displaystyle (0,1)}

.

Probability paper[edit]
A piece of graph paper that incorporates the Gumbel distribution.
In pre-software times probability paper was used to picture the Gumbel distribution (see illustration). The paper is based on linearization of the cumulative distribution function 

F

{\displaystyle F}
{\displaystyle -\ln(-\ln(F))={\frac {x-\mu }{\beta }}}

In the paper the horizontal axis is constructed at a double log scale. The vertical axis is linear. By plotting 

F

{\displaystyle F}

 on the horizontal axis of the paper and the 

x

{\displaystyle x}

-variable on the vertical axis, the distribution is represented by a straight line with a slope 1
{\displaystyle /\beta }

. When distribution fitting software became available, the task of plotting the distribution was made easier.

Gumbel reparameterization tricks[edit]
In machine learning, the Gumbel distribution is sometimes employed to generate samples from the categorical distribution. This technique is called "Gumbel-max trick" and is a special example of "reparameterization tricks".[18]
In detail, let 
{\displaystyle (\pi _{1},\ldots ,\pi _{n})}

 be nonnegative, and not all zero, and let 
{\displaystyle g_{1},\ldots ,g_{n}}

 be independent samples of Gumbel(0, 1), the probability of the random variable 
{\displaystyle \arg \max _{i}(g_{i}+\log \pi _{i})}

 can be calculated by routine integration,
{\displaystyle Pr(\arg \max _{i}(g_{i}+\log \pi _{i})=j)={\frac {\pi _{j}}{\sum _{i}\pi _{i}}}}

That is, 

arg
⁡

max

i

(

g

i

+
log
⁡

π

i

)
∼

Categorical
{\displaystyle \arg \max _{i}(g_{i}+\log \pi _{i})\sim {\text{Categorical}}\left({\frac {\pi _{j}}{\sum _{i}\pi _{i}}}\right)_{j}}

Equivalently, given any 
{\displaystyle x_{1},...,x_{n}\in \mathbb {R} }

, we can sample from its Boltzmann distribution by
{\displaystyle Pr(\arg \max _{i}(g_{i}+x_{i})=j)={\frac {e^{x_{j}}}{\sum _{i}e^{x_{i}}}}}

Related equations include:[19]
{\displaystyle x\sim \operatorname {Exp} (\lambda )}

, then 

(
−
ln
⁡
x
−
γ
)
∼

Gumbel
{\displaystyle (-\ln x-\gamma )\sim {\text{Gumbel}}(-\gamma +\ln \lambda ,1)}

.

arg
⁡

max

i

(

g

i

+
log
⁡

π

i

)
∼

Categorical
{\displaystyle \arg \max _{i}(g_{i}+\log \pi _{i})\sim {\text{Categorical}}\left({\frac {\pi _{j}}{\sum _{i}\pi _{i}}}\right)_{j}}

.

max

i

(

g

i

+
log
⁡

π

i

)
∼

Gumbel
{\displaystyle \max _{i}(g_{i}+\log \pi _{i})\sim {\text{Gumbel}}\left(\log \left(\sum _{i}\pi _{i}\right),1\right)}

. That is, the Gumbel distribution is a max-stable distribution family.
{\displaystyle \mathbb {E} [\max _{i}(g_{i}+\beta x_{i})]=\log \left(\sum _{i}e^{\beta x_{i}}\right)+\gamma .}
