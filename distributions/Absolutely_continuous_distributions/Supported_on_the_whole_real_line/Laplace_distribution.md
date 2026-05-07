# Laplace distribution

Probability distribution

| Laplace |
| --- |
| Probability density function |
| Cumulative distribution function |
| Parameters | μ {\displaystyle \mu } location (real) b > 0 {\displaystyle b>0} scale (real) ${\displaystyle \mu }$ ${\displaystyle b>0}$ |
| Support | R {\displaystyle \mathbb {R} } ${\displaystyle \mathbb {R} }$ |
| PDF | 1 2 b exp ⁡ ( − \| x − μ \| b ) {\displaystyle {\frac {1}{2b}}\exp \left(-{\frac {\|x-\mu \|}{b}}\right)} ${\displaystyle {\frac {1}{2b}}\exp \left(-{\frac {\|x-\mu \|}{b}}\right)}$ |
| CDF | { 1 2 exp ⁡ ( x − μ b ) if x ≤ μ 1 − 1 2 exp ⁡ ( − x − μ b ) if x ≥ μ {\displaystyle {\begin{cases}{\frac {1}{2}}\exp \left({\frac {x-\mu }{b}}\right)&{\text{if }}x\leq \mu \\[8pt]1-{\frac {1}{2}}\exp \left(-{\frac {x-\mu }{b}}\right)&{\text{if }}x\geq \mu \end{cases}}} ${\displaystyle {\begin{cases}{\frac {1}{2}}\exp \left({\frac {x-\mu }{b}}\right)&{\text{if }}x\leq \mu \\[8pt]1-{\frac {1}{2}}\exp \left(-{\frac {x-\mu }{b}}\right)&{\text{if }}x\geq \mu \end{cases}}}$ |
| Quantile | { μ + b ln ⁡ ( 2 F ) if F ≤ 1 2 μ − b ln ⁡ ( 2 − 2 F ) if F ≥ 1 2 {\displaystyle {\begin{cases}\mu +b\ln \left(2F\right)&{\text{if }}F\leq {\frac {1}{2}}\\[8pt]\mu -b\ln \left(2-2F\right)&{\text{if }}F\geq {\frac {1}{2}}\end{cases}}} ${\displaystyle {\begin{cases}\mu +b\ln \left(2F\right)&{\text{if }}F\leq {\frac {1}{2}}\\[8pt]\mu -b\ln \left(2-2F\right)&{\text{if }}F\geq {\frac {1}{2}}\end{cases}}}$ |
| Mean | μ {\displaystyle \mu } ${\displaystyle \mu }$ |
| Median | μ {\displaystyle \mu } ${\displaystyle \mu }$ |
| Mode | μ {\displaystyle \mu } ${\displaystyle \mu }$ |
| Variance | 2 b 2 {\displaystyle 2b^{2}} ${\displaystyle 2b^{2}}$ |
| MAD | b ln ⁡ 2 {\displaystyle b\ln 2} ${\displaystyle b\ln 2}$ |
| Skewness | 0 {\displaystyle 0} ${\displaystyle 0}$ |
| Excess kurtosis | 3 {\displaystyle 3} ${\displaystyle 3}$ |
| Entropy | log ⁡ ( 2 b e ) {\displaystyle \log(2be)} ${\displaystyle \log(2be)}$ |
| MGF | exp ⁡ ( μ t ) 1 − b 2 t 2 for \| t \| < 1 / b {\displaystyle {\frac {\exp(\mu t)}{1-b^{2}t^{2}}}{\text{ for }}\|t\|<1/b} ${\displaystyle {\frac {\exp(\mu t)}{1-b^{2}t^{2}}}{\text{ for }}\|t\|<1/b}$ |
| CF | exp ⁡ ( μ i t ) 1 + b 2 t 2 {\displaystyle {\frac {\exp(\mu it)}{1+b^{2}t^{2}}}} ${\displaystyle {\frac {\exp(\mu it)}{1+b^{2}t^{2}}}}$ |
| Expected shortfall | { μ + b ( p 1 − p ) ( 1 − ln ⁡ ( 2 p ) ) , p < .5 μ + b ( 1 − ln ⁡ ( 2 ( 1 − p ) ) ) , p ≥ .5 {\displaystyle {\begin{cases}\mu +b\left({\frac {p}{1-p}}\right)(1-\ln(2p))&,p<.5\\\mu +b\left(1-\ln \left(2(1-p)\right)\right)&,p\geq .5\end{cases}}} [1] ${\displaystyle {\begin{cases}\mu +b\left({\frac {p}{1-p}}\right)(1-\ln(2p))&,p<.5\\\mu +b\left(1-\ln \left(2(1-p)\right)\right)&,p\geq .5\end{cases}}}$ |

In probability theory and statistics, the Laplace distribution is a continuous probability distribution named after Pierre-Simon Laplace.  It is also sometimes called the double exponential distribution, because it can be thought of as two exponential distributions (with an additional location parameter) spliced together along the x-axis,[2] although the term is also sometimes used to refer to the Gumbel distribution.  The difference between two independent identically distributed exponential random variables is governed by a Laplace distribution, as is a Brownian motion evaluated at an exponentially distributed random time[citation needed].  Increments of Laplace motion or a variance gamma process evaluated over the time scale also have a Laplace distribution.

Definitions[edit]
Probability density function[edit]
A random variable has a 

Laplace
{\displaystyle \operatorname {Laplace} (\mu ,b)}

 distribution if its probability density function is
{\displaystyle f(x\mid \mu ,b)={\frac {1}{2b}}e^{-{\frac {|x-\mu |}{b}}},}

where 

μ

{\displaystyle \mu }

 is a location parameter, and 
{\displaystyle b>0}

, which is sometimes referred to as the "diversity", is a scale parameter. If 
{\displaystyle \mu =0}
{\displaystyle b=1}

, the positive half-line is exactly an exponential distribution scaled by 1/2.[3]
The probability density function of the Laplace distribution is also reminiscent of the normal distribution; however, whereas the normal distribution is expressed in terms of the squared difference from the mean 

μ

{\displaystyle \mu }

, the Laplace density is expressed in terms of the absolute difference from the mean. Consequently, the Laplace distribution has fatter tails than the normal distribution. It is a special case of the generalized normal distribution and the hyperbolic distribution. Continuous symmetric distributions that have exponential tails, like the Laplace distribution, but which have probability density functions that are differentiable at the mode include the logistic distribution, hyperbolic secant distribution, and the Champernowne distribution.

Cumulative distribution function[edit]
The Laplace distribution is easy to integrate (if one distinguishes two symmetric cases) due to the use of the absolute value function.  Its cumulative distribution function is as follows:
{\displaystyle {\begin{aligned}F(x)&=\int _{-\infty }^{x}\!\!f(u)\,\mathrm {d} u={\begin{cases}{\frac {1}{2}}\exp \left({\frac {x-\mu }{b}}\right)&{\mbox{if }}x<\mu \\1-{\frac {1}{2}}\exp \left(-{\frac {x-\mu }{b}}\right)&{\mbox{if }}x\geq \mu \end{cases}}\\&={\tfrac {1}{2}}+{\tfrac {1}{2}}\operatorname {sgn}(x-\mu )\left(1-\exp \left(-{\frac {|x-\mu |}{b}}\right)\right).\end{aligned}}}

The inverse cumulative distribution function is given by
{\displaystyle F^{-1}(p)=\mu -b\,\operatorname {sgn}(p-0.5)\,\ln(1-2|p-0.5|).}

Properties[edit]
Moments[edit]
{\displaystyle \mu _{r}'={\bigg (}{\frac {1}{2}}{\bigg )}\sum _{k=0}^{r}{\bigg [}{\frac {r!}{(r-k)!}}b^{k}\mu ^{(r-k)}\{1+(-1)^{k}\}{\bigg ]}.}

Related distributions[edit]
If 

X
∼

Laplace
{\displaystyle X\sim {\textrm {Laplace}}(\mu ,b)}

 then 

k
X
+
c
∼

Laplace
{\displaystyle kX+c\sim {\textrm {Laplace}}(k\mu +c,|k|b)}

.
If 

X
∼

Laplace
{\displaystyle X\sim {\textrm {Laplace}}(0,1)}

 then 

b
X
∼

Laplace
{\displaystyle bX\sim {\textrm {Laplace}}(0,b)}

.
If 

X
∼

Laplace
{\displaystyle X\sim {\textrm {Laplace}}(0,b)}

 then 

|
X
|

∼

Exponential
{\displaystyle \left|X\right|\sim {\textrm {Exponential}}\left(b^{-1}\right)}

 (exponential distribution).
If 

X
,
Y
∼

Exponential
{\displaystyle X,Y\sim {\textrm {Exponential}}(\lambda )}

 then 

X
−
Y
∼

Laplace
{\displaystyle X-Y\sim {\textrm {Laplace}}\left(0,\lambda ^{-1}\right)}

．
If 

X
∼

Laplace
{\displaystyle X\sim {\textrm {Laplace}}(\mu ,b)}

 then 

|

X
−
μ

|

∼

Exponential
{\displaystyle \left|X-\mu \right|\sim {\textrm {Exponential}}(b^{-1})}

.
If 

X
∼

Laplace
{\displaystyle X\sim {\textrm {Laplace}}(\mu ,b)}

 then 
{\displaystyle X\sim {\textrm {EPD}}(\mu ,b,1)}

 (exponential power distribution).
{\displaystyle X_{1},...,X_{4}\sim {\textrm {N}}(0,1)}

 (normal distribution) then 

X

1

X

2

−

X

3

X

4

∼

Laplace
{\displaystyle X_{1}X_{2}-X_{3}X_{4}\sim {\textrm {Laplace}}(0,1)}

 and 

(

X

1

2

−

X

2

2

+

X

3

2

−

X

4

2

)

/

2
∼

Laplace
{\displaystyle (X_{1}^{2}-X_{2}^{2}+X_{3}^{2}-X_{4}^{2})/2\sim {\textrm {Laplace}}(0,1)}

.
If 

X

i

∼

Laplace
{\displaystyle X_{i}\sim {\textrm {Laplace}}(\mu ,b)}

 then 
{\displaystyle {\frac {\displaystyle 2}{b}}\sum _{i=1}^{n}|X_{i}-\mu |\sim \chi ^{2}(2n)}

 (chi-squared distribution).
If 

X
,
Y
∼

Laplace
{\displaystyle X,Y\sim {\textrm {Laplace}}(\mu ,b)}

 then 
{\displaystyle {\tfrac {|X-\mu |}{|Y-\mu |}}\sim \operatorname {F} (2,2)}

. (F-distribution)
{\displaystyle X,Y\sim {\textrm {U}}(0,1)}

 (uniform distribution) then 

log
⁡
(
X

/

Y
)
∼

Laplace
{\displaystyle \log(X/Y)\sim {\textrm {Laplace}}(0,1)}

.
If 

X
∼

Exponential
{\displaystyle X\sim {\textrm {Exponential}}(\lambda )}

 and 

Y
∼

Bernoulli
{\displaystyle Y\sim {\textrm {Bernoulli}}(0.5)}

 (Bernoulli distribution) independent of 

X

{\displaystyle X}

, then 

X
(
2
Y
−
1
)
∼

Laplace
{\displaystyle X(2Y-1)\sim {\textrm {Laplace}}\left(0,\lambda ^{-1}\right)}

.
If 

X
∼

Exponential
{\displaystyle X\sim {\textrm {Exponential}}(\lambda )}

 and 

Y
∼

Exponential
{\displaystyle Y\sim {\textrm {Exponential}}(\nu )}

 independent of 

X

{\displaystyle X}

, then 

λ
X
−
ν
Y
∼

Laplace
{\displaystyle \lambda X-\nu Y\sim {\textrm {Laplace}}(0,1)}
{\displaystyle X}

 has a Rademacher distribution and 

Y
∼

Exponential
{\displaystyle Y\sim {\textrm {Exponential}}(\lambda )}

 then 

X
Y
∼

Laplace
{\displaystyle XY\sim {\textrm {Laplace}}(0,1/\lambda )}

.
If 

V
∼

Exponential
{\displaystyle V\sim {\textrm {Exponential}}(1)}
{\displaystyle Z\sim N(0,1)}

 independent of 

V

{\displaystyle V}

, then 
{\displaystyle X=\mu +b{\sqrt {2V}}Z\sim \mathrm {Laplace} (\mu ,b)}

.
If 

X
∼

GeometricStable
{\displaystyle X\sim {\textrm {GeometricStable}}(2,0,\lambda ,0)}

 (geometric stable distribution) then 

X
∼

Laplace
{\displaystyle X\sim {\textrm {Laplace}}(0,\lambda )}

.
The Laplace distribution is a limiting case of the hyperbolic distribution.
{\displaystyle X|Y\sim {\textrm {N}}(\mu ,Y^{2})}

 with 

Y
∼

Rayleigh
{\displaystyle Y\sim {\textrm {Rayleigh}}(b)}

 (Rayleigh distribution) then 

X
∼

Laplace
{\displaystyle X\sim {\textrm {Laplace}}(\mu ,b)}

. Note that if 

Y
∼

Rayleigh
{\displaystyle Y\sim {\textrm {Rayleigh}}(b)}

, then 

Y

2

∼

Gamma
{\displaystyle Y^{2}\sim {\textrm {Gamma}}(1,2b^{2})}

 with 
{\displaystyle {\textrm {E}}(Y^{2})=2b^{2}}

, which in turn equals the exponential distribution 
{\displaystyle {\textrm {Exp}}(1/(2b^{2}))}

.
Given an integer 
{\displaystyle n\geq 1}
{\displaystyle X_{i},Y_{i}\sim \Gamma \left({\frac {1}{n}},b\right)}

 (gamma distribution, using 
{\displaystyle k,\theta }

 characterization), then 

∑

i
=
1

n

(

μ
n

+

X

i

−

Y

i

)

∼

Laplace
{\displaystyle \sum _{i=1}^{n}\left({\frac {\mu }{n}}+X_{i}-Y_{i}\right)\sim {\textrm {Laplace}}(\mu ,b)}

 (infinite divisibility)[4]
If X has a Laplace distribution, then Y = eX has a log-Laplace distribution; conversely, if X has a log-Laplace distribution, then its logarithm has a Laplace distribution.
Probability of a Laplace being greater than another[edit]
{\displaystyle X,Y}

 be independent laplace random variables: 

X
∼

Laplace
{\displaystyle X\sim {\textrm {Laplace}}(\mu _{X},b_{X})}

 and 

Y
∼

Laplace
{\displaystyle Y\sim {\textrm {Laplace}}(\mu _{Y},b_{Y})}

, and we want to compute 
{\displaystyle P(X>Y)}

.
The probability of 
{\displaystyle P(X>Y)}

 can be reduced (using the properties below) to 
{\displaystyle P(\mu +bZ_{1}>Z_{2})}

, where 

Z

1

,

Z

2

∼

Laplace
{\displaystyle Z_{1},Z_{2}\sim {\textrm {Laplace}}(0,1)}

. This probability is equal to

P
(
μ
+
b

Z

1

>

Z

2

)
=

{

b

2

e

μ

/

b

−

e

μ

2
(

b

2

−
1
)

,

when 

μ
<
0

1
−

b

2

e

−
μ

/

b

−

e

−
μ

2
(

b

2

−
1
)

,

when 
{\displaystyle P(\mu +bZ_{1}>Z_{2})={\begin{cases}{\frac {b^{2}e^{\mu /b}-e^{\mu }}{2(b^{2}-1)}},&{\text{when }}\mu <0\\1-{\frac {b^{2}e^{-\mu /b}-e^{-\mu }}{2(b^{2}-1)}},&{\text{when }}\mu >0\\\end{cases}}}

When 
{\displaystyle b=1}

, both expressions are replaced by their limit as 
{\displaystyle b\to 1}

:

P
(
μ
+

Z

1

>

Z

2

)
=

{

e

μ

(
2
−
μ
)

4

,

when 

μ
<
0

1
−

e

−
μ

(
2
+
μ
)

4

,

when 
{\displaystyle P(\mu +Z_{1}>Z_{2})={\begin{cases}e^{\mu }{\frac {(2-\mu )}{4}},&{\text{when }}\mu <0\\1-e^{-\mu }{\frac {(2+\mu )}{4}},&{\text{when }}\mu >0\\\end{cases}}}

To compute the case for 
{\displaystyle \mu >0}

, note that 
{\displaystyle P(\mu +Z_{1}>Z_{2})=1-P(\mu +Z_{1}<Z_{2})=1-P(-\mu -Z_{1}>-Z_{2})=1-P(-\mu +Z_{1}>Z_{2})}

since 
{\displaystyle Z\sim -Z}

 when 

Z
∼

Laplace
{\displaystyle Z\sim {\textrm {Laplace}}(0,1)}

 .

Relation to the exponential distribution[edit]
A Laplace random variable can be represented as the difference of two independent and identically distributed (iid) exponential random variables.[4] One way to show this is by using the characteristic function approach. For any set of independent continuous random variables, for any linear combination of those variables, its characteristic function (which uniquely determines the distribution) can be acquired by multiplying the corresponding characteristic functions.
Consider two i.i.d random variables 

X
,
Y
∼

Exponential
{\displaystyle X,Y\sim {\textrm {Exponential}}(\lambda )}

. The characteristic functions for 
{\displaystyle X,-Y}
{\displaystyle {\frac {\lambda }{-it+\lambda }},\quad {\frac {\lambda }{it+\lambda }}}

respectively. On multiplying these characteristic functions (equivalent to the characteristic function of the sum of the random variables 
{\displaystyle X+(-Y)}

), the result is
{\displaystyle {\frac {\lambda ^{2}}{(-it+\lambda )(it+\lambda )}}={\frac {\lambda ^{2}}{t^{2}+\lambda ^{2}}}.}

This is the same as the characteristic function for 

Z
∼

Laplace
{\displaystyle Z\sim {\textrm {Laplace}}(0,1/\lambda )}

, which is
{\displaystyle {\frac {1}{1+{\frac {t^{2}}{\lambda ^{2}}}}}.}

Sargan distributions[edit]
Sargan distributions are a system of distributions of which the Laplace distribution is a core member. A 

p

{\displaystyle p}

th order Sargan distribution has density[5][6]
{\displaystyle f_{p}(x)={\tfrac {1}{2}}\exp(-\alpha |x|){\frac {\displaystyle 1+\sum _{j=1}^{p}\beta _{j}\alpha ^{j}|x|^{j}}{\displaystyle 1+\sum _{j=1}^{p}j!\beta _{j}}},}

for parameters 
{\displaystyle \alpha \geq 0,\beta _{j}\geq 0}

. The Laplace distribution results for 
{\displaystyle p=0}

.

Statistical inference[edit]
Given 

n

{\displaystyle n}

 independent and identically distributed samples 
{\displaystyle x_{1},x_{2},...,x_{n}}

, the maximum likelihood (MLE) estimator of 

μ

{\displaystyle \mu }

 is the sample median,[7]
{\displaystyle {\hat {\mu }}=\mathrm {med} (x).}

The MLE estimator of 

b

{\displaystyle b}

 is the mean absolute deviation from the median,[citation needed]
{\displaystyle {\hat {b}}={\frac {1}{n}}\sum _{i=1}^{n}|x_{i}-{\hat {\mu }}|.}

revealing a link between the Laplace distribution and least absolute deviations.
A correction for small samples can be applied as follows:
{\displaystyle {\hat {b}}^{*}={\hat {b}}\cdot n/(n-2)}

(see: exponential distribution#Parameter estimation).

Occurrence and applications[edit]
The Laplacian distribution has been used in speech recognition to model priors on DFT coefficients [8] and in JPEG image compression to model AC coefficients [9] generated by a DCT.

The addition of noise drawn from a Laplacian distribution, with scaling parameter appropriate to a function's sensitivity, to the output of a statistical database query is the most common means to provide differential privacy in statistical databases.
Fitted Laplace distribution to maximum one-day rainfalls 
In regression analysis, the least absolute deviations estimate arises as the maximum likelihood estimate if the errors have a Laplace distribution.
The Lasso can be thought of as a Bayesian regression with a Laplacian prior for the coefficients.[10]
In hydrology the Laplace distribution is applied to extreme events such as annual maximum one-day rainfalls and river discharges. The blue picture illustrates an example of fitting the Laplace distribution to ranked annually maximum one-day rainfalls showing also the 90% confidence belt based on the binomial distribution. The rainfall data are represented by plotting positions as part of the cumulative frequency analysis.
The Laplace distribution has applications in finance.  For example, S.G. Kou developed a model for financial instrument prices incorporating a Laplace distribution (in some cases an asymmetric Laplace distribution) to address problems of skewness, kurtosis and the volatility smile that often occur when using a normal distribution for pricing these instruments.[11][12]
The Laplace distribution, being a composite or double distribution, is applicable in situations where the lower values originate under different external conditions than the higher ones so that they follow a different pattern.[13]
Random variate generation[edit]
Further information: Non-uniform random variate generation
Given a random variable 

U

{\displaystyle U}

 drawn from the uniform distribution in the interval 
{\displaystyle \left(-1/2,1/2\right)}

, the random variable
{\displaystyle X=\mu -b\,\operatorname {sgn}(U)\,\ln(1-2|U|)}

has a Laplace distribution with parameters 

μ

{\displaystyle \mu }
{\displaystyle b}

. This follows from the inverse cumulative distribution function given above.
A 

Laplace
{\displaystyle {\textrm {Laplace}}(0,b)}

 variate can also be generated as the difference of two i.i.d. 

Exponential
{\displaystyle {\textrm {Exponential}}(1/b)}

 random variables. Equivalently, 

Laplace
{\displaystyle {\textrm {Laplace}}(0,1)}

 can also be generated as the logarithm of the ratio of two i.i.d. uniform random variables.

History[edit]
This distribution is often referred to as "Laplace's first law of errors". He published it in 1774, modeling the frequency of an error as an exponential function of its magnitude once its sign was disregarded. Laplace would later replace this model with his "second law of errors", based on the normal distribution, after the discovery of the central limit theorem.[14][15]
Keynes published a paper in 1911 based on his earlier thesis wherein he showed that the Laplace distribution minimised the absolute deviation from the median.[16]
