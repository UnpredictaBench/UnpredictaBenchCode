# Truncated normal distribution

Type of probability distribution

Not to be confused with rectified normal distribution, where negative elements are reset to zero, nor a censored normal distribution, where some elements are known to be outside of a specific range.

| Probability density functionProbability density function for the truncated normal distribution for different sets of parameters. In all cases, a = −10 and b = 10. For the black: μ = −8, σ = 2; blue: μ = 0, σ = 2; red: μ = 9, σ = 10; orange: μ = 0, σ = 10. |
| --- |
| Cumulative distribution functionCumulative distribution function for the truncated normal distribution for different sets of parameters. In all cases, a = −10 and b = 10. For the black: μ = −8, σ = 2; blue: μ = 0, σ = 2; red: μ = 9, σ = 10; orange: μ = 0, σ = 10. |
| Notation | ξ = x − μ σ , α = a − μ σ , β = b − μ σ {\displaystyle \xi ={\frac {x-\mu }{\sigma }},\ \alpha ={\frac {a-\mu }{\sigma }},\ \beta ={\frac {b-\mu }{\sigma }}} Z = Φ ( β ) − Φ ( α ) {\displaystyle Z=\Phi (\beta )-\Phi (\alpha )} ${\displaystyle \xi ={\frac {x-\mu }{\sigma }},\ \alpha ={\frac {a-\mu }{\sigma }},\ \beta ={\frac {b-\mu }{\sigma }}}$ ${\displaystyle Z=\Phi (\beta )-\Phi (\alpha )}$ |
| Parameters | μ ∈ R {\displaystyle \mu \in \mathbb {R} } σ 2 ≥ 0 {\displaystyle \sigma ^{2}\geq 0} (but see definition) a ∈ R {\displaystyle a\in \mathbb {R} } — minimum value of x {\displaystyle x} b ∈ R {\displaystyle b\in \mathbb {R} } — maximum value of x {\displaystyle x} ( b > a {\displaystyle b>a} ) ${\displaystyle \mu \in \mathbb {R} }$ ${\displaystyle \sigma ^{2}\geq 0}$ ${\displaystyle a\in \mathbb {R} }$ ${\displaystyle x}$ ${\displaystyle b\in \mathbb {R} }$ ${\displaystyle x}$ ${\displaystyle b>a}$ |
| Support | x ∈ [ a , b ] {\displaystyle x\in [a,b]} ${\displaystyle x\in [a,b]}$ |
| PDF | f ( x ; μ , σ , a , b ) = φ ( ξ ) σ Z {\displaystyle f(x;\mu ,\sigma ,a,b)={\frac {\varphi (\xi )}{\sigma Z}}\,} [1] ${\displaystyle f(x;\mu ,\sigma ,a,b)={\frac {\varphi (\xi )}{\sigma Z}}\,}$ |
| CDF | F ( x ; μ , σ , a , b ) = Φ ( ξ ) − Φ ( α ) Z {\displaystyle F(x;\mu ,\sigma ,a,b)={\frac {\Phi (\xi )-\Phi (\alpha )}{Z}}} ${\displaystyle F(x;\mu ,\sigma ,a,b)={\frac {\Phi (\xi )-\Phi (\alpha )}{Z}}}$ |
| Mean | μ + φ ( α ) − φ ( β ) Z σ {\displaystyle \mu +{\frac {\varphi (\alpha )-\varphi (\beta )}{Z}}\sigma } ${\displaystyle \mu +{\frac {\varphi (\alpha )-\varphi (\beta )}{Z}}\sigma }$ |
| Median | μ + Φ − 1 ( Φ ( α ) + Φ ( β ) 2 ) σ {\displaystyle \mu +\Phi ^{-1}\left({\frac {\Phi (\alpha )+\Phi (\beta )}{2}}\right)\sigma } ${\displaystyle \mu +\Phi ^{-1}\left({\frac {\Phi (\alpha )+\Phi (\beta )}{2}}\right)\sigma }$ |
| Mode | { a , i f μ < a μ , i f a ≤ μ ≤ b b , i f μ > b {\displaystyle \left\{{\begin{array}{ll}a,&\mathrm {if} \ \mu <a\\\mu ,&\mathrm {if} \ a\leq \mu \leq b\\b,&\mathrm {if} \ \mu >b\end{array}}\right.} ${\displaystyle \left\{{\begin{array}{ll}a,&\mathrm {if} \ \mu <a\\\mu ,&\mathrm {if} \ a\leq \mu \leq b\\b,&\mathrm {if} \ \mu >b\end{array}}\right.}$ |
| Variance | σ 2 [ 1 − β φ ( β ) − α φ ( α ) Z − ( φ ( α ) − φ ( β ) Z ) 2 ] {\displaystyle \sigma ^{2}\left[1-{\frac {\beta \varphi (\beta )-\alpha \varphi (\alpha )}{Z}}-\left({\frac {\varphi (\alpha )-\varphi (\beta )}{Z}}\right)^{2}\right]} ${\displaystyle \sigma ^{2}\left[1-{\frac {\beta \varphi (\beta )-\alpha \varphi (\alpha )}{Z}}-\left({\frac {\varphi (\alpha )-\varphi (\beta )}{Z}}\right)^{2}\right]}$ |
| Entropy | ln ⁡ ( 2 π e σ Z ) + α φ ( α ) − β φ ( β ) 2 Z {\displaystyle \ln({\sqrt {2\pi e}}\sigma Z)+{\frac {\alpha \varphi (\alpha )-\beta \varphi (\beta )}{2Z}}} ${\displaystyle \ln({\sqrt {2\pi e}}\sigma Z)+{\frac {\alpha \varphi (\alpha )-\beta \varphi (\beta )}{2Z}}}$ |
| MGF | e μ t + σ 2 t 2 / 2 [ Φ ( β − σ t ) − Φ ( α − σ t ) Φ ( β ) − Φ ( α ) ] {\displaystyle e^{\mu t+\sigma ^{2}t^{2}/2}\left[{\frac {\Phi (\beta -\sigma t)-\Phi (\alpha -\sigma t)}{\Phi (\beta )-\Phi (\alpha )}}\right]} ${\displaystyle e^{\mu t+\sigma ^{2}t^{2}/2}\left[{\frac {\Phi (\beta -\sigma t)-\Phi (\alpha -\sigma t)}{\Phi (\beta )-\Phi (\alpha )}}\right]}$ |

In probability and statistics, the truncated normal distribution is the probability distribution derived from that of a normally distributed random variable by bounding the random variable from either below or above (or both). The truncated normal distribution has wide applications in statistics and econometrics.

Definitions[edit]
Suppose 

X

{\displaystyle X}

 has a normal distribution with mean 

μ

{\displaystyle \mu }

 and variance 
{\displaystyle \sigma ^{2}}

 and lies within the interval 

(
a
,
b
)
,

with
{\displaystyle (a,b),{\text{with}}\;-\infty \leq a<b\leq \infty }

. Then 

X

{\displaystyle X}

 conditional on 
{\displaystyle a<X<b}

 has a truncated normal distribution.
Its probability density function, 

f

{\displaystyle f}

, for 
{\displaystyle a\leq x\leq b}

, is given by
{\displaystyle f(x;\mu ,\sigma ,a,b)={\frac {1}{\sigma }}\,{\frac {\varphi ({\frac {x-\mu }{\sigma }})}{\Phi ({\frac {b-\mu }{\sigma }})-\Phi ({\frac {a-\mu }{\sigma }})}}}

and by 
{\displaystyle f=0}

 otherwise.
Here,
{\displaystyle \varphi (\xi )={\frac {1}{\sqrt {2\pi }}}\exp \left(-{\frac {1}{2}}\xi ^{2}\right)}

is the probability density function of the standard normal distribution and 
{\displaystyle \Phi (\cdot )}

 is its cumulative distribution function
{\displaystyle \Phi (x)={\frac {1}{2}}\left(1+\operatorname {erf} (x/{\sqrt {2}})\right).}

By definition, if 
{\displaystyle b=\infty }

, then 
{\displaystyle \Phi \left({\tfrac {b-\mu }{\sigma }}\right)=1}

, and similarly, if 
{\displaystyle a=-\infty }

, then 
{\displaystyle \Phi \left({\tfrac {a-\mu }{\sigma }}\right)=0}

.
The above formulae show that when 
{\displaystyle -\infty <a<b<+\infty }

 the scale parameter 
{\displaystyle \sigma ^{2}}

 of the truncated normal distribution is allowed to assume negative values. The parameter 

σ

{\displaystyle \sigma }

 is in this case imaginary, but the function 

f

{\displaystyle f}

 is nevertheless real, positive, and normalizable. The scale parameter 
{\displaystyle \sigma ^{2}}

 of the untruncated normal distribution must be positive because the distribution would not be normalizable otherwise. The doubly truncated normal distribution, on the other hand, can in principle have a negative scale parameter (which is different from the variance, see summary formulae), because no such integrability problems arise on a bounded domain. In this case the distribution cannot be interpreted as an untruncated normal conditional on 
{\displaystyle a<X<b}

, of course, but can still be interpreted as a maximum-entropy distribution with first and second moments as constraints, and has an additional peculiar feature: it presents two local maxima instead of one, located at 
{\displaystyle x=a}
{\displaystyle x=b}

.

Properties[edit]
The truncated normal is one of two possible maximum entropy probability distributions for a fixed mean and variance constrained to the interval [a,b], the other being the truncated U.[2] Truncated normals with fixed support form an exponential family.
Nielsen[3]  reported closed-form formula for calculating the Kullback-Leibler divergence and the Bhattacharyya distance between two truncated normal distributions with the support of the first distribution nested into the support of the second distribution.

Moments[edit]
If the random variable has been truncated only from below, some probability mass has been shifted to higher values, giving a first-order stochastically dominating distribution and hence increasing the mean to a value higher than the mean 

μ

{\displaystyle \mu }

 of the original normal distribution. Likewise, if the random variable has been truncated only from above, the truncated distribution has a mean less than 
{\displaystyle \mu .}

Regardless of whether the random variable is bounded above, below, or both, the truncation is a mean-preserving contraction combined with a mean-changing rigid shift, and hence the variance of the truncated distribution is less than the variance 
{\displaystyle \sigma ^{2}}

 of the original normal distribution.

Two sided truncation[edit]
Source:[4]
{\displaystyle \alpha =(a-\mu )/\sigma }
{\displaystyle \beta =(b-\mu )/\sigma }

. Then:
{\displaystyle \operatorname {E} (X\mid a<X<b)=\mu -\sigma {\frac {\varphi (\beta )-\varphi (\alpha )}{\Phi (\beta )-\Phi (\alpha )}}}
{\displaystyle \operatorname {Var} (X\mid a<X<b)=\sigma ^{2}\left[1-{\frac {\beta \varphi (\beta )-\alpha \varphi (\alpha )}{\Phi (\beta )-\Phi (\alpha )}}-\left({\frac {\varphi (\beta )-\varphi (\alpha )}{\Phi (\beta )-\Phi (\alpha )}}\right)^{2}\right]}

Care must be taken in the numerical evaluation of these formulas, which can result in catastrophic cancellation when the interval 
{\displaystyle [a,b]}

 does not include 

μ

{\displaystyle \mu }

. There are better ways to rewrite them that avoid this issue.[5]

One sided truncation (of lower tail)[edit]
Sources:[6][7]
In this case 
{\displaystyle \;b=\infty ,\;\varphi (\beta )=0,\;\Phi (\beta )=1,}

 then
{\displaystyle \operatorname {E} (X\mid X>a)=\mu +\sigma \varphi (\alpha )/Z,\!}
{\displaystyle \operatorname {Var} (X\mid X>a)=\sigma ^{2}[1+\alpha \varphi (\alpha )/Z-(\varphi (\alpha )/Z)^{2}],}

where 
{\displaystyle Z=1-\Phi (\alpha ).}

One sided truncation (of upper tail)[edit]
In this case 
{\displaystyle \;a=\alpha =-\infty ,\;\varphi (\alpha )=0,\;\Phi (\alpha )=0,}

 then
{\displaystyle \operatorname {E} (X\mid X<b)=\mu -\sigma {\frac {\varphi (\beta )}{\Phi (\beta )}},}
{\displaystyle \operatorname {Var} (X\mid X<b)=\sigma ^{2}\left[1-\beta {\frac {\varphi (\beta )}{\Phi (\beta )}}-\left({\frac {\varphi (\beta )}{\Phi (\beta )}}\right)^{2}\right].}

Barr & Sherrill (1999) give a simpler expression for the variance of one sided truncations. Their formula is in terms of the chi-square CDF, which is implemented in standard software libraries. Bebu & Mathew (2009) provide formulas for (generalized) confidence intervals around the truncated moments.

A recursive formula[edit]
As for the non-truncated case, there is a recursive formula for the truncated moments.[8]
In particular, for 
{\displaystyle n\geq 0}

, we have
{\displaystyle \operatorname {E} \left[\left({\frac {x-\mu }{\sigma }}\right)^{n+2}\right]={\frac {\alpha ^{n+1}\varphi (\alpha )-\beta ^{n+1}\varphi (\beta )}{\Phi (\beta )-\Phi (\alpha )}}+(n+1)\operatorname {E} \left[\left({\frac {x-\mu }{\sigma }}\right)^{n}\right].}

Proof[edit]
By the change of variables 
{\displaystyle \xi =(x-\mu )/\sigma }

, one obtains
{\displaystyle \operatorname {E} \left[\left({\frac {x-\mu }{\sigma }}\right)^{n+2}\right]=\int _{\alpha }^{\beta }{\frac {\xi ^{n+2}\varphi (\xi )}{\Phi (\beta )-\Phi (\alpha )}}d\xi .}

Using 
{\displaystyle \varphi '(\xi )=-\xi \varphi (\xi ),}

 integration by parts yields
{\displaystyle \operatorname {E} \left[\left({\frac {x-\mu }{\sigma }}\right)^{n+2}\right]=\left[{\frac {-\xi ^{n+1}\varphi (\xi )}{\Phi (\beta )-\Phi (\alpha )}}\right]_{\alpha }^{\beta }+(n+1)\int _{\alpha }^{\beta }{\frac {\xi ^{n}\varphi (\xi )}{\Phi (\beta )-\Phi (\alpha )}}d\xi ,}

which gives the equation to be proven.

Multivariate[edit]
Computing the moments of a multivariate truncated normal is harder.

Generating values from the truncated normal distribution[edit]
Further information: Pseudo-random number sampling
This section's use of external links may not follow Wikipedia's policies or guidelines. Please improve this article by removing excessive or inappropriate external links, and converting useful links where appropriate into footnote references. (May 2022) (Learn how and when to remove this message)
A random variate 

x

{\displaystyle x}

 defined as
{\displaystyle x=\Phi ^{-1}(\Phi (\alpha )+U\cdot (\Phi (\beta )-\Phi (\alpha )))\sigma +\mu }

with 

Φ

{\displaystyle \Phi }

 the cumulative distribution function of the normal distribution to be sampled from (i.e. with correct mean and variance) and 
{\displaystyle \Phi ^{-1}}

 its inverse, 

U

{\displaystyle U}

 a uniform random number on 
{\displaystyle (0,1)}

, follows the distribution truncated to the range 
{\displaystyle (a,b)}

. This is simply the inverse transform method for simulating random variables. Although one of the simplest, this method can either fail when sampling in the tail of the normal distribution,[9] or be much too slow.[10] Thus, in  practice, one has to find alternative methods of simulation.
One such truncated normal generator (implemented in Matlab and
in R (programming language) as trandn.R  ) is based on an acceptance rejection idea due to Marsaglia.[11] Despite the slightly suboptimal acceptance rate of Marsaglia (1964) in comparison with Robert (1995),  Marsaglia's method is typically  faster,[10] because it does not require the costly numerical evaluation of the exponential function.    
For more on simulating a draw from the truncated normal distribution, see Robert (1995), Lynch (2007, Section 8.1.3 (pages 200–206)), Devroye (1986).  The MSM package in R has a function, rtnorm, that calculates draws from a truncated normal.  The truncnorm package in R also has functions to draw from a truncated normal.
Chopin (2011) proposed (arXiv) an algorithm inspired from the Ziggurat algorithm of Marsaglia and Tsang (1984, 2000), which is usually considered as the fastest Gaussian sampler, and is also very close to Ahrens's algorithm (1995). Implementations can be found in C, C++, Matlab and Python.
Sampling from the multivariate truncated normal distribution is considerably more difficult.[12] Exact or perfect simulation is only feasible in the case of truncation of the normal distribution to a polytope region.[12][13] In  more general cases, Damien & Walker (2001) introduce a general methodology for sampling truncated densities within a Gibbs sampling framework. Their algorithm introduces one latent variable and, within a Gibbs sampling framework, it is more computationally efficient than the algorithm of Robert (1995).
