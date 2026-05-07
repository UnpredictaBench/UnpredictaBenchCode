# Compound Poisson distribution

Aspect of probability theory

In probability theory, a compound Poisson distribution is the probability distribution of the sum of a number of independent identically-distributed random variables, where the number of terms to be added is itself a Poisson-distributed variable. The result can be either a continuous or a discrete distribution.

Definition[edit]
Suppose that

N
∼
Poisson
{\displaystyle N\sim \operatorname {Poisson} (\lambda ),}

i.e., N is a random variable whose distribution is a Poisson distribution with expected value λ, and that
{\displaystyle X_{1},X_{2},X_{3},\dots }

are identically distributed random variables that are mutually independent and also independent of N. Then the probability distribution of the sum of 

N

{\displaystyle N}

 i.i.d. random variables
{\displaystyle Y=\sum _{n=1}^{N}X_{n}}

is a compound Poisson distribution.
In the case N = 0, then this is a sum of 0 terms, so the value of Y is 0. Hence the conditional distribution of Y given that N = 0 is a degenerate distribution.
The compound Poisson distribution is obtained by marginalising the joint distribution of (Y,N) over N, and this joint distribution can be obtained by combining the conditional distribution Y | N with the marginal distribution of N.

Properties[edit]
The expected value and the variance of the compound distribution can be derived in a simple way from law of total expectation and the law of total variance. Thus
{\displaystyle \operatorname {E} (Y)=\operatorname {E} \left[\operatorname {E} (Y\mid N)\right]=\operatorname {E} \left[N\operatorname {E} (X)\right]=\operatorname {E} (N)\operatorname {E} (X),}
{\displaystyle {\begin{aligned}\operatorname {Var} (Y)&=\operatorname {E} \left[\operatorname {Var} (Y\mid N)\right]+\operatorname {Var} \left[\operatorname {E} (Y\mid N)\right]=\operatorname {E} \left[N\operatorname {Var} (X)\right]+\operatorname {Var} \left[N\operatorname {E} (X)\right],\\[6pt]&=\operatorname {E} (N)\operatorname {Var} (X)+\left(\operatorname {E} (X)\right)^{2}\operatorname {Var} (N).\end{aligned}}}

Then, since E(N) = Var(N) if N is Poisson-distributed, these formulae can be reduced to
{\displaystyle \operatorname {E} (Y)=\operatorname {E} (N)\operatorname {E} (X)=\lambda \operatorname {E} (X),}
{\displaystyle \operatorname {Var} (Y)=\operatorname {E} (N)(\operatorname {Var} (X)+(\operatorname {E} (X))^{2})=\operatorname {E} (N){\operatorname {E} (X^{2})}=\lambda {\operatorname {E} (X^{2})}.}

The probability distribution of Y can be determined in terms of characteristic functions:
{\displaystyle \varphi _{Y}(t)=\operatorname {E} (e^{itY})=\operatorname {E} \left(\left(\operatorname {E} (e^{itX}\mid N)\right)^{N}\right)=\operatorname {E} \left((\varphi _{X}(t))^{N}\right),\,}

and hence, using the probability-generating function of the Poisson distribution, we have
{\displaystyle \varphi _{Y}(t)={\textrm {e}}^{\lambda (\varphi _{X}(t)-1)}.\,}

An alternative approach is via cumulant generating functions:
{\displaystyle K_{Y}(t)=\ln \operatorname {E} [e^{tY}]=\ln \operatorname {E} [\operatorname {E} [e^{tY}\mid N]]=\ln \operatorname {E} [e^{NK_{X}(t)}]=K_{N}(K_{X}(t)).\,}

Via the law of total cumulance it can be shown that, if the mean of the Poisson distribution λ = 1, the cumulants of Y are the same as the moments of X1.[citation needed]
Every infinitely divisible probability distribution is a limit of compound Poisson distributions.[1] And compound Poisson distributions is infinitely divisible by the definition.

Discrete compound Poisson distribution[edit]
When 
{\displaystyle X_{1},X_{2},X_{3},\dots }

 are positive integer-valued i.i.d random variables with 
{\displaystyle P(X_{1}=k)=\alpha _{k},\ (k=1,2,\ldots )}

, then this compound Poisson distribution is named  discrete compound Poisson distribution[2][3][4] (or stuttering-Poisson distribution[5]) . We say that the discrete random variable 

Y

{\displaystyle Y}

 satisfying probability generating function characterization
{\displaystyle P_{Y}(z)=\sum \limits _{i=0}^{\infty }P(Y=i)z^{i}=\exp \left(\sum \limits _{k=1}^{\infty }\alpha _{k}\lambda (z^{k}-1)\right),\quad (|z|\leq 1)}

has a discrete compound Poisson(DCP) distribution with parameters 
{\displaystyle (\alpha _{1}\lambda ,\alpha _{2}\lambda ,\ldots )\in \mathbb {R} ^{\infty }}

 (where 

∑

i
=
1

∞

α

i

=
1

{\textstyle \sum _{i=1}^{\infty }\alpha _{i}=1}

, with 

α

i

≥
0
,
λ
>
0

{\textstyle \alpha _{i}\geq 0,\lambda >0}

), which is denoted by
{\displaystyle X\sim {\text{DCP}}(\lambda {\alpha _{1}},\lambda {\alpha _{2}},\ldots )}

Moreover, if 
{\displaystyle X\sim {\operatorname {DCP} }(\lambda {\alpha _{1}},\ldots ,\lambda {\alpha _{r}})}

, we say 

X

{\displaystyle X}

 has a discrete compound Poisson distribution of order 

r

{\displaystyle r}

 . When  
{\displaystyle r=1,2}

, DCP becomes Poisson distribution and Hermite distribution, respectively. When  
{\displaystyle r=3,4}

, DCP becomes triple stuttering-Poisson distribution and quadruple stuttering-Poisson distribution, respectively.[6] Other special cases include: shift geometric distribution, negative binomial distribution, Geometric Poisson distribution, Neyman type A distribution, Luria–Delbrück distribution in Luria–Delbrück experiment. For more special case of DCP, see the reviews paper[7] and references therein.
Feller's characterization of the compound Poisson distribution states that a non-negative integer valued r.v. 

X

{\displaystyle X}

 is infinitely divisible if and only if its distribution is a discrete compound Poisson distribution.[8] The negative binomial distribution is discrete infinitely divisible, i.e., if X has a negative binomial distribution, then for any positive integer n, there exist discrete i.i.d. random variables X1, ..., Xn whose sum has the same distribution that X has. The shift geometric distribution is discrete compound Poisson distribution since it is a trivial case of negative binomial distribution.
This distribution can model batch arrivals (such as in a bulk queue[5][9]). The discrete compound Poisson distribution is also widely used in actuarial science for modelling the distribution of the total claim amount.[3]
When some 
{\displaystyle \alpha _{k}}

 are negative, it is the discrete pseudo compound Poisson distribution.[3] We define that any discrete random variable 

Y

{\displaystyle Y}

 satisfying probability generating function characterization
{\displaystyle G_{Y}(z)=\sum \limits _{i=0}^{\infty }P(Y=i)z^{i}=\exp \left(\sum \limits _{k=1}^{\infty }\alpha _{k}\lambda (z^{k}-1)\right),\quad (|z|\leq 1)}

has a discrete pseudo compound Poisson distribution with parameters 
{\displaystyle (\lambda _{1},\lambda _{2},\ldots )=:(\alpha _{1}\lambda ,\alpha _{2}\lambda ,\ldots )\in \mathbb {R} ^{\infty }}

 where 

∑

i
=
1

∞

α

i

=
1

{\textstyle \sum _{i=1}^{\infty }{\alpha _{i}}=1}

 and 

∑

i
=
1

∞

|

α

i

|

<
∞

{\textstyle \sum _{i=1}^{\infty }{\left|{\alpha _{i}}\right|}<\infty }

, with 
{\displaystyle {\alpha _{i}}\in \mathbb {R} ,\lambda >0}

.

Compound Poisson Gamma distribution[edit]
If X has a gamma distribution, of which the exponential distribution is a special case, then the conditional distribution of Y | N is again a gamma distribution. The marginal distribution of Y is a Tweedie distribution with variance power 1 < p < 2 (proof via comparison of characteristic function).[10] To be more explicit, if

N
∼
Poisson
{\displaystyle N\sim \operatorname {Poisson} (\lambda ),}
{\displaystyle X_{i}\sim \operatorname {\Gamma } (\alpha ,\beta )}

i.i.d., then the distribution of
{\displaystyle Y=\sum _{i=1}^{N}X_{i}}

is a reproductive exponential dispersion model 
{\displaystyle ED(\mu ,\sigma ^{2})}

 with
{\displaystyle {\begin{aligned}\operatorname {E} [Y]&=\lambda {\frac {\alpha }{\beta }}=:\mu ,\\[4pt]\operatorname {Var} [Y]&=\lambda {\frac {\alpha (1+\alpha )}{\beta ^{2}}}=:\sigma ^{2}\mu ^{p}.\end{aligned}}}

The mapping of parameters Tweedie parameter 
{\displaystyle \mu ,\sigma ^{2},p}

 to the Poisson and Gamma parameters 
{\displaystyle \lambda ,\alpha ,\beta }

 is the following:
{\displaystyle {\begin{aligned}\lambda &={\frac {\mu ^{2-p}}{(2-p)\sigma ^{2}}},\\[4pt]\alpha &={\frac {2-p}{p-1}},\\[4pt]\beta &={\frac {\mu ^{1-p}}{(p-1)\sigma ^{2}}}.\end{aligned}}}

Compound Poisson processes[edit]
Main article: Compound Poisson process
A compound Poisson process with rate 
{\displaystyle \lambda >0}

 and jump size distribution G is a continuous-time stochastic process 
{\displaystyle \{\,Y(t):t\geq 0\,\}}

 given by
{\displaystyle Y(t)=\sum _{i=1}^{N(t)}D_{i},}

where the sum is by convention equal to zero as long as N(t) = 0. Here, 
{\displaystyle \{\,N(t):t\geq 0\,\}}

 is a Poisson process with rate 

λ

{\displaystyle \lambda }

, and 
{\displaystyle \{\,D_{i}:i\geq 1\,\}}

 are independent and identically distributed random variables, with distribution function G, which are also independent of 
{\displaystyle \{\,N(t):t\geq 0\,\}.\,}

[11]
For the discrete version of compound Poisson process, it can be used in survival analysis for the frailty models.[12]

Applications[edit]
A compound Poisson distribution, in which the summands have an exponential distribution, was used by Revfeim to model the distribution of the total rainfall in a day, where each day contains a Poisson-distributed number of events each of which provides an amount of rainfall which has an exponential distribution.[13] Thompson applied the same model to monthly total rainfalls.[14]
There have been applications to insurance claims[15][16] and x-ray computed tomography.[17][18][19]
