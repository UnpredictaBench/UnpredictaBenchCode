# Geometric distribution

Probability distribution

Not to be confused with Hypergeometric distribution.

| Geometric |
| --- |
| Probability mass function |
| Cumulative distribution function |
| Parameters | 0 < p ≤ 1 {\displaystyle 0<p\leq 1} success probability (real) ${\displaystyle 0<p\leq 1}$ | 0 < p ≤ 1 {\displaystyle 0<p\leq 1} success probability (real) ${\displaystyle 0<p\leq 1}$ |
| Support | k trials where k ∈ N = { 1 , 2 , 3 , … } {\displaystyle k\in \mathbb {N} =\{1,2,3,\dotsc \}} ${\displaystyle k\in \mathbb {N} =\{1,2,3,\dotsc \}}$ | k failures where k ∈ N 0 = { 0 , 1 , 2 , … } {\displaystyle k\in \mathbb {N} _{0}=\{0,1,2,\dotsc \}} ${\displaystyle k\in \mathbb {N} _{0}=\{0,1,2,\dotsc \}}$ |
| PMF | ( 1 − p ) k − 1 p {\displaystyle (1-p)^{k-1}p} ${\displaystyle (1-p)^{k-1}p}$ | ( 1 − p ) k p {\displaystyle (1-p)^{k}p} ${\displaystyle (1-p)^{k}p}$ |
| CDF | 1 − ( 1 − p ) ⌊ x ⌋ {\displaystyle 1-(1-p)^{\lfloor x\rfloor }} for x ≥ 1 {\displaystyle x\geq 1} , 0 {\displaystyle 0} for x < 1 {\displaystyle x<1} ${\displaystyle 1-(1-p)^{\lfloor x\rfloor }}$ ${\displaystyle x\geq 1}$ ${\displaystyle 0}$ ${\displaystyle x<1}$ | 1 − ( 1 − p ) ⌊ x ⌋ + 1 {\displaystyle 1-(1-p)^{\lfloor x\rfloor +1}} for x ≥ 0 {\displaystyle x\geq 0} , 0 {\displaystyle 0} for x < 0 {\displaystyle x<0} ${\displaystyle 1-(1-p)^{\lfloor x\rfloor +1}}$ ${\displaystyle x\geq 0}$ ${\displaystyle 0}$ ${\displaystyle x<0}$ |
| Mean | 1 p {\displaystyle {\frac {1}{p}}} ${\displaystyle {\frac {1}{p}}}$ | 1 − p p {\displaystyle {\frac {1-p}{p}}} ${\displaystyle {\frac {1-p}{p}}}$ |
| Median | ⌈ − 1 log 2 ⁡ ( 1 − p ) ⌉ {\displaystyle \left\lceil {\frac {-1}{\log _{2}(1-p)}}\right\rceil } (not unique if − 1 / log 2 ⁡ ( 1 − p ) {\displaystyle -1/\log _{2}(1-p)} is an integer) ${\displaystyle \left\lceil {\frac {-1}{\log _{2}(1-p)}}\right\rceil }$ ${\displaystyle -1/\log _{2}(1-p)}$ | ⌈ − 1 log 2 ⁡ ( 1 − p ) ⌉ − 1 {\displaystyle \left\lceil {\frac {-1}{\log _{2}(1-p)}}\right\rceil -1} (not unique if − 1 / log 2 ⁡ ( 1 − p ) {\displaystyle -1/\log _{2}(1-p)} is an integer) ${\displaystyle \left\lceil {\frac {-1}{\log _{2}(1-p)}}\right\rceil -1}$ ${\displaystyle -1/\log _{2}(1-p)}$ |
| Mode | 1 {\displaystyle 1} ${\displaystyle 1}$ | 0 {\displaystyle 0} ${\displaystyle 0}$ |
| Variance | 1 − p p 2 {\displaystyle {\frac {1-p}{p^{2}}}} ${\displaystyle {\frac {1-p}{p^{2}}}}$ | 1 − p p 2 {\displaystyle {\frac {1-p}{p^{2}}}} ${\displaystyle {\frac {1-p}{p^{2}}}}$ |
| Skewness | 2 − p 1 − p {\displaystyle {\frac {2-p}{\sqrt {1-p}}}} ${\displaystyle {\frac {2-p}{\sqrt {1-p}}}}$ | 2 − p 1 − p {\displaystyle {\frac {2-p}{\sqrt {1-p}}}} ${\displaystyle {\frac {2-p}{\sqrt {1-p}}}}$ |
| Excess kurtosis | 6 + p 2 1 − p {\displaystyle 6+{\frac {p^{2}}{1-p}}} ${\displaystyle 6+{\frac {p^{2}}{1-p}}}$ | 6 + p 2 1 − p {\displaystyle 6+{\frac {p^{2}}{1-p}}} ${\displaystyle 6+{\frac {p^{2}}{1-p}}}$ |
| Entropy | − ( 1 − p ) log ⁡ ( 1 − p ) − p log ⁡ p p {\displaystyle {\tfrac {-(1-p)\log(1-p)-p\log p}{p}}} ${\displaystyle {\tfrac {-(1-p)\log(1-p)-p\log p}{p}}}$ | − ( 1 − p ) log ⁡ ( 1 − p ) − p log ⁡ p p {\displaystyle {\tfrac {-(1-p)\log(1-p)-p\log p}{p}}} ${\displaystyle {\tfrac {-(1-p)\log(1-p)-p\log p}{p}}}$ |
| MGF | p e t 1 − ( 1 − p ) e t , {\displaystyle {\frac {pe^{t}}{1-(1-p)e^{t}}},} for t < − ln ⁡ ( 1 − p ) {\displaystyle t<-\ln(1-p)} ${\displaystyle {\frac {pe^{t}}{1-(1-p)e^{t}}},}$ ${\displaystyle t<-\ln(1-p)}$ | p 1 − ( 1 − p ) e t , {\displaystyle {\frac {p}{1-(1-p)e^{t}}},} for t < − ln ⁡ ( 1 − p ) {\displaystyle t<-\ln(1-p)} ${\displaystyle {\frac {p}{1-(1-p)e^{t}}},}$ ${\displaystyle t<-\ln(1-p)}$ |
| CF | p e i t 1 − ( 1 − p ) e i t {\displaystyle {\frac {pe^{it}}{1-(1-p)e^{it}}}} ${\displaystyle {\frac {pe^{it}}{1-(1-p)e^{it}}}}$ | p 1 − ( 1 − p ) e i t {\displaystyle {\frac {p}{1-(1-p)e^{it}}}} ${\displaystyle {\frac {p}{1-(1-p)e^{it}}}}$ |
| PGF | p z 1 − ( 1 − p ) z {\displaystyle {\frac {pz}{1-(1-p)z}}} ${\displaystyle {\frac {pz}{1-(1-p)z}}}$ | p 1 − ( 1 − p ) z {\displaystyle {\frac {p}{1-(1-p)z}}} ${\displaystyle {\frac {p}{1-(1-p)z}}}$ |
| Fisher information | 1 p 2 ( 1 − p ) {\displaystyle {\tfrac {1}{p^{2}(1-p)}}} ${\displaystyle {\tfrac {1}{p^{2}(1-p)}}}$ | 1 p 2 ( 1 − p ) {\displaystyle {\tfrac {1}{p^{2}(1-p)}}} ${\displaystyle {\tfrac {1}{p^{2}(1-p)}}}$ |

In probability theory and statistics, the geometric distribution is either one of two discrete probability distributions:

- The probability distribution of the number 

X

{\displaystyle X}

 of Bernoulli trials needed to get one success, supported on 
{\displaystyle \mathbb {N} =\{1,2,3,\ldots \}}

; ${\displaystyle X}$ ${\displaystyle \mathbb {N} =\{1,2,3,\ldots \}}$
- The probability distribution of the number 
{\displaystyle Y=X-1}

 of failures before the first success, supported on 
{\displaystyle \mathbb {N} _{0}=\{0,1,2,\ldots \}}

. ${\displaystyle Y=X-1}$ ${\displaystyle \mathbb {N} _{0}=\{0,1,2,\ldots \}}$

These two different geometric distributions should not be confused with each other. Often, the name shifted geometric distribution is adopted for the former one (distribution of 

X

{\displaystyle X}

); however, to avoid ambiguity, it is considered wise to indicate which is intended, by mentioning the support explicitly. ${\displaystyle X}$

The geometric distribution gives the probability that the first occurrence of success requires 

k

{\displaystyle k}

 independent trials, each with success probability 

p

{\displaystyle p}

. If the probability of success on each trial is 

p

{\displaystyle p}

, then the probability that the 

k

{\displaystyle k}

-th trial is the first success is ${\displaystyle k}$ ${\displaystyle p}$ ${\displaystyle p}$ ${\displaystyle k}$
{\displaystyle \Pr(X=k)=(1-p)^{k-1}p} ${\displaystyle \Pr(X=k)=(1-p)^{k-1}p}$
{\displaystyle k=1,2,3,4,\dots } ${\displaystyle k=1,2,3,4,\dots }$

The above form of the geometric distribution is used for modeling the number of trials up to and including the first success. By contrast, the following form of the geometric distribution is used for modeling the number of failures until the first success:
{\displaystyle \Pr(Y=k)=\Pr(X=k+1)=(1-p)^{k}p} ${\displaystyle \Pr(Y=k)=\Pr(X=k+1)=(1-p)^{k}p}$
{\displaystyle k=0,1,2,3,\dots } ${\displaystyle k=0,1,2,3,\dots }$

The geometric distribution gets its name because its probabilities follow a geometric sequence. It is sometimes called the Furry distribution after Wendell H. Furry.[1]: 210

Definition[edit]
The geometric distribution is the discrete probability distribution that describes when the first success in an infinite sequence of independent and identically distributed Bernoulli trials occurs. Its probability mass function depends on its parameterization and support. When supported on 

N

{\displaystyle \mathbb {N} }

, the probability mass function is 
{\displaystyle P(X=k)=(1-p)^{k-1}p}

 where 
{\displaystyle k=1,2,3,\dotsc }

 is the number of trials and 

p

{\displaystyle p}

 is the probability of success in each trial.[2]: 260–261 
The support may also be 
{\displaystyle \mathbb {N} _{0}}

, defining 
{\displaystyle Y=X-1}

. This alters the probability mass function into 
{\displaystyle P(Y=k)=(1-p)^{k}p}

 where 
{\displaystyle k=0,1,2,\dotsc }

 is the number of failures before the first success.[3]: 66 
An alternative parameterization of the distribution gives the probability mass function 
{\displaystyle P(Y=k)=\left({\frac {P}{Q}}\right)^{k}\left(1-{\frac {P}{Q}}\right)}

 where 
{\displaystyle P={\frac {1-p}{p}}}
{\displaystyle Q={\frac {1}{p}}}

.[1]: 208–209 
An example of a geometric distribution arises from rolling a six-sided die until a "1" appears. Each roll is independent with a 
{\displaystyle 1/6}

 chance of success. The number of rolls needed follows a geometric distribution with 
{\displaystyle p=1/6}

.

Properties[edit]
Memorylessness[edit]
Main article: Memorylessness
The geometric distribution is the only memoryless discrete probability distribution.[4] It is the discrete version of the same property found in the exponential distribution.[1]: 228  The property asserts that the number of previously failed trials does not affect the number of future trials needed for a success. 
Because there are two definitions of the geometric distribution, there are also two definitions of memorylessness for discrete random variables.[5] Expressed in terms of conditional probability, the two definitions are
{\displaystyle \Pr(X>m+n\mid X>n)=\Pr(X>m),}
{\displaystyle \Pr(Y>m+n\mid Y\geq n)=\Pr(Y>m),}

where 

m

{\displaystyle m}
{\displaystyle n}

 are natural numbers, 

X

{\displaystyle X}

 is a geometrically distributed random variable defined over 

N

{\displaystyle \mathbb {N} }

, and 

Y

{\displaystyle Y}

 is a geometrically distributed random variable defined over 
{\displaystyle \mathbb {N} _{0}}

. Note that these definitions are not equivalent for discrete random variables; 

Y

{\displaystyle Y}

 does not satisfy the first equation and 

X

{\displaystyle X}

 does not satisfy the second. 

Moments and cumulants[edit]
The expected value and variance of a geometrically distributed random variable 

X

{\displaystyle X}

 defined over 

N

{\displaystyle \mathbb {N} }

 is[2]: 261 
{\displaystyle \operatorname {E} (X)={\frac {1}{p}},\qquad \operatorname {var} (X)={\frac {1-p}{p^{2}}}.}

With a geometrically distributed random variable 

Y

{\displaystyle Y}

 defined over 
{\displaystyle \mathbb {N} _{0}}

, the expected value changes into
{\displaystyle \operatorname {E} (Y)={\frac {1-p}{p}},}

while the variance stays the same.[6]: 114–115 
For example, when rolling a six-sided die until landing on a "1", the average number of rolls needed is 
{\displaystyle {\frac {1}{1/6}}=6}

 and the average number of failures is 
{\displaystyle {\frac {1-1/6}{1/6}}=5}

.
The moment generating function of the geometric distribution when defined over 

N

{\displaystyle \mathbb {N} }
{\displaystyle \mathbb {N} _{0}}

 respectively is[7][6]: 114 
{\displaystyle {\begin{aligned}M_{X}(t)&={\frac {pe^{t}}{1-(1-p)e^{t}}}\\M_{Y}(t)&={\frac {p}{1-(1-p)e^{t}}},t<-\ln(1-p)\end{aligned}}}

The moments for the number of failures before the first success are given by
{\displaystyle {\begin{aligned}\mathrm {E} (Y^{n})&{}=\sum _{k=0}^{\infty }(1-p)^{k}p\cdot k^{n}\\&{}=p\operatorname {Li} _{-n}(1-p)&({\text{for }}n\neq 0)\end{aligned}}}

where 
{\displaystyle \operatorname {Li} _{-n}(1-p)}

 is the polylogarithm function.[8]
The cumulant generating function of the geometric distribution defined over 
{\displaystyle \mathbb {N} _{0}}

 is[1]: 216  
{\displaystyle K(t)=\ln p-\ln(1-(1-p)e^{t})}

The cumulants 
{\displaystyle \kappa _{r}}

 satisfy the recursion
{\displaystyle \kappa _{r+1}=q{\frac {\delta \kappa _{r}}{\delta q}},r=1,2,\dotsc }

where 
{\displaystyle q=1-p}

, when defined over 
{\displaystyle \mathbb {N} _{0}}

.[1]: 216 

Proof of expected value[edit]
Consider the expected value 
{\displaystyle \mathrm {E} (X)}

 of X as above, i.e. the average number of trials until a success. 
The first trial either succeeds with probability 

p

{\displaystyle p}

, or fails with probability 
{\displaystyle 1-p}

. 
If it fails, the remaining mean number of trials until a success is identical to the original mean - 
this follows from the fact that all trials are independent.
From this we get the formula:
{\displaystyle \operatorname {\mathrm {E} } (X)=p+(1-p)(1+\mathrm {E} [X]),}

which, when solved for 
{\displaystyle \mathrm {E} (X)}

, gives:
{\displaystyle \operatorname {E} (X)={\frac {1}{p}}.}

The expected number of failures 

Y

{\displaystyle Y}

 can be found from the linearity of expectation, 
{\displaystyle \mathrm {E} (Y)=\mathrm {E} (X-1)=\mathrm {E} (X)-1={\frac {1}{p}}-1={\frac {1-p}{p}}}

. It can also be shown in the following way:
{\displaystyle {\begin{aligned}\operatorname {E} (Y)&=p\sum _{k=0}^{\infty }(1-p)^{k}k\\&=p(1-p)\sum _{k=0}^{\infty }(1-p)^{k-1}k\\&=p(1-p)\left(-\sum _{k=0}^{\infty }{\frac {d}{dp}}\left[(1-p)^{k}\right]\right)\\&=p(1-p)\left[{\frac {d}{dp}}\left(-\sum _{k=0}^{\infty }(1-p)^{k}\right)\right]\\&=p(1-p){\frac {d}{dp}}\left(-{\frac {1}{p}}\right)\\&={\frac {1-p}{p}}.\end{aligned}}}

The interchange of summation and differentiation is justified by the fact that convergent power series converge uniformly on compact subsets of the set of points where they converge.

Summary statistics[edit]
The mean of the geometric distribution is its expected value which is, as previously discussed in § Moments and cumulants, 
{\displaystyle {\frac {1}{p}}}
{\displaystyle {\frac {1-p}{p}}}

 when defined over 

N

{\displaystyle \mathbb {N} }
{\displaystyle \mathbb {N} _{0}}

 respectively.
The median of the geometric distribution is 
{\displaystyle \left\lceil -{\frac {\log 2}{\log(1-p)}}\right\rceil }

when defined over 

N

{\displaystyle \mathbb {N} }

[9] and 
{\displaystyle \left\lfloor -{\frac {\log 2}{\log(1-p)}}\right\rfloor }

 when defined over 
{\displaystyle \mathbb {N} _{0}}

.[3]: 69 
The mode of the geometric distribution is the first value in the support set. This is 1 when defined over 

N

{\displaystyle \mathbb {N} }

 and 0 when defined over 
{\displaystyle \mathbb {N} _{0}}

.[3]: 69 
The skewness of the geometric distribution is 
{\displaystyle {\frac {2-p}{\sqrt {1-p}}}}

.[6]: 115 
The kurtosis of the geometric distribution is 
{\displaystyle 9+{\frac {p^{2}}{1-p}}}

.[6]: 115  The excess kurtosis of a distribution is the difference between its kurtosis and the kurtosis of a normal distribution, 

3

{\displaystyle 3}

.[10]: 217  Therefore, the excess kurtosis of the geometric distribution is 
{\displaystyle 6+{\frac {p^{2}}{1-p}}}

. Since 
{\displaystyle {\frac {p^{2}}{1-p}}\geq 0}

, the excess kurtosis is always positive so the distribution is leptokurtic.[3]: 69  In other words, the tail of a geometric distribution decays faster than a Gaussian.[10]: 217 

Entropy and Fisher's information[edit]
Entropy (geometric distribution, failures before success)[edit]
Entropy is a measure of uncertainty in a probability distribution. For the geometric distribution that models the number of failures before the first success, the probability mass function is:
{\displaystyle P(X=k)=(1-p)^{k}p,\quad k=0,1,2,\dots }

The entropy 
{\displaystyle H(X)}

 for this distribution is defined as:
{\displaystyle {\begin{aligned}H(X)&=-\sum _{k=0}^{\infty }P(X=k)\ln P(X=k)\\&=-\sum _{k=0}^{\infty }(1-p)^{k}p\ln \left((1-p)^{k}p\right)\\&=-\sum _{k=0}^{\infty }(1-p)^{k}p\left[k\ln(1-p)+\ln p\right]\\&=-\log p-{\frac {1-p}{p}}\log(1-p)\end{aligned}}}

The entropy increases as the probability 

p

{\displaystyle p}

 decreases, reflecting greater uncertainty as success becomes rarer.

Fisher's information (geometric distribution, failures before success)[edit]
Fisher information measures the amount of information that an observable random variable 

X

{\displaystyle X}

 carries about an unknown parameter 

p

{\displaystyle p}

. For the geometric distribution (failures before the first success), the Fisher information with respect to 

p

{\displaystyle p}

 is given by:
{\displaystyle I(p)={\frac {1}{p^{2}(1-p)}}}

Proof:

The likelihood function for a geometric random variable 

X

{\displaystyle X}
{\displaystyle L(p;X)=(1-p)^{X}p}

The log-likelihood function is: 
{\displaystyle \ln L(p;X)=X\ln(1-p)+\ln p}

The score function (first derivative of the log-likelihood w.r.t. 

p

{\displaystyle p}
{\displaystyle {\frac {\partial }{\partial p}}\ln L(p;X)={\frac {1}{p}}-{\frac {X}{1-p}}}

The second derivative of the log-likelihood function is: 
{\displaystyle {\frac {\partial ^{2}}{\partial p^{2}}}\ln L(p;X)=-{\frac {1}{p^{2}}}-{\frac {X}{(1-p)^{2}}}}

Fisher information is calculated as the negative expected value of the second derivative: 
{\displaystyle {\begin{aligned}I(p)&=-E\left[{\frac {\partial ^{2}}{\partial p^{2}}}\ln L(p;X)\right]\\&=-\left(-{\frac {1}{p^{2}}}-{\frac {1-p}{p(1-p)^{2}}}\right)\\&={\frac {1}{p^{2}(1-p)}}\end{aligned}}}

Fisher information increases as 

p

{\displaystyle p}

 decreases, indicating that rarer successes provide more information about the parameter 

p

{\displaystyle p}

.

Entropy (geometric distribution, trials until success)[edit]
For the geometric distribution modeling the number of trials until the first success, the probability mass function is:
{\displaystyle P(X=k)=(1-p)^{k-1}p,\quad k=1,2,3,\dots }

The entropy 
{\displaystyle H(X)}

 for this distribution is the same as that of version modeling trials until failure, 
{\displaystyle {\begin{aligned}H(X)&=-\log p-{\frac {1-p}{p}}\log(1-p)\end{aligned}}}

Fisher's information (geometric distribution, trials until success)[edit]
Fisher information for the geometric distribution modeling the number of trials until the first success is given by:
{\displaystyle I(p)={\frac {1}{p^{2}(1-p)}}}

Proof:

The likelihood function for a geometric random variable 

X

{\displaystyle X}
{\displaystyle L(p;X)=(1-p)^{X-1}p}

The log-likelihood function is:
{\displaystyle \ln L(p;X)=(X-1)\ln(1-p)+\ln p}

The score function (first derivative of the log-likelihood w.r.t. 

p

{\displaystyle p}
{\displaystyle {\frac {\partial }{\partial p}}\ln L(p;X)={\frac {1}{p}}-{\frac {X-1}{1-p}}}

The second derivative of the log-likelihood function is:
{\displaystyle {\frac {\partial ^{2}}{\partial p^{2}}}\ln L(p;X)=-{\frac {1}{p^{2}}}-{\frac {X-1}{(1-p)^{2}}}}

Fisher information is calculated as the negative expected value of the second derivative:
{\displaystyle {\begin{aligned}I(p)&=-E\left[{\frac {\partial ^{2}}{\partial p^{2}}}\ln L(p;X)\right]\\&=-\left(-{\frac {1}{p^{2}}}-{\frac {1-p}{p(1-p)^{2}}}\right)\\&={\frac {1}{p^{2}(1-p)}}\end{aligned}}}

General properties[edit]
The probability generating functions of geometric random variables 

X

{\displaystyle X}
{\displaystyle Y}

 defined over 

N

{\displaystyle \mathbb {N} }
{\displaystyle \mathbb {N} _{0}}

 are, respectively,[6]: 114–115  
{\displaystyle {\begin{aligned}G_{X}(s)&={\frac {s\,p}{1-s\,(1-p)}},\\[10pt]G_{Y}(s)&={\frac {p}{1-s\,(1-p)}},\quad |s|<(1-p)^{-1}.\end{aligned}}}

The characteristic function 
{\displaystyle \varphi (t)}

 is equal to 
{\displaystyle G(e^{it})}

 so the geometric distribution's characteristic function, when defined over 

N

{\displaystyle \mathbb {N} }
{\displaystyle \mathbb {N} _{0}}

 respectively, is[11]: 1630 
{\displaystyle {\begin{aligned}\varphi _{X}(t)&={\frac {pe^{it}}{1-(1-p)e^{it}}},\\[10pt]\varphi _{Y}(t)&={\frac {p}{1-(1-p)e^{it}}}.\end{aligned}}}

The entropy of a geometric distribution with parameter 

p

{\displaystyle p}

 is[12]
{\displaystyle -{\frac {p\log _{2}p+(1-p)\log _{2}(1-p)}{p}}}

Given a mean, the geometric distribution is the maximum entropy probability distribution of all discrete probability distributions. The corresponding continuous distribution is the exponential distribution.[13]
The geometric distribution defined on 
{\displaystyle \mathbb {N} _{0}}

 is infinitely divisible, that is, for any positive integer 

n

{\displaystyle n}

, there exist 

n

{\displaystyle n}

 independent identically distributed random variables whose sum is also geometrically distributed. This is because the negative binomial distribution can be derived from a Poisson-stopped sum of logarithmic random variables.[11]: 606–607 
The decimal digits of the geometrically distributed random variable Y are a sequence of independent (and not identically distributed) random variables.[citation needed]  For example, the hundreds digit D has this probability distribution: 
{\displaystyle \Pr(D=d)={q^{100d} \over 1+q^{100}+q^{200}+\cdots +q^{900}},}

 where q = 1 − p, and similarly for the other digits, and, more generally, similarly for numeral systems with other bases than 10.  When the base is 2, this shows that a geometrically distributed random variable can be written as a sum of independent random variables whose probability distributions are indecomposable.
Golomb coding is the optimal prefix code[clarification needed] for the geometric discrete distribution.[12]
Related distributions[edit]
The sum of 

r

{\displaystyle r}

 independent geometric random variables with parameter 

p

{\displaystyle p}

 is a negative binomial random variable with parameters 

r

{\displaystyle r}
{\displaystyle p}

.[14] The geometric distribution is a special case of the negative binomial distribution, with 
{\displaystyle r=1}

.
The geometric distribution is a special case of discrete compound Poisson distribution.[11]: 606 
The minimum of 

n

{\displaystyle n}

 geometric random variables with parameters 
{\displaystyle p_{1},\dotsc ,p_{n}}

 is also geometrically distributed with parameter 
{\displaystyle 1-\prod _{i=1}^{n}(1-p_{i})}

.[15]
Suppose 0 < r < 1, and for k = 1, 2, 3, ... the random variable Xk has a Poisson distribution with expected value rk/k.  Then 
{\displaystyle \sum _{k=1}^{\infty }k\,X_{k}}

 has a geometric distribution taking values in 
{\displaystyle \mathbb {N} _{0}}

, with expected value r/(1 − r).[citation needed]
The exponential distribution is the continuous analogue of the geometric distribution. Applying the floor function to the exponential distribution with parameter 

λ

{\displaystyle \lambda }

 creates a geometric distribution with parameter 
{\displaystyle p=1-e^{-\lambda }}

 defined over 
{\displaystyle \mathbb {N} _{0}}

.[3]: 74  This can be used to generate geometrically distributed random numbers as detailed in § Random variate generation.
If p = 1/n and X is geometrically distributed with parameter p, then the distribution of X/n approaches an exponential distribution with expected value 1 as n → ∞, since
{\displaystyle {\begin{aligned}\Pr(X/n>a)=\Pr(X>na)&=(1-p)^{na}=\left(1-{\frac {1}{n}}\right)^{na}=\left[\left(1-{\frac {1}{n}}\right)^{n}\right]^{a}\\&\to [e^{-1}]^{a}=e^{-a}{\text{ as }}n\to \infty .\end{aligned}}}

More generally, if p = λ/n, where λ is a parameter, then as n→ ∞ the distribution of X/n approaches an exponential distribution with rate λ:
{\displaystyle \Pr(X>nx)=\lim _{n\to \infty }(1-\lambda /n)^{nx}=e^{-\lambda x}}

 therefore the distribution function of X/n converges to 
{\displaystyle 1-e^{-\lambda x}}

, which is that of an exponential random variable.[citation needed]
The index of dispersion of the geometric distribution is 
{\displaystyle {\frac {1}{p}}}

 and its coefficient of variation is 
{\displaystyle {\frac {1}{\sqrt {1-p}}}}

. The distribution is overdispersed.[1]: 216 
Statistical inference[edit]
The true parameter 

p

{\displaystyle p}

 of an unknown geometric distribution can be inferred through estimators and conjugate distributions.

Method of moments[edit]
Provided they exist, the first 

l

{\displaystyle l}

 moments of a probability distribution can be estimated from a sample 
{\displaystyle x_{1},\dotsc ,x_{n}}

 using the formula
{\displaystyle m_{i}={\frac {1}{n}}\sum _{j=1}^{n}x_{j}^{i}}

where 
{\displaystyle m_{i}}

 is the 

i

{\displaystyle i}

th sample moment and 
{\displaystyle 1\leq i\leq l}

.[16]: 349–350  Estimating 
{\displaystyle \mathrm {E} (X)}

 with 
{\displaystyle m_{1}}

 gives the sample mean, denoted 
{\displaystyle {\bar {x}}}

. Substituting this estimate in the formula for the expected value of a geometric distribution and solving for 

p

{\displaystyle p}

 gives the estimators 
{\displaystyle {\hat {p}}={\frac {1}{\bar {x}}}}
{\displaystyle {\hat {p}}={\frac {1}{{\bar {x}}+1}}}

 when supported on 

N

{\displaystyle \mathbb {N} }
{\displaystyle \mathbb {N} _{0}}

 respectively. These estimators are biased since 
{\displaystyle \mathrm {E} \left({\frac {1}{\bar {x}}}\right)>{\frac {1}{\mathrm {E} ({\bar {x}})}}=p}

 as a result of Jensen's inequality.[17]: 53–54 

Maximum likelihood estimation[edit]
The maximum likelihood estimator of 

p

{\displaystyle p}

 is the value that maximizes the likelihood function given a sample.[16]: 308  By finding the zero of the derivative of the log-likelihood function when the distribution is defined over 

N

{\displaystyle \mathbb {N} }

, the maximum likelihood estimator can be found to be 
{\displaystyle {\hat {p}}={\frac {1}{\bar {x}}}}

, where 
{\displaystyle {\bar {x}}}

 is the sample mean.[18] If the domain is 
{\displaystyle \mathbb {N} _{0}}

, then the estimator shifts to 
{\displaystyle {\hat {p}}={\frac {1}{{\bar {x}}+1}}}

. As previously discussed in § Method of moments, these estimators are biased.
Regardless of the domain, the bias is equal to
{\displaystyle b\equiv \operatorname {E} {\bigg [}\;({\hat {p}}_{\mathrm {mle} }-p)\;{\bigg ]}={\frac {p\,(1-p)}{n}}}

which yields the bias-corrected maximum likelihood estimator,[citation needed]
{\displaystyle {\hat {p\,}}_{\text{mle}}^{*}={\hat {p\,}}_{\text{mle}}-{\hat {b\,}}}

Bayesian inference[edit]
In Bayesian inference, the parameter 

p

{\displaystyle p}

 is a random variable from a prior distribution with a posterior distribution calculated using Bayes' theorem after observing samples.[17]: 167  If a beta distribution is chosen as the prior distribution, then the posterior will also be a beta distribution and it is called the conjugate distribution. In particular, if a 
{\displaystyle \mathrm {Beta} (\alpha ,\beta )}

 prior is selected, then the posterior, after observing samples 
{\displaystyle k_{1},\dotsc ,k_{n}\in \mathbb {N} }
{\displaystyle p\sim \mathrm {Beta} \left(\alpha +n,\ \beta +\sum _{i=1}^{n}(k_{i}-1)\right).\!}

Alternatively, if the samples are in 
{\displaystyle \mathbb {N} _{0}}

, the posterior distribution is[20]
{\displaystyle p\sim \mathrm {Beta} \left(\alpha +n,\beta +\sum _{i=1}^{n}k_{i}\right).}

Since the expected value of a 
{\displaystyle \mathrm {Beta} (\alpha ,\beta )}

 distribution is 
{\displaystyle {\frac {\alpha }{\alpha +\beta }}}
{\displaystyle \alpha }
{\displaystyle \beta }

 approach zero, the posterior mean approaches its maximum likelihood estimate.

Random variate generation[edit]
Further information: Non-uniform random variate generation
The geometric distribution can be generated experimentally from i.i.d. standard uniform random variables by finding the first such random variable to be less than or equal to 

p

{\displaystyle p}

. However, the number of random variables needed is also geometrically distributed and the algorithm slows as 

p

{\displaystyle p}

 decreases.[21]: 498 
Random generation can be done in constant time by truncating exponential random numbers. An exponential random variable 

E

{\displaystyle E}

 can become geometrically distributed with parameter 

p

{\displaystyle p}

 through 
{\displaystyle \lceil -E/\log(1-p)\rceil }

. In turn, 

E

{\displaystyle E}

 can be generated from a standard uniform random variable 

U

{\displaystyle U}

 altering the formula into 
{\displaystyle \lceil \log(U)/\log(1-p)\rceil }

.[21]: 499–500 [22]

Applications[edit]
The geometric distribution is used in many disciplines. In queueing theory, the M/M/1 queue has a steady state following a geometric distribution.[23] In stochastic processes, the Yule Furry process is geometrically distributed.[24] The distribution also arises when modeling the lifetime of a device in discrete contexts.[25] It has also been used to fit data including modeling patients spreading COVID-19.[26]
