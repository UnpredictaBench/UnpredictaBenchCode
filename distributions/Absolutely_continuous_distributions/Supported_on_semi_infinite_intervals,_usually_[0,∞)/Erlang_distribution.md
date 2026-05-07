# Erlang distribution

Family of continuous probability distributions

This article is about the mathematical / statistical distribution concept. For other uses, see Erlang.

| Erlang |
| --- |
| Probability density function |
| Cumulative distribution function |
| Parameters | k ∈ { 1 , 2 , 3 , … } , {\displaystyle k\in \{1,2,3,\ldots \},} shape λ ∈ ( 0 , ∞ ) , {\displaystyle \lambda \in (0,\infty ),} rate alt.: β = 1 / λ , {\displaystyle \beta =1/\lambda ,} scale ${\displaystyle k\in \{1,2,3,\ldots \},}$ ${\displaystyle \lambda \in (0,\infty ),}$ ${\displaystyle \beta =1/\lambda ,}$ |
| Support | x ∈ [ 0 , ∞ ) {\displaystyle x\in [0,\infty )} ${\displaystyle x\in [0,\infty )}$ |
| PDF | λ k x k − 1 e − λ x ( k − 1 ) ! {\displaystyle {\frac {\lambda ^{k}x^{k-1}e^{-\lambda x}}{(k-1)!}}} ${\displaystyle {\frac {\lambda ^{k}x^{k-1}e^{-\lambda x}}{(k-1)!}}}$ |
| CDF | P ( k , λ x ) = γ ( k , λ x ) ( k − 1 ) ! = 1 − ∑ n = 0 k − 1 1 n ! e − λ x ( λ x ) n {\displaystyle P(k,\lambda x)={\frac {\gamma (k,\lambda x)}{(k-1)!}}=1-\sum _{n=0}^{k-1}{\frac {1}{n!}}e^{-\lambda x}(\lambda x)^{n}} ${\displaystyle P(k,\lambda x)={\frac {\gamma (k,\lambda x)}{(k-1)!}}=1-\sum _{n=0}^{k-1}{\frac {1}{n!}}e^{-\lambda x}(\lambda x)^{n}}$ |
| Mean | k λ {\displaystyle {\frac {k}{\lambda }}} ${\displaystyle {\frac {k}{\lambda }}}$ |
| Median | No simple closed form |
| Mode | 1 λ ( k − 1 ) {\displaystyle {\frac {1}{\lambda }}(k-1)} ${\displaystyle {\frac {1}{\lambda }}(k-1)}$ |
| Variance | k λ 2 {\displaystyle {\frac {k}{\lambda ^{2}}}} ${\displaystyle {\frac {k}{\lambda ^{2}}}}$ |
| Skewness | 2 k {\displaystyle {\frac {2}{\sqrt {k}}}} ${\displaystyle {\frac {2}{\sqrt {k}}}}$ |
| Excess kurtosis | 6 k {\displaystyle {\frac {6}{k}}} ${\displaystyle {\frac {6}{k}}}$ |
| Entropy | ( 1 − k ) ψ ( k ) + ln ⁡ [ Γ ( k ) λ ] + k {\displaystyle (1-k)\psi (k)+\ln \left[{\frac {\Gamma (k)}{\lambda }}\right]+k} ${\displaystyle (1-k)\psi (k)+\ln \left[{\frac {\Gamma (k)}{\lambda }}\right]+k}$ |
| MGF | ( 1 − t λ ) − k {\displaystyle \left(1-{\frac {t}{\lambda }}\right)^{-k}} for t < λ {\displaystyle t<\lambda } ${\displaystyle \left(1-{\frac {t}{\lambda }}\right)^{-k}}$ ${\displaystyle t<\lambda }$ |
| CF | ( 1 − i t λ ) − k {\displaystyle \left(1-{\frac {it}{\lambda }}\right)^{-k}} ${\displaystyle \left(1-{\frac {it}{\lambda }}\right)^{-k}}$ |

The Erlang distribution is a two-parameter family of continuous probability distributions with support 
{\displaystyle x\in [0,\infty )}

. The two parameters are: ${\displaystyle x\in [0,\infty )}$

- a positive integer 
{\displaystyle k,}

 the "shape", and ${\displaystyle k,}$
- a positive real number 
{\displaystyle \lambda ,}

 the "rate". The "scale", 
{\displaystyle \beta ,}

 the reciprocal of the rate, is sometimes used instead. ${\displaystyle \lambda ,}$ ${\displaystyle \beta ,}$

The Erlang distribution is the distribution of a sum of 

k

{\displaystyle k}

 independent exponential variables with mean 
{\displaystyle 1/\lambda }

 each.  Equivalently, it is the distribution of the time until the kth event of a Poisson process with a rate of 

λ

{\displaystyle \lambda }

.  The Erlang and Poisson distributions are complementary, in that while the Poisson distribution counts the events that occur in a fixed amount of time, the Erlang distribution counts the amount of time until the occurrence of a fixed number of events.  When 
{\displaystyle k=1}

, the distribution  simplifies to the exponential distribution. The Erlang distribution is a special case of the gamma distribution in which the shape of the distribution is discretized. ${\displaystyle k}$ ${\displaystyle 1/\lambda }$ ${\displaystyle \lambda }$ ${\displaystyle k=1}$

The Erlang distribution was developed by A. K. Erlang to examine the number of telephone calls that might be made at the same time to the operators of the switching stations. This work on telephone traffic engineering has been expanded to consider waiting times in queueing systems in general. The distribution is also used in the field of stochastic processes.

Characterization[edit]
Probability density function[edit]
The probability density function of the Erlang distribution is
{\displaystyle f(x;k,\lambda )={\lambda ^{k}x^{k-1}e^{-\lambda x} \over (k-1)!}\quad {\mbox{for }}x,\lambda \geq 0,}

The parameter k is called the shape parameter, and the parameter 

λ

{\displaystyle \lambda }

 is called the rate parameter.
An alternative, but equivalent, parametrization uses the scale parameter 

β

{\displaystyle \beta }

, which is the reciprocal of the rate parameter (i.e., 
{\displaystyle \beta =1/\lambda }
{\displaystyle f(x;k,\beta )={\frac {x^{k-1}e^{-{\frac {x}{\beta }}}}{\beta ^{k}(k-1)!}}\quad {\mbox{for }}x,\beta \geq 0.}

When the scale parameter 

β

{\displaystyle \beta }

 equals 2, the distribution simplifies to the chi-squared distribution with 2k degrees of freedom. It can therefore be regarded as a generalized chi-squared distribution for even numbers of degrees of freedom.

Cumulative distribution function (CDF)[edit]
The cumulative distribution function of the Erlang distribution is
{\displaystyle F(x;k,\lambda )=P(k,\lambda x)={\frac {\gamma (k,\lambda x)}{\Gamma (k)}}={\frac {\gamma (k,\lambda x)}{(k-1)!}},}

where 

γ

{\displaystyle \gamma }

 is the lower incomplete gamma function and 

P

{\displaystyle P}

 is the lower regularized gamma function.
The CDF may also be expressed as
{\displaystyle F(x;k,\lambda )=1-\sum _{n=0}^{k-1}{\frac {1}{n!}}e^{-\lambda x}(\lambda x)^{n}.}

Erlang-k[edit]
The Erlang-k distribution (where k is a positive integer) 
{\displaystyle E_{k}(\lambda )}

 is defined by setting k in the PDF of the Erlang distribution.[1] For instance, the Erlang-2 distribution is 
{\displaystyle E_{2}(\lambda )={\lambda ^{2}x}e^{-\lambda x}\quad {\mbox{for }}x,\lambda \geq 0}

, which is the same as 
{\displaystyle f(x;2,\lambda )}

.

Median[edit]
An asymptotic expansion is known for the median of an Erlang distribution,[2] for which coefficients can be computed and bounds are known.[3][4] An approximation is 
{\displaystyle {\frac {k}{\lambda }}\left(1-{\dfrac {1}{3k+0.2}}\right),}

 i.e. below the mean 
{\displaystyle {\frac {k}{\lambda }}.}

[5]

Generating Erlang-distributed random variates[edit]
Erlang-distributed random variates can be generated from uniformly distributed random numbers (
{\displaystyle U\in [0,1]}

) using the following formula:[6]
{\displaystyle E(k,\lambda )=-{\frac {1}{\lambda }}\ln \prod _{i=1}^{k}U_{i}=-{\frac {1}{\lambda }}\sum _{i=1}^{k}\ln U_{i}}

Applications[edit]
Waiting times[edit]
Events that occur independently with some average rate are modeled with a Poisson process.  The waiting times between k occurrences of the event are Erlang distributed.  (The related question of the number of events in a given amount of time is described by the Poisson distribution.)
The Erlang distribution, which measures the time between incoming calls, can be used in conjunction with the expected duration of incoming calls to produce information about the traffic load measured in erlangs.  This can be used to determine the probability of packet loss or delay, according to various assumptions made about whether blocked calls are aborted (Erlang B formula) or queued until served (Erlang C formula).  The Erlang-B and C formulae are still in everyday use for traffic modeling for applications such as the design of call centers.

Other applications[edit]
The age distribution of cancer incidence often follows the Erlang distribution, whereas the shape and scale parameters predict, respectively, the number of driver events  and the time interval between them.[7][8] More generally, the Erlang distribution has been suggested as good approximation of cell cycle time distribution, as result of multi-stage models.[9][10]
The kinesin is a molecular machine with two "feet" that "walks" along a filament. The waiting time between each step is exponentially distributed. When green fluorescent protein is attached to a foot of the kinesin, then the green dot visibly moves with Erlang distribution of k = 2.[11]
It has also been used in marketing for describing interpurchase times.[12]

Properties[edit]
If 

X
∼
Erlang
{\displaystyle X\sim \operatorname {Erlang} (k,\lambda )}

 then 

a
⋅
X
∼
Erlang
{\displaystyle a\cdot X\sim \operatorname {Erlang} \left(k,{\frac {\lambda }{a}}\right)}

 with 
{\displaystyle a\in \mathbb {R} }

If 

X
∼
Erlang
{\displaystyle X\sim \operatorname {Erlang} (k_{1},\lambda )}

 and 

Y
∼
Erlang
{\displaystyle Y\sim \operatorname {Erlang} (k_{2},\lambda )}

 then 

X
+
Y
∼
Erlang
{\displaystyle X+Y\sim \operatorname {Erlang} (k_{1}+k_{2},\lambda )}
{\displaystyle X,Y}

 are independent
Related distributions[edit]
The Erlang distribution is the distribution of the sum of k independent and identically distributed random variables, each having an exponential distribution. The long-run rate at which events occur is the reciprocal of the expectation of 
{\displaystyle X,}

 that is, 
{\displaystyle \lambda /k.}

 The (age specific event) rate of the Erlang distribution is, for 
{\displaystyle k>1,}

 monotonic in 
{\displaystyle x,}

 increasing from 0 at 
{\displaystyle x=0,}
{\displaystyle \lambda }
{\displaystyle x}

 tends to infinity.[13]
That is: if 

X

i

∼
Exponential
{\displaystyle X_{i}\sim \operatorname {Exponential} (\lambda ),}

 then 

∑

i
=
1

k

X

i

∼
Erlang
{\displaystyle \sum _{i=1}^{k}{X_{i}}\sim \operatorname {Erlang} (k,\lambda )}

Because of the factorial function in the denominator of the PDF and CDF, the Erlang distribution is only defined when the parameter k is a positive integer. In fact, this distribution is sometimes called the Erlang-k distribution (e.g., an Erlang-2 distribution is an Erlang distribution with 
{\displaystyle k=2}

). The gamma distribution generalizes the Erlang distribution by allowing k to be any positive real number, using the gamma function instead of the factorial function.
That is: if k is an integer and 

X
∼
Gamma
{\displaystyle X\sim \operatorname {Gamma} (k,\lambda ),}

 then 

X
∼
Erlang
{\displaystyle X\sim \operatorname {Erlang} (k,\lambda )}

If 

U
∼
Exponential
{\displaystyle U\sim \operatorname {Exponential} (\lambda )}

 and 

V
∼
Erlang
{\displaystyle V\sim \operatorname {Erlang} (n,\lambda )}

 then 

U
V

+
1
∼
Pareto
{\displaystyle {\frac {U}{V}}+1\sim \operatorname {Pareto} (1,n)}

The Erlang distribution is a special case of the Pearson type III distribution[citation needed]
The Erlang distribution is related to the chi-squared distribution. If 

X
∼
Erlang
{\displaystyle X\sim \operatorname {Erlang} (k,\lambda ),}

 then 
{\displaystyle 2\lambda X\sim \chi _{2k}^{2}.}

[citation needed]
The Erlang distribution is related to the Poisson distribution by the Poisson process: If 
{\displaystyle S_{n}=\sum _{i=1}^{n}X_{i}}

 such that 

X

i

∼
Exponential
{\displaystyle X_{i}\sim \operatorname {Exponential} (\lambda ),}

 then 

S

n

∼
Erlang
{\displaystyle S_{n}\sim \operatorname {Erlang} (n,\lambda )}
{\displaystyle \operatorname {Pr} (N(x)\leq n-1)=\operatorname {Pr} (S_{n}>x)=1-F_{X}(x;n,\lambda )=\sum _{k=0}^{n-1}{\frac {1}{k!}}e^{-\lambda x}(\lambda x)^{k}.}

 Taking the differences over 

n

{\displaystyle n}

 gives the Poisson distribution.
