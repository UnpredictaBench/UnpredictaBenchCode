# Discrete uniform distribution

Probability distribution on equally likely outcomes

| Discrete uniform |
| --- |
| Probability mass functionn = 5 where n = b − a + 1 |
| Cumulative distribution function |
| Notation | U { a , b } {\displaystyle {\mathcal {U}}\{a,b\}} or u n i f { a , b } {\displaystyle \mathrm {unif} \{a,b\}} ${\displaystyle {\mathcal {U}}\{a,b\}}$ ${\displaystyle \mathrm {unif} \{a,b\}}$ |
| Parameters | a , b {\displaystyle a,b} integers with b ≥ a {\displaystyle b\geq a} n = b − a + 1 {\displaystyle n=b-a+1} ${\displaystyle a,b}$ ${\displaystyle b\geq a}$ ${\displaystyle n=b-a+1}$ |
| Support | k ∈ { a , a + 1 , … , b − 1 , b } {\displaystyle k\in \{a,a+1,\dots ,b-1,b\}} ${\displaystyle k\in \{a,a+1,\dots ,b-1,b\}}$ |
| PMF | 1 n {\displaystyle {\frac {1}{n}}} ${\displaystyle {\frac {1}{n}}}$ |
| CDF | ⌊ k ⌋ − a + 1 n {\displaystyle {\frac {\lfloor k\rfloor -a+1}{n}}} ${\displaystyle {\frac {\lfloor k\rfloor -a+1}{n}}}$ |
| Mean | a + b 2 {\displaystyle {\frac {a+b}{2}}} ${\displaystyle {\frac {a+b}{2}}}$ |
| Median | a + b 2 {\displaystyle {\frac {a+b}{2}}} ${\displaystyle {\frac {a+b}{2}}}$ |
| Mode | N/A |
| Variance | ( b − a + 1 ) 2 − 1 12 {\displaystyle {\frac {(b-a+1)^{2}-1}{12}}} ${\displaystyle {\frac {(b-a+1)^{2}-1}{12}}}$ |
| Skewness | 0 {\displaystyle 0} ${\displaystyle 0}$ |
| Excess kurtosis | − 6 ( n 2 + 1 ) 5 ( n 2 − 1 ) {\displaystyle -{\frac {6(n^{2}+1)}{5(n^{2}-1)}}} ${\displaystyle -{\frac {6(n^{2}+1)}{5(n^{2}-1)}}}$ |
| Entropy | ln ⁡ ( n ) {\displaystyle \ln(n)} ${\displaystyle \ln(n)}$ |
| MGF | e a t − e ( b + 1 ) t n ( 1 − e t ) {\displaystyle {\frac {e^{at}-e^{(b+1)t}}{n(1-e^{t})}}} ${\displaystyle {\frac {e^{at}-e^{(b+1)t}}{n(1-e^{t})}}}$ |
| CF | e i a t − e i ( b + 1 ) t n ( 1 − e i t ) {\displaystyle {\frac {e^{iat}-e^{i(b+1)t}}{n(1-e^{it})}}} ${\displaystyle {\frac {e^{iat}-e^{i(b+1)t}}{n(1-e^{it})}}}$ |
| PGF | z a − z b + 1 n ( 1 − z ) {\displaystyle {\frac {z^{a}-z^{b+1}}{n(1-z)}}} ${\displaystyle {\frac {z^{a}-z^{b+1}}{n(1-z)}}}$ |

In probability theory and statistics, the discrete uniform distribution is a symmetric probability distribution wherein each of some finite whole number n of outcome values are equally likely to be observed. Thus every one of the n outcome values has equal probability 1/n. Intuitively, a discrete uniform distribution is "a known, finite number of outcomes all equally likely to happen."

A simple example of the discrete uniform distribution comes from throwing a fair six-sided die. The possible values are 1, 2, 3, 4, 5, 6, and each time the die is thrown the probability of each given value is 1/6. If two dice were thrown and their values added, the possible sums would not have equal probability and so the distribution of sums of two dice rolls is not uniform.

Although it is common to consider discrete uniform distributions over a contiguous range of integers, such as in this six-sided die example, one can define discrete uniform distributions over any finite set. For instance, the six-sided die could have abstract symbols rather than numbers on each of its faces. Less simply, a random permutation is a permutation generated uniformly randomly from the permutations of a given set and a uniform spanning tree of a graph is a spanning tree selected with uniform probabilities from the full set of spanning trees of the graph.

The discrete uniform distribution itself is non-parametric. However, in the common case that its possible outcome values are the integers in an interval 

[
a
,
b
]

{\textstyle [a,b]}

, then a and b are parameters of the distribution and 

n
=
b
−
a
+
1.

{\textstyle n=b-a+1.}

 In these cases the cumulative distribution function (CDF) of the discrete uniform distribution can be expressed, for any k, as ${\textstyle [a,b]}$ ${\textstyle n=b-a+1.}$
{\displaystyle F(k;a,b)=\min \left(\max \left({\frac {\lfloor k\rfloor -a+1}{b-a+1}},0\right),1\right),} ${\displaystyle F(k;a,b)=\min \left(\max \left({\frac {\lfloor k\rfloor -a+1}{b-a+1}},0\right),1\right),}$

or simply
{\displaystyle F(k;a,b)={\frac {\lfloor k\rfloor -a+1}{b-a+1}}} ${\displaystyle F(k;a,b)={\frac {\lfloor k\rfloor -a+1}{b-a+1}}}$

on the distribution's support 

k
∈
[
a
,
b
]
.

{\textstyle k\in [a,b].} ${\textstyle k\in [a,b].}$

Estimation of maximum[edit]
Main article: German tank problem
The problem of estimating the maximum 

N

{\displaystyle N}

 of a discrete uniform distribution on the integer interval 
{\displaystyle [1,N]}

 from a sample of k observations is commonly known as the German tank problem, following the practical application of this maximum estimation problem, during World War II, by Allied forces seeking to estimate German tank production.
A uniformly minimum variance unbiased (UMVU) estimator for the distribution's maximum in terms of m, the sample maximum, and k, the sample size, is[1]
{\displaystyle {\hat {N}}={\frac {k+1}{k}}m-1=m+{\frac {m}{k}}-1.}

This can be seen as a very simple case of maximum spacing estimation.
This has a variance of[1]

1
k

(
N
−
k
)
(
N
+
1
)

(
k
+
2
)

≈

N

2

k

2

 for small samples 
{\displaystyle {\frac {1}{k}}{\frac {(N-k)(N+1)}{(k+2)}}\approx {\frac {N^{2}}{k^{2}}}{\text{ for small samples }}k\ll N}

so a standard deviation of approximately 
{\displaystyle {\tfrac {N}{k}}}

, the population-average gap size between samples.
The sample maximum 

m

{\displaystyle m}

 itself is the maximum likelihood estimator for the population maximum, but it is biased.
If samples from a discrete uniform distribution are not numbered in order but are recognizable or markable, one can instead estimate population size via a mark and recapture method.

Random permutation[edit]
Main article: Random permutation
See rencontres numbers for an account of the probability distribution of the number of fixed points of a uniformly distributed random permutation.

Properties[edit]
The family of uniform discrete distributions over ranges of integers with one or both bounds unknown has a finite-dimensional sufficient statistic, namely the triple of the sample maximum, sample minimum, and sample size.
Uniform discrete distributions over bounded integer ranges do not constitute an exponential family of distributions because their support varies with their parameters.
For families of distributions in which their supports do not depend on their parameters, the Pitman–Koopman–Darmois theorem states that only exponential families have sufficient statistics of dimensions that are bounded as sample size increases. The uniform distribution is thus a simple example showing the necessity of the conditions for this theorem.
