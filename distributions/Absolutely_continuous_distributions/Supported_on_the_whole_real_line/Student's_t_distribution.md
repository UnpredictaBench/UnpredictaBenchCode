# Student's t-distribution

Probability distribution

This article is about the mathematics of Student's t-distribution. For its uses in statistics, see Student's t-test.

| Student's t |
| --- |
| Probability density function |
| Cumulative distribution function |
| Parameters | ν > 0 {\displaystyle \nu >0} degrees of freedom (real, almost always a positive integer) ${\displaystyle \nu >0}$ |
| Support | x ∈ ( − ∞ , ∞ ) {\displaystyle x\in (-\infty ,\infty )} ${\displaystyle x\in (-\infty ,\infty )}$ |
| PDF | Γ ( ν + 1 2 ) π ν Γ ( ν 2 ) ( 1 + x 2 ν ) − ν + 1 2 {\displaystyle {\frac {\Gamma {\left({\frac {\nu +1}{2}}\right)}}{{\sqrt {\pi \nu }}\,\Gamma {\left({\frac {\nu }{2}}\right)}}}\left(1+{\frac {x^{2}}{\nu }}\right)^{-{\frac {\nu +1}{2}}}} ${\displaystyle {\frac {\Gamma {\left({\frac {\nu +1}{2}}\right)}}{{\sqrt {\pi \nu }}\,\Gamma {\left({\frac {\nu }{2}}\right)}}}\left(1+{\frac {x^{2}}{\nu }}\right)^{-{\frac {\nu +1}{2}}}}$ |
| CDF | 1 2 + x Γ ( ν + 1 2 ) π ν Γ ( ν 2 ) × 2 F 1 ( 1 2 , ν + 1 2 ; 3 2 ; − x 2 ν ) , {\displaystyle {\begin{aligned}&{\frac {1}{2}}+x{\frac {\Gamma {\left({\frac {\nu +1}{2}}\right)}}{{\sqrt {\pi \nu }}\,\Gamma {\left({\frac {\nu }{2}}\right)}}}\times \\&\qquad {}_{2}F_{1}\!\left({\frac {1}{2}},{\frac {\nu +1}{2}};{\frac {3}{2}};-{\frac {x^{2}}{\nu }}\right),\end{aligned}}} where 2 F 1 {\displaystyle {}_{2}F_{1}} is the hypergeometric function ${\displaystyle {\begin{aligned}&{\frac {1}{2}}+x{\frac {\Gamma {\left({\frac {\nu +1}{2}}\right)}}{{\sqrt {\pi \nu }}\,\Gamma {\left({\frac {\nu }{2}}\right)}}}\times \\&\qquad {}_{2}F_{1}\!\left({\frac {1}{2}},{\frac {\nu +1}{2}};{\frac {3}{2}};-{\frac {x^{2}}{\nu }}\right),\end{aligned}}}$ ${\displaystyle {}_{2}F_{1}}$ |
| Mean | 0 {\displaystyle 0} for ν > 1 , {\displaystyle \nu >1,} otherwise undefined ${\displaystyle 0}$ ${\displaystyle \nu >1,}$ |
| Median | 0 {\displaystyle 0} ${\displaystyle 0}$ |
| Mode | 0 {\displaystyle 0} ${\displaystyle 0}$ |
| Variance | ν ν − 2 {\displaystyle {\frac {\nu }{\nu -2}}} for ν > 2 , {\displaystyle \nu >2,} ∞ {\displaystyle \infty } for 1 < ν ≤ 2 , {\displaystyle 1<\nu \leq 2,} otherwise undefined ${\displaystyle {\frac {\nu }{\nu -2}}}$ ${\displaystyle \nu >2,}$ ${\displaystyle \infty }$ ${\displaystyle 1<\nu \leq 2,}$ |
| Skewness | 0 {\displaystyle 0} for ν > 3 , {\displaystyle \ \nu >3\ ,} otherwise undefined ${\displaystyle 0}$ ${\displaystyle \ \nu >3\ ,}$ |
| Excess kurtosis | 6 ν − 4 {\displaystyle {\frac {6}{\nu -4}}} for ν > 4 , {\displaystyle \nu >4,} ∞ {\displaystyle \infty } for 2 < ν ≤ 4 , {\displaystyle 2<\nu \leq 4,} otherwise undefined ${\displaystyle {\frac {6}{\nu -4}}}$ ${\displaystyle \nu >4,}$ ${\displaystyle \infty }$ ${\displaystyle 2<\nu \leq 4,}$ |
| Entropy | ν + 1 2 [ ψ ( ν + 1 2 ) − ψ ( ν 2 ) ] + ln ⁡ [ ν B ( ν 2 , 1 2 ) ] (nats) , {\displaystyle {\begin{aligned}&{\frac {\nu +1}{2}}\left[\psi {\left({\frac {\nu +1}{2}}\right)}-\psi {\left({\frac {\nu }{2}}\right)}\right]\\&\quad +\ln \left[{\sqrt {\nu }}\,\mathrm {B} {\left({\frac {\nu }{2}},{\frac {1}{2}}\right)}\right]~{\text{(nats)}},\end{aligned}}} where ψ {\displaystyle \psi } is the digamma function and B {\displaystyle \mathrm {B} } is the beta function ${\displaystyle {\begin{aligned}&{\frac {\nu +1}{2}}\left[\psi {\left({\frac {\nu +1}{2}}\right)}-\psi {\left({\frac {\nu }{2}}\right)}\right]\\&\quad +\ln \left[{\sqrt {\nu }}\,\mathrm {B} {\left({\frac {\nu }{2}},{\frac {1}{2}}\right)}\right]~{\text{(nats)}},\end{aligned}}}$ ${\displaystyle \psi }$ ${\displaystyle \mathrm {B} }$ |
| MGF | undefined |
| CF | ( ν \| t \| ) ν / 2 K ν / 2 ( ν \| t \| ) Γ ( ν / 2 ) 2 ν / 2 − 1 {\displaystyle {\frac {{\big (}{\sqrt {\nu }}\,\|t\|{\big )}^{\nu /2}\,K_{\nu /2}{\big (}{\sqrt {\nu }}\,\|t\|{\big )}}{\Gamma (\nu /2)\,2^{\nu /2-1}}}} for ν > 0 {\displaystyle \nu >0} , where K ν {\displaystyle K_{\nu }} is the modified Bessel function of the second kind[1] ${\displaystyle {\frac {{\big (}{\sqrt {\nu }}\,\|t\|{\big )}^{\nu /2}\,K_{\nu /2}{\big (}{\sqrt {\nu }}\,\|t\|{\big )}}{\Gamma (\nu /2)\,2^{\nu /2-1}}}}$ ${\displaystyle \nu >0}$ ${\displaystyle K_{\nu }}$ |
| Expected shortfall | μ + s ( ( ν + [ T − 1 ( 1 − p ) ] 2 ) × τ ( T − 1 ( 1 − p ) ) ( ν − 1 ) ( 1 − p ) ) , {\displaystyle \mu +s\left({\frac {{\big (}\nu +[T^{-1}(1-p)]^{2}{\big )}\times \tau {\big (}T^{-1}(1-p){\big )}}{(\nu -1)(1-p)}}\right),} where T − 1 {\displaystyle T^{-1}} is the inverse standardized Student t CDF, and τ {\displaystyle \tau } is the standardized Student t PDF.[2] ${\displaystyle \mu +s\left({\frac {{\big (}\nu +[T^{-1}(1-p)]^{2}{\big )}\times \tau {\big (}T^{-1}(1-p){\big )}}{(\nu -1)(1-p)}}\right),}$ ${\displaystyle T^{-1}}$ ${\displaystyle \tau }$ |

In probability theory and statistics, Student's t distribution (or simply the t distribution) 
{\displaystyle t_{\nu }}

 is a continuous probability distribution that generalizes the standard normal distribution. Like the latter, it is symmetric around zero and bell-shaped. ${\displaystyle t_{\nu }}$

However, 
{\displaystyle t_{\nu }}

 has heavier tails, and the amount of probability mass in the tails is controlled by the parameter 

ν

{\displaystyle \nu }

. For 
{\displaystyle \nu =1}

 the Student's t distribution 
{\displaystyle t_{\nu }}

 becomes the standard Cauchy distribution, which has very "fat" tails; whereas for 
{\displaystyle \nu \to \infty }

 it becomes the standard normal distribution 
{\displaystyle {\mathcal {N}}(0,1),}

 which has very "thin" tails. ${\displaystyle t_{\nu }}$ ${\displaystyle \nu }$ ${\displaystyle \nu =1}$ ${\displaystyle t_{\nu }}$ ${\displaystyle \nu \to \infty }$ ${\displaystyle {\mathcal {N}}(0,1),}$

The name "Student" is a pseudonym used by William Sealy Gosset in his scientific paper publications during his work at the Guinness Brewery in Dublin, Ireland.

The Student's t distribution plays a role in a number of widely used statistical analyses, including Student's t-test for assessing the statistical significance of the difference between two sample means, the construction of confidence intervals for the difference between two population means, and in linear regression analysis.

In the form of the location-scale t distribution 
{\displaystyle \operatorname {\ell st} (\mu ,\tau ^{2},\nu )}

 it generalizes the normal distribution and also arises in the Bayesian analysis of data from a normal family as a compound distribution when marginalizing over the variance parameter. ${\displaystyle \operatorname {\ell st} (\mu ,\tau ^{2},\nu )}$

Definitions[edit]
Probability density function[edit]
Student's t distribution has the probability density function (PDF) given by
{\displaystyle f(t)={\frac {\Gamma {\left({\frac {\nu +1}{2}}\right)}}{{\sqrt {\pi \nu }}\,\Gamma {\left({\frac {\nu }{2}}\right)}}}\left(1+{\frac {t^{2}}{\nu }}\right)^{-(\nu +1)/2},}

where 

ν

{\displaystyle \nu }

 is the number of degrees of freedom, and 

Γ

{\displaystyle \Gamma }

 is the gamma function. This may also be written as
{\displaystyle f(t)={\frac {1}{{\sqrt {\nu }}\,\mathrm {B} {\left({\frac {1}{2}},{\frac {\nu }{2}}\right)}}}\left(1+{\frac {t^{2}}{\nu }}\right)^{-(\nu +1)/2},}

where 

B

{\displaystyle \mathrm {B} }

 is the beta function. In particular for integer valued degrees of freedom 

ν

{\displaystyle \nu }

 we have:
{\displaystyle \nu >1}

 and even,
{\displaystyle {\frac {\Gamma {\left({\frac {\nu +1}{2}}\right)}}{{\sqrt {\pi \nu }}\,\Gamma {\left({\frac {\nu }{2}}\right)}}}={\frac {1}{2{\sqrt {\nu }}}}\cdot {\frac {(\nu -1)\cdot (\nu -3)\cdots 5\cdot 3}{(\nu -2)\cdot (\nu -4)\cdots 4\cdot 2}}.}
{\displaystyle \nu >1}

 and odd,
{\displaystyle {\frac {\Gamma {\left({\frac {\nu +1}{2}}\right)}}{{\sqrt {\pi \nu }}\,\Gamma {\left({\frac {\nu }{2}}\right)}}}={\frac {1}{\pi {\sqrt {\nu }}}}\cdot {\frac {(\nu -1)\cdot (\nu -3)\cdots 4\cdot 2}{(\nu -2)\cdot (\nu -4)\cdots 5\cdot 3}}.}

The probability density function is symmetric, and its overall shape resembles the bell shape of a normally distributed variable with mean 0 and variance 1, except that it is a bit lower and wider. As the number of degrees of freedom grows, the t distribution approaches the normal distribution with mean 0 and variance 1. For this reason 

ν

{\displaystyle {\nu }}

 is also known as the normality parameter.[3]
The following images show the density of the t distribution for increasing values of 
{\displaystyle \nu .}

 The normal distribution is shown as a blue line for comparison. Note that the t distribution (red line) becomes closer to the normal distribution as 

ν

{\displaystyle \nu }

 increases.

Density of the t distribution (red) for 1, 2, 3, 5, 10, and 30 degrees of freedom compared to the standard normal distribution (blue).Previous plots shown in green.1 degree of freedom2 degrees of freedom3 degrees of freedom5 degrees of freedom10 degrees of freedom30 degrees of freedom
Cumulative distribution function[edit]
The cumulative distribution function (CDF) can be written in terms of I, the regularized
incomplete beta function. For  t > 0 ,
{\displaystyle F(t)=\int _{-\infty }^{t}f(u)\,du~=~1-{\frac {1}{2}}I_{x(t)}{\left({\frac {\nu }{2}},\,{\frac {1}{2}}\right)},}

where
{\displaystyle x(t)={\frac {\nu }{t^{2}+\nu }}\,.}

Other values would be obtained by symmetry. An alternative formula, valid for 
{\displaystyle t^{2}<\nu \,,}
{\displaystyle \int _{-\infty }^{t}f(u)\,du={\frac {1}{2}}+t\,{\frac {\Gamma \!\left({\frac {\nu +1}{2}}\right)}{{\sqrt {\pi \nu }}\,\Gamma \!\left({\frac {\nu }{\ 2\ }}\right)}}\;{}_{2}F_{1}\!\left({\frac {1}{2}},{\frac {\nu +1}{2}};\,{\frac {3}{2}};\,-{\frac {t^{2}}{\nu }}\right),}

where 
{\displaystyle {}_{2}F_{1}(\ ,\ ;\ ;\ )}

 is a particular instance of the hypergeometric function.
For information on its inverse cumulative distribution function, see quantile function § Student's t-distribution.

Special cases[edit]
Certain values of 
{\displaystyle \ \nu \ }

 give a simple form for Student's t-distribution.
{\displaystyle \ \nu \ }

PDF

CDF

notes
{\displaystyle {\frac {1}{\pi (1+t^{2})}}}

1
2

+

1
π

arctan
{\displaystyle {\frac {1}{2}}+{\frac {1}{\pi }}\arctan(t)}

See Cauchy distribution
{\displaystyle {\frac {1}{2\,{\sqrt {2}}\,\left(1+{\frac {t^{2}}{2}}\right)^{3/2}}}}
{\displaystyle {\frac {1}{2}}+{\frac {t}{2{\sqrt {2}}\,{\sqrt {1+{\frac {t^{2}}{2}}}}}}}
{\displaystyle {\frac {2}{\pi {\sqrt {3}}\,\left(1+{\frac {t^{2}}{3}}\right)^{2}}}}

1
2

+

1
π

[

t

3

1
+

t

2

3

+
arctan
{\displaystyle {\frac {1}{2}}+{\frac {1}{\pi }}\left[{\frac {\frac {t}{\sqrt {3}}}{1+{\frac {t^{2}}{3}}}}+\arctan {\frac {t}{\sqrt {3}}}\right]}
{\displaystyle {\frac {3}{8\left(1+{\frac {t^{2}}{4}}\right)^{5/2}}}}
{\displaystyle {\frac {1}{2}}+{\frac {3}{8}}\left[{\frac {t}{\sqrt {1+{\frac {t^{2}}{4}}}}}\right]\left[1-{\frac {t^{2}}{12\left(1+{\frac {t^{2}}{4}}\right)}}\right]}
{\displaystyle {\frac {8}{3\pi {\sqrt {5}}\,\left(1+{\frac {t^{2}}{5}}\right)^{3}}}}

1
2

+

1
π

[

t

5

(

1
+

t

2

5

)

(

1
+

2

3

(

1
+

t

2

5

)

)

+
arctan
{\displaystyle {\frac {1}{2}}+{\frac {1}{\pi }}\left[{\frac {t}{{\sqrt {5}}\left(1+{\frac {t^{2}}{5}}\right)}}\left(1+{\frac {2}{3\left(1+{\frac {t^{2}}{5}}\right)}}\right)+\arctan {\frac {t}{\sqrt {5}}}\right]}
{\displaystyle \ \infty \ }
{\displaystyle {\frac {1}{\sqrt {2\pi }}}\,e^{-t^{2}/2}}
{\displaystyle {\frac {1}{2}}\left[1+\operatorname {erf} \left({\frac {t}{\sqrt {2}}}\right)\right]}

See Normal distribution, Error function

Properties[edit]
Moments[edit]
{\displaystyle \nu >1}

, the raw moments of the t distribution are

E

⁡

{

T

k

}

=

{

0

k

 odd 

,

0
<
k
<
ν

,

1

π

Γ

(

ν
2

)

[

Γ

(

k
+
1

2

)

Γ

(

ν
−
k

2

)

ν

k
2

]

k

 even 
{\displaystyle \operatorname {\mathbb {E} } \left\{T^{k}\right\}={\begin{cases}\quad 0&k{\text{ odd }},\quad 0<k<\nu \,,\\[2ex]{\frac {1}{{\sqrt {\pi }}\,\Gamma {\left({\frac {\nu }{2}}\right)}}}\left[\Gamma \!\left({\frac {k+1}{2}}\right)\,\Gamma \!\left({\frac {\nu -k}{2}}\right)\,\nu ^{\frac {k}{2}}\right]&k{\text{ even }},\quad 0<k<\nu \,.\end{cases}}}

Moments of order 
{\displaystyle \ \nu \ }

 or higher do not exist.[4]
The term for 
{\displaystyle 0<k<\nu }

, k even, may be simplified using the properties of the gamma function to

E

⁡

{

T

k

}

=

ν

k
2

∏

j
=
1

k

/

2

2
j
−
1

ν
−
2
j

k

 even
{\displaystyle \operatorname {\mathbb {E} } \left\{T^{k}\right\}=\nu ^{\frac {k}{2}}\,\prod _{j=1}^{k/2}{\frac {2j-1}{\nu -2j}}\qquad k{\text{ even}},\quad 0<k<\nu ~.}

For a t distribution with 

ν

{\displaystyle \nu }

 degrees of freedom, the expected value is 

0

{\displaystyle 0}
{\displaystyle \nu >1\,,}

 and its variance is 
{\displaystyle {\frac {\nu }{\nu -2}}}
{\displaystyle \nu >2\,.}

 The skewness is 0 if 
{\displaystyle \nu >3}

 and the excess kurtosis is 
{\displaystyle {\frac {6}{\nu -4}}}
{\displaystyle \nu >4\,.}

How the t distribution arises (characterization) [edit]
As the distribution of a test statistic[edit]
Student's t-distribution with 

ν

{\displaystyle \nu }

 degrees of freedom can be defined as the distribution of the random variable T with[5][6]
{\displaystyle T={\frac {Z}{\sqrt {V/\nu }}}=Z{\sqrt {\frac {\nu }{V}}},}

where

Z is a standard normal with expected value 0 and variance 1;
V has a chi-squared distribution (χ2-distribution) with 

ν

{\displaystyle \nu }

 degrees of freedom;
Z and V are independent;
A different distribution is defined as that of the random variable defined, for a given constant μ, by
{\displaystyle (Z+\mu ){\sqrt {\frac {\nu }{V}}}.}

This random variable has a noncentral t-distribution with noncentrality parameter μ. This distribution is important in studies of the power of Student's t-test.

Derivation[edit]
Suppose X1, ..., Xn are independent realizations of the normally-distributed, random variable X, which has an expected value μ and variance σ2. Let
{\displaystyle {\overline {X}}_{n}={\frac {1}{n}}(X_{1}+\cdots +X_{n})}

be the sample mean, and
{\displaystyle s^{2}={\frac {1}{n-1}}\sum _{i=1}^{n}\left(X_{i}-{\overline {X}}_{n}\right)^{2}}

be an unbiased estimate of the variance from the sample.  It can be shown that the random variable
{\displaystyle V=(n-1){\frac {s^{2}}{\sigma ^{2}}}}

has a chi-squared distribution with 
{\displaystyle \nu =n-1}

 degrees of freedom (by Cochran's theorem).[7]  It is readily shown that the quantity
{\displaystyle Z=\left({\overline {X}}_{n}-\mu \right){\frac {\sqrt {n}}{\sigma }}}

is normally distributed with mean 0 and variance 1, since the sample mean 
{\displaystyle {\overline {X}}_{n}}

 is normally distributed with mean μ and variance σ2/n.  Moreover, it is possible to show that these two random variables (the normally distributed one Z and the chi-squared-distributed one V) are independent. Consequently[clarification needed] the pivotal quantity
{\displaystyle T\equiv {\frac {Z}{\sqrt {V/\nu }}}=\left({\overline {X}}_{n}-\mu \right){\frac {\sqrt {n}}{s}},}

which differs from Z in that the exact standard deviation σ is replaced by the sample standard error s, has a Student's t-distribution as defined above. Notice that the unknown population variance σ2 does not appear in T, since it was in both the numerator and the denominator, so it canceled. Gosset intuitively obtained the probability density function stated above, with 

ν

{\displaystyle \nu }

 equal to n − 1, and Fisher proved it in 1925.[8]
The distribution of the test statistic T depends on 

ν

{\displaystyle \nu }

, but not μ or σ; the lack of dependence on μ and σ is what makes the t-distribution important in both theory and practice.

Sampling distribution of t-statistic[edit]
The t distribution arises as the sampling distribution
of the t statistic. Below the one-sample t statistic is discussed, for the corresponding two-sample t statistic see Student's t-test.

Unbiased variance estimate[edit]
{\displaystyle \ x_{1},\ldots ,x_{n}\sim {\mathcal {N}}(\mu ,\sigma ^{2})\ }

 be independent and identically distributed samples from a normal distribution with mean 

μ

{\displaystyle \mu }

 and variance 
{\displaystyle \ \sigma ^{2}~.}

 The sample mean and unbiased sample variance are given by:
{\displaystyle {\begin{aligned}{\bar {x}}&={\frac {\ x_{1}+\cdots +x_{n}\ }{n}}\ ,\\[5pt]s^{2}&={\frac {1}{\ n-1\ }}\ \sum _{i=1}^{n}(x_{i}-{\bar {x}})^{2}~.\end{aligned}}}

The resulting (one sample) t statistic is given by
{\displaystyle t={\frac {{\bar {x}}-\mu }{\ s/{\sqrt {n\ }}\ }}\sim t_{n-1}~.}

and is distributed according to a Student's t distribution with 
{\displaystyle \ n-1\ }

 degrees of freedom.
Thus for inference purposes the t statistic is a useful "pivotal quantity" in the case when the mean and variance 
{\displaystyle (\mu ,\sigma ^{2})}

 are unknown population parameters, in the sense that the t statistic has then a probability distribution that depends on neither 

μ

{\displaystyle \mu }
{\displaystyle \ \sigma ^{2}~.}

ML variance estimate[edit]
Instead of the unbiased estimate 
{\displaystyle \ s^{2}\ }

 we may also use the maximum likelihood estimate
{\displaystyle \ s_{\mathsf {ML}}^{2}={\frac {\ 1\ }{n}}\ \sum _{i=1}^{n}(x_{i}-{\bar {x}})^{2}\ }

yielding the statistic
{\displaystyle \ t_{\mathsf {ML}}={\frac {{\bar {x}}-\mu }{\sqrt {s_{\mathsf {ML}}^{2}/n\ }}}={\sqrt {{\frac {n}{n-1}}\ }}\ t~.}

This is distributed according to the location-scale t distribution:
{\displaystyle t_{\mathsf {ML}}\sim \operatorname {\ell st} (0,\ \tau ^{2}=n/(n-1),\ n-1)~.}

Compound distribution of normal with inverse gamma distribution[edit]
The location-scale t distribution results from compounding a Gaussian distribution (normal distribution) with mean 
{\displaystyle \ \mu \ }

 and unknown variance, with an inverse gamma distribution placed over the variance with parameters 

a
=

ν
2

{\textstyle a={\frac {\nu }{2}}}

 and 

b
=

ν

τ

2

2

.

{\textstyle b={\frac {\nu \tau ^{2}}{2}}\,.}

 In other words, the random variable X is assumed to have a Gaussian distribution with an unknown variance distributed as inverse gamma, and then the variance is marginalized out (integrated out).
Equivalently, this distribution results from compounding a Gaussian distribution with a scaled-inverse-chi-squared distribution with parameters 

ν

{\displaystyle \nu }
{\displaystyle \ \tau ^{2}~.}

 The scaled-inverse-chi-squared distribution is exactly the same distribution as the inverse gamma distribution, but with a different parameterization, i.e. 
{\displaystyle \nu =2a,\;\tau ^{2}={\frac {b}{a}}\,.}

The reason for the usefulness of this characterization is that in Bayesian statistics the inverse gamma distribution is the conjugate prior distribution of the variance of a Gaussian distribution. As a result, the location-scale t distribution arises naturally in many Bayesian inference problems.[9]

Maximum entropy distribution[edit]
Student's t distribution is the maximum entropy probability distribution for a random variate X having a certain value of 

E

⁡

{

ln
⁡
(
ν
+

X

2

)

}

{\textstyle \operatorname {\mathbb {E} } \left\{\ln(\nu +X^{2})\right\}}

.[10][clarification needed][better source needed]
This follows immediately from the observation that the pdf can be written in exponential family form with 
{\displaystyle \nu +X^{2}}

 as sufficient statistic.

Integral of Student's probability density function and p-value[edit]
The function A(t | ν)  is the integral of Student's probability density function, f(t) between  -t and t, for  t ≥ 0  . It thus gives the probability that a value of t less than that calculated from observed data would occur by chance. Therefore, the function A(t | ν)  can be used when testing whether the difference between the means of two sets of data is statistically significant, by calculating the corresponding value of t and the probability of its occurrence if the two sets of data were drawn from the same population. This is used in a variety of situations, particularly in t tests. For the statistic t, with ν degrees of freedom, A(t | ν)  is the probability that t would be less than the observed value if the two means were the same (provided that the smaller mean is subtracted from the larger, so that  t ≥ 0 ). It can be easily calculated from the cumulative distribution function Fν(t) of the t distribution:
{\displaystyle A(t\mid \nu )=F_{\nu }(t)-F_{\nu }(-t)=1-I_{\frac {\nu }{\nu +t^{2}}}\!\left({\frac {\nu }{2}},{\frac {1}{2}}\right),}

where   Ix(a, b)   is the regularized incomplete beta function.
For statistical hypothesis testing this function is used to construct the p-value.

Related distributions[edit]
In general[edit]
The noncentral t distribution generalizes the t distribution to include a noncentrality parameter. Unlike the nonstandardized t distributions, the noncentral distributions are not symmetric (the median is not the same as the mode).
The discrete Student's t distribution is defined by its probability mass function at r being proportional to:[11] 
{\displaystyle \prod _{j=1}^{k}{\frac {1}{(r+j+a)^{2}+b^{2}}}\quad \quad r=\ldots ,-1,0,1,\ldots ~.}

 Here a, b, and k are parameters. This distribution arises from the construction of a system of discrete distributions similar to that of the Pearson distributions for continuous distributions.[12]
One can generate Student  A(t | ν)  samples by taking the ratio of variables from the normal distribution and the square-root of the χ² distribution. If we use instead of the normal distribution, e.g., the Irwin–Hall distribution, we obtain over-all a symmetric 4 parameter distribution, which includes the normal, the uniform, the triangular, the Student t and the Cauchy distribution. This is also more flexible than some other symmetric generalizations of the normal distribution.
t distribution is an instance of ratio distributions.
The square of a random variable distributed  tn is distributed as Snedecor's F distribution F1,n.
Location-scale t-distribution[edit]
Location-scale transformation[edit]
Student's t distribution generalizes to the three parameter location-scale t distribution 
{\displaystyle \operatorname {\ell st} (\mu ,\ \tau ^{2},\ \nu )\ }

 by introducing a location parameter 
{\displaystyle \ \mu \ }

 and a scale parameter 
{\displaystyle \ \tau ~.}

 With
{\displaystyle \ T\sim t_{\nu }\ }

and location-scale family transformation
{\displaystyle \ X=\mu +\tau \ T\ }

we get
{\displaystyle X\sim \operatorname {\ell st} (\mu ,\ \tau ^{2},\ \nu )~.}

The resulting distribution is also called the non-standardized Student's t distribution.

Density and first two moments[edit]
The location-scale t distribution has a density defined by:[13]
{\displaystyle p(x\mid \nu ,\mu ,\tau )={\frac {\Gamma {\left({\frac {\nu +1}{2}}\right)}}{\Gamma {\left({\frac {\nu }{2}}\right)}\tau {\sqrt {\pi \nu }}}}\left(1+{\frac {1}{\nu }}\left({\frac {x-\mu }{\tau }}\right)^{2}\right)^{-(\nu +1)/2}}

Equivalently, the density can be written in terms of 
{\displaystyle \tau ^{2}}
{\displaystyle p(x\mid \nu ,\mu ,\tau ^{2})={\frac {\Gamma {\left({\frac {\nu +1}{2}}\right)}}{\Gamma {\left({\frac {\nu }{2}}\right)}{\sqrt {\pi \nu \tau ^{2}}}}}\left(1+{\frac {1}{\nu }}{\frac {(x-\mu )^{2}}{\tau ^{2}}}\right)^{-(\nu +1)/2}}

Other properties of this version of the distribution are:[13]

E

⁡
{

X

}

=
μ

 for 

ν
>
1

,

var
⁡
{

X

}

=

τ

2

ν

ν
−
2

 for 

ν
>
2

,

mode
{\displaystyle {\begin{aligned}\operatorname {\mathbb {E} } \{\ X\ \}&=\mu &{\text{ for }}\nu >1\ ,\\\operatorname {var} \{\ X\ \}&=\tau ^{2}{\frac {\nu }{\nu -2}}&{\text{ for }}\nu >2\ ,\\\operatorname {mode} \{\ X\ \}&=\mu ~.\end{aligned}}}

Special cases[edit]
{\displaystyle X}

 follows a location-scale t distribution 
{\displaystyle X\sim \operatorname {\ell st} \left(\mu ,\,\tau ^{2},\,\nu \right)}

 then for 
{\displaystyle \nu \to \infty }
{\displaystyle X}

 is normally distributed 
{\displaystyle X\sim \mathrm {N} {\left(\mu ,\tau ^{2}\right)}}

 with mean 

μ

{\displaystyle \mu }

 and variance 
{\displaystyle \tau ^{2}\,.}

The location-scale t distribution 
{\displaystyle \ \operatorname {\ell st} \left(\mu ,\ \tau ^{2},\ \nu =1\right)\ }

 with degree of freedom 
{\displaystyle \nu =1}

 is equivalent to the Cauchy distribution 
{\displaystyle \mathrm {Cau} \left(\mu ,\tau \right)~.}

The location-scale t distribution 
{\displaystyle \operatorname {\ell st} \left(\mu =0,\ \tau ^{2}=1,\ \nu \right)\ }

 with 
{\displaystyle \mu =0}
{\displaystyle \ \tau ^{2}=1\ }

 reduces to the Student's t distribution 
{\displaystyle \ t_{\nu }~.}

Occurrence and applications[edit]
In frequentist statistical inference[edit]
Student's t distribution arises in a variety of statistical estimation problems where the goal is to estimate an unknown parameter, such as a mean value, in a setting where the data are observed with additive errors. If (as in nearly all practical statistical work) the population standard deviation of these errors is unknown and has to be estimated from the data, the t distribution is often used to account for the extra uncertainty that results from this estimation. In most such problems, if the standard deviation of the errors were known, a normal distribution would be used instead of the t distribution.
Confidence intervals and hypothesis tests are two statistical procedures in which the quantiles of the sampling distribution of a particular statistic (e.g. the standard score) are required. In any situation where this statistic is a linear function of the data, divided by the usual estimate of the standard deviation, the resulting quantity can be rescaled and centered to follow Student's t distribution. Statistical analyses involving means, weighted means, and regression coefficients all lead to statistics having this form.
Quite often, textbook problems will treat the population standard deviation as if it were known and thereby avoid the need to use the Student's t distribution. These problems are generally of two kinds: (1) those in which the sample size is so large that one may treat a data-based estimate of the variance as if it were certain, and (2) those that illustrate mathematical reasoning, in which the problem of estimating the standard deviation is temporarily ignored because that is not the point that the author or instructor is then explaining.

Hypothesis testing[edit]
A number of statistics can be shown to have t distributions for samples of moderate size under null hypotheses that are of interest, so that the t distribution forms the basis for significance tests. For example, the distribution of Spearman's rank correlation coefficient ρ, in the null case (zero correlation) is well approximated by the t distribution for sample sizes above about 20.[citation needed]

Confidence intervals[edit]
Suppose the number A is so chosen that
{\displaystyle \ \operatorname {\mathbb {P} } \left\{\ {-A}<T<A\ \right\}=0.9\ ,}

when T has a t distribution with n − 1   degrees of freedom. By symmetry, this is the same as saying that A satisfies

P

⁡

{

T
<
A

}

=
0.95

,

{\displaystyle \ \operatorname {\mathbb {P} } \left\{\ T<A\ \right\}=0.95\ ,}

so A is the "95th percentile" of this probability distribution, or 

A
=

t

(
0.05
{\displaystyle \ A=t_{(0.05,n-1)}~.}

 Then
{\displaystyle \ \operatorname {\mathbb {P} } \left\{\ {-A}<{\frac {\ {\overline {X}}_{n}-\mu \ }{S_{n}/{\sqrt {n\ }}}}<A\ \right\}=0.9\ ,}

where Sn  is the sample standard deviation of the observed values. This is equivalent to
{\displaystyle \ \operatorname {\mathbb {P} } \left\{\ {\overline {X}}_{n}-A{\frac {S_{n}}{\ {\sqrt {n\ }}\ }}<\mu <{\overline {X}}_{n}+A\ {\frac {S_{n}}{\ {\sqrt {n\ }}\ }}\ \right\}=0.9.}

Therefore, the interval whose endpoints are
{\displaystyle \ {\overline {X}}_{n}\ \pm A\ {\frac {S_{n}}{\ {\sqrt {n\ }}\ }}\ }

is a 90% confidence interval for μ. Therefore, if we find the mean of a set of observations that we can reasonably expect to have a normal distribution, we can use the t distribution to examine whether the confidence limits on that mean include some theoretically predicted value – such as the value predicted on a null hypothesis.
It is this result that is used in the Student's t tests: since the difference between the means of samples from two normal distributions is itself distributed normally, the t distribution can be used to examine whether that difference can reasonably be supposed to be zero.
If the data are normally distributed, the one-sided (1 − α) upper confidence limit (UCL) of the mean, can be calculated using the following equation:
{\displaystyle {\mathsf {UCL}}_{1-\alpha }={\overline {X}}_{n}+t_{\alpha ,n-1}\ {\frac {S_{n}}{\ {\sqrt {n\ }}\ }}~.}

The resulting UCL will be the greatest average value that will occur for a given confidence interval and population size. In other words, 
{\displaystyle {\overline {X}}_{n}}

 being the mean of the set of observations, the probability that the mean of the distribution is inferior to UCL1 − α   is equal to the confidence level 1 − α .

Prediction intervals[edit]
The t distribution can be used to construct a prediction interval for an unobserved sample from a normal distribution with unknown mean and variance.

In Bayesian statistics[edit]
The Student's t distribution, especially in its three-parameter (location-scale) version, arises frequently in Bayesian statistics as a result of its connection with the normal distribution. Whenever the variance of a normally distributed random variable is unknown and a conjugate prior placed over it that follows an inverse gamma distribution, the resulting marginal distribution of the variable will follow a Student's t distribution. Equivalent constructions with the same results involve a conjugate scaled-inverse-chi-squared distribution over the variance, or a conjugate gamma distribution over the precision. If an improper prior proportional to ⁠1/ σ² ⁠ is placed over the variance, the t distribution also arises. This is the case regardless of whether the mean of the normally distributed variable is known, is unknown distributed according to a conjugate normally distributed prior, or is unknown distributed according to an improper constant prior.
Related situations that also produce a t distribution are:

The marginal posterior distribution of the unknown mean of a normally distributed variable, with unknown prior mean and variance following the above model.
The prior predictive distribution and posterior predictive distribution of a new normally distributed data point when a series of independent identically distributed normally distributed data points have been observed, with prior mean and variance as in the above model.
Robust parametric modeling[edit]
The t distribution is often used as an alternative to the normal distribution as a model for data, which often has heavier tails than the normal distribution allows for; see e.g. Lange et al.[14] The classical approach was to identify outliers (e.g., using Grubbs's test) and exclude or downweight them in some way. However, it is not always easy to identify outliers (especially in high dimensions), and the t distribution is a natural choice of model for such data and provides a parametric approach to robust statistics.
A Bayesian account can be found in Gelman et al.[15] The degrees of freedom parameter controls the kurtosis of the distribution and is correlated with the scale parameter. The likelihood can have multiple local maxima and, as such, it is often necessary to fix the degrees of freedom at a fairly low value and estimate the other parameters taking this as given. Some authors[citation needed] report that values between 3 and 9 are often good choices. Venables and Ripley[citation needed] suggest that a value of 5 is often a good choice.

Student's t process[edit]
For practical regression and prediction needs, Student's t processes were introduced, that are generalisations of the Student t distributions for functions. A Student's t process is constructed from the Student t distributions like a Gaussian process is constructed from the Gaussian distributions. For a Gaussian process, all sets of values have a multidimensional Gaussian distribution. Analogously, 
{\displaystyle X(t)}

 is a Student t process on an interval 
{\displaystyle I=[a,b]}

 if the correspondent values of the process 
{\displaystyle \ X(t_{1}),\ \ldots \ ,X(t_{n})\ }
{\displaystyle t_{i}\in I}

) have a joint multivariate Student t distribution.[16] These processes are used for regression, prediction, Bayesian optimization and related problems. For multivariate regression and multi-output prediction, the multivariate Student t processes are introduced and used.[17]

Table of selected values[edit]
The following table lists values for t distributions with ν degrees of freedom for a range of one-sided or two-sided critical regions. The first column is ν, the percentages along the top are confidence levels 
{\displaystyle \ \alpha \ ,}

 and the numbers in the body of the table are the 
{\displaystyle t_{\alpha ,n-1}}

 factors described in the section on confidence intervals.
The last row with infinite ν gives critical points for a normal distribution since a t distribution with infinitely many degrees of freedom is a normal distribution. (See Related distributions above).

One-sided

75%

80%

85%

90%

95%

97.5%

99%

99.5%

99.75%

99.9%

99.95%

Two-sided

50%

60%

70%

80%

90%

95%

98%

99%

99.5%

99.8%

99.9%

1

1.000

1.376

1.963

3.078

6.314

12.706

31.821

63.657

127.321

318.309

636.619

2

0.816

1.061

1.386

1.886

2.920

4.303

6.965

9.925

14.089

22.327

31.599

3

0.765

0.978

1.250

1.638

2.353

3.182

4.541

5.841

7.453

10.215

12.924

4

0.741

0.941

1.190

1.533

2.132

2.776

3.747

4.604

5.598

7.173

8.610

5

0.727

0.920

1.156

1.476

2.015

2.571

3.365

4.032

4.773

5.893

6.869

6

0.718

0.906

1.134

1.440

1.943

2.447

3.143

3.707

4.317

5.208

5.959

7

0.711

0.896

1.119

1.415

1.895

2.365

2.998

3.499

4.029

4.785

5.408

8

0.706

0.889

1.108

1.397

1.860

2.306

2.896

3.355

3.833

4.501

5.041

9

0.703

0.883

1.100

1.383

1.833

2.262

2.821

3.250

3.690

4.297

4.781

10

0.700

0.879

1.093

1.372

1.812

2.228

2.764

3.169

3.581

4.144

4.587

11

0.697

0.876

1.088

1.363

1.796

2.201

2.718

3.106

3.497

4.025

4.437

12

0.695

0.873

1.083

1.356

1.782

2.179

2.681

3.055

3.428

3.930

4.318

13

0.694

0.870

1.079

1.350

1.771

2.160

2.650

3.012

3.372

3.852

4.221

14

0.692

0.868

1.076

1.345

1.761

2.145

2.624

2.977

3.326

3.787

4.140

15

0.691

0.866

1.074

1.341

1.753

2.131

2.602

2.947

3.286

3.733

4.073

16

0.690

0.865

1.071

1.337

1.746

2.120

2.583

2.921

3.252

3.686

4.015

17

0.689

0.863

1.069

1.333

1.740

2.110

2.567

2.898

3.222

3.646

3.965

18

0.688

0.862

1.067

1.330

1.734

2.101

2.552

2.878

3.197

3.610

3.922

19

0.688

0.861

1.066

1.328

1.729

2.093

2.539

2.861

3.174

3.579

3.883

20

0.687

0.860

1.064

1.325

1.725

2.086

2.528

2.845

3.153

3.552

3.850

21

0.686

0.859

1.063

1.323

1.721

2.080

2.518

2.831

3.135

3.527

3.819

22

0.686

0.858

1.061

1.321

1.717

2.074

2.508

2.819

3.119

3.505

3.792

23

0.685

0.858

1.060

1.319

1.714

2.069

2.500

2.807

3.104

3.485

3.767

24

0.685

0.857

1.059

1.318

1.711

2.064

2.492

2.797

3.091

3.467

3.745

25

0.684

0.856

1.058

1.316

1.708

2.060

2.485

2.787

3.078

3.450

3.725

26

0.684

0.856

1.058

1.315

1.706

2.056

2.479

2.779

3.067

3.435

3.707

27

0.684

0.855

1.057

1.314

1.703

2.052

2.473

2.771

3.057

3.421

3.690

28

0.683

0.855

1.056

1.313

1.701

2.048

2.467

2.763

3.047

3.408

3.674

29

0.683

0.854

1.055

1.311

1.699

2.045

2.462

2.756

3.038

3.396

3.659

30

0.683

0.854

1.055

1.310

1.697

2.042

2.457

2.750

3.030

3.385

3.646

40

0.681

0.851

1.050

1.303

1.684

2.021

2.423

2.704

2.971

3.307

3.551

50

0.679

0.849

1.047

1.299

1.676

2.009

2.403

2.678

2.937

3.261

3.496

60

0.679

0.848

1.045

1.296

1.671

2.000

2.390

2.660

2.915

3.232

3.460

80

0.678

0.846

1.043

1.292

1.664

1.990

2.374

2.639

2.887

3.195

3.416

100

0.677

0.845

1.042

1.290

1.660

1.984

2.364

2.626

2.871

3.174

3.390

120

0.677

0.845

1.041

1.289

1.658

1.980

2.358

2.617

2.860

3.160

3.373

∞

0.674

0.842

1.036

1.282

1.645

1.960

2.326

2.576

2.807

3.090

3.291

One-sided

75%

80%

85%

90%

95%

97.5%

99%

99.5%

99.75%

99.9%

99.95%

Two-sided

50%

60%

70%

80%

90%

95%

98%

99%

99.5%

99.8%

99.9%

Calculating the confidence interval

Let's say we have a sample with size 11, sample mean 10, and sample variance 2. For 90% confidence with 10 degrees of freedom, the one-sided t value from the table is 1.372 . Then with confidence interval calculated from
{\displaystyle {\overline {X}}_{n}\pm t_{\alpha ,\nu }\,{\frac {S_{n}}{\sqrt {n}}}\,,}

we determine that with 90% confidence we have a true mean lying below

10
+
1.372

2

11

=
10.585

.

{\displaystyle 10+1.372\,{\frac {\sqrt {2}}{\sqrt {11}}}=10.585\,.}

In other words, 90% of the times that an upper threshold is calculated by this method from particular samples, this upper threshold exceeds the true mean.
And with 90% confidence we have a true mean lying above

10
−
1.372

2

11

=
9.414

.

{\displaystyle \ 10-1.372\ {\frac {\sqrt {2\ }}{\ {\sqrt {11\ }}\ }}=9.414~.}

In other words, 90% of the times that a lower threshold is calculated by this method from particular samples, this lower threshold lies below the true mean.
So that at 80% confidence (calculated from 100% − 2 × (1 − 90%) = 80%), we have a true mean lying within the interval

(

10
−
1.372

2

11

,

10
+
1.372

2

11

)

=
(
9.414
,

10.585
{\displaystyle \left(10-1.372\,{\frac {\sqrt {2}}{\sqrt {11}}},\,10+1.372\,{\frac {\sqrt {2}}{\sqrt {11}}}\right)=(9.414,\,10.585)\,.}

Saying that 80% of the times that upper and lower thresholds are calculated by this method from a given sample, the true mean is both below the upper threshold and above the lower threshold is not the same as saying that there is an 80% probability that the true mean lies between a particular pair of upper and lower thresholds that have been calculated by this method; see confidence interval and prosecutor's fallacy.
Nowadays, statistical software, such as the R programming language, and functions available in many spreadsheet programs compute values of the t distribution and its inverse without tables.

Computational methods[edit]
Monte Carlo sampling[edit]
There are various approaches to constructing random samples from the Student's t distribution. The matter depends on whether the samples are required on a stand-alone basis, or are to be constructed by application of a quantile function to uniform samples; e.g., in the multi-dimensional applications basis of copula-dependency.[citation needed] In the case of stand-alone sampling, an extension of the Box–Muller method and its polar form is easily deployed.[18] It has the merit that it applies equally well to all real positive degrees of freedom, ν, while many other candidate methods fail if ν is close to zero.[18]

History[edit]
Statistician William Sealy Gosset, known as "Student"
In statistics, the t distribution was first derived as a posterior distribution in 1876 by Helmert[19][20][21] and Lüroth.[22][23][24] As such, Student's t-distribution is an example of Stigler's Law of Eponymy. The t distribution also appeared in a more general form as Pearson type IV distribution in Karl Pearson's 1895 paper.[25]
In the English-language literature, the distribution takes its name from William Sealy Gosset's 1908 paper in Biometrika under the pseudonym "Student" during his work at the Guinness Brewery in Dublin, Ireland.[26] One version of the origin of the pseudonym is that Gosset's employer preferred staff to use pen names when publishing scientific papers instead of their real name, so he used the name "Student" to hide his identity. Another version is that Guinness did not want their competitors to know that they were using the t test to determine the quality of raw material.[27][28]
Gosset worked at Guinness and was interested in the problems of small samples – for example, the chemical properties of barley where sample sizes might be as few as 3. Gosset's paper refers to the distribution as the "frequency distribution of standard deviations of samples drawn from a normal population". It became well known through the work of Ronald Fisher, who called the distribution "Student's distribution" and represented the test value with the letter t.[8][29]
