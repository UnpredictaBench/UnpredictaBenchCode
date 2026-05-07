# Skellam distribution

Discrete probability distribution

| Skellam |
| --- |
| Probability mass functionExamples of the probability mass function for the Skellam distribution. The horizontal axis is the index k. (The function is only defined at integer values of k. The connecting lines do not indicate continuity.) |
| Parameters | μ 1 ≥ 0 , μ 2 ≥ 0 {\displaystyle \mu _{1}\geq 0,~~\mu _{2}\geq 0} ${\displaystyle \mu _{1}\geq 0,~~\mu _{2}\geq 0}$ |
| Support | k ∈ { … , − 2 , − 1 , 0 , 1 , 2 , … } {\displaystyle k\in \{\ldots ,-2,-1,0,1,2,\ldots \}} ${\displaystyle k\in \{\ldots ,-2,-1,0,1,2,\ldots \}}$ |
| PMF | e − ( μ 1 + μ 2 ) ( μ 1 μ 2 ) k / 2 I k ( 2 μ 1 μ 2 ) {\displaystyle e^{-(\mu _{1}\!+\!\mu _{2})}\left({\frac {\mu _{1}}{\mu _{2}}}\right)^{k/2}\!\!I_{k}(2{\sqrt {\mu _{1}\mu _{2}}})} ${\displaystyle e^{-(\mu _{1}\!+\!\mu _{2})}\left({\frac {\mu _{1}}{\mu _{2}}}\right)^{k/2}\!\!I_{k}(2{\sqrt {\mu _{1}\mu _{2}}})}$ |
| Mean | μ 1 − μ 2 {\displaystyle \mu _{1}-\mu _{2}\,} ${\displaystyle \mu _{1}-\mu _{2}\,}$ |
| Median | N/A |
| Variance | μ 1 + μ 2 {\displaystyle \mu _{1}+\mu _{2}\,} ${\displaystyle \mu _{1}+\mu _{2}\,}$ |
| Skewness | μ 1 − μ 2 ( μ 1 + μ 2 ) 3 / 2 {\displaystyle {\frac {\mu _{1}-\mu _{2}}{(\mu _{1}+\mu _{2})^{3/2}}}} ${\displaystyle {\frac {\mu _{1}-\mu _{2}}{(\mu _{1}+\mu _{2})^{3/2}}}}$ |
| Excess kurtosis | 1 μ 1 + μ 2 {\displaystyle {\frac {1}{\mu _{1}+\mu _{2}}}} ${\displaystyle {\frac {1}{\mu _{1}+\mu _{2}}}}$ |
| MGF | e − ( μ 1 + μ 2 ) + μ 1 e t + μ 2 e − t {\displaystyle e^{-(\mu _{1}+\mu _{2})+\mu _{1}e^{t}+\mu _{2}e^{-t}}} ${\displaystyle e^{-(\mu _{1}+\mu _{2})+\mu _{1}e^{t}+\mu _{2}e^{-t}}}$ |
| CF | e − ( μ 1 + μ 2 ) + μ 1 e i t + μ 2 e − i t {\displaystyle e^{-(\mu _{1}+\mu _{2})+\mu _{1}e^{it}+\mu _{2}e^{-it}}} ${\displaystyle e^{-(\mu _{1}+\mu _{2})+\mu _{1}e^{it}+\mu _{2}e^{-it}}}$ |

The Skellam distribution is the discrete probability distribution of the difference 
{\displaystyle N_{1}-N_{2}}

 of two statistically independent random variables 
{\displaystyle N_{1}}
{\displaystyle N_{2},}

 each Poisson-distributed with respective expected values 
{\displaystyle \mu _{1}}
{\displaystyle \mu _{2}}

. It is useful in describing the statistics of the difference of two images with simple photon noise, as well as describing the point spread distribution in sports where all scored points are equal, such as baseball, hockey and soccer. ${\displaystyle N_{1}-N_{2}}$ ${\displaystyle N_{1}}$ ${\displaystyle N_{2},}$ ${\displaystyle \mu _{1}}$ ${\displaystyle \mu _{2}}$

The distribution is also applicable to a special case of the difference of dependent Poisson random variables, but just the obvious case where the two variables have a common additive random contribution which is cancelled by the differencing: see Karlis & Ntzoufras (2003) for details and an application.

The probability mass function for the Skellam distribution for a difference 
{\displaystyle K=N_{1}-N_{2}}

 between two independent Poisson-distributed random variables with means 
{\displaystyle \mu _{1}}
{\displaystyle \mu _{2}}

 is given by: ${\displaystyle K=N_{1}-N_{2}}$ ${\displaystyle \mu _{1}}$ ${\displaystyle \mu _{2}}$
{\displaystyle p(k;\mu _{1},\mu _{2})=\Pr\{K=k\}=e^{-(\mu _{1}+\mu _{2})}\left({\mu _{1} \over \mu _{2}}\right)^{k/2}I_{k}(2{\sqrt {\mu _{1}\mu _{2}}})} ${\displaystyle p(k;\mu _{1},\mu _{2})=\Pr\{K=k\}=e^{-(\mu _{1}+\mu _{2})}\left({\mu _{1} \over \mu _{2}}\right)^{k/2}I_{k}(2{\sqrt {\mu _{1}\mu _{2}}})}$

where Ik(z) is the modified Bessel function of the first kind. Since k is an integer we have that Ik(z) = I|k|(z).

Derivation[edit]
The probability mass function of a Poisson-distributed random variable with mean μ is given by
{\displaystyle p(k;\mu )={\mu ^{k} \over k!}e^{-\mu }.\,}
{\displaystyle k\geq 0}

 (and zero otherwise). The Skellam probability mass function for the difference of two independent counts 
{\displaystyle K=N_{1}-N_{2}}

 is the convolution of two Poisson distributions: (Skellam, 1946)
{\displaystyle {\begin{aligned}p(k;\mu _{1},\mu _{2})&=\sum _{n=-\infty }^{\infty }p(k+n;\mu _{1})p(n;\mu _{2})\\&=e^{-(\mu _{1}+\mu _{2})}\sum _{n=\max(0,-k)}^{\infty }{{\mu _{1}^{k+n}\mu _{2}^{n}} \over {n!(k+n)!}}\end{aligned}}}

Since the Poisson distribution is zero for negative values of the count 
{\displaystyle (p(N<0;\mu )=0)}

, the second sum is only taken for those terms where 
{\displaystyle n\geq 0}
{\displaystyle n+k\geq 0}

. It can be shown that the above sum implies that
{\displaystyle {\frac {p(k;\mu _{1},\mu _{2})}{p(-k;\mu _{1},\mu _{2})}}=\left({\frac {\mu _{1}}{\mu _{2}}}\right)^{k}}

so that:
{\displaystyle p(k;\mu _{1},\mu _{2})=e^{-(\mu _{1}+\mu _{2})}\left({\mu _{1} \over \mu _{2}}\right)^{k/2}I_{|k|}(2{\sqrt {\mu _{1}\mu _{2}}})}

where I k(z) is the modified Bessel function of the first kind. The special case for 
{\displaystyle \mu _{1}=\mu _{2}(=\mu )}

 is given by Irwin (1937):
{\displaystyle p{\left(k;\mu ,\mu \right)}=e^{-2\mu }I_{|k|}(2\mu ).}

Using the limiting values of the modified Bessel function for small arguments, we can recover the Poisson distribution as a special case of the Skellam distribution for 
{\displaystyle \mu _{2}=0}

.

Properties[edit]
As it is a discrete probability function, the Skellam probability mass function is normalized:
{\displaystyle \sum _{k=-\infty }^{\infty }p(k;\mu _{1},\mu _{2})=1.}

We know that the probability generating function (pgf) for a Poisson distribution is:
{\displaystyle G\left(t;\mu \right)=e^{\mu (t-1)}.}

It follows that the pgf, 
{\displaystyle G(t;\mu _{1},\mu _{2})}

, for a Skellam probability mass function will be:
{\displaystyle {\begin{aligned}G(t;\mu _{1},\mu _{2})&=\sum _{k=-\infty }^{\infty }p(k;\mu _{1},\mu _{2})t^{k}\\[4pt]&=G\left(t;\mu _{1}\right)G\left(1/t;\mu _{2}\right)\\[4pt]&=e^{-(\mu _{1}+\mu _{2})+\mu _{1}t+\mu _{2}/t}.\end{aligned}}}

Notice that the form of the probability-generating function implies that the distribution of the sums or the differences of any number of independent Skellam-distributed variables are again Skellam-distributed. It is sometimes claimed that any linear combination of two Skellam distributed variables are again Skellam-distributed, but this is clearly not true since any multiplier other than 
{\displaystyle \pm 1}

 would change the support of the distribution and alter the pattern of moments in a way that no Skellam distribution can satisfy.
The moment-generating function is given by:
{\displaystyle M\left(t;\mu _{1},\mu _{2}\right)=G(e^{t};\mu _{1},\mu _{2})=\sum _{k=0}^{\infty }{t^{k} \over k!}\,m_{k}}

which yields the raw moments mk . Define:
{\displaystyle \Delta \ {\stackrel {\mathrm {def} }{=}}\ \mu _{1}-\mu _{2}}
{\displaystyle \mu \ {\stackrel {\mathrm {def} }{=}}\ {\tfrac {1}{2}}(\mu _{1}+\mu _{2}).}

Then the raw moments mk are
{\displaystyle {\begin{aligned}m_{1}&=\Delta \\m_{2}&=2\mu +\Delta ^{2}\\m_{3}&=\Delta \left(1+6\mu +\Delta ^{2}\right)\end{aligned}}}

The central moments M k are
{\displaystyle {\begin{aligned}M_{2}&=2\mu ,\\M_{3}&=\Delta ,\\M_{4}&=2\mu +12\mu ^{2}.\,\end{aligned}}}

The mean, variance, skewness, and kurtosis excess are respectively:
{\displaystyle {\begin{aligned}\operatorname {E} (n)&=\Delta ,\\[4pt]\sigma ^{2}&=2\mu ,\\[4pt]\gamma _{1}&=\Delta /(2\mu )^{3/2},\\[4pt]\gamma _{2}&=1/2.\end{aligned}}}

The cumulant-generating function is given by:
{\displaystyle K(t;\mu _{1},\mu _{2})\ {\stackrel {\mathrm {def} }{=}}\ \ln(M(t;\mu _{1},\mu _{2}))=\sum _{k=0}^{\infty }{\frac {t^{k}}{k!}}\,\kappa _{k}}

which yields the cumulants:
{\displaystyle {\begin{aligned}\kappa _{2k}&=2\mu ,\\\kappa _{2k+1}&=\Delta .\end{aligned}}}

For the special case when μ1 = μ2, an asymptotic expansion of the modified Bessel function of the first kind yields for large μ:
{\displaystyle p(k;\mu ,\mu )\sim {\frac {1}{\sqrt {4\pi \mu }}}\left[1+\sum _{n=1}^{\infty }\left(-1\right)^{n}{\frac {\left\{4k^{2}-1^{2}\right\}\left\{4k^{2}-3^{2}\right\}\cdots \left\{4k^{2}-(2n-1)^{2}\right\}}{n!\,2^{3n}\,(2\mu )^{n}}}\right].}

(Abramowitz & Stegun 1972, p. 377).  Also, for this special case, when k is also large, and of order of the square root of 2μ, the distribution tends to a normal distribution:
{\displaystyle p(k;\mu ,\mu )\sim {\frac {e^{-k^{2}/4\mu }}{\sqrt {4\pi \mu }}}.}

These special results can easily be extended to the more general case of different means.

Bounds on weight above zero[edit]
If 

X
∼
Skellam
{\displaystyle X\sim \operatorname {Skellam} (\mu _{1},\mu _{2})}

, with 
{\displaystyle \mu _{1}<\mu _{2}}

, then
{\displaystyle {\frac {\exp \left[-\left({\sqrt {\mu _{1}}}-{\sqrt {\mu _{2}}}\right)^{2}\right]}{\left(\mu _{1}+\mu _{2}\right)^{2}}}-{\frac {e^{-(\mu _{1}+\mu _{2})}}{2{\sqrt {\mu _{1}\mu _{2}}}}}-{\frac {e^{-(\mu _{1}+\mu _{2})}}{4\mu _{1}\mu _{2}}}\leq \Pr\{X\geq 0\}\leq \exp \left[-\left({\sqrt {\mu _{1}}}-{\sqrt {\mu _{2}}}\right)^{2}\right]}

Details can be found in Poisson distribution § Poisson races
