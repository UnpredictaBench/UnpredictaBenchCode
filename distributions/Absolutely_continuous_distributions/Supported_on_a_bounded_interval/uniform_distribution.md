# Continuous uniform distribution

Uniform distribution on an interval

| Continuous uniform |
| --- |
| Probability density functionUsing maximum convention |
| Cumulative distribution function |
| Notation | U [ a , b ] {\displaystyle {\mathcal {U}}_{[a,b]}} ${\displaystyle {\mathcal {U}}_{[a,b]}}$ |
| Parameters | − ∞ < a < b < ∞ {\displaystyle -\infty <a<b<\infty } ${\displaystyle -\infty <a<b<\infty }$ |
| Support | [ a , b ] {\displaystyle [a,b]} ${\displaystyle [a,b]}$ |
| PDF | { 1 b − a for x ∈ [ a , b ] 0 otherwise {\displaystyle {\begin{cases}{\frac {1}{b-a}}&{\text{for }}x\in [a,b]\\0&{\text{otherwise}}\end{cases}}} ${\displaystyle {\begin{cases}{\frac {1}{b-a}}&{\text{for }}x\in [a,b]\\0&{\text{otherwise}}\end{cases}}}$ |
| CDF | { 0 for x < a x − a b − a for x ∈ [ a , b ] 1 for x > b {\displaystyle {\begin{cases}0&{\text{for }}x<a\\{\frac {x-a}{b-a}}&{\text{for }}x\in [a,b]\\1&{\text{for }}x>b\end{cases}}} ${\displaystyle {\begin{cases}0&{\text{for }}x<a\\{\frac {x-a}{b-a}}&{\text{for }}x\in [a,b]\\1&{\text{for }}x>b\end{cases}}}$ |
| Mean | 1 2 ( a + b ) {\displaystyle {\tfrac {1}{2}}(a+b)} ${\displaystyle {\tfrac {1}{2}}(a+b)}$ |
| Median | 1 2 ( a + b ) {\displaystyle {\tfrac {1}{2}}(a+b)} ${\displaystyle {\tfrac {1}{2}}(a+b)}$ |
| Mode | any value in ( a , b ) {\displaystyle {\text{any value in }}(a,b)} ${\displaystyle {\text{any value in }}(a,b)}$ |
| Variance | 1 12 ( b − a ) 2 {\displaystyle {\tfrac {1}{12}}(b-a)^{2}} ${\displaystyle {\tfrac {1}{12}}(b-a)^{2}}$ |
| MAD | 1 4 ( b − a ) {\displaystyle {\tfrac {1}{4}}(b-a)} ${\displaystyle {\tfrac {1}{4}}(b-a)}$ |
| Skewness | 0 {\displaystyle 0} ${\displaystyle 0}$ |
| Excess kurtosis | − 6 5 {\displaystyle -{\tfrac {6}{5}}} ${\displaystyle -{\tfrac {6}{5}}}$ |
| Entropy | log ⁡ ( b − a ) {\displaystyle \log(b-a)} ${\displaystyle \log(b-a)}$ |
| MGF | { e t b − e t a t ( b − a ) for t ≠ 0 1 for t = 0 {\displaystyle {\begin{cases}{\frac {\mathrm {e} ^{tb}-\mathrm {e} ^{ta}}{t(b-a)}}&{\text{for }}t\neq 0\\1&{\text{for }}t=0\end{cases}}} ${\displaystyle {\begin{cases}{\frac {\mathrm {e} ^{tb}-\mathrm {e} ^{ta}}{t(b-a)}}&{\text{for }}t\neq 0\\1&{\text{for }}t=0\end{cases}}}$ |
| CF | { e i t b − e i t a i t ( b − a ) for t ≠ 0 1 for t = 0 {\displaystyle {\begin{cases}{\frac {\mathrm {e} ^{\mathrm {i} tb}-\mathrm {e} ^{\mathrm {i} ta}}{\mathrm {i} t(b-a)}}&{\text{for }}t\neq 0\\1&{\text{for }}t=0\end{cases}}} ${\displaystyle {\begin{cases}{\frac {\mathrm {e} ^{\mathrm {i} tb}-\mathrm {e} ^{\mathrm {i} ta}}{\mathrm {i} t(b-a)}}&{\text{for }}t\neq 0\\1&{\text{for }}t=0\end{cases}}}$ |

In probability theory and statistics, the continuous uniform distributions or rectangular distributions are a family of symmetric probability distributions. Such a distribution describes an experiment where there is an arbitrary outcome that lies between certain bounds.[1] The bounds are defined by the parameters, 

a

{\displaystyle a}
{\displaystyle b,}

 which are the minimum and maximum values. The interval can either be closed (i.e. 
{\displaystyle [a,b]}

) or open (i.e. 
{\displaystyle (a,b)}

).[2] Therefore, the distribution is often abbreviated 
{\displaystyle U(a,b),}

 where 

U

{\displaystyle U}

 stands for uniform distribution.[1] The difference between the bounds defines the interval length; all intervals of the same length on the distribution's support are equally probable. It is the maximum entropy probability distribution for a random variable 

X

{\displaystyle X}

 under no constraint other than that it is contained in the distribution's support.[3] ${\displaystyle a}$ ${\displaystyle b,}$ ${\displaystyle [a,b]}$ ${\displaystyle (a,b)}$ ${\displaystyle U(a,b),}$ ${\displaystyle U}$ ${\displaystyle X}$

Definitions[edit]
Probability density function[edit]
The probability density function of the continuous uniform distribution is
{\displaystyle f(x)={\begin{cases}{\dfrac {1}{b-a}}&{\text{for }}a\leq x\leq b,\\[8pt]0&{\text{for }}x<a\ {\text{ or }}\ x>b.\end{cases}}}

The values of 
{\displaystyle f(x)}

 at the two boundaries 

a

{\displaystyle a}
{\displaystyle b}

 are usually unimportant, because they do not alter the value of 

∫

c

d

f
(
x
)
d
x

{\textstyle \int _{c}^{d}f(x)dx}

 over any interval 
{\displaystyle [c,d],}

 nor of 

∫

a

b

x
f
(
x
)

d
x
,

{\textstyle \int _{a}^{b}xf(x)\,dx,}

 nor of any higher moment. Sometimes they are chosen to be zero, and sometimes chosen to be 
{\displaystyle {\tfrac {1}{b-a}}.}

 The latter is appropriate in the context of estimation by the method of maximum likelihood. In the context of Fourier analysis, one may take the value of 
{\displaystyle f(a)}
{\displaystyle f(b)}

 to be 
{\displaystyle {\tfrac {1}{2(b-a)}},}

 because then the inverse transform of many integral transforms of this uniform function will yield back the function itself, rather than a function which is equal "almost everywhere", i.e. except on a set of points with zero measure. Also, it is consistent with the sign function, which has no such ambiguity.
Any probability density function integrates to 
{\displaystyle 1,}

 so the probability density function of the continuous uniform distribution is graphically portrayed as a rectangle where ⁠
{\displaystyle b-a}

⁠ is the base length and ⁠
{\displaystyle {\tfrac {1}{b-a}}}

⁠ is the height. As the base length increases, the height (the density at any particular value within the distribution boundaries) decreases.[4]
In terms of mean 

μ

{\displaystyle \mu }

 and variance 
{\displaystyle \sigma ^{2},}

 the probability density function of the continuous uniform distribution is

f
(
x
)
=

{

1

2
σ

3

for 

−
σ

3

≤
x
−
μ
≤
σ

3

,

0

otherwise

.

{\displaystyle f(x)={\begin{cases}{\dfrac {1}{2\sigma {\sqrt {3}}}}&{\text{for }}-\sigma {\sqrt {3}}\leq x-\mu \leq \sigma {\sqrt {3}},\\[2pt]0&{\text{otherwise}}.\end{cases}}}

Cumulative distribution function[edit]
The cumulative distribution function of the continuous uniform distribution is:
{\displaystyle F(x)={\begin{cases}0&{\text{for }}x<a,\\[8pt]{\frac {x-a}{b-a}}&{\text{for }}a\leq x\leq b,\\[8pt]1&{\text{for }}x>b.\end{cases}}}

Its inverse is:
{\displaystyle F^{-1}(p)=a+p(b-a)\quad {\text{ for }}0<p<1.}

In terms of mean 

μ

{\displaystyle \mu }

 and variance 
{\displaystyle \sigma ^{2},}

 the cumulative distribution function of the continuous uniform distribution is:
{\displaystyle F(x)={\begin{cases}0&{\text{for }}x-\mu <-\sigma {\sqrt {3}},\\{\frac {1}{2}}\left({\frac {x-\mu }{\sigma {\sqrt {3}}}}+1\right)&{\text{for }}-\sigma {\sqrt {3}}\leq x-\mu <\sigma {\sqrt {3}},\\1&{\text{for }}x-\mu \geq \sigma {\sqrt {3}};\end{cases}}}

its inverse is:
{\displaystyle F^{-1}(p)=\sigma {\sqrt {3}}(2p-1)+\mu \quad {\text{ for }}0\leq p\leq 1.}

Example 1. Using the continuous uniform distribution function[edit]
For a random variable 
{\displaystyle X\sim U(0,23),}

 find 
{\displaystyle \Pr(2<X<18):}
{\displaystyle \Pr(2<X<18)=(18-2)\cdot {\frac {1}{23-0}}={\frac {16}{23}}.}

In a graphical representation of the continuous uniform distribution function 
{\displaystyle [f(x){\text{ vs }}x],}

 the area under the curve within the specified bounds, displaying the probability, is a rectangle. For the specific example above, the base would be ⁠
{\displaystyle 16,}

⁠ and the height would be ⁠
{\displaystyle {\tfrac {1}{23}}.}

⁠[5]

Example 2. Using the continuous uniform distribution function (conditional)[edit]
For a random variable 
{\displaystyle X\sim U(0,23),}

 find 
{\displaystyle \Pr(X>12\mid X>8):}
{\displaystyle \Pr(X>12\mid X>8)=(23-12)\cdot {\frac {1}{23-8}}={\frac {11}{15}}.}

The example above is a conditional probability case for the continuous uniform distribution: given that ⁠
{\displaystyle X>8}

⁠ is true, what is the probability that ⁠
{\displaystyle X>12?}

⁠ Conditional probability changes the sample space, so a new interval length ⁠
{\displaystyle b-a'}

⁠ has to be calculated, where 
{\displaystyle b=23}
{\displaystyle a'=8.}

[5] The graphical representation would still follow Example 1, where the area under the curve within the specified bounds displays the probability; the base of the rectangle would be ⁠
{\displaystyle 11,}

⁠ and the height would be ⁠
{\displaystyle {\tfrac {1}{15}}.}

⁠[5]

Generating functions[edit]
Moment-generating function[edit]
The moment-generating function of the continuous uniform distribution is:[6]
{\displaystyle M_{X}=\operatorname {E} \left[e^{tX}\right]=\int _{a}^{b}e^{tx}{\frac {dx}{b-a}}={\frac {e^{tb}-e^{ta}}{t(b-a)}}={\frac {B^{t}-A^{t}}{t(b-a)}},}

from which we may calculate the raw moments 
{\displaystyle m_{k}:}
{\displaystyle m_{1}={\frac {a+b}{2}},}
{\displaystyle m_{2}={\frac {a^{2}+ab+b^{2}}{3}},}
{\displaystyle m_{k}={\frac {\sum _{i=0}^{k}a^{i}b^{k-i}}{k+1}}.}

For a random variable following the continuous uniform distribution, the expected value is 
{\displaystyle m_{1}={\tfrac {a+b}{2}},}

 and the variance is 
{\displaystyle m_{2}-m_{1}^{2}={\tfrac {(b-a)^{2}}{12}}.}

For the special case 
{\displaystyle a=-b,}

 the probability density function of the continuous uniform distribution is:

f
(
x
)
=

{

1

2
b

for 

−
b
≤
x
≤
b
,

0

otherwise

;

{\displaystyle f(x)={\begin{cases}{\frac {1}{2b}}&{\text{for }}-b\leq x\leq b,\\[8pt]0&{\text{otherwise}};\end{cases}}}

the moment-generating function reduces to the simple form:

M

X

=

sinh
{\displaystyle M_{X}={\frac {\sinh bt}{bt}}.}

Cumulant-generating function[edit]
For ⁠
{\displaystyle n\geq 2,}

⁠ the 

n

{\displaystyle n}

-th cumulant of the continuous uniform distribution on the interval ⁠
{\displaystyle [-{\tfrac {1}{2}},{\tfrac {1}{2}}]}
{\displaystyle {\tfrac {B_{n}}{n}},}

 where 
{\displaystyle B_{n}}

 is the 

n

{\displaystyle n}

-th Bernoulli number.[7]

Standard uniform distribution[edit]
The continuous uniform distribution with parameters 
{\displaystyle a=0}
{\displaystyle b=1,}
{\displaystyle U(0,1),}

 is called the standard uniform distribution.
One interesting property of the standard uniform distribution is that if 
{\displaystyle u_{1}}

 has a standard uniform distribution, then so does 
{\displaystyle 1-u_{1}.}

 This property can be used for generating antithetic variates, among other things. In other words, this property is known as the inversion method where the continuous standard uniform distribution can be used to generate random numbers for any other continuous distribution.[4] If 
{\displaystyle u_{1}}

 is a uniform random number with standard uniform distribution, i.e. with 
{\displaystyle U(0,1),}

 then 
{\displaystyle x=F^{-1}(u_{1})}

 generates a random number 

x

{\displaystyle x}

 from any continuous distribution with the specified cumulative distribution function 
{\displaystyle F.}

[4]

Relationship to other functions[edit]
As long as the same conventions are followed at the transition points, the probability density function of the continuous uniform distribution may also be expressed in terms of the Heaviside step function as:
{\displaystyle f(x)={\frac {\operatorname {H} (x-a)-\operatorname {H} (x-b)}{b-a}},}

or in terms of the rectangle function as:

f
(
x
)
=

1

b
−
a

rect
{\displaystyle f(x)={\frac {1}{b-a}}\ \operatorname {rect} \left({\frac {x-{\frac {a+b}{2}}}{b-a}}\right).}

There is no ambiguity at the transition point of the sign function. Using the half-maximum convention at the transition points, the continuous uniform distribution may be expressed in terms of the sign function as:
{\displaystyle f(x)={\frac {\operatorname {sgn} {(x-a)}-\operatorname {sgn} {(x-b)}}{2(b-a)}}.}

Properties[edit]
Moments[edit]
The mean (first raw moment) of the continuous uniform distribution is:
{\displaystyle \operatorname {E} [X]=\int _{a}^{b}x{\frac {dx}{b-a}}={\frac {b^{2}-a^{2}}{2(b-a)}}={\frac {b+a}{2}}.}

The second raw moment of this distribution is:
{\displaystyle \operatorname {E} \left[X^{2}\right]=\int _{a}^{b}x^{2}{\frac {dx}{b-a}}={\frac {b^{3}-a^{3}}{3(b-a)}}.}

In general, the 

n

{\displaystyle n}

-th raw moment of this distribution is:
{\displaystyle \operatorname {E} \left[X^{n}\right]=\int _{a}^{b}x^{n}{\frac {dx}{b-a}}={\frac {b^{n+1}-a^{n+1}}{(n+1)(b-a)}}.}

The variance (second central moment) of this distribution is:
{\displaystyle \operatorname {Var} [X]=\operatorname {E} \left[{\left(X-\operatorname {E} [X]\right)}^{2}\right]=\int _{a}^{b}\left(x-{\frac {a+b}{2}}\right)^{2}{\frac {dx}{b-a}}={\frac {(b-a)^{2}}{12}}.}

Order statistics[edit]
{\displaystyle X_{1},...,X_{n}}

 be an i.i.d. sample from 
{\displaystyle U(0,1),}

 and let 
{\displaystyle X_{(k)}}

 be the 

k

{\displaystyle k}

-th order statistic from this sample.
{\displaystyle X_{(k)}}

 has a beta distribution, with parameters 

k

{\displaystyle k}

 and ⁠
{\displaystyle n-k+1.}

⁠
The expected value is:
{\displaystyle \operatorname {E} \left[X_{(k)}\right]={\frac {k}{n+1}}.}

This fact is useful when making Q–Q plots.
The variance is:
{\displaystyle \operatorname {Var} \left[X_{(k)}\right]={\frac {k(n-k+1)}{(n+1)^{2}(n+2)}}.}

See also: Order statistic § Probability distributions of order statistics
Uniformity[edit]
The probability that a continuously uniformly distributed random variable falls within any interval of fixed length is independent of the location of the interval itself (but it is dependent on the interval size 
{\displaystyle (\ell )}

), so long as the interval is contained in the distribution's support.
Indeed, if 
{\displaystyle X\sim U(a,b)}

 and if 
{\displaystyle [x,x+\ell ]}

 is a subinterval of 
{\displaystyle [a,b]}

 with fixed 
{\displaystyle \ell >0,}

 then:
{\displaystyle \Pr {\big (}X\in [x,x+\ell ]{\big )}=\int _{x}^{x+\ell }{\frac {dy}{b-a}}={\frac {\ell }{b-a}},}

which is independent of 
{\displaystyle x.}

 This fact motivates the distribution's name.

Uniform distribution on more general sets[edit]
The uniform distribution can be generalized to sets more general than intervals. 
Formally, let 

S

{\displaystyle S}

 be a Borel set of positive, finite Lebesgue measure 
{\displaystyle \lambda (S),}
{\displaystyle 0<\lambda (S)<+\infty .}

 The uniform distribution on 

S

{\displaystyle S}

 can be specified by defining the probability density function to be zero outside 

S

{\displaystyle S}

 and constantly equal to 
{\displaystyle {\tfrac {1}{\lambda (S)}}}
{\displaystyle S.}

An interesting special case is when the set S is a simplex. It is possible to obtain a uniform distribution on the standard n-vertex simplex in the following way.[8]: Thm.4.1 take n independent random variables with the same exponential distribution; denote them by X1,...,Xn; and let Yi := Xi / (sumi Xi). Then, the vector Y1,...,Yn is uniformly distributed on the simplex.

Related distributions[edit]
If X has a standard uniform distribution, then by the inverse transform sampling method, Y = − λ−1 ln(X) has an exponential distribution with (rate) parameter λ.
If X has a standard uniform distribution, then Y = Xn has a beta distribution with parameters (1/n,1). As such,
The standard uniform distribution is a special case of the beta distribution, with parameters (1,1).
The Irwin–Hall distribution is the sum of n i.i.d. U(0,1) distributions.
The Bates distribution is the average of n i.i.d. U(0,1) distributions.
The sum of two independent uniform distributions U1(a,b)+U2(c,d) yields a trapezoidal distribution, symmetric about its mean, on the support [a+c,b+d]. The plateau has width equals to the absolute different of the width of U1 and U2. The width of the sloped parts corresponds to the width of the narrowest uniform distribution.
If the uniform distributions have the same width w, the result is a triangular distribution, symmetric about its mean, on the support [a+c,a+c+2w].
The sum of two independent, equally distributed, uniform distributions U1(a,b)+U2(a,b) yields a symmetric triangular distribution on the support [2a,2b].
The distance between two i.i.d. uniform random variables |U1(a,b)-U2(a,b)| also has a triangular distribution, although not symmetric, on the support [0,b-a].
Statistical inference[edit]
Estimation of parameters[edit]
Estimation of maximum[edit]
Minimum-variance unbiased estimator[edit]
Main article: German tank problem
Given a uniform distribution on 
{\displaystyle [0,b]}

 with unknown 
{\displaystyle b,}

 the minimum-variance unbiased estimator (UMVUE) for the maximum is:

b
^

UMVU
{\displaystyle {\hat {b}}_{\text{UMVU}}={\frac {k+1}{k}}m=m+{\frac {m}{k}},}

where 

m

{\displaystyle m}

 is the sample maximum and 

k

{\displaystyle k}

 is the sample size, sampling without replacement (though this distinction almost surely makes no difference for a continuous distribution). This follows for the same reasons as estimation for the discrete distribution, and can be seen as a very simple case of maximum spacing estimation. This problem is commonly known as the German tank problem, due to application of maximum estimation to estimates of German tank production during World War II.

Method of moments estimator[edit]
The method of moments estimator is:
{\displaystyle {\hat {b}}_{MM}=2{\bar {X}},}

where 
{\displaystyle {\bar {X}}}

 is the sample mean.

Maximum likelihood estimator[edit]
The maximum likelihood estimator is:
{\displaystyle {\hat {b}}_{ML}=m,}

where 

m

{\displaystyle m}

 is the sample maximum, also denoted as 
{\displaystyle m=X_{(n)},}

 the maximum order statistic of the sample.

Estimation of minimum[edit]
Given a uniform distribution on 
{\displaystyle [a,b]}

 with unknown a, the maximum likelihood estimator for a is:
{\displaystyle {\hat {a}}_{ML}=\min\{X_{1},\dots ,X_{n}\}}

,
the sample minimum.[9]

Estimation of midpoint[edit]
The midpoint of the distribution, 
{\displaystyle {\tfrac {a+b}{2}},}

 is both the mean and the median of the uniform distribution. Although both the sample mean and the sample median are unbiased estimators of the midpoint, neither is as efficient as the sample mid-range, i.e. the arithmetic mean of the sample maximum and the sample minimum, which is the UMVU estimator of the midpoint (and also the maximum likelihood estimate).

Confidence interval[edit]
For the maximum[edit]
{\displaystyle X_{1},X_{2},X_{3},...,X_{n}}

 be a sample from 
{\displaystyle U_{[0,L]},}

 where 

L

{\displaystyle L}

 is the maximum value in the population. Then 
{\displaystyle X_{(n)}=\max(X_{1},X_{2},X_{3},...,X_{n})}

 has the Lebesgue–Borel density 
{\displaystyle f={\frac {d\Pr _{X_{(n)}}}{d\lambda }}:}
{\displaystyle f(t)=n{\frac {1}{L}}\left({\frac {t}{L}}\right)^{n-1}\!=n{\frac {t^{n-1}}{L^{n}}}1\!\!1_{[0,L]}(t),}

 where 
{\displaystyle 1\!\!1_{[0,L]}}

 is the indicator function of 
{\displaystyle [0,L].}

The confidence interval given before is mathematically incorrect, as
{\displaystyle \Pr {\big (}[{\hat {\theta }},{\hat {\theta }}+\varepsilon ]\ni \theta {\big )}\geq 1-\alpha }

cannot be solved for 

ε

{\displaystyle \varepsilon }

 without knowledge of 

θ

{\displaystyle \theta }

. However, one can solve
{\displaystyle \Pr {\big (}[{\hat {\theta }},{\hat {\theta }}(1+\varepsilon )]\ni \theta {\big )}\geq 1-\alpha }
{\displaystyle \varepsilon \geq \alpha ^{-1/n}-1}

 for any unknown but valid 
{\displaystyle \theta ;}

one then chooses the smallest 

ε

{\displaystyle \varepsilon }

 possible satisfying the condition above. Note that the interval length depends upon the random variable 
{\displaystyle {\hat {\theta }}.}

Occurrence and applications[edit]
The probabilities for uniform distribution function are simple to calculate due to the simplicity of the function form.[2] Therefore, there are various applications that this distribution can be used for as shown below: hypothesis testing situations, random sampling cases, finance, etc. Furthermore, generally, experiments of physical origin follow a uniform distribution (e.g. emission of radioactive particles).[1] However, it is important to note that in any application, there is the unchanging assumption that the probability of falling in an interval of fixed length is constant.[2]

Economics example for uniform distribution[edit]
In the field of economics, usually demand and replenishment may not follow the expected normal distribution. As a result, other distribution models are used to better predict probabilities and trends such as Bernoulli process.[11] But according to Wanke (2008), in the particular case of investigating lead-time for inventory management at the beginning of the life cycle when a completely new product is being analyzed, the uniform distribution proves to be more useful.[11] In this situation, other distribution may not be viable since there is no existing data on the new product or that the demand history is unavailable so there isn't really an appropriate or known distribution.[11] The uniform distribution would be ideal in this situation since the random variable of lead-time (related to demand) is unknown for the new product but the results are likely to range between a plausible range of two values.[11] The lead-time would thus represent the random variable. From the uniform distribution model, other factors related to lead-time were able to be calculated such as cycle service level and shortage per cycle. It was also noted that the uniform distribution was also used due to the simplicity of the calculations.[11]

Sampling from an arbitrary distribution[edit]
Main article: Inverse transform sampling
The uniform distribution is useful for sampling from arbitrary distributions. A general method is the inverse transform sampling method, which uses the cumulative distribution function (CDF) of the target random variable. This method is very useful in theoretical work. Since simulations using this method require inverting the CDF of the target variable, alternative methods have been devised for the cases where the CDF is not known in closed form. One such method is rejection sampling.
The normal distribution is an important example where the inverse transform method is not efficient. However, there is an exact method, the Box–Muller transformation, which uses the inverse transform to convert two independent uniform random variables into two independent normally distributed random variables.

Quantization error[edit]
Main article: Quantization error
In analog-to-digital conversion, a quantization error occurs. This error is either due to rounding or truncation. When the original signal is much larger than one least significant bit (LSB), the quantization error is not significantly correlated with the signal, and has an approximately uniform distribution. The RMS error therefore follows from the variance of this distribution.

Random variate generation[edit]
There are many applications in which it is useful to run simulation experiments. Many programming languages come with implementations to generate pseudo-random numbers which are effectively distributed according to the standard uniform distribution.
On the other hand, the uniformly distributed numbers are often used as the basis for non-uniform random variate generation.
{\displaystyle u}

 is a value sampled from the standard uniform distribution, then the value 
{\displaystyle a+(b-a)u}

 follows the uniform distribution parameterized by 

a

{\displaystyle a}
{\displaystyle b,}

 as described above.

History[edit]
While the historical origins in the conception of uniform distribution are inconclusive, it is speculated that the term "uniform" arose from the concept of equiprobability in dice games (note that the dice games would have discrete and not continuous uniform sample space). Equiprobability was mentioned in Gerolamo Cardano's Liber de Ludo Aleae, a manual written in 16th century and detailed on advanced probability calculus in relation to dice.[12]
