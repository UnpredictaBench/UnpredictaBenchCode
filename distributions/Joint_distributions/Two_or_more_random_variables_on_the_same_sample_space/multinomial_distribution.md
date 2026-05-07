# Multinomial distribution

Generalization of the binomial distribution

| Multinomial Distribution |
| --- |
| Parameters | n ∈ { 0 , 1 , 2 , … } {\displaystyle n\in \{0,1,2,\ldots \}} number of trials k > 0 {\displaystyle k>0} number of mutually exclusive events (integer) p 1 , … , p k {\displaystyle p_{1},\ldots ,p_{k}} event probabilities, where p 1 + ⋯ + p k = 1 {\displaystyle p_{1}+\dots +p_{k}=1} ${\displaystyle n\in \{0,1,2,\ldots \}}$ ${\displaystyle k>0}$ ${\displaystyle p_{1},\ldots ,p_{k}}$ ${\displaystyle p_{1}+\dots +p_{k}=1}$ |
| Support | { ( x 1 , … , x k ) \| ∑ i = 1 k x i = n , x i ≥ 0 ( i = 1 , … , k ) } {\displaystyle \left\lbrace (x_{1},\dots ,x_{k})\,{\Big \vert }\,\sum _{i=1}^{k}x_{i}=n,x_{i}\geq 0\ (i=1,\dots ,k)\right\rbrace } ${\displaystyle \left\lbrace (x_{1},\dots ,x_{k})\,{\Big \vert }\,\sum _{i=1}^{k}x_{i}=n,x_{i}\geq 0\ (i=1,\dots ,k)\right\rbrace }$ |
| PMF | n ! x 1 ! ⋯ x k ! p 1 x 1 ⋯ p k x k {\displaystyle {\frac {n!}{x_{1}!\cdots x_{k}!}}p_{1}^{x_{1}}\cdots p_{k}^{x_{k}}} ${\displaystyle {\frac {n!}{x_{1}!\cdots x_{k}!}}p_{1}^{x_{1}}\cdots p_{k}^{x_{k}}}$ |
| Mean | E ⁡ ( X i ) = n p i {\displaystyle \operatorname {E} (X_{i})=np_{i}} ${\displaystyle \operatorname {E} (X_{i})=np_{i}}$ |
| Variance | Var ⁡ ( X i ) = n p i ( 1 − p i ) {\displaystyle \operatorname {Var} (X_{i})=np_{i}(1-p_{i})} Cov ⁡ ( X i , X j ) = − n p i p j ( i ≠ j ) {\displaystyle \operatorname {Cov} (X_{i},X_{j})=-np_{i}p_{j}~~(i\neq j)} ${\displaystyle \operatorname {Var} (X_{i})=np_{i}(1-p_{i})}$ ${\displaystyle \operatorname {Cov} (X_{i},X_{j})=-np_{i}p_{j}~~(i\neq j)}$ |
| Entropy | − log ⁡ ( n ! ) − n ∑ i = 1 k p i log ⁡ ( p i ) + ∑ i = 1 k ∑ x i = 0 n ( n x i ) p i x i ( 1 − p i ) n − x i log ⁡ ( x i ! ) {\displaystyle {\begin{aligned}&-\log(n!)-n\sum _{i=1}^{k}p_{i}\log(p_{i})\\&+\sum _{i=1}^{k}\sum _{x_{i}=0}^{n}{\binom {n}{x_{i}}}p_{i}^{x_{i}}(1-p_{i})^{n-x_{i}}\log(x_{i}!)\end{aligned}}} ${\displaystyle {\begin{aligned}&-\log(n!)-n\sum _{i=1}^{k}p_{i}\log(p_{i})\\&+\sum _{i=1}^{k}\sum _{x_{i}=0}^{n}{\binom {n}{x_{i}}}p_{i}^{x_{i}}(1-p_{i})^{n-x_{i}}\log(x_{i}!)\end{aligned}}}$ |
| MGF | ( ∑ i = 1 k p i e t i ) n {\displaystyle \left(\sum _{i=1}^{k}p_{i}e^{t_{i}}\right)^{n}} ${\displaystyle \left(\sum _{i=1}^{k}p_{i}e^{t_{i}}\right)^{n}}$ |
| CF | ( ∑ j = 1 k p j e i t j ) n {\displaystyle \left(\sum _{j=1}^{k}p_{j}e^{it_{j}}\right)^{n}} where i 2 = − 1 {\displaystyle i^{2}=-1} ${\displaystyle \left(\sum _{j=1}^{k}p_{j}e^{it_{j}}\right)^{n}}$ ${\displaystyle i^{2}=-1}$ |
| PGF | ( ∑ i = 1 k p i z i ) n {\displaystyle \left(\sum _{i=1}^{k}p_{i}z_{i}\right)^{n}} for ( z 1 , … , z k ) ∈ C k {\displaystyle (z_{1},\ldots ,z_{k})\in \mathbb {C} ^{k}} ${\displaystyle \left(\sum _{i=1}^{k}p_{i}z_{i}\right)^{n}}$ ${\displaystyle (z_{1},\ldots ,z_{k})\in \mathbb {C} ^{k}}$ |

In probability theory, the multinomial distribution is a generalization of the binomial distribution. For example, it models the probability of counts for each side of a k-sided die rolled n times. For n independent trials each of which leads to a success for exactly one of k categories, with each category having a given fixed success probability, the multinomial distribution gives the probability of any particular combination of numbers of successes for the various categories.

When k is 2 and n is 1, the multinomial distribution is the Bernoulli distribution. When k is 2 and n is bigger than 1, it is the binomial distribution. When k is bigger than 2 and n is 1, it is the categorical distribution. The term "multinoulli" is sometimes used for the categorical distribution to emphasize this four-way relationship (so n determines the suffix, and k the prefix).

The Bernoulli distribution models the outcome of a single Bernoulli trial. In other words, it models whether flipping a (possibly biased) coin one time will result in either a success (obtaining a head) or failure (obtaining a tail). The binomial distribution generalizes this to the number of heads from performing n independent flips (Bernoulli trials) of the same coin. The multinomial distribution models the outcome of n experiments, where the outcome of each trial has a categorical distribution, such as rolling a (possibly biased) k-sided die n times.

Let k be a fixed finite number. Mathematically, we have k possible mutually exclusive outcomes, with corresponding probabilities p1, ..., pk, and n independent trials. Since the k outcomes are mutually exclusive and one must occur we have pi ≥ 0 for i = 1, ..., k and 

∑

i
=
1

k

p

i

=
1

{\textstyle \sum _{i=1}^{k}p_{i}=1}

.  Then if the random variables Xi indicate the number of times outcome number i is observed over the n trials, the vector X = (X1, ..., Xk) follows a multinomial distribution with parameters n and p, where p = (p1, ..., pk). While the trials are independent, their outcomes Xi are dependent because they must sum to n. ${\textstyle \sum _{i=1}^{k}p_{i}=1}$

Definitions[edit]
Probability mass function[edit]
Suppose one does an experiment of extracting n balls of k different colors from a bag, replacing the extracted balls after each draw. Balls of the same color are equivalent. Denote the variable which is the number of extracted balls of color i (i = 1, ..., k) as Xi, and denote as pi the probability that a given extraction will be in color i. The probability mass function of this multinomial distribution is:

f
(

x

1

,
…
,

x

k

;
n
,

p

1

,
…
,

p

k

)

=
Pr
(

X

1

=

x

1

 and 

…

 and 

X

k

=

x

k

)

=

{

n
!

x

1

!
⋯

x

k

!

p

1

x

1

×
⋯
×

p

k

x

k

,

when 

∑

i
=
1

k

x

i

=
n

0

otherwise,

{\displaystyle {\begin{aligned}f(x_{1},\ldots ,x_{k};n,p_{1},\ldots ,p_{k})&{}=\Pr(X_{1}=x_{1}{\text{ and }}\dots {\text{ and }}X_{k}=x_{k})\\[1ex]&{}={\begin{cases}{\displaystyle {n! \over x_{1}!\cdots x_{k}!}p_{1}^{x_{1}}\times \cdots \times p_{k}^{x_{k}}},\quad &{\text{when }}\sum _{i=1}^{k}x_{i}=n\\\\0&{\text{otherwise,}}\end{cases}}\end{aligned}}}

for non-negative integers x1, ..., xk.
The probability mass function can be expressed using the gamma function as:
{\displaystyle f(x_{1},\dots ,x_{k};p_{1},\ldots ,p_{k})={\frac {\Gamma (\sum _{i}x_{i}+1)}{\prod _{i}\Gamma (x_{i}+1)}}\prod _{i=1}^{k}p_{i}^{x_{i}}.}

This form shows its resemblance to the Dirichlet distribution, which is its conjugate prior.

Example[edit]
Suppose that in a three-way election for a large country, candidate A received 20% of the votes, candidate B received 30% of the votes, and candidate C received 50% of the votes.  If six voters are selected randomly, what is the probability that there will be exactly one supporter for candidate A, two supporters for candidate B and three supporters for candidate C in the sample?
Note: Since we’re assuming that the voting population is large, it is reasonable and permissible to think of the probabilities as unchanging once a voter is selected for the sample.  Technically speaking this is sampling without replacement, so the correct distribution is the multivariate hypergeometric distribution, but the distributions converge as the population grows large in comparison to a fixed sample size.[1]

Pr
(
A

=

1
,
B

=

2
,
C

=

3
)
=

6
!

1
!
2
!
3
!

(

0.2

1

)

(

0.3

2

)

(

0.5

3

)

=
0.135

{\displaystyle \Pr(A{=}1,B{=}2,C{=}3)={\frac {6!}{1!2!3!}}\left(0.2^{1}\right)\left(0.3^{2}\right)\left(0.5^{3}\right)=0.135}

Properties[edit]
Normalization[edit]
The multinomial distribution is normalized according to:
{\displaystyle \sum _{\sum _{j=1}^{k}x_{j}=n}f(x_{1},\dots ,x_{k};n,p_{1},\dots ,p_{k})=1}

where the sum is over all permutations of 
{\displaystyle x_{j}}

 such that 

∑

j
=
1

k

x

j

=
n

{\textstyle \sum _{j=1}^{k}x_{j}=n}

.

Expected value and variance[edit]
The expected number of times the outcome i was observed over n trials is
{\displaystyle \operatorname {E} (X_{i})=np_{i}.\,}

The covariance matrix is as follows.  Each diagonal entry is the variance of a binomially distributed random variable, and is therefore
{\displaystyle \operatorname {Var} (X_{i})=np_{i}(1-p_{i}).\,}

The off-diagonal entries are the covariances:
{\displaystyle \operatorname {Cov} (X_{i},X_{j})=-np_{i}p_{j}\,}

for i, j distinct.
All covariances are negative because for fixed n, an increase in one component of a multinomial vector requires a decrease in another component.
When these expressions are combined into a matrix with i, j element 
{\displaystyle \operatorname {cov} (X_{i},X_{j}),}

 the result is a k × k positive-semidefinite covariance matrix of rank k − 1. In the special case where k = n and where the pi are all equal, the covariance matrix is the centering matrix.
The entries of the corresponding correlation matrix are
{\displaystyle {\begin{aligned}\rho (X_{i},X_{i})&=1\\[1ex]\rho (X_{i},X_{j})&={\frac {\operatorname {Cov} (X_{i},X_{j})}{\sqrt {\operatorname {Var} (X_{i})\operatorname {Var} (X_{j})}}}\\&={\frac {-p_{i}p_{j}}{\sqrt {p_{i}(1-p_{i})p_{j}(1-p_{j})}}}\\&=-{\sqrt {\frac {p_{i}p_{j}}{(1-p_{i})(1-p_{j})}}}.\end{aligned}}}

Note that the number of trials n drops out of this expression.
Each of the k components separately has a binomial distribution with parameters n and pi, for the appropriate value of the subscript i.
The support of the multinomial distribution is the set
{\displaystyle \left\{(n_{1},\dots ,n_{k})\in \mathbb {N} ^{k}\mid n_{1}+\cdots +n_{k}=n\right\}.}

Its number of elements is
{\displaystyle {\binom {n+k-1}{k-1}}.}

Matrix notation[edit]
In matrix notation, 
{\displaystyle \operatorname {E} (\mathbf {X} )=n\mathbf {p} ,\,}

and 

Var
⁡
(

X

)
=
n
{
diag
{\displaystyle \operatorname {Var} (\mathbf {X} )=n\lbrace \operatorname {diag} (\mathbf {p} )-\mathbf {p} \mathbf {p} ^{\rm {T}}\rbrace ,\,}

with pT = the row vector transpose of the column vector p.

Visualization[edit]
As slices of generalized Pascal's triangle[edit]
Just like one can interpret the binomial distribution as (normalized) one-dimensional (1D) slices of Pascal's triangle, so too can one interpret the multinomial distribution as 2D (triangular) slices of Pascal's pyramid, or 3D/4D/+ (pyramid-shaped) slices of higher-dimensional analogs of Pascal's triangle. This reveals an interpretation of the range of the distribution: discretized equilateral "pyramids" in arbitrary dimension—i.e. a simplex with a grid.[citation needed]

As polynomial coefficients[edit]
Similarly, just like one can interpret the binomial distribution as the polynomial coefficients of 
{\displaystyle (p+q)^{n}}

 when expanded, one can interpret the multinomial distribution as the coefficients of 
{\displaystyle (p_{1}+p_{2}+p_{3}+\cdots +p_{k})^{n}}

 when expanded, noting that just the coefficients must sum up to 1.

Large deviation theory[edit]
See also: Sanov's theorem
Asymptotics[edit]
By Stirling's formula, at the limit of 
{\displaystyle n,x_{1},\dots ,x_{k}\to \infty }

, we have
{\displaystyle \ln {\binom {n}{x_{1},\dots ,x_{k}}}+\sum _{i=1}^{k}x_{i}\ln p_{i}=-nD_{\text{KL}}({\hat {p}}\|p)-{\frac {k-1}{2}}\ln(2\pi n)-{\frac {1}{2}}\sum _{i=1}^{k}\ln({\hat {p}}_{i})+o(1)}

where relative frequencies 
{\displaystyle {\hat {p}}_{i}=x_{i}/n}

 in the data can be interpreted as probabilities from the empirical distribution 
{\displaystyle {\hat {p}}}

, and 
{\displaystyle D_{\text{KL}}}

 is the Kullback–Leibler divergence.
This formula can be interpreted as follows.
Consider 
{\displaystyle \Delta _{k}}

, the space of all possible distributions over the categories 
{\displaystyle \{1,2,\dots ,k\}}

. It is a simplex. After 

n

{\displaystyle n}

 independent samples from the categorical distribution 

p

{\displaystyle p}

 (which is how we construct the multinomial distribution), we obtain an empirical distribution 
{\displaystyle {\hat {p}}}

.
By the asymptotic formula, the probability that empirical distribution 
{\displaystyle {\hat {p}}}

 deviates from the actual distribution 

p

{\displaystyle p}

 decays exponentially as we sample more data, at a rate of 
{\displaystyle D_{\text{KL}}({\hat {p}}\|p)}

. The more experiments and the more different 
{\displaystyle {\hat {p}}}

 is from 

p

{\displaystyle p}

, the less likely it is to see such an empirical distribution.
{\displaystyle A}

 is a closed subset of 
{\displaystyle \Delta _{k}}

, then by dividing up 

A

{\displaystyle A}

 into pieces, and reasoning about the growth rate of 
{\displaystyle Pr({\hat {p}}\in A_{\epsilon })}

 on each piece 
{\displaystyle A_{\epsilon }}

, we obtain Sanov's theorem, which states that
{\displaystyle \lim _{n\to \infty }{\frac {1}{n}}\ln \Pr({\hat {p}}\in A)=-\inf _{{\hat {p}}\in A}D_{\text{KL}}({\hat {p}}\|p)}

Concentration at large n[edit]
Due to the exponential decay, at large 

n

{\displaystyle n}

, almost all the probability mass is concentrated in a small neighborhood of 

p

{\displaystyle p}

. In this small neighborhood, we can take the first nonzero term in the Taylor expansion of 
{\displaystyle D_{KL}}

, to obtain
{\displaystyle {\begin{aligned}\ln {\binom {n}{x_{1},\cdots ,x_{k}}}p_{1}^{x_{1}}\cdots p_{k}^{x_{k}}&\approx -{\frac {n}{2}}\sum _{i=1}^{k}{\frac {({\hat {p}}_{i}-p_{i})^{2}}{p_{i}}}\\&=-{\frac {1}{2}}\sum _{i=1}^{k}{\frac {(x_{i}-np_{i})^{2}}{np_{i}}}\end{aligned}}}

This resembles the Gaussian distribution, which suggests the following theorem:
Theorem. At the 
{\displaystyle n\to \infty }

 limit, 
{\displaystyle n\sum _{i=1}^{k}{\frac {({\hat {p}}_{i}-p_{i})^{2}}{p_{i}}}=\sum _{i=1}^{k}{\frac {(x_{i}-np_{i})^{2}}{np_{i}}}}

 converges in distribution to the chi-squared distribution 
{\displaystyle \chi ^{2}(k-1)}

.

If we sample from the multinomial distribution 
{\displaystyle \mathrm {Multinomial} (n;0.2,0.3,0.5)}

, and plot the heatmap of the samples within the 2-dimensional simplex (here shown as a black triangle), we notice that as 
{\displaystyle n\to \infty }

, the distribution converges to a Gaussian around the point 
{\displaystyle (0.2,0.3,0.5)}

, with the contours converging in shape to ellipses, with radii converging as 
{\displaystyle 1/{\sqrt {n}}}

. Meanwhile, the separation between the discrete points converge as 
{\displaystyle 1/n}

, and so the discrete multinomial distribution converges to a continuous Gaussian distribution.
[Proof]
The space of all distributions over categories 
{\displaystyle \{1,2,\ldots ,k\}}

 is a simplex: 
{\displaystyle \Delta _{k}=\left\{(y_{1},\ldots ,y_{k})\colon y_{1},\ldots ,y_{k}\geq 0,\sum _{i}y_{i}=1\right\}}

, and the set of all possible empirical distributions after 

n

{\displaystyle n}

 experiments is a subset of the simplex: 
{\displaystyle \Delta _{k,n}=\left\{(x_{1}/n,\ldots ,x_{k}/n)\colon x_{1},\ldots ,x_{k}\in \mathbb {N} ,\sum _{i}x_{i}=n\right\}}

. That is, it is the intersection between 
{\displaystyle \Delta _{k}}

 and the lattice 
{\displaystyle (\mathbb {Z} ^{k})/n}
{\displaystyle n}

 increases, most of the probability mass is concentrated in a subset of 
{\displaystyle \Delta _{k,n}}

 near 

p

{\displaystyle p}

, and the probability distribution near 

p

{\displaystyle p}

 becomes well-approximated by 
{\displaystyle {\binom {n}{x_{1},\cdots ,x_{k}}}p_{1}^{x_{1}}\cdots p_{k}^{x_{k}}\approx e^{-{\frac {n}{2}}\sum _{i}{\frac {\left({\hat {p}}_{i}-p_{i}\right)^{2}}{p_{i}}}}}

From this, we see that the subset upon which the mass is concentrated has radius on the order of 
{\displaystyle 1/{\sqrt {n}}}

, but the points in the subset are separated by distance on the order of 
{\displaystyle 1/n}

, so at large 

n

{\displaystyle n}

, the points merge into a continuum.
To convert this from a discrete probability distribution to a continuous probability density, we need to multiply by the volume occupied by each point of 
{\displaystyle \Delta _{k,n}}
{\displaystyle \Delta _{k}}

. However, by symmetry, every point occupies exactly the same volume (except a negligible set on the boundary), so we obtain a probability density 
{\displaystyle \rho ({\hat {p}})=Ce^{-{\frac {n}{2}}\sum _{i}{\frac {\left({\hat {p}}_{i}-p_{i}\right)^{2}}{p_{i}}}}}

, where 

C

{\displaystyle C}

 is a constant.
Finally, since the simplex 
{\displaystyle \Delta _{k}}

 is not all of 
{\displaystyle \mathbb {R} ^{k}}

, but only within a 
{\displaystyle (k-1)}

-dimensional plane, we obtain the desired result.

Conditional concentration at large n[edit]
The above concentration phenomenon can be easily generalized to the case where we condition upon independent constraints. This is the theoretical justification for Pearson's chi-squared test.
Theorem.

Given functions 
{\displaystyle f_{1},\dots ,f_{\ell }}

, such that they are continuously differentiable in a neighborhood of 

p

{\displaystyle p}

, and the vectors 
{\displaystyle (1,1,\dots ,1),\nabla f_{1}(p),\dots ,\nabla f_{\ell }(p)}

 are linearly independent;
given sequences 
{\displaystyle \epsilon _{1}(n),\dots ,\epsilon _{\ell }(n)}

, such that asymptotically 
{\displaystyle {\frac {1}{n}}\ll \epsilon _{i}(n)\ll {\frac {1}{\sqrt {n}}}}

 for each 
{\displaystyle i\in \{1,\dots ,\ell \}}

;
then for the multinomial distribution conditional on constraints 
{\displaystyle f_{1}({\hat {p}})\in [f_{1}(p)-\epsilon _{1}(n),f_{1}(p)+\epsilon _{1}(n)],\dots ,f_{\ell }({\hat {p}})\in [f_{\ell }(p)-\epsilon _{\ell }(n),f_{\ell }(p)+\epsilon _{\ell }(n)]}

, we have the quantity 
{\displaystyle n\sum _{i}{\frac {({\hat {p}}_{i}-p_{i})^{2}}{p_{i}}}=\sum _{i}{\frac {(x_{i}-np_{i})^{2}}{np_{i}}}}

 converging in distribution to 
{\displaystyle \chi ^{2}(k-1-\ell )}

 at the 
{\displaystyle n\to \infty }

 limit.
In the case that all 
{\displaystyle {\hat {p}}_{i}}

 are equal, this reduces to the concentration of entropies around the maximum entropy.[2][3]
This theorem can be shown by starting with the previous case, then taking the conditional on the constraints. 

Related distributions[edit]
In some fields such as natural language processing, categorical and multinomial distributions are synonymous and it is common to speak of a multinomial distribution when a categorical distribution is actually meant. This stems from the fact that it is sometimes convenient to express the outcome of a categorical distribution as a "1-of-k" vector (a vector with one element containing a 1 and all other elements containing a 0) rather than as an integer in the range 
{\displaystyle 1\dots k}

; in this form, a categorical distribution is equivalent to a multinomial distribution over a single trial.

When k = 2, the multinomial distribution is the binomial distribution.
Categorical distribution, the distribution of each trial; for k = 2, this is the Bernoulli distribution.
The Dirichlet distribution is the conjugate prior of the multinomial in Bayesian statistics.
Dirichlet-multinomial distribution.
Beta-binomial distribution.
Negative multinomial distribution
Hardy–Weinberg principle ( a trinomial distribution with probabilities 
{\displaystyle (\theta ^{2},2\theta (1-\theta ),(1-\theta )^{2})}

)
Statistical inference[edit]
This section needs expansion with: A new sub-section about simultaneous confidence intervals (with proper citations, e.g.: [1]).. You can help by adding missing information.  (March 2024)
Equivalence tests for multinomial distributions[edit]
The goal of equivalence testing is to establish the agreement between a theoretical multinomial distribution and  observed counting frequencies. The theoretical distribution may be a fully specified multinomial distribution or a parametric family of multinomial distributions.
{\displaystyle q}

 denote a theoretical multinomial distribution and let 

p

{\displaystyle p}

 be a true underlying distribution. The distributions 

p

{\displaystyle p}
{\displaystyle q}

 are considered equivalent if 
{\displaystyle d(p,q)<\varepsilon }

 for a distance 

d

{\displaystyle d}

 and a tolerance parameter 
{\displaystyle \varepsilon >0}

. The equivalence test problem is 
{\displaystyle H_{0}=\{d(p,q)\geq \varepsilon \}}

 versus 
{\displaystyle H_{1}=\{d(p,q)<\varepsilon \}}

. The true underlying distribution 

p

{\displaystyle p}

 is unknown. Instead, the counting frequencies 
{\displaystyle p_{n}}

 are observed, where 

n

{\displaystyle n}

 is a sample size. An equivalence test uses 
{\displaystyle p_{n}}

 to reject 
{\displaystyle H_{0}}
{\displaystyle H_{0}}

 can be rejected then the equivalence between 

p

{\displaystyle p}
{\displaystyle q}

 is shown at a given significance level. The equivalence test for Euclidean distance can be found in text book of Wellek (2010).[4] The equivalence test for the total variation distance is developed in Ostrovski (2017).[5] The exact equivalence test for the specific cumulative distance is proposed in Frey (2009).[6]
The distance between the true underlying distribution 

p

{\displaystyle p}

 and a family of the multinomial distributions 

M

{\displaystyle {\mathcal {M}}}

 is defined by 
{\displaystyle d(p,{\mathcal {M}})=\min _{h\in {\mathcal {M}}}d(p,h)}

. Then the equivalence test problem is given by 
{\displaystyle H_{0}=\{d(p,{\mathcal {M}})\geq \varepsilon \}}
{\displaystyle H_{1}=\{d(p,{\mathcal {M}})<\varepsilon \}}

. The distance 
{\displaystyle d(p,{\mathcal {M}})}

 is usually computed using numerical optimization. The tests for this case are developed recently in Ostrovski (2018).[7]

Confidence intervals for the difference of two proportions[edit]
In the setting of a multinomial distribution, constructing confidence intervals for the difference between the proportions of observations from two events, 
{\displaystyle p_{i}-p_{j}}

, requires the incorporation of the negative covariance between the sample estimators 
{\displaystyle {\hat {p}}_{i}={\frac {X_{i}}{n}}}
{\displaystyle {\hat {p}}_{j}={\frac {X_{j}}{n}}}

.
Some of the literature on the subject focused on the use-case of matched-pairs binary data, which requires careful attention when translating the formulas to the general case of 
{\displaystyle p_{i}-p_{j}}

 for any multinomial distribution. Formulas in the current section will be generalized, while formulas in the next section will focus on the matched-pairs binary data use-case.
Wald's standard error (SE) of the difference of proportion can be estimated using:[8]: 378 [9]
{\displaystyle {\widehat {\operatorname {SE} }}({\hat {p}}_{i}-{\hat {p}}_{j})={\sqrt {\frac {\left({\hat {p}}_{i}+{\hat {p}}_{j}\right)-\left({\hat {p}}_{i}-{\hat {p}}_{j}\right)^{2}}{n}}}}

For a 
{\displaystyle 100(1-\alpha )\%}

 approximate confidence interval, the margin of error may incorporate the appropriate quantile from the standard normal distribution, as follows:
{\displaystyle ({\hat {p}}_{i}-{\hat {p}}_{j})\pm z_{\alpha /2}\cdot {\widehat {\operatorname {SE} }}({\hat {p}}_{i}-{\hat {p}}_{j})}

[Proof]
As the sample size (

n

{\displaystyle n}

) increases, the sample proportions will approximately follow a multivariate normal distribution, thanks to the multidimensional central limit theorem (and it could also be shown using the Cramér–Wold theorem). Therefore, their difference will also be approximately normal. Also, these estimators are weakly consistent and plugging them into the SE estimator makes it also weakly consistent. Hence, thanks to Slutsky's theorem, the pivotal quantity 
{\displaystyle {\frac {({\hat {p}}_{i}-{\hat {p}}_{j})-(p_{i}-p_{j})}{\widehat {\operatorname {SE} ({\hat {p}}_{i}-{\hat {p}}_{j})}}}}

  approximately follows the standard normal distribution. And from that, the above approximate confidence interval is directly derived.
The SE can be constructed using the calculus of the variance of the difference of two random variables:
{\displaystyle {\begin{aligned}{\widehat {\operatorname {SE} }}({\hat {p}}_{i}-{\hat {p}}_{j})&={\sqrt {{\frac {{\hat {p}}_{i}(1-{\hat {p}}_{i})}{n}}+{\frac {{\hat {p}}_{j}(1-{\hat {p}}_{j})}{n}}-2\left(-{\frac {{\hat {p}}_{i}{\hat {p}}_{j}}{n}}\right)}}\\&={\sqrt {{\frac {1}{n}}\left({\hat {p}}_{i}+{\hat {p}}_{j}-{\hat {p}}_{i}^{2}-{\hat {p}}_{j}^{2}+2{\hat {p}}_{i}{\hat {p}}_{j}\right)}}\\&={\sqrt {\frac {({\hat {p}}_{i}+{\hat {p}}_{j})-({\hat {p}}_{i}-{\hat {p}}_{j})^{2}}{n}}}\end{aligned}}}

A modification which includes a continuity correction adds 
{\displaystyle {\frac {1}{n}}}

 to the margin of error as follows:[10]: 102–103 
{\displaystyle ({\hat {p}}_{i}-{\hat {p}}_{j})\pm \left(z_{\alpha /2}\cdot {\widehat {\operatorname {SE} }}({\hat {p}}_{i}-{\hat {p}}_{j})+{\frac {1}{n}}\right)}

Another alternative is to rely on a Bayesian estimator using Jeffreys prior which leads to using a dirichlet distribution, with all parameters being equal to 0.5, as a prior. The posterior will be the calculations from above, but after adding 1/2 to each of the k elements, leading to an overall increase of the sample size by 
{\displaystyle {\frac {k}{2}}}

. This was originally developed for a multinomial distribution with four events, and is known as wald+2, for analyzing matched pairs data (see the next section for more details).[11]
This leads to the following SE:
{\displaystyle {\widehat {\operatorname {SE} }}{({\hat {p}}_{i}-{\hat {p}}_{j})}_{wald+{\frac {k}{2}}}={\sqrt {\frac {\left({\hat {p}}_{i}+{\hat {p}}_{j}+{\frac {1}{n}}\right){\frac {n}{n+{\frac {k}{2}}}}-\left({\hat {p}}_{i}-{\hat {p}}_{j}\right)^{2}\left({\frac {n}{n+{\frac {k}{2}}}}\right)^{2}}{n+{\frac {k}{2}}}}}}

[Proof]
{\displaystyle {\begin{aligned}{\widehat {\operatorname {SE} }}{({\hat {p}}_{i}-{\hat {p}}_{j})}_{wald+{\frac {k}{2}}}&={\sqrt {\frac {\left({\frac {x_{i}+1/2}{n+{\frac {k}{2}}}}+{\frac {x_{j}+1/2}{n+{\frac {k}{2}}}}\right)-\left({\frac {x_{i}+1/2}{n+{\frac {k}{2}}}}-{\frac {x_{j}+1/2}{n+{\frac {k}{2}}}}\right)^{2}}{n+{\frac {k}{2}}}}}\\&={\sqrt {\frac {\left({\frac {x_{i}}{n}}+{\frac {x_{j}}{n}}+{\frac {1}{n}}\right){\frac {n}{n+{\frac {k}{2}}}}-\left({\frac {x_{i}}{n}}-{\frac {x_{j}}{n}}\right)^{2}\left({\frac {n}{n+{\frac {k}{2}}}}\right)^{2}}{n+{\frac {k}{2}}}}}\\&={\sqrt {\frac {\left({\hat {p}}_{i}+{\hat {p}}_{j}+{\frac {1}{n}}\right){\frac {n}{n+{\frac {k}{2}}}}-\left({\hat {p}}_{i}-{\hat {p}}_{j}\right)^{2}\left({\frac {n}{n+{\frac {k}{2}}}}\right)^{2}}{n+{\frac {k}{2}}}}}\end{aligned}}}

Which can just be plugged into the original Wald formula as follows:
{\displaystyle \left(p_{i}-p_{j}\right){\frac {n}{n+{\frac {k}{2}}}}\pm z_{\alpha /2}\cdot {\widehat {\operatorname {SE} }}{({\hat {p}}_{i}-{\hat {p}}_{j})}_{wald+{\frac {k}{2}}}}

Occurrence and applications[edit]
Confidence intervals for the difference in matched-pairs binary data (using multinomial with k=4)[edit]
For the case of matched-pairs binary data, a common task is to build the confidence interval of the difference of the proportion of the matched events. For example, we might have a test for some disease, and we may want to check the results of it for some population at two points in time (1 and 2), to check if there was a change in the proportion of the positives for the disease during that time.
Such scenarios can be represented using a two-by-two contingency table with the number of elements that had each of the combination of events. We can use small f for sampling frequencies: 
{\displaystyle f_{11},f_{10},f_{01},f_{00}}

, and capital F for population frequencies: 
{\displaystyle F_{11},F_{10},F_{01},F_{00}}

. These four combinations could be modeled as coming from a multinomial distribution (with four potential outcomes). The sizes of the sample and population can be n and N respectively. And in such a case, there is an interest in building a confidence interval for the difference of proportions from the marginals of the following (sampled) contingency table:

Test 2 positive
Test 2 negative
Row total

Test 1 positive
{\displaystyle f_{11}}
{\displaystyle f_{10}}
{\displaystyle f_{1*}=f_{11}+f_{10}}

Test 1 negative
{\displaystyle f_{01}}
{\displaystyle f_{00}}
{\displaystyle f_{0*}=f_{01}+f_{00}}

Column total
{\displaystyle f_{*1}=f_{11}+f_{01}}
{\displaystyle f_{*0}=f_{10}+f_{00}}

n

{\displaystyle n}

In this case, checking the difference in marginal proportions means we are interested in using the following definitions: 
{\displaystyle p_{1*}={\frac {F_{1*}}{N}}={\frac {F_{11}+F_{10}}{N}}}
{\displaystyle p_{*1}={\frac {F_{*1}}{N}}={\frac {F_{11}+F_{01}}{N}}}

.
And the difference we want to build confidence intervals for is:
{\displaystyle p_{*1}-p_{1*}={\frac {F_{11}+F_{01}}{N}}-{\frac {F_{11}+F_{10}}{N}}={\frac {F_{01}}{N}}-{\frac {F_{10}}{N}}=p_{01}-p_{10}}

Hence, a confidence intervals for the marginal positive proportions (
{\displaystyle p_{*1}-p_{1*}}

) is the same as building a confidence interval for the difference of the proportions from the secondary diagonal of the two-by-two contingency table (
{\displaystyle p_{01}-p_{10}}

).
Calculating a p-value for such a difference is known as McNemar's test. Building confidence interval around it can be constructed using methods described above for Confidence intervals for the difference of two proportions.
The Wald confidence intervals from the previous section can be applied to this setting, and appears in the literature using alternative notations. Specifically, the SE often presented is based on the contingency table frequencies instead of the sample proportions. For example, the Wald confidence intervals, provided above, can be written as:[10]: 102–103 
{\displaystyle {\begin{aligned}{\widehat {\operatorname {SE} }}(p_{*1}-p_{1*})&={\widehat {\operatorname {SE} }}(p_{01}-p_{10})\\[1ex]&={\frac {\sqrt {n\left(f_{10}+f_{01}\right)-\left(f_{10}-f_{01}\right)^{2}}}{n{\sqrt {n}}}}\end{aligned}}}

Further research in the literature has identified several shortcomings in both the Wald and the Wald with continuity correction methods, and other methods have been proposed for practical application.[10]
One such modification includes Agresti and Min’s Wald+2 (similar to some of their other works[12]) in which each cell frequency had an extra 
{\displaystyle {\frac {1}{2}}}

 added to it.[11] This leads to the Wald+2 confidence intervals. In a Bayesian interpretation, this is like building the estimators taking as prior a dirichlet distribution with all parameters being equal to 0.5 (which is, in fact, the Jeffreys prior). The +2 in the name wald+2 can now be taken to mean that in the context of a two-by-two contingency table, which is a multinomial distribution with four possible events, then since we add 1/2 an observation to each of them, then this translates to an overall addition of 2 observations (due to the prior).
This leads to the following modified SE for the case of matched pairs data:
{\displaystyle {\widehat {\operatorname {SE} }}(p_{*1}-p_{1*})={\frac {\sqrt {\left(n+2\right)\left(f_{10}+f_{01}+1\right)-\left(f_{10}-f_{01}\right)^{2}}}{\left(n+2\right){\sqrt {n+2}}}}}

Which can just be plugged into the original Wald formula as follows:
{\displaystyle \left(p_{*1}-p_{1*}\right){\frac {n}{n+2}}\pm z_{\alpha /2}\cdot {\widehat {\operatorname {SE} }}({\hat {p}}_{i}-{\hat {p}}_{j})_{wald+2}}

Other modifications include Bonett and Price’s Adjusted Wald, and Newcombe’s Score.

Computational methods[edit]
Random variate generation[edit]
Further information: Non-uniform random variate generation
First, reorder the parameters 
{\displaystyle p_{1},\ldots ,p_{k}}

 such that they are sorted in descending order (this is only to speed up computation and not strictly necessary). Now, for each trial, draw an auxiliary variable X from a uniform (0, 1) distribution. The resulting outcome is the component
{\displaystyle j=\min \left\{j'\in \{1,\dots ,k\}\colon \left(\sum _{i=1}^{j'}p_{i}\right)-X\geq 0\right\}.}

{Xj = 1, Xk = 0 for k ≠ j } is one observation from the multinomial distribution with 
{\displaystyle p_{1},\ldots ,p_{k}}

 and n = 1.  A sum of independent repetitions of this experiment is an observation from a multinomial distribution with n equal to the number of such repetitions.

Sampling using repeated conditional binomial samples[edit]
Given the parameters 
{\displaystyle p_{1},p_{2},\ldots ,p_{k}}

 and a total for the sample 

n

{\displaystyle n}

 such that 

∑

i
=
1

k

X

i

=
n

{\textstyle \sum _{i=1}^{k}X_{i}=n}

, it is possible to sample sequentially for the number in an arbitrary state 
{\displaystyle X_{i}}

, by partitioning the state space into 

i

{\displaystyle i}

 and not-

i

{\displaystyle i}

, conditioned on any prior samples already taken, repeatedly.

Algorithm: Sequential conditional binomial sampling[edit]
S = n
rho = 1
for i in [1,k-1]:
    if rho != 0:
        X[i] ~ Binom(S,p[i]/rho)
    else 
        X[i] = 0
    S = S - X[i]
    rho = rho - p[i]
X[k] = S

Heuristically, each application of the binomial sample reduces the available number to sample from and the conditional probabilities are likewise updated to ensure logical consistency.[13]

Software implementations[edit]
The MultinomialCI R package allows the computation of simultaneous confidence intervals for the probabilities of a multinomial distribution given a set of observations.[14]
