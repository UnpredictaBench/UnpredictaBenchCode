# Logistic distribution

Continuous probability distribution

| Logistic distribution |
| --- |
| Probability density function |
| Cumulative distribution function |
| Parameters | μ , {\displaystyle \mu ,} location (real) s > 0 , {\displaystyle s>0,} scale (real) ${\displaystyle \mu ,}$ ${\displaystyle s>0,}$ |
| Support | x ∈ ( − ∞ , ∞ ) {\displaystyle x\in (-\infty ,\infty )} ${\displaystyle x\in (-\infty ,\infty )}$ |
| PDF | e − ( x − μ ) / s s ( 1 + e − ( x − μ ) / s ) 2 {\displaystyle {\frac {e^{-(x-\mu )/s}}{s\left(1+e^{-(x-\mu )/s}\right)^{2}}}} ${\displaystyle {\frac {e^{-(x-\mu )/s}}{s\left(1+e^{-(x-\mu )/s}\right)^{2}}}}$ |
| CDF | 1 1 + e − ( x − μ ) / s = 1 + tanh ⁡ x − μ 2 s 2 {\displaystyle {\frac {1}{1+e^{-(x-\mu )/s}}}={\frac {1+\tanh {\frac {x-\mu }{2s}}}{2}}} ${\displaystyle {\frac {1}{1+e^{-(x-\mu )/s}}}={\frac {1+\tanh {\frac {x-\mu }{2s}}}{2}}}$ |
| Quantile | μ + s log ⁡ ( p 1 − p ) {\displaystyle \mu +s\log \left({\frac {p}{1-p}}\right)} ${\displaystyle \mu +s\log \left({\frac {p}{1-p}}\right)}$ |
| Mean | μ {\displaystyle \mu } ${\displaystyle \mu }$ |
| Median | μ {\displaystyle \mu } ${\displaystyle \mu }$ |
| Mode | μ {\displaystyle \mu } ${\displaystyle \mu }$ |
| Variance | s 2 π 2 3 {\displaystyle {\frac {s^{2}\pi ^{2}}{3}}} ${\displaystyle {\frac {s^{2}\pi ^{2}}{3}}}$ |
| Skewness | 0 {\displaystyle 0} ${\displaystyle 0}$ |
| Excess kurtosis | 6 / 5 {\displaystyle 6/5} ${\displaystyle 6/5}$ |
| Entropy | ln ⁡ s + 2 {\displaystyle \ln s+2} ${\displaystyle \ln s+2}$ |
| MGF | e μ t B ( 1 − s t , 1 + s t ) {\displaystyle e^{\mu t}\mathrm {B} (1-st,1+st)} for t ∈ ( − 1 / s , 1 / s ) {\displaystyle t\in (-1/s,1/s)} and B {\displaystyle \mathrm {B} } is the Beta function ${\displaystyle e^{\mu t}\mathrm {B} (1-st,1+st)}$ ${\displaystyle t\in (-1/s,1/s)}$ ${\displaystyle \mathrm {B} }$ |
| CF | e i t μ π s t sinh ⁡ ( π s t ) {\displaystyle e^{it\mu }{\frac {\pi st}{\sinh(\pi st)}}} ${\displaystyle e^{it\mu }{\frac {\pi st}{\sinh(\pi st)}}}$ |
| Expected shortfall | μ + s H ( p ) 1 − p {\displaystyle \mu +{\frac {sH(p)}{1-p}}} where H ( p ) {\displaystyle H(p)} is the binary entropy function[1] H ( p ) = − p ln ⁡ ( p ) − ( 1 − p ) ln ⁡ ( 1 − p ) {\displaystyle H(p)=-p\ln(p)-(1-p)\ln(1-p)} ${\displaystyle \mu +{\frac {sH(p)}{1-p}}}$ ${\displaystyle H(p)}$ ${\displaystyle H(p)=-p\ln(p)-(1-p)\ln(1-p)}$ |

In probability theory and statistics, the logistic distribution is a continuous probability distribution. Its cumulative distribution function is the logistic function, which appears in logistic regression and feedforward neural networks. It resembles the normal distribution in shape but has heavier tails (higher kurtosis).  The logistic distribution is a special case of the Tukey lambda distribution.

Specification[edit]
Cumulative distribution function[edit]
The logistic distribution receives its name from its cumulative distribution function, which is an instance of the family of logistic functions. The cumulative distribution function of the logistic distribution is also a scaled version of the hyperbolic tangent.

F
(
x
;
μ
,
s
)
=

1

1
+

e

−
(
x
−
μ
)

/

s

=

1
2

+

1
2

tanh
{\displaystyle F(x;\mu ,s)={\frac {1}{1+e^{-(x-\mu )/s}}}={\frac {1}{2}}+{\frac {1}{2}}\operatorname {tanh} \left({\frac {x-\mu }{2s}}\right).}

In this equation μ is the mean, and s is a scale parameter proportional to the standard deviation.

Probability density function[edit]
The probability density function is the partial derivative of the cumulative distribution function:

f
(
x
;
μ
,
s
)

=

∂
F
(
x
;
μ
,
s
)

∂
x

=

e

−
(
x
−
μ
)

/

s

s

(

1
+

e

−
(
x
−
μ
)

/

s

)

2

=

1

s

(

e

(
x
−
μ
)

/

(
2
s
)

+

e

−
(
x
−
μ
)

/

(
2
s
)

)

2

=

1

4
s

sech
{\displaystyle {\begin{aligned}f(x;\mu ,s)&={\frac {\partial F(x;\mu ,s)}{\partial x}}={\frac {e^{-(x-\mu )/s}}{s\left(1+e^{-(x-\mu )/s}\right)^{2}}}\\[4pt]&={\frac {1}{s\left(e^{(x-\mu )/(2s)}+e^{-(x-\mu )/(2s)}\right)^{2}}}\\[4pt]&={\frac {1}{4s}}\operatorname {sech} ^{2}\left({\frac {x-\mu }{2s}}\right).\end{aligned}}}

When the location parameter μ is 0 and the scale parameter s is 1, then the probability density function of the logistic distribution is given by

f
(
x
;
0
,
1
)

=

e

−
x

(
1
+

e

−
x

)

2

=

1

(

e

x

/

2

+

e

−
x

/

2

)

2

=

1
4

sech
{\displaystyle {\begin{aligned}f(x;0,1)&={\frac {e^{-x}}{(1+e^{-x})^{2}}}\\[4pt]&={\frac {1}{(e^{x/2}+e^{-x/2})^{2}}}\\[5pt]&={\frac {1}{4}}\operatorname {sech} ^{2}\left({\frac {x}{2}}\right).\end{aligned}}}

Because this function can be expressed in terms of the square of the hyperbolic secant function "sech", it is sometimes referred to as the sech-square(d) distribution or hyperbolic secant square(d) distribution.[2] This should not be confused with the hyperbolic secant distribution.

Quantile function[edit]
The inverse cumulative distribution function (quantile function) of the logistic distribution is a generalization of the logit function.  Its derivative is called the quantile density function.  They are defined as follows:
{\displaystyle Q(p;\mu ,s)=\mu +s\ln \left({\frac {p}{1-p}}\right).}
{\displaystyle Q'(p;s)={\frac {s}{p(1-p)}}.}

Alternative parameterization[edit]
An alternative parameterization of the logistic distribution can be derived by expressing the scale parameter, 

s

{\displaystyle s}

, in terms of the standard deviation, 

σ

{\displaystyle \sigma }

, using the substitution 
{\displaystyle s\,=\,q\,\sigma }

, where 

q

=

3

/

π

=

0.551328895
…

{\displaystyle q\,=\,{\sqrt {3}}/{\pi }\,=\,0.551328895\ldots }

.  The alternative forms of the above functions are reasonably straightforward.

Applications[edit]
The logistic distribution—and the S-shaped pattern of its cumulative distribution function (the logistic function) and quantile function (the logit function)—have been extensively used in many different areas.

Logistic regression[edit]
One of the most common applications is in logistic regression, which is used for modeling categorical dependent variables (e.g., yes-no choices or a choice of 3 or 4 possibilities), much as standard linear regression is used for modeling continuous variables (e.g., income or population). Specifically, logistic regression models can be phrased as latent variable models with error variables following a logistic distribution. This phrasing is common in the theory of discrete choice models, where the logistic distribution plays the same role in logistic regression as the normal distribution does in probit regression. Indeed, the logistic and normal distributions have a quite similar shape. However, the logistic distribution has heavier tails, which often increases the robustness of analyses based on it compared with using the normal distribution.

Physics[edit]
The PDF of this distribution has the same functional form as the derivative of the Fermi function. In the theory of electron properties in semiconductors and metals, this derivative sets the relative weight of the various electron energies in their contributions to electron transport. Those energy levels whose energies are closest to the distribution's "mean" (Fermi level) dominate processes such as electronic conduction, with some smearing induced by temperature.[3]: 34  However the pertinent probability distribution in Fermi–Dirac statistics is actually a simple Bernoulli distribution, with the probability factor given by the Fermi function.
The logistic distribution arises as limit distribution of a finite-velocity damped random motion described by a telegraph process in which the random times between consecutive velocity changes have independent exponential distributions with linearly increasing parameters.[4]

Hydrology[edit]
Fitted cumulative logistic distribution to October rainfalls
In hydrology the distribution of long duration river discharge and rainfall (e.g., monthly and yearly totals, consisting of the sum of 30 respectively 360 daily values) is often thought to be almost normal according to the central limit theorem.[5] The normal distribution, however, needs a numeric approximation. As the logistic distribution, which can be solved analytically, is similar to the normal distribution, it can be used instead. The blue picture illustrates an example of fitting the logistic distribution to ranked October rainfalls—that are almost normally distributed—and it shows the 90% confidence belt based on the binomial distribution. The rainfall data are represented by plotting positions as part of the cumulative frequency analysis.

Chess ratings[edit]
The United States Chess Federation has switched its formula for calculating chess ratings from the normal distribution to the logistic distribution; see the article on Elo rating system (itself based on the normal distribution).

Related distributions[edit]
Logistic distribution mimics the sech distribution; they are different cases of the Champernowne distribution.
{\displaystyle X\sim \mathrm {Logistic} (\mu ,s)}

 then 
{\displaystyle kX+\ell \sim \mathrm {Logistic} (k\mu +\ell ,|k|s)}
{\displaystyle X\sim }

 U(0, 1) then 

μ
+
s
⋅

logit
{\displaystyle \mu +s\cdot {\text{logit}}(X)\sim \mathrm {Logistic} (\mu ,s)}

, where 

logit
{\displaystyle {\text{logit}}(X)=\log X-\log(1-X)}

 is the logit function.
{\displaystyle X\sim \mathrm {Gumbel} (\mu _{X},\beta )}
{\displaystyle Y\sim \mathrm {Gumbel} (\mu _{Y},\beta )}

 independently then 
{\displaystyle X-Y\sim \mathrm {Logistic} (\mu _{X}-\mu _{Y},\beta )\,}
{\displaystyle X}
{\displaystyle Y\sim \mathrm {Gumbel} (\mu ,\beta )}

 then 
{\displaystyle X+Y\nsim \mathrm {Logistic} (2\mu ,\beta )\,}

 (The sum is not a logistic distribution). 
{\displaystyle E(X+Y)=2\mu +2\beta \gamma \neq 2\mu =E\left(\mathrm {Logistic} (2\mu ,\beta )\right)}

.
If X ~ Logistic(μ, s) then exp(X) ~ LogLogistic
{\displaystyle \left(\alpha =e^{\mu },\beta ={\frac {1}{s}}\right)}

,  and  exp(X) + γ ~ shifted log-logistic
{\displaystyle \left(\alpha =e^{\mu },\beta ={\frac {1}{s}},\gamma \right)}

.
If X ~ Exponential(1) then

μ
+
s
log
⁡
(

e

X

−
1
)
∼
Logistic
{\displaystyle \mu +s\log(e^{X}-1)\sim \operatorname {Logistic} (\mu ,s).}

If X, Y ~ Exponential(λ) independently then

μ
+
s
log
⁡

(

X
Y

)

∼
Logistic
{\displaystyle \mu +s\log \left({\frac {X}{Y}}\right)\sim \operatorname {Logistic} (\mu ,s).}

The metalog distribution is generalization of the logistic distribution, in which power series expansions in terms of 

p

{\displaystyle p}

 are substituted for logistic parameters 

μ

{\displaystyle \mu }
{\displaystyle \sigma }

. The resulting metalog quantile function is highly shape flexible, has a simple closed form, and can be fit to data with linear least squares.
Derivations[edit]
Higher-order moments[edit]
The nth-order central moment can be expressed in terms of the quantile function:
{\displaystyle {\begin{aligned}\operatorname {E} [(X-\mu )^{n}]&=\int _{-\infty }^{\infty }(x-\mu )^{n}\,dF(x)\\&=\int _{0}^{1}{\big (}Q(p)-\mu {\big )}^{n}\,dp=s^{n}\int _{0}^{1}\left[\ln \!\left({\frac {p}{1-p}}\right)\right]^{n}\,dp.\end{aligned}}}

This integral is well-known[6] and can be expressed in terms of Bernoulli numbers:
{\displaystyle \operatorname {E} [(X-\mu )^{n}]=s^{n}\pi ^{n}(2^{n}-2)\cdot |B_{n}|.}
