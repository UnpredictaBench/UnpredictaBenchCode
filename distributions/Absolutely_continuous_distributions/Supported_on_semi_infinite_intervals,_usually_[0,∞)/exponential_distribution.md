# Exponential distribution

Probability distribution

Not to be confused with the exponential family of probability distributions.

| Exponential |
| --- |
| Probability density function |
| Cumulative distribution function |
| Parameters | λ > 0 , {\displaystyle \lambda >0,} rate, or inverse scale ${\displaystyle \lambda >0,}$ |
| Support | x ∈ [ 0 , ∞ ) {\displaystyle x\in [0,\infty )} ${\displaystyle x\in [0,\infty )}$ |
| PDF | λ e − λ x {\displaystyle \lambda e^{-\lambda x}} ${\displaystyle \lambda e^{-\lambda x}}$ |
| CDF | 1 − e − λ x {\displaystyle 1-e^{-\lambda x}} ${\displaystyle 1-e^{-\lambda x}}$ |
| Quantile | − ln ⁡ ( 1 − p ) λ {\displaystyle -{\frac {\ln(1-p)}{\lambda }}} ${\displaystyle -{\frac {\ln(1-p)}{\lambda }}}$ |
| Mean | 1 λ {\displaystyle {\frac {1}{\lambda }}} ${\displaystyle {\frac {1}{\lambda }}}$ |
| Median | ln ⁡ 2 λ {\displaystyle {\frac {\ln 2}{\lambda }}} ${\displaystyle {\frac {\ln 2}{\lambda }}}$ |
| Mode | 0 {\displaystyle 0} ${\displaystyle 0}$ |
| Variance | 1 λ 2 {\displaystyle {\frac {1}{\lambda ^{2}}}} ${\displaystyle {\frac {1}{\lambda ^{2}}}}$ |
| Skewness | 2 {\displaystyle 2} ${\displaystyle 2}$ |
| Excess kurtosis | 6 {\displaystyle 6} ${\displaystyle 6}$ |
| Entropy | 1 − ln ⁡ λ {\displaystyle 1-\ln \lambda } ${\displaystyle 1-\ln \lambda }$ |
| MGF | λ λ − t , for t < λ {\displaystyle {\frac {\lambda }{\lambda -t}},{\text{ for }}t<\lambda } ${\displaystyle {\frac {\lambda }{\lambda -t}},{\text{ for }}t<\lambda }$ |
| CF | λ λ − i t {\displaystyle {\frac {\lambda }{\lambda -it}}} ${\displaystyle {\frac {\lambda }{\lambda -it}}}$ |
| Fisher information | 1 λ 2 {\displaystyle {\frac {1}{\lambda ^{2}}}} ${\displaystyle {\frac {1}{\lambda ^{2}}}}$ |
| Kullback–Leibler divergence | ln ⁡ λ 0 λ + λ λ 0 − 1 {\displaystyle \ln {\frac {\lambda _{0}}{\lambda }}+{\frac {\lambda }{\lambda _{0}}}-1} ${\displaystyle \ln {\frac {\lambda _{0}}{\lambda }}+{\frac {\lambda }{\lambda _{0}}}-1}$ |
| Expected shortfall | − ln ⁡ ( 1 − p ) + 1 λ {\displaystyle {\frac {-\ln(1-p)+1}{\lambda }}} ${\displaystyle {\frac {-\ln(1-p)+1}{\lambda }}}$ |

In probability theory and statistics, the exponential distribution or negative exponential distribution is the probability distribution of the distance between events in a Poisson point process, i.e., a process in which events occur continuously and independently at a constant average rate; the distance parameter could be any meaningful mono-dimensional measure of the process, such as time between production errors, or length along a roll of fabric in the weaving manufacturing process.[1] It is a particular case of the gamma distribution. It is the continuous analogue of the geometric distribution, and it has the key property of being memoryless.[2] In addition to being used for the analysis of Poisson point processes it is found in various other contexts.[3]

The exponential distribution is not the same as the class of exponential families of distributions. This is a large class of probability distributions that includes the exponential distribution as one of its members, but also includes many other distributions, such as the normal, binomial, gamma, and Poisson distributions.[3]

Definitions
Probability density function
The probability density function (pdf) of an exponential distribution is
{\displaystyle f(x;\lambda )={\begin{cases}\lambda e^{-\lambda x}&x\geq 0,\\0&x<0.\end{cases}}}

Here λ > 0 is the parameter of the distribution, often called the rate parameter. The distribution is supported on the interval [0, ∞). If a random variable X has this distribution, we write X ~ Exp(λ).
The exponential distribution exhibits infinite divisibility.

Cumulative distribution function
The cumulative distribution function is given by
{\displaystyle F(x;\lambda )={\begin{cases}1-e^{-\lambda x}&x\geq 0,\\0&x<0.\end{cases}}}

Alternative parametrization
The exponential distribution is sometimes parametrized in terms of the scale parameter β = 1/λ, which is also the mean:
{\displaystyle f(x;\beta )={\begin{cases}{\frac {1}{\beta }}e^{-x/\beta }&x\geq 0,\\0&x<0.\end{cases}}\qquad \qquad F(x;\beta )={\begin{cases}1-e^{-x/\beta }&x\geq 0,\\0&x<0.\end{cases}}}

Properties
Mean, variance, moments, and median
The mean is the probability mass centre, that is, the first moment.
The median is the preimage F−1(1/2).
The mean or expected value of an exponentially distributed random variable X with rate parameter λ is given by
{\displaystyle \operatorname {E} [X]={\frac {1}{\lambda }}.}

In light of the examples given below, this makes sense; a person who receives an average of two telephone calls per hour can expect that the time between consecutive calls will be 0.5 hour, or 30 minutes.
The variance of X is given by
{\displaystyle \operatorname {Var} [X]={\frac {1}{\lambda ^{2}}},}

so the standard deviation is equal to the mean.
The moments of X, for 
{\displaystyle n\in \mathbb {N} }

 are given by
{\displaystyle \operatorname {E} \left[X^{n}\right]={\frac {n!}{\lambda ^{n}}}.}

The central moments of X, for 
{\displaystyle n\in \mathbb {N} }

 are given by
{\displaystyle \mu _{n}={\frac {!n}{\lambda ^{n}}}={\frac {n!}{\lambda ^{n}}}\sum _{k=0}^{n}{\frac {(-1)^{k}}{k!}}.}

where !n is the subfactorial of n
The median of X is given by
{\displaystyle \operatorname {m} [X]={\frac {\ln(2)}{\lambda }}<\operatorname {E} [X],}

where ln refers to the natural logarithm.  Thus the absolute difference between the mean and median is
{\displaystyle \left|\operatorname {E} \left[X\right]-\operatorname {m} \left[X\right]\right|={\frac {1-\ln(2)}{\lambda }}<{\frac {1}{\lambda }}=\operatorname {\sigma } [X],}

in accordance with the median-mean inequality.

Memorylessness property of exponential random variable
An exponentially distributed random variable T obeys the relation
{\displaystyle \Pr \left(T>s+t\mid T>s\right)=\Pr(T>t),\qquad \forall s,t\geq 0.}

This can be seen by considering the complementary cumulative distribution function:
{\displaystyle {\begin{aligned}\Pr \left(T>s+t\mid T>s\right)&={\frac {\Pr \left(T>s+t\cap T>s\right)}{\Pr \left(T>s\right)}}\\[4pt]&={\frac {\Pr \left(T>s+t\right)}{\Pr \left(T>s\right)}}\\[4pt]&={\frac {e^{-\lambda (s+t)}}{e^{-\lambda s}}}\\[4pt]&=e^{-\lambda t}\\[4pt]&=\Pr(T>t).\end{aligned}}}

When T is interpreted as the waiting time for an event to occur relative to some initial time, this relation implies that, if T is conditioned on a failure to observe the event over some initial period of time s, the distribution of the remaining waiting time is the same as the original unconditional distribution. For example, if an event has not occurred after 30 seconds, the conditional probability that occurrence will take at least 10 more seconds is equal to the unconditional probability of observing the event more than 10 seconds after the initial time.
The exponential distribution and the geometric distribution are the only memoryless probability distributions.
The exponential distribution is consequently also necessarily the only continuous probability distribution that has a constant failure rate.

Quantiles
 Tukey criteria for anomalies.[citation needed]
The quantile function (inverse cumulative distribution function) for Exp(λ) is
{\displaystyle F^{-1}(p;\lambda )={\frac {-\ln(1-p)}{\lambda }},\qquad 0\leq p<1}

The quartiles are therefore:

first quartile: ln(4/3)/λ
median: ln(2)/λ
third quartile: ln(4)/λ
And as a consequence the interquartile range is ln(3)/λ.

Conditional Value at Risk (Expected Shortfall)
The conditional value at risk (CVaR) also known as the expected shortfall or superquantile for Exp(λ) is derived as follows:[4]
{\displaystyle {\begin{aligned}{\bar {q}}_{\alpha }(X)&={\frac {1}{1-\alpha }}\int _{\alpha }^{1}q_{p}(X)dp\\&={\frac {1}{(1-\alpha )}}\int _{\alpha }^{1}{\frac {-\ln(1-p)}{\lambda }}dp\\&={\frac {-1}{\lambda (1-\alpha )}}\int _{1-\alpha }^{0}-\ln(y)dy\\&={\frac {-1}{\lambda (1-\alpha )}}\int _{0}^{1-\alpha }\ln(y)dy\\&={\frac {-1}{\lambda (1-\alpha )}}[(1-\alpha )\ln(1-\alpha )-(1-\alpha )]\\&={\frac {-\ln(1-\alpha )+1}{\lambda }}\\\end{aligned}}}

Buffered Probability of Exceedance (bPOE)
Main article: Buffered probability of exceedance
The buffered probability of exceedance is one minus the probability level at which the CVaR equals the threshold 

x

{\displaystyle x}

.  It is derived as follows:[4]
{\displaystyle {\begin{aligned}{\bar {p}}_{x}(X)&=\{1-\alpha |{\bar {q}}_{\alpha }(X)=x\}\\&=\{1-\alpha |{\frac {-\ln(1-\alpha )+1}{\lambda }}=x\}\\&=\{1-\alpha |\ln(1-\alpha )=1-\lambda x\}\\&=\{1-\alpha |e^{\ln(1-\alpha )}=e^{1-\lambda x}\}=\{1-\alpha |1-\alpha =e^{1-\lambda x}\}=e^{1-\lambda x}\end{aligned}}}

Kullback–Leibler divergence
The directed Kullback–Leibler divergence in nats of 
{\displaystyle e^{\lambda }}

 ("approximating" distribution) from 
{\displaystyle e^{\lambda _{0}}}

 ('true' distribution) is given by
{\displaystyle {\begin{aligned}\Delta (\lambda _{0}\parallel \lambda )&=\mathbb {E} _{\lambda _{0}}\left(\log {\frac {p_{\lambda _{0}}(x)}{p_{\lambda }(x)}}\right)\\&=\mathbb {E} _{\lambda _{0}}\left(\log {\frac {\lambda _{0}e^{\lambda _{0}x}}{\lambda e^{\lambda x}}}\right)\\&=\log(\lambda _{0})-\log(\lambda )-(\lambda _{0}-\lambda )E_{\lambda _{0}}(x)\\&=\log(\lambda _{0})-\log(\lambda )+{\frac {\lambda }{\lambda _{0}}}-1.\end{aligned}}}

Maximum entropy distribution
Among all continuous probability distributions with support [0, ∞) and mean μ, the exponential distribution with λ = 1/μ has the largest differential entropy. In other words, it is the maximum entropy probability distribution for a random variate X which is greater than or equal to zero and for which E[X] is fixed.[5]

Distribution of the minimum of exponential random variables
Let X1, ..., Xn be independent exponentially distributed random variables with rate parameters λ1, ..., λn.  Then
{\displaystyle \min \left\{X_{1},\dotsc ,X_{n}\right\}}

is also exponentially distributed, with parameter
{\displaystyle \lambda =\lambda _{1}+\dotsb +\lambda _{n}.}

This can be seen by considering the complementary cumulative distribution function:
{\displaystyle {\begin{aligned}&\Pr \left(\min\{X_{1},\dotsc ,X_{n}\}>x\right)\\={}&\Pr \left(X_{1}>x,\dotsc ,X_{n}>x\right)\\={}&\prod _{i=1}^{n}\Pr \left(X_{i}>x\right)\\={}&\prod _{i=1}^{n}\exp \left(-x\lambda _{i}\right)=\exp \left(-x\sum _{i=1}^{n}\lambda _{i}\right).\end{aligned}}}

The index of the variable which achieves the minimum is distributed according to the categorical distribution
{\displaystyle \Pr \left(X_{k}=\min\{X_{1},\dotsc ,X_{n}\}\right)={\frac {\lambda _{k}}{\lambda _{1}+\dotsb +\lambda _{n}}}.}

A proof can be seen by letting 

I
=

argmin
{\displaystyle I=\operatorname {argmin} _{i\in \{1,\dotsb ,n\}}\{X_{1},\dotsc ,X_{n}\}}

. Then,
{\displaystyle {\begin{aligned}\Pr(I=k)&=\int _{0}^{\infty }\Pr(X_{k}=x)\Pr(\forall _{i\neq k}X_{i}>x)\,dx\\&=\int _{0}^{\infty }\lambda _{k}e^{-\lambda _{k}x}\left(\prod _{i=1,i\neq k}^{n}e^{-\lambda _{i}x}\right)dx\\&=\lambda _{k}\int _{0}^{\infty }e^{-\left(\lambda _{1}+\dotsb +\lambda _{n}\right)x}dx\\&={\frac {\lambda _{k}}{\lambda _{1}+\dotsb +\lambda _{n}}}.\end{aligned}}}

Note that
{\displaystyle \max\{X_{1},\dotsc ,X_{n}\}}

is not exponentially distributed, if X1, ..., Xn do not all have parameter 0.[6]

Joint moments of i.i.d. exponential order statistics
{\displaystyle X_{1},\dotsc ,X_{n}}
{\displaystyle n}

 independent and identically distributed exponential random variables with rate parameter λ.
{\displaystyle X_{(1)},\dotsc ,X_{(n)}}

 denote the corresponding order statistics.
{\displaystyle i<j}

 , the joint moment 
{\displaystyle \operatorname {E} \left[X_{(i)}X_{(j)}\right]}

 of the order statistics 
{\displaystyle X_{(i)}}
{\displaystyle X_{(j)}}

 is given by
{\displaystyle {\begin{aligned}\operatorname {E} \left[X_{(i)}X_{(j)}\right]&=\sum _{k=0}^{j-1}{\frac {1}{(n-k)\lambda }}\operatorname {E} \left[X_{(i)}\right]+\operatorname {E} \left[X_{(i)}^{2}\right]\\&=\sum _{k=0}^{j-1}{\frac {1}{(n-k)\lambda }}\sum _{k=0}^{i-1}{\frac {1}{(n-k)\lambda }}+\sum _{k=0}^{i-1}{\frac {1}{((n-k)\lambda )^{2}}}+\left(\sum _{k=0}^{i-1}{\frac {1}{(n-k)\lambda }}\right)^{2}.\end{aligned}}}

This can be seen by invoking the law of total expectation and the memoryless property:

E
⁡

[

X

(
i
)

X

(
j
)

]

=

∫

0

∞

E
⁡

[

X

(
i
)

X

(
j
)

∣

X

(
i
)

=
x

]

f

X

(
i
)

(
x
)

d
x

=

∫

x
=
0

∞

x
E
⁡

[

X

(
j
)

∣

X

(
j
)

≥
x

]

f

X

(
i
)

(
x
)

d
x

(

since

X

(
i
)

=
x

⟹

X

(
j
)

≥
x

)

=

∫

x
=
0

∞

x

[

E
⁡

[

X

(
j
)

]

+
x

]

f

X

(
i
)

(
x
)

d
x

(

by the memoryless property
{\displaystyle {\begin{aligned}\operatorname {E} \left[X_{(i)}X_{(j)}\right]&=\int _{0}^{\infty }\operatorname {E} \left[X_{(i)}X_{(j)}\mid X_{(i)}=x\right]f_{X_{(i)}}(x)\,dx\\&=\int _{x=0}^{\infty }x\operatorname {E} \left[X_{(j)}\mid X_{(j)}\geq x\right]f_{X_{(i)}}(x)\,dx&&\left({\textrm {since}}~X_{(i)}=x\implies X_{(j)}\geq x\right)\\&=\int _{x=0}^{\infty }x\left[\operatorname {E} \left[X_{(j)}\right]+x\right]f_{X_{(i)}}(x)\,dx&&\left({\text{by the memoryless property}}\right)\\&=\sum _{k=0}^{j-1}{\frac {1}{(n-k)\lambda }}\operatorname {E} \left[X_{(i)}\right]+\operatorname {E} \left[X_{(i)}^{2}\right].\end{aligned}}}

The first equation follows from the law of total expectation.
The second equation exploits the fact that once we condition on 
{\displaystyle X_{(i)}=x}

, it must follow that 
{\displaystyle X_{(j)}\geq x}

. The third equation relies on the memoryless property to replace 
{\displaystyle \operatorname {E} \left[X_{(j)}\mid X_{(j)}\geq x\right]}

 with 
{\displaystyle \operatorname {E} \left[X_{(j)}\right]+x}

.

Sum of two independent exponential random variables
The probability distribution function (PDF) of a sum of two independent random variables is the convolution of their individual PDFs.  If 
{\displaystyle X_{1}}
{\displaystyle X_{2}}

 are independent exponential random variables with respective rate parameters 
{\displaystyle \lambda _{1}}
{\displaystyle \lambda _{2},}

 then the probability density of 
{\displaystyle Z=X_{1}+X_{2}}

 is given by
{\displaystyle {\begin{aligned}f_{Z}(z)&=\int _{-\infty }^{\infty }f_{X_{1}}(x_{1})f_{X_{2}}(z-x_{1})\,dx_{1}\\&=\int _{0}^{z}\lambda _{1}e^{-\lambda _{1}x_{1}}\lambda _{2}e^{-\lambda _{2}(z-x_{1})}\,dx_{1}\\&=\lambda _{1}\lambda _{2}e^{-\lambda _{2}z}\int _{0}^{z}e^{(\lambda _{2}-\lambda _{1})x_{1}}\,dx_{1}\\&={\begin{cases}{\dfrac {\lambda _{1}\lambda _{2}}{\lambda _{2}-\lambda _{1}}}\left(e^{-\lambda _{1}z}-e^{-\lambda _{2}z}\right)&{\text{ if }}\lambda _{1}\neq \lambda _{2}\\[4pt]\lambda ^{2}ze^{-\lambda z}&{\text{ if }}\lambda _{1}=\lambda _{2}=\lambda .\end{cases}}\end{aligned}}}

The entropy of this distribution is available in closed form: assuming 
{\displaystyle \lambda _{1}>\lambda _{2}}

 (without loss of generality), then
{\displaystyle {\begin{aligned}H(Z)&=1+\gamma +\ln \left({\frac {\lambda _{1}-\lambda _{2}}{\lambda _{1}\lambda _{2}}}\right)+\psi \left({\frac {\lambda _{1}}{\lambda _{1}-\lambda _{2}}}\right),\end{aligned}}}

where 

γ

{\displaystyle \gamma }

 is the Euler-Mascheroni constant, and 
{\displaystyle \psi (\cdot )}

 is the digamma function.[7]
In the case of equal rate parameters, the result is an Erlang distribution with shape 2 and parameter 
{\displaystyle \lambda ,}

 which in turn is a special case of gamma distribution.
The sum of n independent Exp(λ) exponential random variables is Gamma(n, λ) distributed.

Related distributions
If X ~ Laplace(μ, β−1), then |X − μ| ~ Exp(β).[8]
If X ~ U(0, 1) then −log(X) ~ Exp(1).
If X ~ Pareto(1, λ), then log(X) ~ Exp(λ).[8]
If X ~ SkewLogistic(θ), then 
{\displaystyle \log \left(1+e^{-X}\right)\sim \operatorname {Exp} (\theta )}

.
If Xi ~ U(0, 1) then 
{\displaystyle \lim _{n\to \infty }n\min \left(X_{1},\ldots ,X_{n}\right)\sim \operatorname {Exp} (1)}

The exponential distribution is a limit of a scaled beta distribution: 

lim

n
→
∞

n
Beta
{\displaystyle \lim _{n\to \infty }n\operatorname {Beta} (1,n)=\operatorname {Exp} (1).}

The exponential distribution is a special case of type 3 Pearson distribution.
The exponential distribution is the special case of a Gamma distribution with shape parameter 1.[8]
If X ~ Exp(λ) and Xi ~ Exp(λi) then:
{\displaystyle kX\sim \operatorname {Exp} \left({\frac {\lambda }{k}}\right)}

, closure under scaling by a positive factor.
1 + X ~ BenktanderWeibull(λ, 1), which reduces to a truncated exponential distribution.
keX ~ Pareto(k, λ).[8]
e−λX ~ U(0, 1).
e−X ~ Beta(λ, 1).[8]
⁠1/k⁠eX ~ PowerLaw(k, λ)

X

∼
Rayleigh
{\displaystyle {\sqrt {X}}\sim \operatorname {Rayleigh} \left({\frac {1}{\sqrt {2\lambda }}}\right)}

, the Rayleigh distribution[8]

X
∼
Weibull
{\displaystyle X\sim \operatorname {Weibull} \left({\frac {1}{\lambda }},1\right)}

, the Weibull distribution[8]

X

2

∼
Weibull
{\displaystyle X^{2}\sim \operatorname {Weibull} \left({\frac {1}{\lambda ^{2}}},{\frac {1}{2}}\right)}

[8]
μ − β log(λX) ∼ Gumbel(μ, β).

⌊
X
⌋
∼
Geometric
{\displaystyle \lfloor X\rfloor \sim \operatorname {Geometric} \left(1-e^{-\lambda }\right)}

, a geometric distribution on 0,1,2,3,...

⌈
X
⌉
∼
Geometric
{\displaystyle \lceil X\rceil \sim \operatorname {Geometric} \left(1-e^{-\lambda }\right)}

, a geometric distribution on 1,2,3,4,...
If also Y ~ Erlang(n, λ) or
{\displaystyle Y\sim \Gamma \left(n,{\frac {1}{\lambda }}\right)}

 then 

X
Y

+
1
∼
Pareto
{\displaystyle {\frac {X}{Y}}+1\sim \operatorname {Pareto} (1,n)}

If also λ ~ Gamma(k, θ) (shape, scale parametrisation) then the marginal distribution of X is Lomax(k, 1/θ), the gamma mixture
λ1X1 − λ2Y2 ~ Laplace(0, 1).
min{X1, ..., Xn} ~ Exp(λ1 + ... + λn).
If also λi = λ then:
{\displaystyle X_{1}+\cdots +X_{k}=\sum _{i}X_{i}\sim }

 Erlang(k, λ) = Gamma(k, λ) with integer shape parameter k and rate parameter λ.[9]
{\displaystyle T=(X_{1}+\cdots +X_{n})=\sum _{i=1}^{n}X_{i}}

, then 
{\displaystyle 2\lambda T\sim \chi _{2n}^{2}}

.
Xi − Xj ~ Laplace(0, λ−1).
If also Xi are independent, then:
{\displaystyle {\frac {X_{i}}{X_{i}+X_{j}}}}
{\displaystyle Z={\frac {\lambda _{i}X_{i}}{\lambda _{j}X_{j}}}}

 has probability density function 
{\displaystyle f_{Z}(z)={\frac {1}{(z+1)^{2}}}}

. This can be used to obtain a confidence interval for 
{\displaystyle {\frac {\lambda _{i}}{\lambda _{j}}}}

.
If also λ = 1:

μ
−
β
log
⁡

(

e

−
X

1
−

e

−
X

)

∼
Logistic
{\displaystyle \mu -\beta \log \left({\frac {e^{-X}}{1-e^{-X}}}\right)\sim \operatorname {Logistic} (\mu ,\beta )}

, the logistic distribution

μ
−
β
log
⁡

(

X

i

X

j

)

∼
Logistic
{\displaystyle \mu -\beta \log \left({\frac {X_{i}}{X_{j}}}\right)\sim \operatorname {Logistic} (\mu ,\beta )}

μ − σ log(X) ~ GEV(μ, σ, 0).
Further if 
{\displaystyle Y\sim \Gamma \left(\alpha ,{\frac {\beta }{\alpha }}\right)}

 then 
{\displaystyle {\sqrt {XY}}\sim \operatorname {K} (\alpha ,\beta )}

 (K-distribution)
If also λ = 1/2 then X ∼ χ22; i.e., X has a chi-squared distribution with 2 degrees of freedom. Hence: 
{\displaystyle \operatorname {Exp} (\lambda )={\frac {1}{2\lambda }}\operatorname {Exp} \left({\frac {1}{2}}\right)\sim {\frac {1}{2\lambda }}\chi _{2}^{2}\Rightarrow \sum _{i=1}^{n}\operatorname {Exp} (\lambda )\sim {\frac {1}{2\lambda }}\chi _{2n}^{2}}
{\displaystyle X\sim \operatorname {Exp} \left({\frac {1}{\lambda }}\right)}
{\displaystyle Y\mid X}

 ~ Poisson(X) then 

Y
∼
Geometric
{\displaystyle Y\sim \operatorname {Geometric} \left({\frac {1}{1+\lambda }}\right)}

     (geometric distribution)
The Hoyt distribution can be obtained from exponential distribution and arcsine distribution
The exponential distribution is a limit of the κ-exponential distribution in the 
{\displaystyle \kappa =0}

 case.
Exponential distribution is a limit of the κ-Generalized Gamma distribution in the 
{\displaystyle \alpha =1}
{\displaystyle \nu =1}

 cases:
{\displaystyle \lim _{(\alpha ,\nu )\to (0,1)}p_{\kappa }(x)=(1+\kappa \nu )(2\kappa )^{\nu }{\frac {\Gamma {\Big (}{\frac {1}{2\kappa }}+{\frac {\nu }{2}}{\Big )}}{\Gamma {\Big (}{\frac {1}{2\kappa }}-{\frac {\nu }{2}}{\Big )}}}{\frac {\alpha \lambda ^{\nu }}{\Gamma (\nu )}}x^{\alpha \nu -1}\exp _{\kappa }(-\lambda x^{\alpha })=\lambda e^{-\lambda x}}

Other related distributions:

Hyper-exponential distribution – the distribution whose density is a weighted sum of exponential densities.
Hypoexponential distribution – the distribution of a general sum of exponential random variables.[8]
exGaussian distribution – the sum of an exponential distribution and a normal distribution.
Statistical inference
Below, suppose random variable X is exponentially distributed with rate parameter λ, and 
{\displaystyle x_{1},\dotsc ,x_{n}}

 are n independent samples from X, with sample mean 
{\displaystyle {\bar {x}}}

.

Parameter estimation
The maximum likelihood estimator for λ is constructed as follows.
The likelihood function for λ, given an independent and identically distributed sample x = (x1, ..., xn) drawn from the variable, is:
{\displaystyle L(\lambda )=\prod _{i=1}^{n}\lambda \exp(-\lambda x_{i})=\lambda ^{n}\exp \left(-\lambda \sum _{i=1}^{n}x_{i}\right)=\lambda ^{n}\exp \left(-\lambda n{\overline {x}}\right),}

where:
{\displaystyle {\overline {x}}={\frac {1}{n}}\sum _{i=1}^{n}x_{i}}

is the sample mean.
The derivative of the likelihood function's logarithm is:
{\displaystyle {\frac {d}{d\lambda }}\ln L(\lambda )={\frac {d}{d\lambda }}\left(n\ln \lambda -\lambda n{\overline {x}}\right)={\frac {n}{\lambda }}-n{\overline {x}}\ {\begin{cases}>0,&0<\lambda <{\frac {1}{\overline {x}}},\\[8pt]=0,&\lambda ={\frac {1}{\overline {x}}},\\[8pt]<0,&\lambda >{\frac {1}{\overline {x}}}.\end{cases}}}

Consequently, the maximum likelihood estimate for the rate parameter is:
{\displaystyle {\widehat {\lambda }}_{\text{mle}}={\frac {1}{\overline {x}}}={\frac {n}{\sum _{i}x_{i}}}}

This is not an unbiased estimator of 
{\displaystyle \lambda ,}

 although 
{\displaystyle {\overline {x}}}

 is an unbiased[10] MLE[11] estimator of 
{\displaystyle 1/\lambda }

 and the distribution mean.
The bias of 
{\displaystyle {\widehat {\lambda }}_{\text{mle}}}

 is equal to
{\displaystyle B\equiv \operatorname {E} \left[\left({\widehat {\lambda }}_{\text{mle}}-\lambda \right)\right]={\frac {\lambda }{n-1}}}

which yields the bias-corrected maximum likelihood estimator
{\displaystyle {\widehat {\lambda }}_{\text{mle}}^{*}={\widehat {\lambda }}_{\text{mle}}-B.}

An approximate minimizer of mean squared error (see also: bias–variance tradeoff) can be found, assuming a sample size greater than two, with a correction factor to the MLE:
{\displaystyle {\widehat {\lambda }}=\left({\frac {n-2}{n}}\right)\left({\frac {1}{\bar {x}}}\right)={\frac {n-2}{\sum _{i}x_{i}}}}

This is derived from the mean and variance of the inverse-gamma distribution, 

Inv-Gamma

(
n
,
λ
)

{\textstyle {\mbox{Inv-Gamma}}(n,\lambda )}

.[12]

Fisher information
The Fisher information, denoted 
{\displaystyle {\mathcal {I}}(\lambda )}

, for an estimator of the rate parameter 

λ

{\displaystyle \lambda }

 is given as:
{\displaystyle {\mathcal {I}}(\lambda )=\operatorname {E} \left[\left.\left({\frac {\partial }{\partial \lambda }}\log f(x;\lambda )\right)^{2}\right|\lambda \right]=\int \left({\frac {\partial }{\partial \lambda }}\log f(x;\lambda )\right)^{2}f(x;\lambda )\,dx}

Plugging in the distribution and solving gives:
{\displaystyle {\mathcal {I}}(\lambda )=\int _{0}^{\infty }\left({\frac {\partial }{\partial \lambda }}\log \lambda e^{-\lambda x}\right)^{2}\lambda e^{-\lambda x}\,dx=\int _{0}^{\infty }\left({\frac {1}{\lambda }}-x\right)^{2}\lambda e^{-\lambda x}\,dx=\lambda ^{-2}.}

This determines the amount of information each independent sample of an exponential distribution carries about the unknown rate parameter 

λ

{\displaystyle \lambda }

.

Confidence intervals
An exact 100(1 − α)% confidence interval for the rate parameter of an exponential distribution is given by:[13]
{\displaystyle {\frac {2n}{{\widehat {\lambda }}_{\textrm {mle}}\chi _{{\frac {\alpha }{2}},2n}^{2}}}<{\frac {1}{\lambda }}<{\frac {2n}{{\widehat {\lambda }}_{\textrm {mle}}\chi _{1-{\frac {\alpha }{2}},2n}^{2}}}\,,}

which is also equal to
{\displaystyle {\frac {2n{\overline {x}}}{\chi _{{\frac {\alpha }{2}},2n}^{2}}}<{\frac {1}{\lambda }}<{\frac {2n{\overline {x}}}{\chi _{1-{\frac {\alpha }{2}},2n}^{2}}}\,,}

where χ2p,v is the 100(p) percentile of the  chi squared distribution with v degrees of freedom, n is the number of observations and x-bar is the sample average. A simple approximation to the exact interval endpoints can be derived using a normal approximation to the χ2p,v distribution. This approximation gives the following values for a 95% confidence interval:

λ

lower

=

λ
^

(

1
−

1.96

n

)

λ

upper

=

λ
^

(

1
+

1.96
{\displaystyle {\begin{aligned}\lambda _{\text{lower}}&={\widehat {\lambda }}\left(1-{\frac {1.96}{\sqrt {n}}}\right)\\\lambda _{\text{upper}}&={\widehat {\lambda }}\left(1+{\frac {1.96}{\sqrt {n}}}\right)\end{aligned}}}

This approximation may be acceptable for samples containing at least 15 to 20 elements.[14]

Bayesian inference with a conjugate prior
The conjugate prior for the exponential distribution is the gamma distribution (of which the exponential distribution is a special case).  The following parameterization of the gamma probability density function is useful:

Gamma
{\displaystyle \operatorname {Gamma} (\lambda ;\alpha ,\beta )={\frac {\beta ^{\alpha }}{\Gamma (\alpha )}}\lambda ^{\alpha -1}\exp(-\lambda \beta ).}

The posterior distribution p can then be expressed in terms of the likelihood function defined above and a gamma prior:
{\displaystyle {\begin{aligned}p(\lambda )&\propto L(\lambda )\Gamma (\lambda ;\alpha ,\beta )\\&=\lambda ^{n}\exp \left(-\lambda n{\overline {x}}\right){\frac {\beta ^{\alpha }}{\Gamma (\alpha )}}\lambda ^{\alpha -1}\exp(-\lambda \beta )\\&\propto \lambda ^{(\alpha +n)-1}\exp(-\lambda \left(\beta +n{\overline {x}}\right)).\end{aligned}}}

Now the posterior density p has been specified up to a missing normalizing constant.  Since it has the form of a gamma pdf, this can easily be filled in, and one obtains:

p
(
λ
)
=
Gamma
{\displaystyle p(\lambda )=\operatorname {Gamma} (\lambda ;\alpha +n,\beta +n{\overline {x}}).}

Here the hyperparameter α can be interpreted as the number of prior observations, and β as the sum of the prior observations.
The posterior mean here is:
{\displaystyle {\frac {\alpha +n}{\beta +n{\overline {x}}}}.}

Bayesian inference with a calibrating prior
The exponential distribution is one of a number of statistical distributions with group structure. As a result of the group structure, the exponential has an associated Haar measure, which is 
{\displaystyle 1/\lambda .}

The use of the Haar measure as the prior (known as the Haar prior) in a Bayesian prediction gives probabilities that are perfectly calibrated, for any underlying true parameter values.[15][16][17] Perfectly calibrated probabilities have the property that the predicted probabilities match the frequency of out-of-sample events exactly. For the exponential, there is an exact expression for Bayesian predictions generated using the Haar prior, given by
{\displaystyle p_{\rm {Haar-prior}}(x_{n+1}\mid x_{1},\ldots ,x_{n})={\frac {n^{n+1}\left({\overline {x}}\right)^{n}}{\left(n{\overline {x}}+x_{n+1}\right)^{n+1}}}.}

This is an example of calibrating prior prediction, in which the prior is chosen to improve calibration (and, in this case, to make the calibration perfect). Calibrating prior prediction for the exponential using the Haar prior is implemented in the R software package fitdistcp.[1]
The same prediction can be derived from a number of other perspectives, as discussed in the prediction section below.

Occurrence and applications
Occurrence of events
The exponential distribution occurs naturally when describing the lengths of the inter-arrival times in a homogeneous Poisson process.
The exponential distribution may be viewed as a continuous counterpart of the geometric distribution, which describes the number of Bernoulli trials necessary for a discrete process to change state. In contrast, the exponential distribution describes the time for a continuous process to change state.
In real-world scenarios, the assumption of a constant rate (or probability per unit time) is rarely satisfied. For example, the rate of incoming phone calls differs according to the time of day. But if we focus on a time interval during which the rate is roughly constant, such as from 2 to 4 p.m. during work days, the exponential distribution can be used as a good approximate model for the time until the next phone call arrives. Similar caveats apply to the following examples which yield approximately exponentially distributed variables:

The time until a radioactive particle decays, or the time between clicks of a Geiger counter
The time between receiving one telephone call and the next
The time until default (on payment to company debt holders) in reduced-form credit risk modeling
Exponential variables can also be used to model situations where certain events occur with a constant probability per unit length, such as the distance between mutations on a DNA strand, or between roadkills on a given road.
In queuing theory, the service times of agents in a system (e.g. how long it takes for a bank teller etc. to serve a customer) are often modeled as exponentially distributed variables.  (The arrival of customers for instance is also modeled by the Poisson distribution if the arrivals are independent and distributed identically.)  The length of a process that can be thought of as a sequence of several independent tasks follows the Erlang distribution (which is the distribution of the sum of several independent exponentially distributed variables).
Reliability theory and reliability engineering also make extensive use of the exponential distribution. Because of the memoryless property of this distribution, it is well-suited to model the constant hazard rate portion of the bathtub curve used in reliability theory. It is also very convenient because it is so easy to add failure rates in a reliability model. The exponential distribution is however not appropriate to model the overall lifetime of organisms or technical devices, because the "failure rates" here are not constant: more failures occur for very young and for very old systems.

Fitted cumulative exponential distribution to annually maximum 1-day rainfalls
In physics, if you observe a gas at a fixed temperature and pressure in a uniform gravitational field, the heights of the various molecules also follow an approximate exponential distribution, known as the Barometric formula. This is a consequence of the entropy property mentioned below.
In hydrology, the exponential distribution is used to analyze extreme values of such variables as monthly and annual maximum values of daily rainfall and river discharge volumes.[18]

The blue picture illustrates an example of fitting the exponential distribution to ranked annually maximum one-day rainfalls showing also the 90% confidence belt based on the binomial distribution. The rainfall data are represented by plotting positions as part of the cumulative frequency analysis.
In operating-rooms management, the distribution of surgery duration for a category of surgeries with no typical work-content (like in an emergency room, encompassing all types of surgeries).

Prediction
Having observed a sample of n data points from an unknown exponential distribution a common task is to use these samples to make predictions about future data from the same source. A common predictive distribution over future samples is the so-called plug-in distribution, formed by plugging a suitable estimate for the rate parameter λ into the exponential density function. A common choice of estimate is the one provided by the principle of maximum likelihood, and using this yields the predictive density over a future sample xn+1, conditioned on the observed samples x = (x1, ..., xn) given by
{\displaystyle p_{\rm {ML}}(x_{n+1}\mid x_{1},\ldots ,x_{n})=\left({\frac {1}{\overline {x}}}\right)\exp \left(-{\frac {x_{n+1}}{\overline {x}}}\right).}

The Bayesian approach provides a predictive distribution which takes into account the uncertainty of the estimated parameter, although this may depend crucially on the choice of prior.
A predictive distribution free of the issues of choosing priors that arise under the subjective Bayesian approach is
{\displaystyle p_{\rm {CNML}}(x_{n+1}\mid x_{1},\ldots ,x_{n})={\frac {n^{n+1}\left({\overline {x}}\right)^{n}}{\left(n{\overline {x}}+x_{n+1}\right)^{n+1}}},}

which can be considered as

a frequentist confidence distribution, obtained from the distribution of the pivotal quantity 
{\displaystyle {x_{n+1}}/{\overline {x}}}

;[19]
a profile predictive likelihood, obtained by eliminating the parameter λ from the joint likelihood of xn+1 and λ by maximization;[20]
an objective Bayesian predictive posterior distribution, obtained using the non-informative Jeffreys prior 1/λ, which is equal to the right Haar prior in this case. Predictions generated using the right Haar prior are guaranteed to give perfectly calibrated probabilities.[21][22]
the Conditional Normalized Maximum Likelihood (CNML) predictive distribution, from information theoretic considerations.[23]
The accuracy of a predictive distribution may be measured using the distance or divergence between the true exponential distribution with rate parameter, λ0, and the predictive distribution based on the sample x. The Kullback–Leibler divergence is a commonly used, parameterisation free measure of the difference between two distributions. Letting Δ(λ0||p) denote the Kullback–Leibler divergence between an exponential with rate parameter λ0 and a predictive distribution p it can be shown that
{\displaystyle {\begin{aligned}\operatorname {E} _{\lambda _{0}}\left[\Delta (\lambda _{0}\parallel p_{\rm {ML}})\right]&=\psi (n)+{\frac {1}{n-1}}-\log(n)\\\operatorname {E} _{\lambda _{0}}\left[\Delta (\lambda _{0}\parallel p_{\rm {CNML}})\right]&=\psi (n)+{\frac {1}{n}}-\log(n)\end{aligned}}}

where the expectation is taken with respect to the exponential distribution with rate parameter λ0 ∈ (0, ∞), and ψ( · ) is the digamma function. It is clear that the CNML predictive distribution is strictly superior to the maximum likelihood plug-in distribution in terms of average Kullback–Leibler divergence for all sample sizes n > 0.

Random variate generation
Further information: Non-uniform random variate generation
A conceptually very simple method for generating exponential variates is based on inverse transform sampling: Given a random variate U drawn from the uniform distribution on the unit interval (0, 1), the variate
{\displaystyle T=F^{-1}(U)}

has an exponential distribution, where F−1 is the quantile function, defined by
{\displaystyle F^{-1}(p)={\frac {-\ln(1-p)}{\lambda }}.}

Moreover, if U is uniform on (0, 1), then so is 1 − U.  This means one can generate exponential variates as follows:
{\displaystyle T={\frac {-\ln(U)}{\lambda }}.}

Other methods for generating exponential variates are discussed by Knuth[24] and Devroye.[25]
A fast method for generating a set of ready-ordered exponential variates without using a sorting routine is also available.[25]

See also
Dead time – an application of exponential distribution to particle detector analysis.
Laplace distribution, or the "double exponential distribution".
Relationships among probability distributions
Marshall–Olkin exponential distribution
References

^ "7.2: Exponential Distribution". Statistics LibreTexts. 2021-07-15. Retrieved 2024-10-11.

^ "Exponential distribution | mathematics | Britannica". www.britannica.com. Retrieved 2024-10-11.

^ a b Weisstein, Eric W. "Exponential Distribution". mathworld.wolfram.com. Retrieved 2024-10-11.

^ a b Norton, Matthew; Khokhlov, Valentyn; Uryasev, Stan (2019). "Calculating CVaR and bPOE for common probability distributions with application to portfolio optimization and density estimation" (PDF). Annals of Operations Research. 299 (1–2). Springer: 1281–1315. arXiv:1811.11301. doi:10.1007/s10479-019-03373-1. Archived from the original (PDF) on 2023-03-31. Retrieved 2023-02-27.

^ Park, Sung Y.; Bera, Anil K. (2009). "Maximum entropy autoregressive conditional heteroskedasticity model" (PDF). Journal of Econometrics. 150 (2). Elsevier: 219–230. doi:10.1016/j.jeconom.2008.12.014. Archived from the original (PDF) on 2016-03-07. Retrieved 2011-06-02.

^ Michael, Lugo. "The expectation of the maximum of exponentials" (PDF). Archived from the original (PDF) on 20 December 2016. Retrieved 13 December 2016.

^ Eckford, Andrew W.; Thomas, Peter J. (2016). "Entropy of the sum of two independent, non-identically-distributed exponential random variables". arXiv:1609.02911 [cs.IT].

^ a b c d e f g h i Leemis, Lawrence M.; McQuestion, Jacquelyn T. (February 2008). "Univariate Distribution Relationships" (PDF). The American Statistician. 62 (1): 45-53. doi:10.1198/000313008X270448.

^ Ibe, Oliver C. (2014). Fundamentals of Applied Probability and Random Processes (2nd ed.). Academic Press. p. 128. ISBN 9780128010358.

^ Richard Arnold Johnson; Dean W. Wichern (2007). Applied Multivariate Statistical Analysis. Pearson Prentice Hall. ISBN 978-0-13-187715-3. Retrieved 10 August 2012.

^ NIST/SEMATECH e-Handbook of Statistical Methods

^ Elfessi, Abdulaziz; Reineke, David M. (2001). "A Bayesian Look at Classical Estimation: The Exponential Distribution". Journal of Statistics Education. 9 (1). doi:10.1080/10691898.2001.11910648.

^ Ross, Sheldon M. (2009). Introduction to probability and statistics for engineers and scientists (4th ed.). Associated Press. p. 267. ISBN 978-0-12-370483-2.

^ Guerriero, V. (2012). "Power Law Distribution: Method of Multi-scale Inferential Statistics". Journal of Modern Mathematics Frontier. 1: 21–28.

^ Severini, T. A. (2002-12-01). "On an exact probability matching property of right-invariant priors". Biometrika. 89 (4): 952–957. doi:10.1093/biomet/89.4.952. ISSN 0006-3444.

^ Gerrard, R.; Tsanakas, A. (2011). "Failure Probability Under Parameter Uncertainty". Risk Analysis. 31 (5): 727–744. Bibcode:2011RiskA..31..727G. doi:10.1111/j.1539-6924.2010.01549.x. ISSN 1539-6924. PMID 21175720.

^ Jewson, Stephen; Sweeting, Trevor; Jewson, Lynne (2025-02-20). "Reducing reliability bias in assessments of extreme weather risk using calibrating priors". Advances in Statistical Climatology, Meteorology and Oceanography. 11 (1): 1–22. Bibcode:2025ASCMO..11....1J. doi:10.5194/ascmo-11-1-2025. ISSN 2364-3579.

^ Ritzema, H.P., ed. (1994). Frequency and Regression Analysis. Chapter 6 in: Drainage Principles and Applications, Publication 16, International Institute for Land Reclamation and Improvement (ILRI), Wageningen, The Netherlands. pp. 175–224. ISBN 90-70754-33-9.

^ Lawless, J. F.; Fredette, M. (2005). "Frequentist predictions intervals and predictive distributions". Biometrika. 92 (3): 529–542. doi:10.1093/biomet/92.3.529.

^ Bjornstad, J.F. (1990). "Predictive Likelihood: A Review". Statist. Sci. 5 (2): 242–254. doi:10.1214/ss/1177012175.

^ Severini, Thomas A.; Mukerjee, Rahul; Ghosh, Malay (2002-12-01). "On an exact probability matching property of right-invariant priors". Biometrika. 89 (4): 952–957. doi:10.1093/biomet/89.4.952. ISSN 0006-3444.

^ Jewson, Stephen; Sweeting, Trevor; Jewson, Lynne (2025-02-20). "Reducing reliability bias in assessments of extreme weather risk using calibrating priors". Advances in Statistical Climatology, Meteorology and Oceanography. 11 (1): 1–22. Bibcode:2025ASCMO..11....1J. doi:10.5194/ascmo-11-1-2025. ISSN 2364-3579.

^ D. F. Schmidt and E. Makalic, "Universal Models for the Exponential Distribution", IEEE Transactions on Information Theory, Volume 55, Number 7, pp. 3087–3090, 2009 doi:10.1109/TIT.2009.2018331

^ Donald E. Knuth (1998). The Art of Computer Programming, volume 2: Seminumerical Algorithms, 3rd edn. Boston: Addison–Wesley. ISBN 0-201-89684-2. See section 3.4.1, p. 133.

^ a b Luc Devroye (1986). Non-Uniform Random Variate Generation. New York: Springer-Verlag. ISBN 0-387-96305-7. See chapter IX, section 2, pp. 392–401.

External links

The Wikibook Probability has a page on the topic of: Exponential distribution

"Exponential distribution", Encyclopedia of Mathematics, EMS Press, 2001 [1994]
Online calculator of Exponential Distribution
vteProbability distributions (list)Discrete univariatewith finite support
Benford
Bernoulli
Beta-binomial
Binomial
Categorical
Hypergeometric
Negative
Poisson binomial
Rademacher
Soliton
Discrete uniform
Zipf
Zipf–Mandelbrot
with infinite support
Beta negative binomial
Borel
Conway–Maxwell–Poisson
Discrete phase-type
Delaporte
Extended negative binomial
Flory–Schulz
Gauss–Kuzmin
Geometric
Logarithmic
Mixed Poisson
Negative binomial
Panjer
Parabolic fractal
Poisson
Skellam
Yule–Simon
Zeta
Continuous univariatesupported on a bounded interval
Arcsine
ARGUS
Balding–Nichols
Bates
Beta
Generalized
Beta rectangular
Continuous Bernoulli
Irwin–Hall
Kumaraswamy
Logit-normal
Noncentral beta
PERT
Power function
Raised cosine
Reciprocal
Triangular
U-quadratic
Uniform
Wigner semicircle
supported on a semi-infinite interval
Benini
Benktander 1st kind
Benktander 2nd kind
Beta prime
Burr
Chi
Chi-squared
Noncentral
Inverse
Scaled
Dagum
Davis
Erlang
Hyper
Exponential
Hyperexponential
Hypoexponential
Logarithmic
F
Noncentral
Folded normal
Fréchet
Gamma
Generalized
Inverse
gamma/Gompertz
Gompertz
Shifted
Half-logistic
Half-normal
Hotelling's T-squared
Hartman–Watson
Inverse Gaussian
Generalized
Kolmogorov
Lévy
Log-Cauchy
Log-Laplace
Log-logistic
Log-normal
Log-t
Lomax
Matrix-exponential
Maxwell–Boltzmann
Maxwell–Jüttner
Mittag-Leffler
Nakagami
Pareto
Phase-type
Poly-Weibull
Rayleigh
Relativistic Breit–Wigner
Rice
Truncated normal
type-2 Gumbel
Weibull
Discrete
Wilks's lambda
supported on the whole real line
Cauchy
Exponential power
Fisher's z
Kaniadakis κ-Gaussian
Gaussian q
Generalized hyperbolic
Generalized logistic (logistic-beta)
Generalized normal
Geometric stable
Gumbel
Holtsmark
Hyperbolic secant
Johnson's SU
Landau
Laplace
Asymmetric
Logistic
Noncentral t
Normal (Gaussian)
Normal-inverse Gaussian
Skew normal
Slash
Stable
Student's t
Tracy–Widom
Variance-gamma
Voigt
with support whose type varies
Generalized chi-squared
Generalized extreme value
Generalized Pareto
Marchenko–Pastur
Kaniadakis κ-exponential
Kaniadakis κ-Gamma
Kaniadakis κ-Weibull
Kaniadakis κ-Logistic
Kaniadakis κ-Erlang
q-exponential
q-Gaussian
q-Weibull
Shifted log-logistic
Tukey lambda
Mixed univariatecontinuous-discrete
Rectified Gaussian
Multivariate (joint)
Discrete: 
Ewens
Multinomial
Dirichlet
Negative
Continuous: 
Dirichlet
Generalized
Multivariate Laplace
Multivariate normal
Multivariate stable
Multivariate t
Normal-gamma
Inverse
Matrix-valued: 
LKJ
Matrix beta
Matrix normal
Matrix t
Matrix gamma
Inverse
Wishart
Normal
Inverse
Normal-inverse
Complex
Uniform distribution on a Stiefel manifold
Directional
Univariate (circular) directional
Circular uniform
Univariate von Mises
Wrapped normal
Wrapped Cauchy
Wrapped exponential
Wrapped asymmetric Laplace
Wrapped Lévy
Bivariate (spherical)
Kent
Bivariate (toroidal)
Bivariate von Mises
Multivariate
von Mises–Fisher
Bingham
Degenerate and singular
Degenerate
Dirac delta function
Singular
Cantor
Families
Circular
Compound Poisson
Elliptical
Exponential
Natural exponential
Location–scale
Maximum entropy
Mixture
Pearson
Tweedie
Wrapped

 Category
 Commons

Authority control databases GND ${\displaystyle f(x;\lambda )={\begin{cases}\lambda e^{-\lambda x}&x\geq 0,\\0&x<0.\end{cases}}}$ ${\displaystyle F(x;\lambda )={\begin{cases}1-e^{-\lambda x}&x\geq 0,\\0&x<0.\end{cases}}}$ ${\displaystyle f(x;\beta )={\begin{cases}{\frac {1}{\beta }}e^{-x/\beta }&x\geq 0,\\0&x<0.\end{cases}}\qquad \qquad F(x;\beta )={\begin{cases}1-e^{-x/\beta }&x\geq 0,\\0&x<0.\end{cases}}}$ ${\displaystyle \operatorname {E} [X]={\frac {1}{\lambda }}.}$ ${\displaystyle \operatorname {Var} [X]={\frac {1}{\lambda ^{2}}},}$ ${\displaystyle n\in \mathbb {N} }$ ${\displaystyle \operatorname {E} \left[X^{n}\right]={\frac {n!}{\lambda ^{n}}}.}$ ${\displaystyle n\in \mathbb {N} }$ ${\displaystyle \mu _{n}={\frac {!n}{\lambda ^{n}}}={\frac {n!}{\lambda ^{n}}}\sum _{k=0}^{n}{\frac {(-1)^{k}}{k!}}.}$ ${\displaystyle \operatorname {m} [X]={\frac {\ln(2)}{\lambda }}<\operatorname {E} [X],}$ ${\displaystyle \left|\operatorname {E} \left[X\right]-\operatorname {m} \left[X\right]\right|={\frac {1-\ln(2)}{\lambda }}<{\frac {1}{\lambda }}=\operatorname {\sigma } [X],}$ ${\displaystyle \Pr \left(T>s+t\mid T>s\right)=\Pr(T>t),\qquad \forall s,t\geq 0.}$ ${\displaystyle {\begin{aligned}\Pr \left(T>s+t\mid T>s\right)&={\frac {\Pr \left(T>s+t\cap T>s\right)}{\Pr \left(T>s\right)}}\\[4pt]&={\frac {\Pr \left(T>s+t\right)}{\Pr \left(T>s\right)}}\\[4pt]&={\frac {e^{-\lambda (s+t)}}{e^{-\lambda s}}}\\[4pt]&=e^{-\lambda t}\\[4pt]&=\Pr(T>t).\end{aligned}}}$ ${\displaystyle F^{-1}(p;\lambda )={\frac {-\ln(1-p)}{\lambda }},\qquad 0\leq p<1}$ ${\displaystyle {\begin{aligned}{\bar {q}}_{\alpha }(X)&={\frac {1}{1-\alpha }}\int _{\alpha }^{1}q_{p}(X)dp\\&={\frac {1}{(1-\alpha )}}\int _{\alpha }^{1}{\frac {-\ln(1-p)}{\lambda }}dp\\&={\frac {-1}{\lambda (1-\alpha )}}\int _{1-\alpha }^{0}-\ln(y)dy\\&={\frac {-1}{\lambda (1-\alpha )}}\int _{0}^{1-\alpha }\ln(y)dy\\&={\frac {-1}{\lambda (1-\alpha )}}[(1-\alpha )\ln(1-\alpha )-(1-\alpha )]\\&={\frac {-\ln(1-\alpha )+1}{\lambda }}\\\end{aligned}}}$ ${\displaystyle x}$ ${\displaystyle {\begin{aligned}{\bar {p}}_{x}(X)&=\{1-\alpha |{\bar {q}}_{\alpha }(X)=x\}\\&=\{1-\alpha |{\frac {-\ln(1-\alpha )+1}{\lambda }}=x\}\\&=\{1-\alpha |\ln(1-\alpha )=1-\lambda x\}\\&=\{1-\alpha |e^{\ln(1-\alpha )}=e^{1-\lambda x}\}=\{1-\alpha |1-\alpha =e^{1-\lambda x}\}=e^{1-\lambda x}\end{aligned}}}$ ${\displaystyle e^{\lambda }}$ ${\displaystyle e^{\lambda _{0}}}$ ${\displaystyle {\begin{aligned}\Delta (\lambda _{0}\parallel \lambda )&=\mathbb {E} _{\lambda _{0}}\left(\log {\frac {p_{\lambda _{0}}(x)}{p_{\lambda }(x)}}\right)\\&=\mathbb {E} _{\lambda _{0}}\left(\log {\frac {\lambda _{0}e^{\lambda _{0}x}}{\lambda e^{\lambda x}}}\right)\\&=\log(\lambda _{0})-\log(\lambda )-(\lambda _{0}-\lambda )E_{\lambda _{0}}(x)\\&=\log(\lambda _{0})-\log(\lambda )+{\frac {\lambda }{\lambda _{0}}}-1.\end{aligned}}}$ ${\displaystyle \min \left\{X_{1},\dotsc ,X_{n}\right\}}$ ${\displaystyle \lambda =\lambda _{1}+\dotsb +\lambda _{n}.}$ ${\displaystyle {\begin{aligned}&\Pr \left(\min\{X_{1},\dotsc ,X_{n}\}>x\right)\\={}&\Pr \left(X_{1}>x,\dotsc ,X_{n}>x\right)\\={}&\prod _{i=1}^{n}\Pr \left(X_{i}>x\right)\\={}&\prod _{i=1}^{n}\exp \left(-x\lambda _{i}\right)=\exp \left(-x\sum _{i=1}^{n}\lambda _{i}\right).\end{aligned}}}$ ${\displaystyle \Pr \left(X_{k}=\min\{X_{1},\dotsc ,X_{n}\}\right)={\frac {\lambda _{k}}{\lambda _{1}+\dotsb +\lambda _{n}}}.}$ ${\displaystyle I=\operatorname {argmin} _{i\in \{1,\dotsb ,n\}}\{X_{1},\dotsc ,X_{n}\}}$ ${\displaystyle {\begin{aligned}\Pr(I=k)&=\int _{0}^{\infty }\Pr(X_{k}=x)\Pr(\forall _{i\neq k}X_{i}>x)\,dx\\&=\int _{0}^{\infty }\lambda _{k}e^{-\lambda _{k}x}\left(\prod _{i=1,i\neq k}^{n}e^{-\lambda _{i}x}\right)dx\\&=\lambda _{k}\int _{0}^{\infty }e^{-\left(\lambda _{1}+\dotsb +\lambda _{n}\right)x}dx\\&={\frac {\lambda _{k}}{\lambda _{1}+\dotsb +\lambda _{n}}}.\end{aligned}}}$ ${\displaystyle \max\{X_{1},\dotsc ,X_{n}\}}$ ${\displaystyle X_{1},\dotsc ,X_{n}}$ ${\displaystyle n}$ ${\displaystyle X_{(1)},\dotsc ,X_{(n)}}$ ${\displaystyle i<j}$ ${\displaystyle \operatorname {E} \left[X_{(i)}X_{(j)}\right]}$ ${\displaystyle X_{(i)}}$ ${\displaystyle X_{(j)}}$ ${\displaystyle {\begin{aligned}\operatorname {E} \left[X_{(i)}X_{(j)}\right]&=\sum _{k=0}^{j-1}{\frac {1}{(n-k)\lambda }}\operatorname {E} \left[X_{(i)}\right]+\operatorname {E} \left[X_{(i)}^{2}\right]\\&=\sum _{k=0}^{j-1}{\frac {1}{(n-k)\lambda }}\sum _{k=0}^{i-1}{\frac {1}{(n-k)\lambda }}+\sum _{k=0}^{i-1}{\frac {1}{((n-k)\lambda )^{2}}}+\left(\sum _{k=0}^{i-1}{\frac {1}{(n-k)\lambda }}\right)^{2}.\end{aligned}}}$ ${\displaystyle {\begin{aligned}\operatorname {E} \left[X_{(i)}X_{(j)}\right]&=\int _{0}^{\infty }\operatorname {E} \left[X_{(i)}X_{(j)}\mid X_{(i)}=x\right]f_{X_{(i)}}(x)\,dx\\&=\int _{x=0}^{\infty }x\operatorname {E} \left[X_{(j)}\mid X_{(j)}\geq x\right]f_{X_{(i)}}(x)\,dx&&\left({\textrm {since}}~X_{(i)}=x\implies X_{(j)}\geq x\right)\\&=\int _{x=0}^{\infty }x\left[\operatorname {E} \left[X_{(j)}\right]+x\right]f_{X_{(i)}}(x)\,dx&&\left({\text{by the memoryless property}}\right)\\&=\sum _{k=0}^{j-1}{\frac {1}{(n-k)\lambda }}\operatorname {E} \left[X_{(i)}\right]+\operatorname {E} \left[X_{(i)}^{2}\right].\end{aligned}}}$ ${\displaystyle X_{(i)}=x}$ ${\displaystyle X_{(j)}\geq x}$ ${\displaystyle \operatorname {E} \left[X_{(j)}\mid X_{(j)}\geq x\right]}$ ${\displaystyle \operatorname {E} \left[X_{(j)}\right]+x}$ ${\displaystyle X_{1}}$ ${\displaystyle X_{2}}$ ${\displaystyle \lambda _{1}}$ ${\displaystyle \lambda _{2},}$ ${\displaystyle Z=X_{1}+X_{2}}$ ${\displaystyle {\begin{aligned}f_{Z}(z)&=\int _{-\infty }^{\infty }f_{X_{1}}(x_{1})f_{X_{2}}(z-x_{1})\,dx_{1}\\&=\int _{0}^{z}\lambda _{1}e^{-\lambda _{1}x_{1}}\lambda _{2}e^{-\lambda _{2}(z-x_{1})}\,dx_{1}\\&=\lambda _{1}\lambda _{2}e^{-\lambda _{2}z}\int _{0}^{z}e^{(\lambda _{2}-\lambda _{1})x_{1}}\,dx_{1}\\&={\begin{cases}{\dfrac {\lambda _{1}\lambda _{2}}{\lambda _{2}-\lambda _{1}}}\left(e^{-\lambda _{1}z}-e^{-\lambda _{2}z}\right)&{\text{ if }}\lambda _{1}\neq \lambda _{2}\\[4pt]\lambda ^{2}ze^{-\lambda z}&{\text{ if }}\lambda _{1}=\lambda _{2}=\lambda .\end{cases}}\end{aligned}}}$ ${\displaystyle \lambda _{1}>\lambda _{2}}$ ${\displaystyle {\begin{aligned}H(Z)&=1+\gamma +\ln \left({\frac {\lambda _{1}-\lambda _{2}}{\lambda _{1}\lambda _{2}}}\right)+\psi \left({\frac {\lambda _{1}}{\lambda _{1}-\lambda _{2}}}\right),\end{aligned}}}$ ${\displaystyle \gamma }$ ${\displaystyle \psi (\cdot )}$ ${\displaystyle \lambda ,}$ ${\displaystyle \log \left(1+e^{-X}\right)\sim \operatorname {Exp} (\theta )}$ ${\displaystyle \lim _{n\to \infty }n\min \left(X_{1},\ldots ,X_{n}\right)\sim \operatorname {Exp} (1)}$ ${\displaystyle \lim _{n\to \infty }n\operatorname {Beta} (1,n)=\operatorname {Exp} (1).}$ ${\displaystyle kX\sim \operatorname {Exp} \left({\frac {\lambda }{k}}\right)}$ ${\displaystyle {\sqrt {X}}\sim \operatorname {Rayleigh} \left({\frac {1}{\sqrt {2\lambda }}}\right)}$ ${\displaystyle X\sim \operatorname {Weibull} \left({\frac {1}{\lambda }},1\right)}$ ${\displaystyle X^{2}\sim \operatorname {Weibull} \left({\frac {1}{\lambda ^{2}}},{\frac {1}{2}}\right)}$ ${\displaystyle \lfloor X\rfloor \sim \operatorname {Geometric} \left(1-e^{-\lambda }\right)}$ ${\displaystyle \lceil X\rceil \sim \operatorname {Geometric} \left(1-e^{-\lambda }\right)}$ ${\displaystyle Y\sim \Gamma \left(n,{\frac {1}{\lambda }}\right)}$ ${\displaystyle {\frac {X}{Y}}+1\sim \operatorname {Pareto} (1,n)}$ ${\displaystyle X_{1}+\cdots +X_{k}=\sum _{i}X_{i}\sim }$ ${\displaystyle T=(X_{1}+\cdots +X_{n})=\sum _{i=1}^{n}X_{i}}$ ${\displaystyle 2\lambda T\sim \chi _{2n}^{2}}$ ${\displaystyle {\frac {X_{i}}{X_{i}+X_{j}}}}$ ${\displaystyle Z={\frac {\lambda _{i}X_{i}}{\lambda _{j}X_{j}}}}$ ${\displaystyle f_{Z}(z)={\frac {1}{(z+1)^{2}}}}$ ${\displaystyle {\frac {\lambda _{i}}{\lambda _{j}}}}$ ${\displaystyle \mu -\beta \log \left({\frac {e^{-X}}{1-e^{-X}}}\right)\sim \operatorname {Logistic} (\mu ,\beta )}$ ${\displaystyle \mu -\beta \log \left({\frac {X_{i}}{X_{j}}}\right)\sim \operatorname {Logistic} (\mu ,\beta )}$ ${\displaystyle Y\sim \Gamma \left(\alpha ,{\frac {\beta }{\alpha }}\right)}$ ${\displaystyle {\sqrt {XY}}\sim \operatorname {K} (\alpha ,\beta )}$ ${\displaystyle \operatorname {Exp} (\lambda )={\frac {1}{2\lambda }}\operatorname {Exp} \left({\frac {1}{2}}\right)\sim {\frac {1}{2\lambda }}\chi _{2}^{2}\Rightarrow \sum _{i=1}^{n}\operatorname {Exp} (\lambda )\sim {\frac {1}{2\lambda }}\chi _{2n}^{2}}$ ${\displaystyle X\sim \operatorname {Exp} \left({\frac {1}{\lambda }}\right)}$ ${\displaystyle Y\mid X}$ ${\displaystyle Y\sim \operatorname {Geometric} \left({\frac {1}{1+\lambda }}\right)}$ ${\displaystyle \kappa =0}$ ${\displaystyle \alpha =1}$ ${\displaystyle \nu =1}$ ${\displaystyle \lim _{(\alpha ,\nu )\to (0,1)}p_{\kappa }(x)=(1+\kappa \nu )(2\kappa )^{\nu }{\frac {\Gamma {\Big (}{\frac {1}{2\kappa }}+{\frac {\nu }{2}}{\Big )}}{\Gamma {\Big (}{\frac {1}{2\kappa }}-{\frac {\nu }{2}}{\Big )}}}{\frac {\alpha \lambda ^{\nu }}{\Gamma (\nu )}}x^{\alpha \nu -1}\exp _{\kappa }(-\lambda x^{\alpha })=\lambda e^{-\lambda x}}$ ${\displaystyle x_{1},\dotsc ,x_{n}}$ ${\displaystyle {\bar {x}}}$ ${\displaystyle L(\lambda )=\prod _{i=1}^{n}\lambda \exp(-\lambda x_{i})=\lambda ^{n}\exp \left(-\lambda \sum _{i=1}^{n}x_{i}\right)=\lambda ^{n}\exp \left(-\lambda n{\overline {x}}\right),}$ ${\displaystyle {\overline {x}}={\frac {1}{n}}\sum _{i=1}^{n}x_{i}}$ ${\displaystyle {\frac {d}{d\lambda }}\ln L(\lambda )={\frac {d}{d\lambda }}\left(n\ln \lambda -\lambda n{\overline {x}}\right)={\frac {n}{\lambda }}-n{\overline {x}}\ {\begin{cases}>0,&0<\lambda <{\frac {1}{\overline {x}}},\\[8pt]=0,&\lambda ={\frac {1}{\overline {x}}},\\[8pt]<0,&\lambda >{\frac {1}{\overline {x}}}.\end{cases}}}$ ${\displaystyle {\widehat {\lambda }}_{\text{mle}}={\frac {1}{\overline {x}}}={\frac {n}{\sum _{i}x_{i}}}}$ ${\displaystyle \lambda ,}$ ${\displaystyle {\overline {x}}}$ ${\displaystyle 1/\lambda }$ ${\displaystyle {\widehat {\lambda }}_{\text{mle}}}$ ${\displaystyle B\equiv \operatorname {E} \left[\left({\widehat {\lambda }}_{\text{mle}}-\lambda \right)\right]={\frac {\lambda }{n-1}}}$ ${\displaystyle {\widehat {\lambda }}_{\text{mle}}^{*}={\widehat {\lambda }}_{\text{mle}}-B.}$ ${\displaystyle {\widehat {\lambda }}=\left({\frac {n-2}{n}}\right)\left({\frac {1}{\bar {x}}}\right)={\frac {n-2}{\sum _{i}x_{i}}}}$ ${\textstyle {\mbox{Inv-Gamma}}(n,\lambda )}$ ${\displaystyle {\mathcal {I}}(\lambda )}$ ${\displaystyle \lambda }$ ${\displaystyle {\mathcal {I}}(\lambda )=\operatorname {E} \left[\left.\left({\frac {\partial }{\partial \lambda }}\log f(x;\lambda )\right)^{2}\right|\lambda \right]=\int \left({\frac {\partial }{\partial \lambda }}\log f(x;\lambda )\right)^{2}f(x;\lambda )\,dx}$ ${\displaystyle {\mathcal {I}}(\lambda )=\int _{0}^{\infty }\left({\frac {\partial }{\partial \lambda }}\log \lambda e^{-\lambda x}\right)^{2}\lambda e^{-\lambda x}\,dx=\int _{0}^{\infty }\left({\frac {1}{\lambda }}-x\right)^{2}\lambda e^{-\lambda x}\,dx=\lambda ^{-2}.}$ ${\displaystyle \lambda }$ ${\displaystyle {\frac {2n}{{\widehat {\lambda }}_{\textrm {mle}}\chi _{{\frac {\alpha }{2}},2n}^{2}}}<{\frac {1}{\lambda }}<{\frac {2n}{{\widehat {\lambda }}_{\textrm {mle}}\chi _{1-{\frac {\alpha }{2}},2n}^{2}}}\,,}$ ${\displaystyle {\frac {2n{\overline {x}}}{\chi _{{\frac {\alpha }{2}},2n}^{2}}}<{\frac {1}{\lambda }}<{\frac {2n{\overline {x}}}{\chi _{1-{\frac {\alpha }{2}},2n}^{2}}}\,,}$ ${\displaystyle {\begin{aligned}\lambda _{\text{lower}}&={\widehat {\lambda }}\left(1-{\frac {1.96}{\sqrt {n}}}\right)\\\lambda _{\text{upper}}&={\widehat {\lambda }}\left(1+{\frac {1.96}{\sqrt {n}}}\right)\end{aligned}}}$ ${\displaystyle \operatorname {Gamma} (\lambda ;\alpha ,\beta )={\frac {\beta ^{\alpha }}{\Gamma (\alpha )}}\lambda ^{\alpha -1}\exp(-\lambda \beta ).}$ ${\displaystyle {\begin{aligned}p(\lambda )&\propto L(\lambda )\Gamma (\lambda ;\alpha ,\beta )\\&=\lambda ^{n}\exp \left(-\lambda n{\overline {x}}\right){\frac {\beta ^{\alpha }}{\Gamma (\alpha )}}\lambda ^{\alpha -1}\exp(-\lambda \beta )\\&\propto \lambda ^{(\alpha +n)-1}\exp(-\lambda \left(\beta +n{\overline {x}}\right)).\end{aligned}}}$ ${\displaystyle p(\lambda )=\operatorname {Gamma} (\lambda ;\alpha +n,\beta +n{\overline {x}}).}$ ${\displaystyle {\frac {\alpha +n}{\beta +n{\overline {x}}}}.}$ ${\displaystyle 1/\lambda .}$ ${\displaystyle p_{\rm {Haar-prior}}(x_{n+1}\mid x_{1},\ldots ,x_{n})={\frac {n^{n+1}\left({\overline {x}}\right)^{n}}{\left(n{\overline {x}}+x_{n+1}\right)^{n+1}}}.}$ ${\displaystyle p_{\rm {ML}}(x_{n+1}\mid x_{1},\ldots ,x_{n})=\left({\frac {1}{\overline {x}}}\right)\exp \left(-{\frac {x_{n+1}}{\overline {x}}}\right).}$ ${\displaystyle p_{\rm {CNML}}(x_{n+1}\mid x_{1},\ldots ,x_{n})={\frac {n^{n+1}\left({\overline {x}}\right)^{n}}{\left(n{\overline {x}}+x_{n+1}\right)^{n+1}}},}$ ${\displaystyle {x_{n+1}}/{\overline {x}}}$ ${\displaystyle {\begin{aligned}\operatorname {E} _{\lambda _{0}}\left[\Delta (\lambda _{0}\parallel p_{\rm {ML}})\right]&=\psi (n)+{\frac {1}{n-1}}-\log(n)\\\operatorname {E} _{\lambda _{0}}\left[\Delta (\lambda _{0}\parallel p_{\rm {CNML}})\right]&=\psi (n)+{\frac {1}{n}}-\log(n)\end{aligned}}}$ ${\displaystyle T=F^{-1}(U)}$ ${\displaystyle F^{-1}(p)={\frac {-\ln(1-p)}{\lambda }}.}$ ${\displaystyle T={\frac {-\ln(U)}{\lambda }}.}$
