# Poisson binomial distribution

Probability distribution

| Poisson binomial |
| --- |
| Parameters | p ∈ [ 0 , 1 ] n {\displaystyle \mathbf {p} \in [0,1]^{n}} — success probabilities for each of the n trials ${\displaystyle \mathbf {p} \in [0,1]^{n}}$ |
| Support | k ∈ { 0, …, n } |
| PMF | ∑ A ∈ F k ∏ i ∈ A p i ∏ j ∈ A c ( 1 − p j ) {\displaystyle \sum \limits _{A\in F_{k}}\prod \limits _{i\in A}p_{i}\prod \limits _{j\in A^{c}}(1-p_{j})} ${\displaystyle \sum \limits _{A\in F_{k}}\prod \limits _{i\in A}p_{i}\prod \limits _{j\in A^{c}}(1-p_{j})}$ |
| CDF | ∑ l = 0 k ∑ A ∈ F l ∏ i ∈ A p i ∏ j ∈ A c ( 1 − p j ) {\displaystyle \sum \limits _{l=0}^{k}\sum \limits _{A\in F_{l}}\prod \limits _{i\in A}p_{i}\prod \limits _{j\in A^{c}}(1-p_{j})} ${\displaystyle \sum \limits _{l=0}^{k}\sum \limits _{A\in F_{l}}\prod \limits _{i\in A}p_{i}\prod \limits _{j\in A^{c}}(1-p_{j})}$ |
| Mean | ∑ i = 1 n p i {\displaystyle \sum \limits _{i=1}^{n}p_{i}} ${\displaystyle \sum \limits _{i=1}^{n}p_{i}}$ |
| Variance | σ 2 = ∑ i = 1 n ( 1 − p i ) p i {\displaystyle \sigma ^{2}=\sum \limits _{i=1}^{n}(1-p_{i})p_{i}} ${\displaystyle \sigma ^{2}=\sum \limits _{i=1}^{n}(1-p_{i})p_{i}}$ |
| Skewness | 1 σ 3 ∑ i = 1 n ( 1 − 2 p i ) ( 1 − p i ) p i {\displaystyle {\frac {1}{\sigma ^{3}}}\sum \limits _{i=1}^{n}(1-2p_{i})(1-p_{i})p_{i}} ${\displaystyle {\frac {1}{\sigma ^{3}}}\sum \limits _{i=1}^{n}(1-2p_{i})(1-p_{i})p_{i}}$ |
| Excess kurtosis | 1 σ 4 ∑ i = 1 n ( 1 − 6 ( 1 − p i ) p i ) ( 1 − p i ) p i {\displaystyle {\frac {1}{\sigma ^{4}}}\sum \limits _{i=1}^{n}(1-6(1-p_{i})p_{i})(1-p_{i})p_{i}} ${\displaystyle {\frac {1}{\sigma ^{4}}}\sum \limits _{i=1}^{n}(1-6(1-p_{i})p_{i})(1-p_{i})p_{i}}$ |
| MGF | ∏ j = 1 n ( 1 − p j + p j e t ) {\displaystyle \prod \limits _{j=1}^{n}(1-p_{j}+p_{j}e^{t})} ${\displaystyle \prod \limits _{j=1}^{n}(1-p_{j}+p_{j}e^{t})}$ |
| CF | ∏ j = 1 n ( 1 − p j + p j e i t ) {\displaystyle \prod \limits _{j=1}^{n}(1-p_{j}+p_{j}e^{it})} ${\displaystyle \prod \limits _{j=1}^{n}(1-p_{j}+p_{j}e^{it})}$ |
| PGF | ∏ j = 1 n ( 1 − p j + p j z ) {\displaystyle \prod \limits _{j=1}^{n}(1-p_{j}+p_{j}z)} ${\displaystyle \prod \limits _{j=1}^{n}(1-p_{j}+p_{j}z)}$ |

In probability theory and statistics, the Poisson binomial distribution  is the discrete probability distribution of a sum of independent Bernoulli trials that are not necessarily identically distributed.  The concept is named after Siméon Denis Poisson.

In other words, it is the probability distribution of the
number of successes in a collection of n independent yes/no experiments with success probabilities 
{\displaystyle p_{1},p_{2},\dots ,p_{n}}

.  The ordinary binomial distribution is a special case of the Poisson binomial distribution, when all success probabilities are the same, that is 
{\displaystyle p_{1}=p_{2}=\cdots =p_{n}}

. ${\displaystyle p_{1},p_{2},\dots ,p_{n}}$ ${\displaystyle p_{1}=p_{2}=\cdots =p_{n}}$

Definitions[edit]
Probability mass function[edit]
The probability of having k successful trials out of a total of n can be written as the sum
{\displaystyle \Pr(K=k)=\sum \limits _{A\in F_{k}}\prod \limits _{i\in A}p_{i}\prod \limits _{j\in A^{c}}(1-p_{j})}

where 
{\displaystyle F_{k}}

 is the set of all subsets of k integers that can be selected from 
{\displaystyle \{1,2,3,...,n\}}

. For example, if n = 3, then 
{\displaystyle F_{2}=\left\{\{1,2\},\{1,3\},\{2,3\}\right\}}
{\displaystyle A^{c}}

 is the complement of 

A

{\displaystyle A}
{\displaystyle A^{c}=\{1,2,3,\dots ,n\}\smallsetminus A}
{\displaystyle F_{k}}

 will contain 
{\displaystyle n!/((n-k)!k!)}

 elements, the sum over which is infeasible to compute in practice unless the number of trials n is small (e.g. if n = 30, 
{\displaystyle F_{15}}

 contains over 1020 elements). However, there are other, more efficient ways to calculate 
{\displaystyle \Pr(K=k)}

.
As long as none of the success probabilities are equal to one, one can calculate the probability of k successes using the recursive formula 
{\displaystyle \Pr(K=k)={\begin{cases}\prod \limits _{i=1}^{n}(1-p_{i})&k=0\\{\frac {1}{k}}\sum \limits _{i=1}^{k}(-1)^{i-1}\Pr(K=k-i)T(i)&k>0\\\end{cases}}}

where
{\displaystyle T(i)=\sum \limits _{j=1}^{n}\left({\frac {p_{j}}{1-p_{j}}}\right)^{i}.}

The recursive formula is not numerically stable, and should be avoided if 

n

{\displaystyle n}

 is greater than approximately 20. 
An alternative is to use a divide-and-conquer algorithm: if we assume 
{\displaystyle n=2^{b}}

 is a power of two, denoting by 
{\displaystyle f(p_{i:j})}

 the Poisson binomial of 
{\displaystyle p_{i},\dots ,p_{j}}
{\displaystyle *}

 the convolution operator, we have 
{\displaystyle f(p_{1:2^{b}})=f(p_{1:2^{b-1}})*f(p_{2^{b-1}+1:2^{b}})}

. 
More generally, the probability mass function of a Poisson binomial can be expressed as the convolution of the vectors 
{\displaystyle P_{1},\dots ,P_{n}}

 where 
{\displaystyle P_{i}=[1-p_{i},p_{i}]}

. This observation leads to the direct convolution (DC) algorithm for computing 
{\displaystyle \Pr(K=0)}

 through 
{\displaystyle \Pr(K=n)}

:

// PMF and nextPMF begin at index 0
function DC(
    {\displaystyle p_{1},\dots ,p_{n}}

) is 
     declare new PMF array of size 1
     PMF[0] = [1]
     for i = 1 to 
    {\displaystyle n}

 do 
          declare new nextPMF array of size i + 1
          nextPMF[0] = (1 - 
    {\displaystyle p_{i}}

) * PMF[0]
          nextPMF[i] = 
    {\displaystyle p_{i}}

 * PMF[i - 1]
          for k = 1 to i - 1 do
               nextPMF[k] = 
    {\displaystyle p_{i}}
    {\displaystyle p_{i}}

) * PMF[k]
          repeat
          PMF = nextPMF
     repeat
     return PMF
end function
{\displaystyle \Pr(K=k)}

will be found in PMF[k]. DC is numerically stable, exact, and, when implemented as a software routine, exceptionally fast for 

n
≤
2000

{\displaystyle n\leq 2000}

. It can also be quite fast for larger 

n

{\displaystyle n}

, depending on the distribution of the 
{\displaystyle p_{i}}

.[4]
Another possibility is using the discrete Fourier transform.[5]
{\displaystyle \Pr(K=k)={\frac {1}{n+1}}\sum _{\ell =0}^{n}C^{-lk}\prod _{m=1}^{n}\left(1+(C^{\ell }-1)p_{m}\right)}

where 
{\displaystyle C=\exp \left({\frac {2i\pi }{n+1}}\right)}
{\displaystyle i={\sqrt {-1}}}

.
Still other methods are described in "Statistical Applications of the Poisson-Binomial and conditional Bernoulli distributions" by Chen and Liu[6] and in "A simple and fast method for computing the Poisson binomial distribution function" by Biscarri et al.[4]

Cumulative distribution function[edit]
The cumulative distribution function (CDF) can be expressed as:
{\displaystyle \Pr(K\leq k)=\sum _{\ell =0}^{k}\sum _{A\in F_{\ell }}\prod _{i\in A}p_{i}\prod _{j\in A^{c}}(1-p_{j}),}

where 
{\displaystyle F_{\ell }}

 is the set of all subsets of size 

ℓ

{\displaystyle \ell }

 that can be selected from 
{\displaystyle \{1,2,3,\ldots ,n\}}

.
It can be computed by invoking the DC function above, and then adding elements 

0

{\displaystyle 0}

 through 

k

{\displaystyle k}

 of the returned PMF array. 

Properties[edit]
Mean and variance[edit]
Since a Poisson binomial distributed variable is a sum of n independent Bernoulli distributed variables, its mean and variance will simply be sums of the mean and variance of the n Bernoulli distributions:
{\displaystyle \mu =\sum \limits _{i=1}^{n}p_{i}}
{\displaystyle \sigma ^{2}=\sum \limits _{i=1}^{n}(1-p_{i})p_{i}}

Entropy[edit]
There is no simple formula for the entropy of a Poisson binomial distribution, but the entropy is bounded above by the entropy of a binomial distribution with the same number parameter and the same mean. Therefore, the entropy is also bounded above by the entropy of a Poisson distribution with the same mean.[7]
The Shepp–Olkin concavity conjecture, due to Lawrence Shepp and Ingram Olkin in 1981, states that the entropy of a Poisson binomial distribution is a concave function of the success probabilities 
{\displaystyle p_{1},p_{2},\dots ,p_{n}}

.[8] This conjecture was proved by Erwan Hillion and Oliver Johnson in 2015.[9] The Shepp–Olkin monotonicity conjecture, also from the same 1981 paper, is that the entropy is monotone increasing in 
{\displaystyle p_{i}}

, if all 
{\displaystyle p_{i}\leq 1/2}

. This conjecture was also proved by Hillion and Johnson, in 2019.[10]

Chernoff bound[edit]
The probability that a Poisson binomial distribution gets large, can be bounded using its moment generating function as follows (valid when 
{\displaystyle s\geq \mu }

 and for any 
{\displaystyle t>0}
{\displaystyle {\begin{aligned}\Pr[S\geq s]&\leq \exp(-st)\operatorname {E} \left[\exp \left[t\sum _{i}X_{i}\right]\right]\\&=\exp(-st)\prod _{i}(1-p_{i}+e^{t}p_{i})\\&=\exp \left(-st+\sum _{i}\log \left(p_{i}(e^{t}-1)+1\right)\right)\\&\leq \exp \left(-st+\sum _{i}\log \left(\exp(p_{i}(e^{t}-1))\right)\right)\\&=\exp \left(-st+\sum _{i}p_{i}(e^{t}-1)\right)\\&=\exp \left(s-\mu -s\log {\frac {s}{\mu }}\right),\end{aligned}}}

where we took 

t
=
log
⁡

(

s

/

μ

)

{\textstyle t=\log \left(s/\mu \right)}

. This is similar to the tail bounds of a binomial distribution.

Related distribution[edit]
Approximation by binomial distribution[edit]
A Poisson binomial distribution 
{\displaystyle PB}

 can be approximated by a binomial distribution 

B

{\displaystyle B}

 where 

μ

{\displaystyle \mu }

, the mean of the 
{\displaystyle p_{i}}

, is the success probability of 

B

{\displaystyle B}

. The variances of 
{\displaystyle PB}
{\displaystyle B}

 are related by the formula
{\displaystyle \operatorname {Var} (PB)=\operatorname {Var} (B)-\sum _{i=1}^{n}(p_{i}-\mu )^{2}}

As can be seen, the closer the 
{\displaystyle p_{i}}

 are to 

μ

{\displaystyle \mu }

, that is, the more the 
{\displaystyle p_{i}}

 tend to homogeneity, the larger 
{\displaystyle PB}

's variance. When all the 
{\displaystyle p_{i}}

are equal to 

μ

{\displaystyle \mu }
{\displaystyle PB}

 becomes 

B

{\displaystyle B}
{\displaystyle \operatorname {Var} (PB)=\operatorname {Var} (B)}

, and the variance is at its maximum.[1]
Ehm has determined bounds for the total variation distance of 
{\displaystyle PB}
{\displaystyle B}

, in effect providing bounds on the error introduced when approximating 
{\displaystyle PB}

 with 

B

{\displaystyle B}

. Let 
{\displaystyle \nu =1-\mu }
{\displaystyle d(PB,B)}

 be the total variation distance of 
{\displaystyle PB}
{\displaystyle B}

. Then
{\displaystyle d(PB,B)\leq (1-\mu ^{n+1}-\nu ^{n+1}){\frac {\sum _{i=1}^{n}(p_{i}-\mu )^{2}}{((n+1)\mu \nu )}}}
{\displaystyle d(PB,B)\geq C\min \left\{\,1,{\frac {1}{n\mu \nu }}\,\right\}\sum _{i=1}^{n}(p_{i}-\mu )^{2}}

where 
{\displaystyle C\geq {\frac {1}{124}}}
{\displaystyle d(PB,B)}

 tends to 0 if and only if 
{\displaystyle \operatorname {Var} (PB)/\operatorname {Var} (B)}

 tends to 1.[11]

Approximation by Poisson distribution[edit]
A Poisson binomial distribution 
{\displaystyle PB}

 can also be approximated by a Poisson distribution 
{\displaystyle Po}

 with mean 
{\displaystyle \lambda =\sum _{i=1}^{n}p_{i}}

. Barbour and Hall have shown that
{\displaystyle {\frac {1}{32}}\min \left\{\,{\frac {1}{\lambda }},1\,\right\}\sum _{i=1}^{n}p_{i}^{2}\leq d(PB,Po)\leq {\frac {1-e^{-\lambda }}{\lambda }}\sum _{i=1}^{n}p_{i}^{2}}

where 
{\displaystyle d(PB,B)}

 is the total variation distance of 
{\displaystyle PB}
{\displaystyle Po}

.[12] It can be seen that the smaller the 
{\displaystyle p_{i}}

, the better 
{\displaystyle Po}

 approximates 
{\displaystyle PB}
{\displaystyle \operatorname {Var} (Po)=\lambda =\sum _{i=1}^{n}p_{i}}
{\displaystyle \operatorname {Var} (PB)=\sum \limits _{i=1}^{n}p_{i}-\sum \limits _{i=1}^{n}p_{i}^{2}}
{\displaystyle \operatorname {Var} (\mathrm {Po} )>\operatorname {Var} (PB)}

; so a Poisson binomial distribution's variance is bounded above by a Poisson distribution with  
{\displaystyle \lambda =\sum _{i=1}^{n}p_{i}}

, and the smaller the 
{\displaystyle p_{i}}

, the closer 
{\displaystyle \operatorname {Var} (\mathrm {Po} )}

 will be to 
{\displaystyle \operatorname {Var} (PB)}

.

Computational methods[edit]
The reference [13] discusses techniques of evaluating the probability mass function of the Poisson binomial distribution. The following software implementations are based on it:

An R package poibin was provided along with the paper,[13] which is available for the computing of the cdf, pmf, quantile function, and random number generation of the Poisson binomial distribution. For computing the PMF, a DFT algorithm or a recursive algorithm can be specified to compute the exact PMF, and approximation methods using the normal and Poisson distribution can also be specified.
poibin – Python implementation – can compute the PMF and CDF, uses the DFT method described in the paper for doing so.
