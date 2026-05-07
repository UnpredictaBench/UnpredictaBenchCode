# Bernoulli distribution

Probability distribution modeling a coin toss which need not be fair

| Bernoulli distribution |
| --- |
| Probability mass function Three examples of Bernoulli distribution: P ( x = 0 ) = 0 . 2 {\displaystyle P(x=0)=0{.}2} and P ( x = 1 ) = 0 . 8 {\displaystyle P(x=1)=0{.}8} P ( x = 0 ) = 0 . 8 {\displaystyle P(x=0)=0{.}8} and P ( x = 1 ) = 0 . 2 {\displaystyle P(x=1)=0{.}2} P ( x = 0 ) = 0 . 5 {\displaystyle P(x=0)=0{.}5} and P ( x = 1 ) = 0 . 5 {\displaystyle P(x=1)=0{.}5} ${\displaystyle P(x=0)=0{.}2}$ ${\displaystyle P(x=1)=0{.}8}$ ${\displaystyle P(x=0)=0{.}8}$ ${\displaystyle P(x=1)=0{.}2}$ ${\displaystyle P(x=0)=0{.}5}$ ${\displaystyle P(x=1)=0{.}5}$ |
| Parameters | 0 ≤ p ≤ 1 {\displaystyle 0\leq p\leq 1} q = 1 − p {\displaystyle q=1-p} ${\displaystyle 0\leq p\leq 1}$ ${\displaystyle q=1-p}$ |
| Support | k ∈ { 0 , 1 } {\displaystyle k\in \{0,1\}} ${\displaystyle k\in \{0,1\}}$ |
| PMF | { q = 1 − p if k = 0 p if k = 1 {\displaystyle {\begin{cases}q=1-p&{\text{if }}k=0\\p&{\text{if }}k=1\end{cases}}} ${\displaystyle {\begin{cases}q=1-p&{\text{if }}k=0\\p&{\text{if }}k=1\end{cases}}}$ |
| CDF | { 0 if k < 0 1 − p if 0 ≤ k < 1 1 if k ≥ 1 {\displaystyle {\begin{cases}0&{\text{if }}k<0\\1-p&{\text{if }}0\leq k<1\\1&{\text{if }}k\geq 1\end{cases}}} ${\displaystyle {\begin{cases}0&{\text{if }}k<0\\1-p&{\text{if }}0\leq k<1\\1&{\text{if }}k\geq 1\end{cases}}}$ |
| Mean | p {\displaystyle p} ${\displaystyle p}$ |
| Median | { 0 if p < 1 / 2 [ 0 , 1 ] if p = 1 / 2 1 if p > 1 / 2 {\displaystyle {\begin{cases}0&{\text{if }}p<1/2\\\left[0,1\right]&{\text{if }}p=1/2\\1&{\text{if }}p>1/2\end{cases}}} ${\displaystyle {\begin{cases}0&{\text{if }}p<1/2\\\left[0,1\right]&{\text{if }}p=1/2\\1&{\text{if }}p>1/2\end{cases}}}$ |
| Mode | { 0 if p < 1 / 2 0 , 1 if p = 1 / 2 1 if p > 1 / 2 {\displaystyle {\begin{cases}0&{\text{if }}p<1/2\\0,1&{\text{if }}p=1/2\\1&{\text{if }}p>1/2\end{cases}}} ${\displaystyle {\begin{cases}0&{\text{if }}p<1/2\\0,1&{\text{if }}p=1/2\\1&{\text{if }}p>1/2\end{cases}}}$ |
| Variance | p ( 1 − p ) = p q {\displaystyle p(1-p)=pq} ${\displaystyle p(1-p)=pq}$ |
| MAD | 2 p ( 1 − p ) = 2 p q {\displaystyle 2p(1-p)=2pq} ${\displaystyle 2p(1-p)=2pq}$ |
| Skewness | q − p p q {\displaystyle {\frac {q-p}{\sqrt {pq}}}} ${\displaystyle {\frac {q-p}{\sqrt {pq}}}}$ |
| Excess kurtosis | 1 − 6 p q p q {\displaystyle {\frac {1-6pq}{pq}}} ${\displaystyle {\frac {1-6pq}{pq}}}$ |
| Entropy | − q ln ⁡ q − p ln ⁡ p {\displaystyle -q\ln q-p\ln p} ${\displaystyle -q\ln q-p\ln p}$ |
| MGF | q + p e t {\displaystyle q+pe^{t}} ${\displaystyle q+pe^{t}}$ |
| CF | q + p e i t {\displaystyle q+pe^{it}} ${\displaystyle q+pe^{it}}$ |
| PGF | q + p z {\displaystyle q+pz} ${\displaystyle q+pz}$ |
| Fisher information | 1 p q {\displaystyle {\frac {1}{pq}}} ${\displaystyle {\frac {1}{pq}}}$ |

In probability theory and statistics, the Bernoulli distribution, named after Swiss mathematician Jacob Bernoulli,[1] is the discrete probability distribution of a random variable which takes the value 1 with probability 

p

{\displaystyle p}

 and the value 0 with probability 
{\displaystyle q=1-p}

. Less formally, it can be thought of as a model for the set of possible outcomes of any single experiment that asks a yes–no question. Such questions lead to outcomes that are Boolean-valued: a single bit whose value is success/yes/true/one with probability p and failure/no/false/zero with probability q. It can be used to represent a (possibly biased) coin toss where 1 and 0 would represent "heads" and "tails", respectively, and p would be the probability of the coin landing on heads (or vice versa where 1 would represent tails and p would be the probability of tails).  In particular, unfair coins would have 
{\displaystyle p\neq 1/2.} ${\displaystyle p}$ ${\displaystyle q=1-p}$ ${\displaystyle p\neq 1/2.}$

The Bernoulli distribution is a special case of the binomial distribution where a single trial is conducted (so n would be 1 for such a binomial distribution). It is also a special case of the two-point distribution, for which the possible outcomes need not be 0 and 1.[2]

Properties[edit]
{\displaystyle X}

 is a random variable with a Bernoulli distribution, then:
{\displaystyle {\begin{aligned}\Pr(X{=}1)&=p,\\\Pr(X{=}0)&=q=1-p.\end{aligned}}}

The probability mass function 

f

{\displaystyle f}

 of this distribution, over possible outcomes k, is[3]
{\displaystyle f(k;p)={\begin{cases}p&{\text{if }}k=1,\\q=1-p&{\text{if }}k=0.\end{cases}}}

This can also be expressed as
{\displaystyle f(k;p)=p^{k}(1-p)^{1-k}\quad {\text{for }}k\in \{0,1\}}

or as
{\displaystyle f(k;p)=pk+(1-p)(1-k)\quad {\text{for }}k\in \{0,1\}.}

The Bernoulli distribution is a special case of the binomial distribution with 
{\displaystyle n=1.}

[4]
The kurtosis goes to infinity for high and low values of 
{\displaystyle p,}

 but for 
{\displaystyle p=1/2}

 the two-point distributions including the Bernoulli distribution have a lower excess kurtosis, namely −2, than any other probability distribution.
The Bernoulli distributions for 
{\displaystyle 0\leq p\leq 1}

 form an exponential family.
The maximum likelihood estimator of 

p

{\displaystyle p}

 based on a random sample is the sample mean.

The probability mass distribution function of a Bernoulli experiment along with its corresponding cumulative distribution function
Mean[edit]
The expected value of a Bernoulli random variable 

X

{\displaystyle X}
{\displaystyle \operatorname {E} [X]=p}

This is because for a Bernoulli distributed random variable 

X

{\displaystyle X}

 with 
{\displaystyle \Pr(X{=}1)=p}

 and 

Pr
(
X

=

0
)
=
q

{\textstyle \Pr(X{=}0)=q}

 we find[3]
{\displaystyle {\begin{aligned}\operatorname {E} [X]&=\Pr(X{=}1)\cdot 1+\Pr(X{=}0)\cdot 0\\[1ex]&=p\cdot 1+q\cdot 0\\[1ex]&=p.\end{aligned}}}

Variance[edit]
The variance of a Bernoulli distributed 

X

{\displaystyle X}
{\displaystyle \operatorname {Var} [X]=pq=p(1-p)}

We first find
{\displaystyle {\begin{aligned}\operatorname {E} [X^{2}]&=\Pr(X{=}1)\cdot 1^{2}+\Pr(X{=}0)\cdot 0^{2}\\&=p\cdot 1^{2}+q\cdot 0^{2}\\&=p=\operatorname {E} [X]\end{aligned}}}

From this follows[3]
{\displaystyle {\begin{aligned}\operatorname {Var} [X]&=\operatorname {E} [X^{2}]-\operatorname {E} [X]^{2}=\operatorname {E} [X]-\operatorname {E} [X]^{2}\\[1ex]&=p-p^{2}=p(1-p)=pq\end{aligned}}}

With this result it is easy to prove that, for any Bernoulli distribution, its variance will have a value inside 
{\displaystyle [0,1/4]}

.

Skewness[edit]
The skewness is 
{\displaystyle {\frac {q-p}{\sqrt {pq}}}={\frac {1-2p}{\sqrt {pq}}}}

. When we take the standardized Bernoulli distributed random variable 
{\displaystyle {\frac {X-\operatorname {E} [X]}{\sqrt {\operatorname {Var} [X]}}}}

 we find that this random variable attains 
{\displaystyle {\frac {q}{\sqrt {pq}}}}

 with probability 

p

{\displaystyle p}

 and attains 
{\displaystyle -{\frac {p}{\sqrt {pq}}}}

 with probability 

q

{\displaystyle q}

. Thus we get
{\displaystyle {\begin{aligned}\gamma _{1}&=\operatorname {E} \left[\left({\frac {X-\operatorname {E} [X]}{\sqrt {\operatorname {Var} [X]}}}\right)^{3}\right]\\&=p\cdot \left({\frac {q}{\sqrt {pq}}}\right)^{3}+q\cdot \left(-{\frac {p}{\sqrt {pq}}}\right)^{3}\\&={\frac {1}{{\sqrt {pq}}^{3}}}\left(pq^{3}-qp^{3}\right)\\&={\frac {pq}{{\sqrt {pq}}^{3}}}(q^{2}-p^{2})\\&={\frac {(1-p)^{2}-p^{2}}{\sqrt {pq}}}\\&={\frac {1-2p}{\sqrt {pq}}}={\frac {q-p}{\sqrt {pq}}}.\end{aligned}}}

Higher moments and cumulants[edit]
The raw moments are all equal because 
{\displaystyle 1^{k}=1}
{\displaystyle 0^{k}=0}
{\displaystyle \operatorname {E} [X^{k}]=\Pr(X{=}1)\cdot 1^{k}+\Pr(X{=}0)\cdot 0^{k}=p\cdot 1+q\cdot 0=p=\operatorname {E} [X].}

The central moment of order 

k

{\displaystyle k}

 is given by
{\displaystyle \mu _{k}=(1-p)(-p)^{k}+p(1-p)^{k}.}

The first six central moments are
{\displaystyle {\begin{aligned}\mu _{1}&=0,\\\mu _{2}&=p(1-p),\\\mu _{3}&=p(1-p)(1-2p),\\\mu _{4}&=p(1-p)(1-3p(1-p)),\\\mu _{5}&=p(1-p)(1-2p)(1-2p(1-p)),\\\mu _{6}&=p(1-p)(1-5p(1-p)(1-p(1-p))).\end{aligned}}}

The higher central moments can be expressed more compactly in terms of 
{\displaystyle \mu _{2}}
{\displaystyle \mu _{3}}
{\displaystyle {\begin{aligned}\mu _{4}&=\mu _{2}(1-3\mu _{2}),\\\mu _{5}&=\mu _{3}(1-2\mu _{2}),\\\mu _{6}&=\mu _{2}(1-5\mu _{2}(1-\mu _{2})).\end{aligned}}}

The first six cumulants are
{\displaystyle {\begin{aligned}\kappa _{1}&=p,\\\kappa _{2}&=\mu _{2},\\\kappa _{3}&=\mu _{3},\\\kappa _{4}&=\mu _{2}(1-6\mu _{2}),\\\kappa _{5}&=\mu _{3}(1-12\mu _{2}),\\\kappa _{6}&=\mu _{2}(1-30\mu _{2}(1-4\mu _{2})).\end{aligned}}}

Entropy and Fisher's Information[edit]
Entropy[edit]
Entropy is a measure of uncertainty or randomness in a probability distribution. For a Bernoulli random variable 

X

{\displaystyle X}

 with success probability 

p

{\displaystyle p}

 and failure probability 
{\displaystyle q=1-p}

, the entropy 
{\displaystyle H(X)}

 is defined as:
{\displaystyle {\begin{aligned}H(X)&=\mathbb {E} _{p}\ln {\frac {1}{\Pr(X)}}\\[1ex]&=-\Pr(X{=}0)\ln \Pr(X{=}0)-\Pr(X{=}1)\ln \Pr(X{=}1)\\[1ex]&=-(q\ln q+p\ln p).\end{aligned}}}

The entropy is maximized when 
{\displaystyle p=0.5}

, indicating the highest level of uncertainty when both outcomes are equally likely. The entropy is zero when 
{\displaystyle p=0}
{\displaystyle p=1}

, where one outcome is certain.

Fisher's Information[edit]
Fisher information measures the amount of information that an observable random variable 

X

{\displaystyle X}

 carries about an unknown parameter 

p

{\displaystyle p}

 upon which the probability of 

X

{\displaystyle X}

 depends. For the Bernoulli distribution, the Fisher information with respect to the parameter 

p

{\displaystyle p}

 is given by:
{\displaystyle I(p)={\frac {1}{pq}}}

Proof:

The Likelihood Function for a Bernoulli random variable

X

{\displaystyle X}
{\displaystyle L(p;X)=p^{X}(1-p)^{1-X}}

 This represents the probability of observing 

X

{\displaystyle X}

 given the parameter 

p

{\displaystyle p}

.
The Log-Likelihood Function is: 
{\displaystyle \ln L(p;X)=X\ln p+(1-X)\ln(1-p)}

The Score Function (the first derivative of the log-likelihood with respect to 

p

{\displaystyle p}
{\displaystyle {\frac {\partial }{\partial p}}\ln L(p;X)={\frac {X}{p}}-{\frac {1-X}{1-p}}}

The second derivative of the log-likelihood function is: 
{\displaystyle {\frac {\partial ^{2}}{\partial p^{2}}}\ln L(p;X)=-{\frac {X}{p^{2}}}-{\frac {1-X}{(1-p)^{2}}}}

Fisher information is calculated as the negative expected value of the second derivative of the log-likelihood:
{\displaystyle {\begin{aligned}I(p)=-E\left[{\frac {\partial ^{2}}{\partial p^{2}}}\ln L(p;X)\right]=-\left(-{\frac {p}{p^{2}}}-{\frac {1-p}{(1-p)^{2}}}\right)={\frac {1}{p(1-p)}}={\frac {1}{pq}}\end{aligned}}}

It is maximized when 
{\displaystyle p=0.5}

, reflecting maximum uncertainty and thus maximum information about the parameter 

p

{\displaystyle p}

.

Related distributions[edit]
{\displaystyle X_{1},\dots ,X_{n}}

 are independent, identically distributed  (i.i.d.)  random variables, all Bernoulli trials with success probability p, then their sum is distributed according to a binomial distribution with parameters n and p:
{\displaystyle \sum _{k=1}^{n}X_{k}\sim \operatorname {B} (n,p)}

 (binomial distribution).[3]
The Bernoulli distribution is simply 
{\displaystyle \operatorname {B} (1,p)}

, also written as 

B
e
r
n
o
u
l
l
i

(
p
)
.

{\textstyle \mathrm {Bernoulli} (p).}

The categorical distribution is the generalization of the Bernoulli distribution for variables with any constant number of discrete values.
The Beta distribution is the conjugate prior of the Bernoulli distribution.[5]
The geometric distribution models the number of independent and identical Bernoulli trials needed to get one success.
If 

Y
∼

B
e
r
n
o
u
l
l
i

(

1
2

)

{\textstyle Y\sim \mathrm {Bernoulli} \left({\frac {1}{2}}\right)}

, then 

2
Y
−
1

{\textstyle 2Y-1}

 has a Rademacher distribution.
