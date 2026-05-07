# Beta distribution

Probability distribution

Not to be confused with Beta function.

| Beta |
| --- |
| Probability density function |
| Cumulative distribution function |
| Notation | Beta(α, β) |
| Parameters | α > 0 shape (real)β > 0 shape (real) |
| Support | x ∈ [ 0 , 1 ] {\displaystyle x\in [0,1]\!} or x ∈ ( 0 , 1 ) {\displaystyle x\in (0,1)\!} ${\displaystyle x\in [0,1]\!}$ ${\displaystyle x\in (0,1)\!}$ |
| PDF | x α − 1 ( 1 − x ) β − 1 B ( α , β ) {\displaystyle {\frac {x^{\alpha -1}(1-x)^{\beta -1}}{\mathrm {B} (\alpha ,\beta )}}\!} where B ( α , β ) = Γ ( α ) Γ ( β ) Γ ( α + β ) {\displaystyle \mathrm {B} (\alpha ,\beta )={\frac {\Gamma (\alpha )\Gamma (\beta )}{\Gamma (\alpha +\beta )}}} and Γ {\displaystyle \Gamma } is the Gamma function. ${\displaystyle {\frac {x^{\alpha -1}(1-x)^{\beta -1}}{\mathrm {B} (\alpha ,\beta )}}\!}$ ${\displaystyle \mathrm {B} (\alpha ,\beta )={\frac {\Gamma (\alpha )\Gamma (\beta )}{\Gamma (\alpha +\beta )}}}$ ${\displaystyle \Gamma }$ |
| CDF | I x ( α , β ) {\displaystyle I_{x}(\alpha ,\beta )\!} (the regularized incomplete beta function) ${\displaystyle I_{x}(\alpha ,\beta )\!}$ |
| Mean | E ⁡ [ X ] = α α + β {\displaystyle \operatorname {E} [X]={\frac {\alpha }{\alpha +\beta }}\!} E ⁡ [ ln ⁡ X ] = ψ ( α ) − ψ ( α + β ) {\displaystyle \operatorname {E} [\ln X]=\psi (\alpha )-\psi (\alpha +\beta )\!} E ⁡ [ X ln ⁡ X ] = α α + β [ ψ ( α + 1 ) − ψ ( α + β + 1 ) ] {\displaystyle \operatorname {E} [X\,\ln X]={\frac {\alpha }{\alpha +\beta }}\,\left[\psi (\alpha +1)-\psi (\alpha +\beta +1)\right]\!} (see section: Geometric mean) where ψ {\displaystyle \psi } is the digamma function ${\displaystyle \operatorname {E} [X]={\frac {\alpha }{\alpha +\beta }}\!}$ ${\displaystyle \operatorname {E} [\ln X]=\psi (\alpha )-\psi (\alpha +\beta )\!}$ ${\displaystyle \operatorname {E} [X\,\ln X]={\frac {\alpha }{\alpha +\beta }}\,\left[\psi (\alpha +1)-\psi (\alpha +\beta +1)\right]\!}$ ${\displaystyle \psi }$ |
| Median | I 1 2 [ − 1 ] ( α , β ) (in general) ≈ α − 1 3 α + β − 2 3 for α , β > 1 {\displaystyle {\begin{matrix}I_{\frac {1}{2}}^{[-1]}(\alpha ,\beta ){\text{ (in general) }}\\[0.5em]\approx {\frac {\alpha -{\tfrac {1}{3}}}{\alpha +\beta -{\tfrac {2}{3}}}}{\text{ for }}\alpha ,\beta >1\end{matrix}}} ${\displaystyle {\begin{matrix}I_{\frac {1}{2}}^{[-1]}(\alpha ,\beta ){\text{ (in general) }}\\[0.5em]\approx {\frac {\alpha -{\tfrac {1}{3}}}{\alpha +\beta -{\tfrac {2}{3}}}}{\text{ for }}\alpha ,\beta >1\end{matrix}}}$ |
| Mode | α − 1 α + β − 2 {\displaystyle {\frac {\alpha -1}{\alpha +\beta -2}}\!} for α, β > 1 Any value in the domain for α = β = 1 No mode if α<1 or β<1. Density diverges at 0 for α ≤ 1, and at 1 if β ≤ 1 ${\displaystyle {\frac {\alpha -1}{\alpha +\beta -2}}\!}$ |
| Variance | var ⁡ [ X ] = α β ( α + β ) 2 ( α + β + 1 ) {\displaystyle \operatorname {var} [X]={\frac {\alpha \beta }{(\alpha +\beta )^{2}(\alpha +\beta +1)}}\!} var ⁡ [ ln ⁡ X ] = ψ 1 ( α ) − ψ 1 ( α + β ) {\displaystyle \operatorname {var} [\ln X]=\psi _{1}(\alpha )-\psi _{1}(\alpha +\beta )\!} (see trigamma function and see section: Geometric variance) ${\displaystyle \operatorname {var} [X]={\frac {\alpha \beta }{(\alpha +\beta )^{2}(\alpha +\beta +1)}}\!}$ ${\displaystyle \operatorname {var} [\ln X]=\psi _{1}(\alpha )-\psi _{1}(\alpha +\beta )\!}$ |
| Skewness | 2 ( β − α ) α + β + 1 ( α + β + 2 ) α β {\displaystyle {\frac {2\,(\beta -\alpha ){\sqrt {\alpha +\beta +1}}}{(\alpha +\beta +2){\sqrt {\alpha \beta }}}}} ${\displaystyle {\frac {2\,(\beta -\alpha ){\sqrt {\alpha +\beta +1}}}{(\alpha +\beta +2){\sqrt {\alpha \beta }}}}}$ |
| Excess kurtosis | 6 [ ( α − β ) 2 ( α + β + 1 ) − α β ( α + β + 2 ) ] α β ( α + β + 2 ) ( α + β + 3 ) {\displaystyle {\frac {6[(\alpha -\beta )^{2}(\alpha +\beta +1)-\alpha \beta (\alpha +\beta +2)]}{\alpha \beta (\alpha +\beta +2)(\alpha +\beta +3)}}} ${\displaystyle {\frac {6[(\alpha -\beta )^{2}(\alpha +\beta +1)-\alpha \beta (\alpha +\beta +2)]}{\alpha \beta (\alpha +\beta +2)(\alpha +\beta +3)}}}$ |
| Entropy | ln ⁡ B ( α , β ) − ( α − 1 ) ψ ( α ) − ( β − 1 ) ψ ( β ) + ( α + β − 2 ) ψ ( α + β ) {\displaystyle {\begin{matrix}\ln \mathrm {B} (\alpha ,\beta )-(\alpha -1)\psi (\alpha )-(\beta -1)\psi (\beta )\\[0.5em]{}+(\alpha +\beta -2)\psi (\alpha +\beta )\end{matrix}}} ${\displaystyle {\begin{matrix}\ln \mathrm {B} (\alpha ,\beta )-(\alpha -1)\psi (\alpha )-(\beta -1)\psi (\beta )\\[0.5em]{}+(\alpha +\beta -2)\psi (\alpha +\beta )\end{matrix}}}$ |
| MGF | 1 + ∑ k = 1 ∞ ( ∏ r = 0 k − 1 α + r α + β + r ) t k k ! {\displaystyle 1+\sum _{k=1}^{\infty }\left(\prod _{r=0}^{k-1}{\frac {\alpha +r}{\alpha +\beta +r}}\right){\frac {t^{k}}{k!}}} ${\displaystyle 1+\sum _{k=1}^{\infty }\left(\prod _{r=0}^{k-1}{\frac {\alpha +r}{\alpha +\beta +r}}\right){\frac {t^{k}}{k!}}}$ |
| CF | 1 F 1 ( α ; α + β ; i t ) {\displaystyle {}_{1}F_{1}(\alpha ;\alpha +\beta ;i\,t)\!} (see Confluent hypergeometric function) ${\displaystyle {}_{1}F_{1}(\alpha ;\alpha +\beta ;i\,t)\!}$ |
| Fisher information | [ var ⁡ [ ln ⁡ X ] cov ⁡ [ ln ⁡ X , ln ⁡ ( 1 − X ) ] cov ⁡ [ ln ⁡ X , ln ⁡ ( 1 − X ) ] var ⁡ [ ln ⁡ ( 1 − X ) ] ] {\displaystyle {\begin{bmatrix}\operatorname {var} [\ln X]&\operatorname {cov} [\ln X,\ln(1-X)]\\\operatorname {cov} [\ln X,\ln(1-X)]&\operatorname {var} [\ln(1-X)]\end{bmatrix}}} see section: Fisher information matrix ${\displaystyle {\begin{bmatrix}\operatorname {var} [\ln X]&\operatorname {cov} [\ln X,\ln(1-X)]\\\operatorname {cov} [\ln X,\ln(1-X)]&\operatorname {var} [\ln(1-X)]\end{bmatrix}}}$ |
| Method of moments | α = ( E [ X ] ( 1 − E [ X ] ) V [ X ] − 1 ) E [ X ] {\displaystyle \alpha =\left({\frac {E[X](1-E[X])}{V[X]}}-1\right)E[X]} β = ( E [ X ] ( 1 − E [ X ] ) V [ X ] − 1 ) ( 1 − E [ X ] ) {\displaystyle \beta =\left({\frac {E[X](1-E[X])}{V[X]}}-1\right)(1-E[X])} ${\displaystyle \alpha =\left({\frac {E[X](1-E[X])}{V[X]}}-1\right)E[X]}$ ${\displaystyle \beta =\left({\frac {E[X](1-E[X])}{V[X]}}-1\right)(1-E[X])}$ |

In probability theory and statistics, the beta distribution is a family of continuous probability distributions defined on the interval [0, 1] or (0, 1) in terms of two positive parameters, denoted by alpha (α) and beta (β), that appear as exponents of the variable and its complement to 1, respectively, and control the shape of the distribution.

The beta distribution has been applied to model the behavior of random variables limited to intervals of finite length in a wide variety of disciplines. The beta distribution is a suitable model for the random behavior of percentages and proportions.

In Bayesian inference, the beta distribution is the conjugate prior probability distribution for the Bernoulli, binomial, negative binomial, and geometric distributions.

The formulation of the beta distribution discussed here is also known as the beta distribution of the first kind, whereas beta distribution of the second kind is an alternative name for the beta prime distribution. The generalization to multiple variables is called a Dirichlet distribution.

Definitions[edit]
Probability density function[edit]
An animation of the beta distribution for different values of its parameters.
The probability density function (PDF) of the beta distribution, for 
{\displaystyle 0\leq x\leq 1}
{\displaystyle 0<x<1}

, and shape parameters 

α

{\displaystyle \alpha }
{\displaystyle \beta >0}

, is a power function of the variable 

x

{\displaystyle x}

 and of its reflection 
{\displaystyle (1-x)}

 as follows:
{\displaystyle {\begin{aligned}f(x;\alpha ,\beta )&=\mathrm {constant} \cdot x^{\alpha -1}(1-x)^{\beta -1}\\[3pt]&={\frac {x^{\alpha -1}(1-x)^{\beta -1}}{\displaystyle \int _{0}^{1}u^{\alpha -1}(1-u)^{\beta -1}\,du}}\\[6pt]&={\frac {\Gamma (\alpha +\beta )}{\Gamma (\alpha )\Gamma (\beta )}}\,x^{\alpha -1}(1-x)^{\beta -1}\\[6pt]&={\frac {1}{\mathrm {B} (\alpha ,\beta )}}x^{\alpha -1}(1-x)^{\beta -1}\end{aligned}}}

where 
{\displaystyle \Gamma (z)}

 is the gamma function.  The beta function, 

B

{\displaystyle \mathrm {B} }

, is a normalization constant to ensure that the total probability is 1. In the above equations 

x

{\displaystyle x}

 is a realization—an observed value that actually occurred—of a random variable 

X

{\displaystyle X}

.
Several authors, including N. L. Johnson and S. Kotz,[1] use the symbols 

p

{\displaystyle p}
{\displaystyle q}

 (instead of 

α

{\displaystyle \alpha }
{\displaystyle \beta }

) for the shape parameters of the beta distribution, reminiscent of the symbols traditionally used for the parameters of the Bernoulli distribution, because the beta distribution approaches the Bernoulli distribution in the limit when both shape parameters 

α

{\displaystyle \alpha }
{\displaystyle \beta }

 approach zero.
In the following, a random variable 

X

{\displaystyle X}

 beta-distributed with parameters 

α

{\displaystyle \alpha }
{\displaystyle \beta }

 will be denoted by:[2][3]

X
∼
Beta
{\displaystyle X\sim \operatorname {Beta} (\alpha ,\beta )}

Other notations for beta-distributed random variables used in the statistical literature are 
{\displaystyle X\sim {\mathcal {B}}e(\alpha ,\beta )}

[4] and 
{\displaystyle X\sim \beta _{\alpha ,\beta }}

.[5]

Cumulative distribution function[edit]
CDF for symmetric beta distribution vs. x and α = β
CDF for skewed beta distribution vs. x and β = 5α
The cumulative distribution function is
{\displaystyle F(x;\alpha ,\beta )={\frac {\mathrm {B} {}(x;\alpha ,\beta )}{\mathrm {B} {}(\alpha ,\beta )}}=I_{x}(\alpha ,\beta )}

where 
{\displaystyle \mathrm {B} (x;\alpha ,\beta )}

 is the incomplete beta function and 
{\displaystyle I_{x}(\alpha ,\beta )}

 is the regularized incomplete beta function.
For positive integers α and β, the cumulative distribution function of a beta distribution can be expressed in terms of the cumulative distribution function of a binomial distribution with[6]

F

beta

(
x
;
α
,
β
)
=

F

binomial
{\displaystyle F_{\text{beta}}(x;\alpha ,\beta )=F_{\text{binomial}}(\beta -1;\alpha +\beta -1,1-x).}

Alternative parameterizations[edit]
Two parameters[edit]
Mean and sample size[edit]
The beta distribution may also be reparameterized in terms of its mean μ (0 < μ < 1) and the sum of the two shape parameters ν = α + β > 0([3] p. 83). Denoting by αPosterior and βPosterior the shape parameters of the posterior beta distribution resulting from applying Bayes' theorem to a binomial likelihood function and a prior probability,  the interpretation of the addition of both shape parameters to be sample size = ν = α·Posterior + β·Posterior is only correct for the Haldane prior probability Beta(0,0).  Specifically, for the Bayes (uniform) prior Beta(1,1) the correct interpretation would be sample size = α·Posterior + β Posterior − 2, or ν = (sample size) + 2.  For sample size much larger than 2, the difference between these two priors becomes negligible.  (See section Bayesian inference for further details.) ν = α + β is referred to as the "sample size" of a beta distribution, but one should remember that it is, strictly speaking, the "sample size" of a binomial likelihood function only when using a Haldane Beta(0,0) prior in Bayes' theorem.
This parametrization may be useful in Bayesian parameter estimation. For example, one may administer a test to a number of individuals. If it is assumed that each person's score (0 ≤ θ ≤ 1) is drawn from a population-level beta distribution, then an important statistic is the mean of this population-level distribution. The mean and sample size parameters are related to the shape parameters α and β via[3]

α = μν, β = (1 − μ)ν
Under this parametrization, one may place an uninformative prior probability over the mean, and a vague prior probability (such as an exponential or gamma distribution) over the positive reals for the sample size, if they are independent, and prior data and/or beliefs justify it.

Mode and concentration[edit]
Concave beta distributions, which have 
{\displaystyle \alpha ,\beta >1}

, can be parametrized in terms of mode and "concentration". The mode, 
{\displaystyle \omega ={\frac {\alpha -1}{\alpha +\beta -2}}}

, and concentration, 
{\displaystyle \kappa =\alpha +\beta }

, can be used to define the usual shape parameters as follows:[7]
{\displaystyle {\begin{aligned}\alpha &=\omega (\kappa -2)+1\\\beta &=(1-\omega )(\kappa -2)+1\end{aligned}}}

For the mode, 
{\displaystyle 0<\omega <1}

, to be well-defined, we need 
{\displaystyle \alpha ,\beta >1}

, or equivalently 
{\displaystyle \kappa >2}

. If instead we define the concentration as 
{\displaystyle c=\alpha +\beta -2}

, the condition simplifies to 
{\displaystyle c>0}

 and the beta density at 
{\displaystyle \alpha =1+c\omega }
{\displaystyle \beta =1+c(1-\omega )}

 can be written as:
{\displaystyle f(x;\omega ,c)={\frac {x^{c\omega }(1-x)^{c(1-\omega )}}{\mathrm {B} {\bigl (}1+c\omega ,1+c(1-\omega ){\bigr )}}}}

where 

c

{\displaystyle c}

 directly scales the sufficient statistics, 
{\displaystyle \log(x)}
{\displaystyle \log(1-x)}

. Note also that in the limit, 
{\displaystyle c\to 0}

, the distribution becomes flat.

Mean and variance[edit]
Solving the system of (coupled) equations given in the above sections as the equations for the mean and the variance of the beta distribution in terms of the original parameters α and β, one can express the α and β parameters in terms of the mean (μ) and the variance (var):

ν

=
α
+
β
=

μ
(
1
−
μ
)

v
a
r

−
1
,

 where 

ν
=
(
α
+
β
)
>
0
,

 therefore: 
{\displaystyle {\begin{aligned}\nu &=\alpha +\beta ={\frac {\mu (1-\mu )}{\mathrm {var} }}-1,{\text{ where }}\nu =(\alpha +\beta )>0,{\text{ therefore: }}{\text{var}}<\mu (1-\mu )\\\alpha &=\mu \nu =\mu \left({\frac {\mu (1-\mu )}{\text{var}}}-1\right),{\text{ if }}{\text{var}}<\mu (1-\mu )\\\beta &=(1-\mu )\nu =(1-\mu )\left({\frac {\mu (1-\mu )}{\text{var}}}-1\right),{\text{ if }}{\text{var}}<\mu (1-\mu ).\end{aligned}}}

This parametrization of the beta distribution may lead to a more intuitive understanding than the one based on the original parameters α and β. For example, by expressing the mode, skewness, excess kurtosis and differential entropy in terms of the mean and the variance:

Four parameters[edit]
A beta distribution with the two shape parameters α and β is supported on the range [0,1] or (0,1).  It is possible to alter the location and scale of the distribution by introducing two further parameters representing the minimum, a, and maximum c (c > a), values of the distribution,[1]  by a linear transformation substituting the non-dimensional variable x in terms of the new variable y (with support [a,c] or (a,c)) and the parameters a and c:

y
=
x
(
c
−
a
)
+
a
,

 therefore 
{\displaystyle y=x(c-a)+a,{\text{ therefore }}x={\frac {y-a}{c-a}}.}

The probability density function of the four parameter beta distribution is equal to the two parameter distribution, scaled by the range (c − a), (so that the total area under the density curve equals a probability of one), and with the "y" variable shifted and scaled as follows:
{\displaystyle {\begin{aligned}f(y;\alpha ,\beta ,a,c)={\frac {f(x;\alpha ,\beta )}{c-a}}&={\frac {\left({\frac {y-a}{c-a}}\right)^{\alpha -1}\left({\frac {c-y}{c-a}}\right)^{\beta -1}}{(c-a)B(\alpha ,\beta )}}\\[1ex]&={\frac {(y-a)^{\alpha -1}(c-y)^{\beta -1}}{(c-a)^{\alpha +\beta -1}B(\alpha ,\beta )}}.\end{aligned}}}

That a random variable Y is beta-distributed with four parameters α, β, a, and c will be denoted by:

Y
∼
Beta
{\displaystyle Y\sim \operatorname {Beta} (\alpha ,\beta ,a,c).}

Some measures of central location are scaled (by (c − a)) and shifted (by a), as follows:
{\displaystyle {\begin{aligned}\mu _{Y}&=\mu _{X}(c-a)+a\\[1ex]&={\frac {\alpha }{\alpha +\beta }}\left(c-a\right)+a={\frac {\alpha c+\beta a}{\alpha +\beta }}\end{aligned}}}

mode

(
Y
)

=

mode
{\displaystyle {\begin{aligned}{\text{mode}}(Y)&={\text{mode}}(X)(c-a)+a\\[1ex]&={\frac {\alpha -1}{\alpha +\beta -2}}\left(c-a\right)+a\\[1ex]&={\frac {(\alpha -1)c+(\beta -1)a}{\alpha +\beta -2}}\ ,&{\text{ if }}\alpha ,\,\beta >1\end{aligned}}}

median

(
Y
)

=

median
{\displaystyle {\begin{aligned}{\text{median}}(Y)&={\text{median}}(X)(c-a)+a\\[1ex]&=I_{\frac {1}{2}}^{[-1]}(\alpha ,\beta )\left(c-a\right)+a\end{aligned}}}

Note: the geometric mean and harmonic mean cannot be transformed by a linear transformation in the way that the mean, median and mode can.
The shape parameters of Y can be written in term of its mean and variance as
{\displaystyle {\begin{aligned}\alpha &={\frac {\left(a-\mu _{Y}\right)\left(a\,c-a\,\mu _{Y}-c\,\mu _{Y}+\mu _{Y}^{2}+\sigma _{Y}^{2}\right)}{\sigma _{Y}^{2}(c-a)}}\\\beta &=-{\frac {\left(c-\mu _{Y}\right)\left(a\,c-a\,\mu _{Y}-c\,\mu _{Y}+\mu _{Y}^{2}+\sigma _{Y}^{2}\right)}{\sigma _{Y}^{2}(c-a)}}\end{aligned}}}

The statistical dispersion measures are scaled (they do not need to be shifted because they are already centered on the mean) by the range (c − a), linearly for the mean deviation and nonlinearly for the variance:

(mean deviation around mean)

(
Y
)

=
(

(mean deviation around mean)
{\displaystyle {\begin{aligned}&{\text{(mean deviation around mean)}}(Y)\\[1ex]&=({\text{(mean deviation around mean)}}(X))(c-a)\\&={\frac {2\alpha ^{\alpha }\beta ^{\beta }}{\mathrm {B} (\alpha ,\beta )(\alpha +\beta )^{\alpha +\beta +1}}}(c-a)\end{aligned}}}
{\displaystyle {\text{var}}(Y)={\text{var}}(X)(c-a)^{2}={\frac {\alpha \beta (c-a)^{2}}{(\alpha +\beta )^{2}(\alpha +\beta +1)}}.}

Since the skewness and excess kurtosis are non-dimensional quantities (as moments centered on the mean and normalized by the standard deviation), they are independent of the parameters a and c, and therefore equal to the expressions given above in terms of X (with support [0,1] or (0,1)):

skewness

(
Y
)
=

skewness
{\displaystyle {\text{skewness}}(Y)={\text{skewness}}(X)={\frac {2(\beta -\alpha ){\sqrt {\alpha +\beta +1}}}{(\alpha +\beta +2){\sqrt {\alpha \beta }}}}.}

kurtosis excess

(
Y
)
=

kurtosis excess
{\displaystyle {\text{kurtosis excess}}(Y)={\text{kurtosis excess}}(X)={\frac {6\left[(\alpha -\beta )^{2}(\alpha +\beta +1)-\alpha \beta (\alpha +\beta +2)\right]}{\alpha \beta (\alpha +\beta +2)(\alpha +\beta +3)}}}

Properties[edit]
Measures of central tendency[edit]
Mode[edit]
The mode of a beta distributed random variable X with α, β > 1 is the most likely value of the distribution (corresponding to the peak in the PDF), and is given by the following expression:[1]
{\displaystyle {\frac {\alpha -1}{\alpha +\beta -2}}.}

When both parameters are less than one (α, β < 1), this is the anti-mode: the lowest point of the probability density curve.[8]
Letting α = β, the expression for the mode simplifies to 1/2, showing that for α = β > 1 the mode (resp. anti-mode when α, β < 1), is at the center of the distribution: it is symmetric in those cases.  See Shapes section in this article for a full list of mode cases, for arbitrary values of α and β. For several of these cases, the maximum value of the density function occurs at one or both ends.  In some cases the (maximum) value of the density function occurring at the end is finite. For example, in the case of α = 2, β = 1 (or α = 1, β = 2), the density function becomes a right-triangle distribution which is finite at both ends. In several other cases there is a singularity at one end, where the value of the density function approaches infinity. For example, in the case α = β = 1/2, the beta distribution simplifies to become the arcsine distribution.  There is debate among mathematicians about some of these cases and whether the ends (x = 0, and x = 1) can be called modes or not.[9][2]

Mode for beta distribution for 1 ≤ α ≤ 5 and 1 ≤ β ≤ 5
Whether the ends are part of the domain of the density function
Whether a singularity can ever be called a mode
Whether cases with two maxima should be called bimodal
Median[edit]
Median for beta distribution for 0 ≤ α ≤ 5 and 0 ≤ β ≤ 5
(Mean–median) for beta distribution versus alpha and beta from 0 to 2
The median of the beta distribution is the unique real number 
{\displaystyle x=I_{1/2}^{[-1]}(\alpha ,\beta )}

 for which the regularized incomplete beta function 
{\displaystyle I_{x}(\alpha ,\beta )={\tfrac {1}{2}}}

. There is no general closed-form expression for the median of the beta distribution for arbitrary values of α and β.  Closed-form expressions for particular values of the parameters α and β follow:[citation needed]

For symmetric cases  α = β, median = 1/2.
For α = 1 and β > 0, median 
{\displaystyle =1-2^{-1/\beta }}

 (this case is the mirror-image of the power function distribution)
For α > 0 and β = 1, median = 
{\displaystyle 2^{-1/\alpha }}

 (this case is the power function distribution[9])
For α = 3 and β = 2, median = 0.6142724318676105..., the real solution to the quartic equation 1 − 8x3 + 6x4 = 0, which lies in [0,1].
For α = 2 and β = 3, median = 0.38572756813238945... = 1−median(Beta(3, 2))
The following are the limits with one parameter finite (non-zero) and the other approaching these limits:[citation needed]

lim

β
→
0

median

=

lim

α
→
∞

median

=
1
,

lim

α
→
0

median

=

lim

β
→
∞

median
{\displaystyle {\begin{aligned}\lim _{\beta \to 0}{\text{median}}=\lim _{\alpha \to \infty }{\text{median}}=1,\\\lim _{\alpha \to 0}{\text{median}}=\lim _{\beta \to \infty }{\text{median}}=0.\end{aligned}}}

A reasonable approximation of the value of the median of the beta distribution, for both α and β greater or equal to one, is given by the formula[10]

median
{\displaystyle {\text{median}}\approx {\frac {\alpha -{\tfrac {1}{3}}}{\alpha +\beta -{\tfrac {2}{3}}}}{\text{ for }}\alpha ,\beta \geq 1.}

When α, β ≥ 1, the relative error (the absolute error divided by the median) in this approximation is less than 4% and for both α ≥ 2 and β ≥ 2 it is less than 1%. The absolute error divided by the difference between the mean and the mode is similarly small:

Mean[edit]
Mean for beta distribution for 0 ≤ α ≤ 5 and 0 ≤ β ≤ 5
The expected value (mean) (μ) of a beta distribution random variable X with two parameters α and β is a function of only the ratio β/α of these parameters:[1]
{\displaystyle {\begin{aligned}\mu =\operatorname {E} [X]&=\int _{0}^{1}xf(x;\alpha ,\beta )\,dx\\&=\int _{0}^{1}x\,{\frac {x^{\alpha -1}(1-x)^{\beta -1}}{\mathrm {B} (\alpha ,\beta )}}\,dx\\&={\frac {\alpha }{\alpha +\beta }}\\&={\frac {1}{1+{\frac {\beta }{\alpha }}}}\end{aligned}}}

Letting α = β in the above expression one obtains μ = 1/2, showing that for α = β the mean is at the center of the distribution: it is symmetric. Also, the following limits can be obtained from the above expression:
{\displaystyle {\begin{aligned}\lim _{{\frac {\beta }{\alpha }}\to 0}\mu =1\\\lim _{{\frac {\beta }{\alpha }}\to \infty }\mu =0\end{aligned}}}

Therefore, for β/α → 0, or for α/β → ∞, the mean is located at the right end, x = 1. For these limit ratios, the beta distribution becomes a one-point degenerate distribution with a Dirac delta function spike at the right end, x = 1, with probability 1, and zero probability everywhere else. There is 100% probability (absolute certainty) concentrated at the right end, x = 1.
Similarly, for β/α → ∞, or for α/β → 0, the mean is located at the left end, x = 0.  The beta distribution becomes a 1-point Degenerate distribution with a Dirac delta function spike at the left end, x = 0, with probability 1, and zero probability everywhere else. There is 100% probability (absolute certainty) concentrated at the left end, x = 0. Following are the limits with one parameter finite (non-zero) and the other approaching these limits:
{\displaystyle {\begin{aligned}\lim _{\beta \to 0}\mu =\lim _{\alpha \to \infty }\mu =1\\\lim _{\alpha \to 0}\mu =\lim _{\beta \to \infty }\mu =0\end{aligned}}}

While for typical unimodal distributions (with centrally located modes, inflexion points at both sides of the mode, and longer tails) (with Beta(α, β) such that α, β > 2) it is known that the sample mean (as an estimate of location) is not as robust as the sample median, the opposite is the case for uniform or "U-shaped" bimodal distributions (with Beta(α, β) such that α, β ≤ 1), with the modes located at the ends of the distribution.  As Mosteller and Tukey remark ([11] p. 207) "the average of the two extreme observations uses all the sample information. This illustrates how, for short-tailed distributions, the extreme observations should get more weight."  By contrast, it follows that the median of "U-shaped" bimodal distributions with modes at the edge of the distribution (with Beta(α, β) such that α, β ≤ 1) is not robust, as the sample median drops the extreme sample observations from consideration.  A practical application of this occurs for example for random walks, since the probability for the time of the last visit to the origin in a random walk is distributed as the arcsine distribution Beta(1/2, 1/2):[5][12] the mean of a number of realizations of a random walk is a much more robust estimator than the median (which is an inappropriate sample measure estimate in this case).

Geometric mean[edit]
(Mean − GeometricMean) for beta distribution versus α and β from 0 to 2, showing the asymmetry between α and β for the geometric mean
Geometric means for beta distribution Purple = G(x), Yellow = G(1 − x), smaller values α and β in front
Geometric means for beta distribution. purple = G(x), yellow = G(1 − x), larger values α and β in front
The logarithm of the geometric mean GX of a distribution with random variable X is the arithmetic mean of ln(X), or, equivalently, its expected value:
{\displaystyle \ln G_{X}=\operatorname {E} [\ln X]}

For a beta distribution, the expected value integral gives:
{\displaystyle {\begin{aligned}\operatorname {E} [\ln X]&=\int _{0}^{1}\ln x\,f(x;\alpha ,\beta )\,dx\\[4pt]&=\int _{0}^{1}\ln x\,{\frac {x^{\alpha -1}(1-x)^{\beta -1}}{\mathrm {B} (\alpha ,\beta )}}\,dx\\[4pt]&={\frac {1}{\mathrm {B} (\alpha ,\beta )}}\,\int _{0}^{1}{\frac {\partial x^{\alpha -1}(1-x)^{\beta -1}}{\partial \alpha }}\,dx\\[4pt]&={\frac {1}{\mathrm {B} (\alpha ,\beta )}}{\frac {\partial }{\partial \alpha }}\int _{0}^{1}x^{\alpha -1}(1-x)^{\beta -1}\,dx\\[4pt]&={\frac {1}{\mathrm {B} (\alpha ,\beta )}}{\frac {\partial \mathrm {B} (\alpha ,\beta )}{\partial \alpha }}\\[4pt]&={\frac {\partial \ln \mathrm {B} (\alpha ,\beta )}{\partial \alpha }}\\[4pt]&={\frac {\partial \ln \Gamma (\alpha )}{\partial \alpha }}-{\frac {\partial \ln \Gamma (\alpha +\beta )}{\partial \alpha }}\\[4pt]&=\psi (\alpha )-\psi (\alpha +\beta )\end{aligned}}}

where ψ is the digamma function.
Therefore, the geometric mean of a beta distribution with shape parameters α and β is the exponential of the digamma functions of α and β as follows:
{\displaystyle G_{X}=e^{\operatorname {E} [\ln X]}=e^{\psi (\alpha )-\psi (\alpha +\beta )}}

While for a beta distribution with equal shape parameters α = β, it follows that skewness = 0 and mode = mean = median = 1/2, the geometric mean is less than 1/2: 0 < GX < 1/2.  The reason for this is that the logarithmic transformation strongly weights the values of X close to zero, as ln(X) strongly tends towards negative infinity as X approaches zero, while ln(X) flattens towards zero as X → 1.
Along a line α = β, the following limits apply:
{\displaystyle {\begin{aligned}&\lim _{\alpha =\beta \to 0}G_{X}=0\\&\lim _{\alpha =\beta \to \infty }G_{X}={\tfrac {1}{2}}\end{aligned}}}

Following are the limits with one parameter finite (non-zero) and the other approaching these limits:
{\displaystyle {\begin{aligned}\lim _{\beta \to 0}G_{X}=\lim _{\alpha \to \infty }G_{X}=1\\\lim _{\alpha \to 0}G_{X}=\lim _{\beta \to \infty }G_{X}=0\end{aligned}}}

The accompanying plot shows the difference between the mean and the geometric mean for shape parameters α and β from zero to 2.  Besides the fact that the difference between them approaches zero as α and β approach infinity and that the difference becomes large for values of α and β approaching zero, one can observe an evident asymmetry of the geometric mean with respect to the shape parameters α and β. The difference between the geometric mean and the mean is larger for small values of α in relation to β than when exchanging the magnitudes of β and α.
N. L.Johnson and S. Kotz[1] suggest the logarithmic approximation to the digamma function ψ(α) ≈ ln(α − 1/2) which results in the following approximation to the geometric mean:
{\displaystyle G_{X}\approx {\frac {\alpha \,-{\frac {1}{2}}}{\alpha +\beta -{\frac {1}{2}}}}{\text{ if }}\alpha ,\beta >1.}

Numerical values for the relative error in this approximation follow: [(α = β = 1): 9.39%]; [(α = β = 2): 1.29%];  [(α = 2, β = 3): 1.51%];  [(α = 3, β = 2): 0.44%]; [(α = β = 3): 0.51%]; [(α = β = 4): 0.26%]; [(α = 3, β = 4): 0.55%];  [(α = 4, β = 3): 0.24%].
Similarly, one can calculate the value of shape parameters required for the geometric mean to equal 1/2. Given the value of the parameter β, what would be the value of the other parameter, α, required for the geometric mean to equal 1/2?.  The answer is that (for β > 1), the value of α required tends towards β + 1/2 as β → ∞. For example, all these couples have the same geometric mean of 1/2: [β = 1, α = 1.4427], [β = 2, α = 2.46958], [β = 3, α = 3.47943], [β = 4, α = 4.48449], [β = 5, α = 5.48756], [β = 10, α = 10.4938], [β = 100, α = 100.499].
The fundamental property of the geometric mean, which can be proven to be false for any other mean, is
{\displaystyle G{\left({\frac {X_{i}}{Y_{i}}}\right)}={\frac {G(X_{i})}{G(Y_{i})}}}

This makes the geometric mean the only correct mean when averaging normalized results, that is results that are presented as ratios to reference values.[13]  This is relevant because the beta distribution is a suitable model for the random behavior of percentages and it is particularly suitable to the statistical modelling of proportions.  The geometric mean plays a central role in maximum likelihood estimation, see section "Parameter estimation, maximum likelihood." Actually, when performing maximum likelihood estimation, besides the geometric mean GX based on the random variable X, also another geometric mean appears naturally: the geometric mean based on the linear transformation ––(1 − X), the mirror-image of X, denoted by G(1−X):
{\displaystyle G_{1-X}=e^{\operatorname {E} [\ln(1-X)]}=e^{\psi (\beta )-\psi (\alpha +\beta )}}

Along a line α = β, the following limits apply:
{\displaystyle {\begin{aligned}&\lim _{\alpha =\beta \to 0}G_{1-X}=0\\&\lim _{\alpha =\beta \to \infty }G_{1-X}={\tfrac {1}{2}}\end{aligned}}}

Following are the limits with one parameter finite (non-zero) and the other approaching these limits:
{\displaystyle {\begin{aligned}\lim _{\beta \to 0}G_{(1-X)}=\lim _{\alpha \to \infty }G_{(1-X)}=0\\\lim _{\alpha \to 0}G_{(1-X)}=\lim _{\beta \to \infty }G_{(1-X)}=1\end{aligned}}}

It has the following approximate value:
{\displaystyle G_{(1-X)}\approx {\frac {\beta -{\frac {1}{2}}}{\alpha +\beta -{\frac {1}{2}}}}{\text{ if }}\alpha ,\beta >1.}

Although both GX and  G1−X are asymmetric, in the case that both shape parameters are equal α = β, the geometric means are equal: GX = G(1−X).  This equality follows from the following symmetry displayed between both geometric means:
{\displaystyle G_{X}(\mathrm {B} (\alpha ,\beta ))=G_{1-X}(\mathrm {B} (\beta ,\alpha )).}

Harmonic mean[edit]
Harmonic mean for beta distribution for 0 < α < 5 and 0 < β < 5
Harmonic mean for beta distribution versus α and β from 0 to 2
Harmonic means for beta distribution Purple = H(X), Yellow = H(1 − X), smaller values α and β in front
Harmonic means for beta distribution: purple = H(X), yellow = H(1 − X), larger values α and β in front
The inverse of the harmonic mean (HX) of a distribution with random variable X is the arithmetic mean of 1/X, or, equivalently, its expected value. Therefore, the harmonic mean (HX) of a beta distribution with shape parameters α and β is:
{\displaystyle {\begin{aligned}H_{X}&={\frac {1}{\operatorname {E} \left[{\frac {1}{X}}\right]}}\\&={\frac {1}{\int _{0}^{1}{\frac {f(x;\alpha ,\beta )}{x}}\,dx}}\\&={\frac {1}{\int _{0}^{1}{\frac {x^{\alpha -1}(1-x)^{\beta -1}}{x\mathrm {B} (\alpha ,\beta )}}\,dx}}\\&={\frac {\alpha -1}{\alpha +\beta -1}}{\text{ if }}\alpha >1{\text{ and }}\beta >0\\\end{aligned}}}

The harmonic mean (HX) of a beta distribution with α < 1 is undefined, because its defining expression is not bounded in [0, 1] for shape parameter α less than unity.
Letting α = β in the above expression one obtains
{\displaystyle H_{X}={\frac {\alpha -1}{2\alpha -1}},}

showing that for α = β the harmonic mean ranges from 0, for α = β = 1, to 1/2, for α = β → ∞.
Following are the limits with one parameter finite (non-zero) and the other approaching these limits:

lim

α
→
0

H

X

 is undefined
{\displaystyle {\begin{aligned}&\lim _{\alpha \to 0}H_{X}{\text{ is undefined}}\\&\lim _{\alpha \to 1}H_{X}=\lim _{\beta \to \infty }H_{X}=0\\&\lim _{\beta \to 0}H_{X}=\lim _{\alpha \to \infty }H_{X}=1\end{aligned}}}

The harmonic mean plays a role in maximum likelihood estimation for the four parameter case, in addition to the geometric mean. Actually, when performing maximum likelihood estimation for the four parameter case, besides the harmonic mean HX based on the random variable X, also another harmonic mean appears naturally: the harmonic mean based on the linear transformation (1 − X), the mirror-image of X, denoted by H1 − X:
{\displaystyle H_{1-X}={\frac {1}{\operatorname {E} \left[{\frac {1}{1-X}}\right]}}={\frac {\beta -1}{\alpha +\beta -1}}{\text{ if }}\beta >1,{\text{ and }}\alpha >0.}

The harmonic mean (H(1 − X)) of a beta distribution with β < 1 is undefined, because its defining expression is not bounded in [0, 1] for shape parameter β less than unity.
Letting α = β in the above expression one obtains
{\displaystyle H_{(1-X)}={\frac {\beta -1}{2\beta -1}},}

showing that for α = β the harmonic mean ranges from 0, for α = β = 1, to 1/2, for α = β → ∞.
Following are the limits with one parameter finite (non-zero) and the other approaching these limits:

lim

β
→
0

H

1
−
X

 is undefined
{\displaystyle {\begin{aligned}&\lim _{\beta \to 0}H_{1-X}{\text{ is undefined}}\\&\lim _{\beta \to 1}H_{1-X}=\lim _{\alpha \to \infty }H_{1-X}=0\\&\lim _{\alpha \to 0}H_{1-X}=\lim _{\beta \to \infty }H_{1-X}=1\end{aligned}}}

Although both HX and  H1−X are asymmetric, in the case that both shape parameters are equal α = β, the harmonic means are equal: HX = H1−X.  This equality follows from the following symmetry displayed between both harmonic means:
{\displaystyle H_{X}(\mathrm {B} (\alpha ,\beta ))=H_{1-X}(\mathrm {B} (\beta ,\alpha )){\text{ if }}\alpha ,\beta >1.}

Measures of statistical dispersion[edit]
Variance[edit]
The variance (the second moment centered on the mean) of a beta distribution random variable X with parameters α and β is:[1][14]
{\displaystyle \operatorname {var} (X)=\operatorname {E} \left[(X-\mu )^{2}\right]={\frac {\alpha \beta }{\left(\alpha +\beta \right)^{2}\left(\alpha +\beta +1\right)}}}

Letting α = β in the above expression one obtains
{\displaystyle \operatorname {var} (X)={\frac {1}{4(2\beta +1)}},}

showing that for α = β the variance decreases monotonically as α = β increases. Setting α = β = 0 in this expression, one finds the maximum variance var(X) = 1/4[1] which only occurs approaching the limit, at α = β = 0.
The beta distribution may also be parametrized in terms of its mean μ (0 < μ < 1) and sample size ν = α + β (ν > 0) (see subsection  Mean and sample size):

α

=
μ
ν
,

 where 

ν
=
(
α
+
β
)
>
0
,

β

=
(
1
−
μ
)
ν
,

 where 
{\displaystyle {\begin{aligned}\alpha &=\mu \nu ,&{\text{ where }}\nu =(\alpha +\beta )>0,\\\beta &=(1-\mu )\nu ,&{\text{ where }}\nu =(\alpha +\beta )>0.\end{aligned}}}

Using this parametrization, one can express the variance in terms of the mean μ and the sample size ν as follows:
{\displaystyle \operatorname {var} (X)={\frac {\mu (1-\mu )}{1+\nu }}}

Since ν = α + β > 0, it follows that var(X) < μ(1 − μ).
For a symmetric distribution, the mean is at the middle of the distribution, μ = 1/2, and therefore:
{\displaystyle \operatorname {var} (X)={\frac {1}{4(1+\nu )}}{\text{ if }}\mu ={\tfrac {1}{2}}}

Also, the following limits (with only the noted variable approaching the limit) can be obtained from the above expressions:
{\displaystyle {\begin{aligned}&\lim _{\beta \to 0}\operatorname {var} (X)=\lim _{\alpha \to 0}\operatorname {var} (X)=\lim _{\beta \to \infty }\operatorname {var} (X)=\lim _{\alpha \to \infty }\operatorname {var} (X)=0\\&\lim _{\nu \to \infty }\operatorname {var} (X)=\lim _{\mu \to 0}\operatorname {var} (X)=\lim _{\mu \to 1}\operatorname {var} (X)=0\\&\lim _{\nu \to 0}\operatorname {var} (X)=\mu (1-\mu )\end{aligned}}}

Geometric variance and covariance[edit]
log geometric variances vs. α and β
log geometric variances vs. α and β
The logarithm of the geometric variance, ln(varGX), of a distribution with random variable X is the second moment of the logarithm of X centered on the geometric mean of X, ln(GX):
{\displaystyle {\begin{aligned}\ln \operatorname {var} _{GX}&=\operatorname {E} \left[\left(\ln X-\ln G_{X}\right)^{2}\right]\\&=\operatorname {E} \left[\left(\ln X-\operatorname {E} \left[\ln X\right]\right)^{2}\right]\\&=\operatorname {E} \left[\left(\ln X\right)^{2}\right]-\left(\operatorname {E} [\ln X]\right)^{2}\\&=\operatorname {var} [\ln X]\end{aligned}}}

and therefore, the geometric variance is:
{\displaystyle \operatorname {var} _{GX}=e^{\operatorname {var} [\ln X]}}

In the Fisher information matrix, and the curvature of the log likelihood function, the logarithm of the geometric variance of the reflected variable 1 − X and the logarithm of the geometric covariance between X and 1 − X appear:
{\displaystyle {\begin{aligned}\ln \operatorname {var_{G(1-X)}} &=\operatorname {E} \left[\left(\ln(1-X)-\ln G_{1-X}\right)^{2}\right]\\&=\operatorname {E} \left[\left(\ln(1-X)-\operatorname {E} [\ln(1-X)]\right)^{2}\right]\\&=\operatorname {E} \left[(\ln(1-X))^{2}\right]-\left(\operatorname {E} [\ln(1-X)]\right)^{2}\\&=\operatorname {var} [\ln(1-X)]\\&\\\operatorname {var_{G(1-X)}} &=e^{\operatorname {var} [\ln(1-X)]}\\&\\\ln \operatorname {cov_{G{X,1-X}}} &=\operatorname {E} [(\ln X-\ln G_{X})(\ln(1-X)-\ln G_{1-X})]\\&=\operatorname {E} [(\ln X-\operatorname {E} [\ln X])(\ln(1-X)-\operatorname {E} [\ln(1-X)])]\\&=\operatorname {E} \left[\ln X\ln(1-X)\right]-\operatorname {E} [\ln X]\operatorname {E} [\ln(1-X)]\\&=\operatorname {cov} [\ln X,\ln(1-X)]\\&\\\operatorname {cov} _{G{X,(1-X)}}&=e^{\operatorname {cov} [\ln X,\ln(1-X)]}\end{aligned}}}

For a beta distribution, higher order logarithmic moments can be derived by using the representation of a beta distribution as a proportion of two gamma distributions and differentiating through the integral. They can be expressed in terms of higher order poly-gamma functions. See the section § Moments of logarithmically transformed random variables.  The variance of the logarithmic variables and covariance of ln X and ln(1−X) are:
{\displaystyle \operatorname {var} [\ln X]=\psi _{1}(\alpha )-\psi _{1}(\alpha +\beta )}
{\displaystyle \operatorname {var} [\ln(1-X)]=\psi _{1}(\beta )-\psi _{1}(\alpha +\beta )}
{\displaystyle \operatorname {cov} [\ln X,\ln(1-X)]=-\psi _{1}(\alpha +\beta )}

where the trigamma function, denoted ψ1(α), is the second of the polygamma functions, and is defined as the derivative of the digamma function:
{\displaystyle \psi _{1}(\alpha )={\frac {d^{2}\ln \Gamma (\alpha )}{d\alpha ^{2}}}={\frac {d\psi (\alpha )}{d\alpha }}.}

Therefore,
{\displaystyle \ln \operatorname {var} _{GX}=\operatorname {var} [\ln X]=\psi _{1}(\alpha )-\psi _{1}(\alpha +\beta )}
{\displaystyle \ln \operatorname {var} _{G(1-X)}=\operatorname {var} [\ln(1-X)]=\psi _{1}(\beta )-\psi _{1}(\alpha +\beta )}
{\displaystyle \ln \operatorname {cov} _{GX,1-X}=\operatorname {cov} [\ln X,\ln(1-X)]=-\psi _{1}(\alpha +\beta )}

The accompanying plots show the log geometric variances and log geometric covariance versus the shape parameters α and β.  The plots show that the log geometric variances and log geometric covariance are close to zero for shape parameters α and β greater than 2, and that the log geometric variances rapidly rise in value for shape parameter values α and β less than unity. The log geometric variances are positive for all values of the shape parameters. The log geometric covariance is negative for all values of the shape parameters, and it reaches large negative values for α and β less than unity.
Following are the limits with one parameter finite (non-zero) and the other approaching these limits:
{\displaystyle {\begin{aligned}&\lim _{\alpha \to 0}\ln \operatorname {var} _{GX}=\lim _{\beta \to 0}\ln \operatorname {var} _{G(1-X)}=\infty \\&\lim _{\beta \to 0}\ln \operatorname {var} _{GX}=\lim _{\alpha \to \infty }\ln \operatorname {var} _{GX}=\lim _{\alpha \to 0}\ln \operatorname {var} _{G(1-X)}=\lim _{\beta \to \infty }\ln \operatorname {var} _{G(1-X)}=0\\&\lim _{\alpha \to \infty }\ln \operatorname {cov} _{GX,(1-X)}=\lim _{\beta \to \infty }\ln \operatorname {cov} _{GX,(1-X)}=0\\&\lim _{\beta \to \infty }\ln \operatorname {var} _{GX}=\psi _{1}(\alpha )\\&\lim _{\alpha \to \infty }\ln \operatorname {var} _{G(1-X)}=\psi _{1}(\beta )\\&\lim _{\alpha \to 0}\ln \operatorname {cov} _{GX,(1-X)}=-\psi _{1}(\beta )\\&\lim _{\beta \to 0}\ln \operatorname {cov} _{GX,(1-X)}=-\psi _{1}(\alpha )\end{aligned}}}

Limits with two parameters varying:
{\displaystyle {\begin{aligned}&\lim _{\alpha \to \infty }(\lim _{\beta \to \infty }\ln \operatorname {var} _{GX})=\lim _{\beta \to \infty }(\lim _{\alpha \to \infty }\ln \operatorname {var} _{G(1-X)})=\lim _{\alpha \to \infty }(\lim _{\beta \to 0}\ln \operatorname {cov} _{GX,(1-X)})=\lim _{\beta \to \infty }(\lim _{\alpha \to 0}\ln \operatorname {cov} _{GX,(1-X)})=0\\&\lim _{\alpha \to \infty }(\lim _{\beta \to 0}\ln \operatorname {var} _{GX})=\lim _{\beta \to \infty }(\lim _{\alpha \to 0}\ln \operatorname {var} _{G(1-X)})=\infty \\&\lim _{\alpha \to 0}(\lim _{\beta \to 0}\ln \operatorname {cov} _{GX,(1-X)})=\lim _{\beta \to 0}(\lim _{\alpha \to 0}\ln \operatorname {cov} _{GX,(1-X)})=-\infty \end{aligned}}}

Although both ln(varGX) and ln(varG(1 − X)) are asymmetric, when the shape parameters are equal, α = β, one has: ln(varGX) = ln(varG(1−X)). This equality follows from the following symmetry displayed between both log geometric variances:
{\displaystyle \ln \operatorname {var} _{GX}(\mathrm {B} (\alpha ,\beta ))=\ln \operatorname {var} _{G(1-X)}(\mathrm {B} (\beta ,\alpha )).}

The log geometric covariance is symmetric:
{\displaystyle \ln \operatorname {cov} _{GX,(1-X)}(\mathrm {B} (\alpha ,\beta ))=\ln \operatorname {cov} _{GX,(1-X)}(\mathrm {B} (\beta ,\alpha ))}

Mean absolute deviation around the mean[edit]
Ratio of ,ean abs.dev. to std.dev. for beta distribution with α and β ranging from 0 to 5
Ratio of mean abs.dev. to std.dev. for beta distribution with mean 0 ≤ μ ≤ 1 and sample size 0 < ν ≤ 10
The mean absolute deviation around the mean for the beta distribution with shape parameters α and β is:[9]
{\displaystyle \operatorname {E} [|X-E[X]|]={\frac {2\alpha ^{\alpha }\beta ^{\beta }}{\mathrm {B} (\alpha ,\beta )(\alpha +\beta )^{\alpha +\beta +1}}}}

The mean absolute deviation around the mean is a more robust estimator of statistical dispersion than the standard deviation for beta distributions with tails and inflection points at each side of the mode, Beta(α, β) distributions with α,β > 2, as it depends on the linear (absolute) deviations rather than the square deviations from the mean.  Therefore, the effect of very large deviations from the mean are not as overly weighted.
Using Stirling's approximation to the Gamma function, N.L.Johnson and S.Kotz[1] derived the following approximation for values of the shape parameters greater than unity (the relative error for this approximation is only −3.5% for α = β = 1, and it decreases to zero as α → ∞, β → ∞):

mean abs. dev. from mean
standard deviation
{\displaystyle {\begin{aligned}{\frac {\text{mean abs. dev. from mean}}{\text{standard deviation}}}&={\frac {\operatorname {E} [|X-E[X]|]}{\sqrt {\operatorname {var} (X)}}}\\&\approx {\sqrt {\frac {2}{\pi }}}\left(1+{\frac {7}{12(\alpha +\beta )}}{}-{\frac {1}{12\alpha }}-{\frac {1}{12\beta }}\right),{\text{ if }}\alpha ,\beta >1.\end{aligned}}}

At the limit α → ∞, β → ∞, the ratio of the mean absolute deviation to the standard deviation (for the beta distribution) becomes equal to the ratio of the same measures for the normal distribution: 
{\displaystyle {\sqrt {\frac {2}{\pi }}}}

.  For α = β = 1 this ratio equals 
{\displaystyle {\frac {\sqrt {3}}{2}}}

, so that from α = β = 1 to α, β → ∞ the ratio decreases by 8.5%.  For α = β = 0 the standard deviation is exactly equal to the mean absolute deviation around the mean. Therefore, this ratio decreases by 15% from α = β = 0 to α = β = 1, and by 25% from α = β = 0 to α, β → ∞ . However, for skewed beta distributions such that α → 0 or β → 0, the ratio of the standard deviation to the mean absolute deviation approaches infinity (although each of them, individually, approaches zero) because the mean absolute deviation approaches zero faster than the standard deviation.
Using the parametrization in terms of mean μ and sample size ν = α + β > 0:

α = μν, β = (1 − μ)ν
one can express the mean absolute deviation around the mean in terms of the mean μ and the sample size ν as follows:
{\displaystyle \operatorname {E} [|X-E[X]|]={\frac {2\mu ^{\mu \nu }(1-\mu )^{(1-\mu )\nu }}{\nu \mathrm {B} (\mu \nu ,(1-\mu )\nu )}}}

For a symmetric distribution, the mean is at the middle of the distribution, μ = 1/2, and therefore:
{\displaystyle {\begin{aligned}\operatorname {E} [|X-E[X]|]={\frac {2^{1-\nu }}{\nu \mathrm {B} ({\tfrac {\nu }{2}},{\tfrac {\nu }{2}})}}&={\frac {2^{1-\nu }\Gamma (\nu )}{\nu (\Gamma ({\tfrac {\nu }{2}}))^{2}}}\\\lim _{\nu \to 0}\left(\lim _{\mu \to {\frac {1}{2}}}\operatorname {E} [|X-E[X]|]\right)&={\frac {1}{2}}\\\lim _{\nu \to \infty }\left(\lim _{\mu \to {\frac {1}{2}}}\operatorname {E} [|X-E[X]|]\right)&=0\end{aligned}}}

Also, the following limits (with only the noted variable approaching the limit) can be obtained from the above expressions:
{\displaystyle {\begin{aligned}\lim _{\beta \to 0}\operatorname {E} [|X-E[X]|]&=\lim _{\alpha \to 0}\operatorname {E} [|X-E[X]|]=0\\\lim _{\beta \to \infty }\operatorname {E} [|X-E[X]|]&=\lim _{\alpha \to \infty }\operatorname {E} [|X-E[X]|]=0\\\lim _{\mu \to 0}\operatorname {E} [|X-E[X]|]&=\lim _{\mu \to 1}\operatorname {E} [|X-E[X]|]=0\\\lim _{\nu \to 0}\operatorname {E} [|X-E[X]|]&={\sqrt {\mu (1-\mu )}}\\\lim _{\nu \to \infty }\operatorname {E} [|X-E[X]|]&=0\end{aligned}}}

Mean absolute difference[edit]
The mean absolute difference for the beta distribution is:
{\displaystyle {\begin{aligned}\mathrm {MD} &=\int _{0}^{1}\int _{0}^{1}f(x;\alpha ,\beta )\,f(y;\alpha ,\beta )\left|x-y\right|dx\,dy\\[1ex]&={\frac {4}{\alpha +\beta }}{\frac {B(\alpha +\beta ,\alpha +\beta )}{B(\alpha ,\alpha )B(\beta ,\beta )}}\end{aligned}}}

The Gini coefficient for the beta distribution is half of the relative mean absolute difference:
{\displaystyle \mathrm {G} =\left({\frac {2}{\alpha }}\right){\frac {B(\alpha +\beta ,\alpha +\beta )}{B(\alpha ,\alpha )B(\beta ,\beta )}}}

Skewness[edit]
Skewness for beta distribution as a function of variance and mean
The skewness (the third moment centered on the mean, normalized by the 3/2 power of the variance) of the beta distribution is[1]
{\displaystyle \gamma _{1}={\frac {\operatorname {E} \left[\left(X-\mu \right)^{3}\right]}{\left(\operatorname {var} (X)\right)^{3/2}}}={\frac {2\left(\beta -\alpha \right){\sqrt {\alpha +\beta +1}}}{\left(\alpha +\beta +2\right){\sqrt {\alpha \beta }}}}.}

Letting α = β in the above expression one obtains γ1 = 0, showing once again that for α = β the distribution is symmetric and hence the skewness is zero. Positive skew (right-tailed) for α < β, negative skew (left-tailed) for α > β.
Using the parametrization in terms of mean μ and sample size ν = α + β:

α

=
μ
ν
,

 where 

ν
=
(
α
+
β
)
>
0
,

β

=
(
1
−
μ
)
ν
,

 where 
{\displaystyle {\begin{aligned}\alpha &=\mu \nu ,&{\text{ where }}\nu =(\alpha +\beta )>0,\\\beta &=(1-\mu )\nu ,&{\text{ where }}\nu =(\alpha +\beta )>0.\end{aligned}}}

one can express the skewness in terms of the mean μ and the sample size ν as follows:
{\displaystyle \gamma _{1}={\frac {\operatorname {E} [(X-\mu )^{3}]}{\left(\operatorname {var} (X)\right)^{3/2}}}={\frac {2(1-2\mu ){\sqrt {1+\nu }}}{(2+\nu ){\sqrt {\mu (1-\mu )}}}}.}

The skewness can also be expressed just in terms of the variance var and the mean μ as follows:
{\displaystyle \gamma _{1}={\frac {\operatorname {E} [(X-\mu )^{3}]}{(\operatorname {var} (X))^{3/2}}}={\frac {2(1-2\mu ){\sqrt {\operatorname {var} }}}{\mu (1-\mu )+\operatorname {var} }}{\text{ if }}\operatorname {var} <\mu (1-\mu )}

The accompanying plot of skewness as a function of variance and mean shows that maximum variance (1/4) is coupled with zero skewness and the symmetry condition (μ = 1/2), and that maximum skewness (positive or negative infinity) occurs when the mean is located at one end or the other, so that the "mass" of the probability distribution is concentrated at the ends (minimum variance).
The following expression for the square of the skewness, in terms of the sample size ν = α + β and the variance var, is useful for the method of moments estimation of four parameters:
{\displaystyle (\gamma _{1})^{2}={\frac {\left(\operatorname {E} [(X-\mu )^{3}]\right)^{2}}{\left(\operatorname {var} (X)\right)^{3}}}={\frac {4}{(2+\nu )^{2}}}\left({\frac {1}{\operatorname {var} }}-4(1+\nu )\right)}

This expression correctly gives a skewness of zero for α = β, since in that case (see § Variance): 
{\displaystyle \operatorname {var} ={\frac {1}{4(1+\nu )}}}

.
For the symmetric case (α = β), skewness = 0 over the whole range, and the following limits apply:
{\displaystyle \lim _{\alpha =\beta \to 0}\gamma _{1}=\lim _{\alpha =\beta \to \infty }\gamma _{1}=\lim _{\nu \to 0}\gamma _{1}=\lim _{\nu \to \infty }\gamma _{1}=\lim _{\mu \to {\frac {1}{2}}}\gamma _{1}=0}

For the asymmetric cases (α ≠ β) the following limits (with only the noted variable approaching the limit) can be obtained from the above expressions:
{\displaystyle {\begin{aligned}&\lim _{\alpha \to 0}\gamma _{1}=\lim _{\mu \to 0}\gamma _{1}=\infty \\&\lim _{\beta \to 0}\gamma _{1}=\lim _{\mu \to 1}\gamma _{1}=-\infty \\&\lim _{\alpha \to \infty }\gamma _{1}=-{\frac {2}{\sqrt {\beta }}},\quad \lim _{\beta \to 0}(\lim _{\alpha \to \infty }\gamma _{1})=-\infty ,\quad \lim _{\beta \to \infty }(\lim _{\alpha \to \infty }\gamma _{1})=0\\&\lim _{\beta \to \infty }\gamma _{1}={\frac {2}{\sqrt {\alpha }}},\quad \lim _{\alpha \to 0}(\lim _{\beta \to \infty }\gamma _{1})=\infty ,\quad \lim _{\alpha \to \infty }(\lim _{\beta \to \infty }\gamma _{1})=0\\&\lim _{\nu \to 0}\gamma _{1}={\frac {1-2\mu }{\sqrt {\mu (1-\mu )}}},\quad \lim _{\mu \to 0}(\lim _{\nu \to 0}\gamma _{1})=\infty ,\quad \lim _{\mu \to 1}(\lim _{\nu \to 0}\gamma _{1})=-\infty \end{aligned}}}

Kurtosis[edit]
Excess Kurtosis for Beta Distribution as a function of variance and mean
The beta distribution has been applied in acoustic analysis to assess damage to gears, as the kurtosis of the beta distribution has been reported to be a good indicator of the condition of a gear.[15] Kurtosis has also been used to distinguish the seismic signal generated by a person's footsteps from other signals. As persons or other targets moving on the ground generate continuous signals in the form of seismic waves, one can separate different targets based on the seismic waves they generate. Kurtosis is sensitive to impulsive signals, so it's much more sensitive to the signal generated by human footsteps than other signals generated by vehicles, winds, noise, etc.[16]  Unfortunately, the notation for kurtosis has not been standardized. Kenney and Keeping[17]  use the symbol γ2 for the excess kurtosis, but Abramowitz and Stegun[18]  use different terminology.  To prevent confusion[19]  between kurtosis (the fourth moment centered on the mean, normalized by the square of the variance) and excess kurtosis, when using symbols, they will be spelled out as follows:[9][20]

excess kurtosis

=

kurtosis
{\displaystyle {\begin{aligned}{\text{excess kurtosis}}&={\text{kurtosis}}-3\\&={\frac {\operatorname {E} [(X-\mu )^{4}]}{(\operatorname {var} (X))^{2}}}-3\\&={\frac {6[\alpha ^{3}-\alpha ^{2}(2\beta -1)+\beta ^{2}(\beta +1)-2\alpha \beta (\beta +2)]}{\alpha \beta (\alpha +\beta +2)(\alpha +\beta +3)}}\\&={\frac {6[(\alpha -\beta )^{2}(\alpha +\beta +1)-\alpha \beta (\alpha +\beta +2)]}{\alpha \beta (\alpha +\beta +2)(\alpha +\beta +3)}}.\end{aligned}}}

Letting α = β in the above expression one obtains

excess kurtosis
{\displaystyle {\text{excess kurtosis}}=-{\frac {6}{3+2\alpha }}{\text{ if }}\alpha =\beta .}

Therefore, for symmetric beta distributions, the excess kurtosis is negative, increasing from a minimum value of −2 at the limit as {α = β} → 0, and approaching a maximum value of zero as {α = β} → ∞.  The value of −2 is the minimum value of excess kurtosis that any distribution (not just beta distributions, but any distribution of any possible kind) can ever achieve.  This minimum value is reached when all the probability density is entirely concentrated at each end x = 0 and x = 1, with nothing in between: a 2-point Bernoulli distribution with equal probability 1/2 at each end (a coin toss: see section below "Kurtosis bounded by the square of the skewness" for further discussion).  The description of kurtosis as a measure of the "potential outliers" (or "potential rare, extreme values") of the probability distribution, is correct for all distributions including the beta distribution. When rare, extreme values can occur in the beta distribution, the higher its kurtosis; otherwise, the kurtosis is lower. For α ≠ β, skewed beta distributions, the excess kurtosis can reach unlimited positive values (particularly for α → 0 for finite β, or for β → 0 for finite α) because the side away from the mode will produce occasional extreme values.  Minimum kurtosis takes place when the mass density is concentrated equally at each end (and therefore the mean is at the center), and there is no probability mass density in between the ends.
Using the parametrization in terms of mean μ and sample size ν = α + β:

α

=
μ
ν
,

 where 

ν
=
(
α
+
β
)
>
0

β

=
(
1
−
μ
)
ν
,

 where 
{\displaystyle {\begin{aligned}\alpha &{}=\mu \nu ,{\text{ where }}\nu =(\alpha +\beta )>0\\\beta &{}=(1-\mu )\nu ,{\text{ where }}\nu =(\alpha +\beta )>0.\end{aligned}}}

one can express the excess kurtosis in terms of the mean μ and the sample size ν as follows:

excess kurtosis
{\displaystyle {\text{excess kurtosis}}={\frac {6}{3+\nu }}{\bigg (}{\frac {(1-2\mu )^{2}(1+\nu )}{\mu (1-\mu )(2+\nu )}}-1{\bigg )}}

The excess kurtosis can also be expressed in terms of just the following two parameters: the variance var, and the sample size ν as follows:

excess kurtosis
{\displaystyle {\text{excess kurtosis}}={\frac {6}{(3+\nu )(2+\nu )}}\left({\frac {1}{\text{ var }}}-6-5\nu \right){\text{ if }}{\text{var}}<\mu (1-\mu )}

and, in terms of the variance var and the mean μ as follows:

excess kurtosis
{\displaystyle {\text{excess kurtosis}}={\frac {6{\text{ var }}(1-{\text{ var }}-5\mu (1-\mu ))}{({\text{var }}+\mu (1-\mu ))(2{\text{ var }}+\mu (1-\mu ))}}{\text{ if }}{\text{var}}<\mu (1-\mu )}

The plot of excess kurtosis as a function of the variance and the mean shows that the minimum value of the excess kurtosis (−2, which is the minimum possible value for excess kurtosis for any distribution) is intimately coupled with the maximum value of variance (1/4) and the symmetry condition: the mean occurring at the midpoint (μ = 1/2). This occurs for the symmetric case of α = β = 0, with zero skewness.  At the limit, this is the 2 point Bernoulli distribution with equal probability 1/2 at each Dirac delta function end x = 0 and x = 1 and zero probability everywhere else. (A coin toss: one face of the coin being x = 0 and the other face being x = 1.)  Variance is maximum because the distribution is bimodal with nothing in between the two modes (spikes) at each end.  Excess kurtosis is minimum: the probability density "mass" is zero at the mean and it is concentrated at the two peaks at each end.  Excess kurtosis reaches the minimum possible value (for any distribution) when the probability density function has two spikes at each end: it is bi-"peaky" with nothing in between them.
On the other hand, the plot shows that for extreme skewed cases, where the mean is located near one or the other end (μ = 0 or μ = 1), the variance is close to zero, and the excess kurtosis rapidly approaches infinity when the mean of the distribution approaches either end.
Alternatively, the excess kurtosis can also be expressed in terms of just the following two parameters: the square of the skewness, and the sample size ν as follows:

excess kurtosis

=

6

3
+
ν

(

(
2
+
ν
)

4

(

skewness

)

2

−
1

)

 if (skewness)

2

−
2
<

excess kurtosis

<

3
2

(

skewness
{\displaystyle {\text{excess kurtosis}}={\frac {6}{3+\nu }}{\bigg (}{\frac {(2+\nu )}{4}}({\text{skewness}})^{2}-1{\bigg )}{\text{ if (skewness)}}^{2}-2<{\text{excess kurtosis}}<{\frac {3}{2}}({\text{skewness}})^{2}}

From this last expression, one can obtain the same limits published over a century ago by Karl Pearson[21] for the beta distribution (see section below titled "Kurtosis bounded by the square of the skewness"). Setting α + β = ν = 0 in the above expression, one obtains Pearson's lower boundary (values for the skewness and excess kurtosis below the boundary (excess kurtosis + 2 − skewness2 = 0) cannot occur for any distribution, and hence Karl Pearson appropriately called the region below this boundary the "impossible region"). The limit of α + β = ν → ∞ determines Pearson's upper boundary.

lim

ν
→
0

excess kurtosis

=
(

skewness

)

2

−
2

lim

ν
→
∞

excess kurtosis

=

3
2

(

skewness
{\displaystyle {\begin{aligned}&\lim _{\nu \to 0}{\text{excess kurtosis}}=({\text{skewness}})^{2}-2\\&\lim _{\nu \to \infty }{\text{excess kurtosis}}={\tfrac {3}{2}}({\text{skewness}})^{2}\end{aligned}}}

therefore:

(

skewness

)

2

−
2
<

excess kurtosis

<

3
2

(

skewness
{\displaystyle ({\text{skewness}})^{2}-2<{\text{excess kurtosis}}<{\tfrac {3}{2}}({\text{skewness}})^{2}}

Values of ν = α + β such that ν ranges from zero to infinity, 0 < ν < ∞, span the whole region of the beta distribution in the plane of excess kurtosis versus squared skewness.
For the symmetric case (α = β), the following limits apply:

lim

α
=
β
→
0

excess kurtosis

=
−
2

lim

α
=
β
→
∞

excess kurtosis

=
0

lim

μ
→

1
2

excess kurtosis
{\displaystyle {\begin{aligned}&\lim _{\alpha =\beta \to 0}{\text{excess kurtosis}}=-2\\&\lim _{\alpha =\beta \to \infty }{\text{excess kurtosis}}=0\\&\lim _{\mu \to {\frac {1}{2}}}{\text{excess kurtosis}}=-{\frac {6}{3+\nu }}\end{aligned}}}

For the unsymmetric cases (α ≠ β) the following limits (with only the noted variable approaching the limit) can be obtained from the above expressions:

lim

α
→
0

excess kurtosis

=

lim

β
→
0

excess kurtosis

=

lim

μ
→
0

excess kurtosis

=

lim

μ
→
1

excess kurtosis

=
∞

lim

α
→
∞

excess kurtosis

=

6
β

,

lim

β
→
0

(

lim

α
→
∞

excess kurtosis

)
=
∞
,

lim

β
→
∞

(

lim

α
→
∞

excess kurtosis

)
=
0

lim

β
→
∞

excess kurtosis

=

6
α

,

lim

α
→
0

(

lim

β
→
∞

excess kurtosis

)
=
∞
,

lim

α
→
∞

(

lim

β
→
∞

excess kurtosis

)
=
0

lim

ν
→
0

excess kurtosis

=
−
6
+

1

μ
(
1
−
μ
)

,

lim

μ
→
0

(

lim

ν
→
0

excess kurtosis

)
=
∞
,

lim

μ
→
1

(

lim

ν
→
0

excess kurtosis
{\displaystyle {\begin{aligned}&\lim _{\alpha \to 0}{\text{excess kurtosis}}=\lim _{\beta \to 0}{\text{excess kurtosis}}=\lim _{\mu \to 0}{\text{excess kurtosis}}=\lim _{\mu \to 1}{\text{excess kurtosis}}=\infty \\&\lim _{\alpha \to \infty }{\text{excess kurtosis}}={\frac {6}{\beta }},{\text{    }}\lim _{\beta \to 0}(\lim _{\alpha \to \infty }{\text{excess kurtosis}})=\infty ,{\text{    }}\lim _{\beta \to \infty }(\lim _{\alpha \to \infty }{\text{excess kurtosis}})=0\\&\lim _{\beta \to \infty }{\text{excess kurtosis}}={\frac {6}{\alpha }},{\text{    }}\lim _{\alpha \to 0}(\lim _{\beta \to \infty }{\text{excess kurtosis}})=\infty ,{\text{    }}\lim _{\alpha \to \infty }(\lim _{\beta \to \infty }{\text{excess kurtosis}})=0\\&\lim _{\nu \to 0}{\text{excess kurtosis}}=-6+{\frac {1}{\mu (1-\mu )}},{\text{    }}\lim _{\mu \to 0}(\lim _{\nu \to 0}{\text{excess kurtosis}})=\infty ,{\text{    }}\lim _{\mu \to 1}(\lim _{\nu \to 0}{\text{excess kurtosis}})=\infty \end{aligned}}}

Characteristic function[edit]
Re(characteristic function) symmetric case α = β ranging from 25 to 0Re(characteristic function) symmetric case α = β ranging from 0 to 25Re(characteristic function) β = α + 1/2; α ranging from 25 to 0Re(characteristic function) α = β + 1/2; β ranging from 25 to 0Re(characteristic function) α = β + 1/2; β ranging from 0 to 25
The characteristic function is the Fourier transform of the probability density function. The characteristic function of the beta distribution is Kummer's confluent hypergeometric function (of the first kind):[1][18][22]
{\displaystyle {\begin{aligned}\varphi _{X}(\alpha ;\beta ;t)&=\operatorname {E} \left[e^{itX}\right]\\&=\int _{0}^{1}e^{itx}f(x;\alpha ,\beta )\,dx\\&={}_{1}F_{1}(\alpha ;\alpha +\beta ;it)\!\\&=\sum _{n=0}^{\infty }{\frac {\alpha ^{\overline {n}}(it)^{n}}{(\alpha +\beta )^{\overline {n}}n!}}\\&=1+\sum _{k=1}^{\infty }\left(\prod _{r=0}^{k-1}{\frac {\alpha +r}{\alpha +\beta +r}}\right){\frac {(it)^{k}}{k!}}\end{aligned}}}

where
{\displaystyle x^{\overline {n}}=x(x+1)(x+2)\cdots (x+n-1)}

is the rising factorial. The value of the characteristic function for t = 0, is one:
{\displaystyle \varphi _{X}(\alpha ;\beta ;0)={}_{1}F_{1}(\alpha ;\alpha +\beta ;0)=1.}

Also, the real and imaginary parts of the characteristic function enjoy the following symmetries with respect to the origin of variable t:
{\displaystyle \operatorname {Re} \left[{}_{1}F_{1}(\alpha ;\alpha +\beta ;it)\right]=\operatorname {Re} \left[{}_{1}F_{1}(\alpha ;\alpha +\beta ;-it)\right]}
{\displaystyle \operatorname {Im} \left[{}_{1}F_{1}(\alpha ;\alpha +\beta ;it)\right]=-\operatorname {Im} \left[{}_{1}F_{1}(\alpha ;\alpha +\beta ;-it)\right]}

The symmetric case α = β simplifies the characteristic function of the beta distribution to a Bessel function, since in the special case α + β = 2α the confluent hypergeometric function (of the first kind) reduces to a Bessel function (the modified Bessel function of the first kind 
{\displaystyle I_{\alpha -{\frac {1}{2}}}}

 ) using Kummer's second transformation as follows:
{\displaystyle {\begin{aligned}{}_{1}F_{1}(\alpha ;2\alpha ;it)&=e^{\frac {it}{2}}{}_{0}F_{1}\left(;\alpha +{\tfrac {1}{2}};{\frac {(it)^{2}}{16}}\right)\\&=e^{\frac {it}{2}}\left({\frac {it}{4}}\right)^{{\frac {1}{2}}-\alpha }\Gamma \left(\alpha +{\tfrac {1}{2}}\right)I_{\alpha -{\frac {1}{2}}}\left({\frac {it}{2}}\right).\end{aligned}}}

In the accompanying plots, the real part (Re) of the characteristic function of the beta distribution is displayed for symmetric (α = β) and skewed (α ≠ β) cases.

Other moments[edit]
Moment generating function[edit]
It also follows[1][9] that the moment generating function is
{\displaystyle {\begin{aligned}M_{X}(\alpha ;\beta ;t)&=\operatorname {E} \left[e^{tX}\right]\\[4pt]&=\int _{0}^{1}e^{tx}f(x;\alpha ,\beta )\,dx\\[4pt]&={}_{1}F_{1}(\alpha ;\alpha +\beta ;t)\\[4pt]&=\sum _{n=0}^{\infty }{\frac {\alpha ^{\overline {n}}}{(\alpha +\beta )^{\overline {n}}}}{\frac {t^{n}}{n!}}\\[4pt]&=1+\sum _{k=1}^{\infty }\left(\prod _{r=0}^{k-1}{\frac {\alpha +r}{\alpha +\beta +r}}\right){\frac {t^{k}}{k!}}.\end{aligned}}}

In particular MX(α; β; 0) = 1.

Higher moments[edit]
Using the moment generating function, the k-th raw moment is given by[1] the factor
{\displaystyle \prod _{r=0}^{k-1}{\frac {\alpha +r}{\alpha +\beta +r}}}

multiplying the (exponential series) term 
{\displaystyle \left({\frac {t^{k}}{k!}}\right)}

 in the series of the moment generating function
{\displaystyle \operatorname {E} [X^{k}]={\frac {\alpha ^{\overline {k}}}{(\alpha +\beta )^{\overline {k}}}}=\prod _{r=0}^{k-1}{\frac {\alpha +r}{\alpha +\beta +r}}}

where (x)(k) is a Pochhammer symbol representing rising factorial. It can also be written in a recursive form as
{\displaystyle \operatorname {E} [X^{k}]={\frac {\alpha +k-1}{\alpha +\beta +k-1}}\operatorname {E} [X^{k-1}].}

Since the moment generating function 
{\displaystyle M_{X}(\alpha ;\beta ;\cdot )}

 has a positive radius of convergence,[citation needed] the beta distribution is determined by its moments.[23]

Moments of transformed random variables[edit]
Moments of linearly transformed, product and inverted random variables[edit]
One can also show the following expectations for a transformed random variable,[1] where the random variable X is Beta-distributed with parameters α and β: X ~ Beta(α, β).  The expected value of the variable 1 − X is the mirror-symmetry of the expected value based on X:
{\displaystyle {\begin{aligned}\operatorname {E} [1-X]&={\frac {\beta }{\alpha +\beta }}\\\operatorname {E} [X(1-X)]&=\operatorname {E} [(1-X)X]={\frac {\alpha \beta }{(\alpha +\beta )(\alpha +\beta +1)}}\end{aligned}}}

Due to the mirror-symmetry of the probability density function of the beta distribution, the variances based on variables X and 1 − X are identical, and the covariance on X(1 − X is the negative of the variance:
{\displaystyle \operatorname {var} [(1-X)]=\operatorname {var} [X]=-\operatorname {cov} [X,(1-X)]={\frac {\alpha \beta }{(\alpha +\beta )^{2}(\alpha +\beta +1)}}}

These are the expected values for inverted variables, (these are related to the harmonic means, see § Harmonic mean):
{\displaystyle {\begin{aligned}\operatorname {E} \left[{\frac {1}{X}}\right]&={\frac {\alpha +\beta -1}{\alpha -1}}&&{\text{ if  }}\alpha >1\\\operatorname {E} \left[{\frac {1}{1-X}}\right]&={\frac {\alpha +\beta -1}{\beta -1}}&&{\text{ if }}\beta >1\end{aligned}}}

The following transformation by dividing the variable X by its mirror-image X/(1 − X) results in the expected value of the "inverted beta distribution" or beta prime distribution (also known as beta distribution of the second kind or Pearson's Type VI):[1]
{\displaystyle {\begin{aligned}\operatorname {E} \left[{\frac {X}{1-X}}\right]&={\frac {\alpha }{\beta -1}}&&{\text{ if }}\beta >1\\\operatorname {E} \left[{\frac {1-X}{X}}\right]&={\frac {\beta }{\alpha -1}}&&{\text{ if }}\alpha >1\end{aligned}}}

Variances of these transformed variables can be obtained by integration, as the expected values of the second moments centered on the corresponding variables:
{\displaystyle {\begin{aligned}\operatorname {var} \left[{\frac {1}{X}}\right]&=\operatorname {E} \left[\left({\frac {1}{X}}-\operatorname {E} \left[{\frac {1}{X}}\right]\right)^{2}\right]=\operatorname {var} \left[{\frac {1-X}{X}}\right]\\&=\operatorname {E} \left[\left({\frac {1-X}{X}}-\operatorname {E} \left[{\frac {1-X}{X}}\right]\right)^{2}\right]={\frac {\beta (\alpha +\beta -1)}{\left(\alpha -2\right)\left(\alpha -1\right)^{2}}}{\text{ if }}\alpha >2\end{aligned}}}

The following variance of the variable X divided by its mirror-image (X/(1−X) results in the variance of the "inverted beta distribution" or beta prime distribution (also known as beta distribution of the second kind or Pearson's Type VI):[1]
{\displaystyle {\begin{aligned}\operatorname {var} \left[{\frac {1}{1-X}}\right]&=\operatorname {E} \left[\left({\frac {1}{1-X}}-\operatorname {E} \left[{\frac {1}{1-X}}\right]\right)^{2}\right]=\operatorname {var} \left[{\frac {X}{1-X}}\right]\\[1ex]&=\operatorname {E} \left[\left({\frac {X}{1-X}}-\operatorname {E} \left[{\frac {X}{1-X}}\right]\right)^{2}\right]={\frac {\alpha (\alpha +\beta -1)}{\left(\beta -2\right)\left(\beta -1\right)^{2}}}{\text{ if }}\beta >2\end{aligned}}}

The covariances are:
{\displaystyle {\begin{aligned}\operatorname {cov} \left[{\frac {1}{X}},{\frac {1}{1-X}}\right]&=\operatorname {cov} \left[{\frac {1-X}{X}},{\frac {X}{1-X}}\right]=\operatorname {cov} \left[{\frac {1}{X}},{\frac {X}{1-X}}\right]\\[1ex]&=\operatorname {cov} \left[{\frac {1-X}{X}},{\frac {1}{1-X}}\right]={\frac {\alpha +\beta -1}{(\alpha -1)(\beta -1)}}{\text{ if }}\alpha ,\beta >1\end{aligned}}}

These expectations and variances appear in the four-parameter Fisher information matrix (§ Fisher information.)

Moments of logarithmically transformed random variables[edit]
Plot of logit(X) = ln(X/(1 −X)) (vertical axis) vs. X in the domain of 0 to 1 (horizontal axis). Logit transformations are interesting, as they usually transform various shapes (including J-shapes) into (usually skewed) bell-shaped densities over the logit variable, and they may remove the end singularities over the original variable
Expected values for logarithmic transformations (useful for maximum likelihood estimates, see § Parameter estimation, Maximum likelihood) are discussed in this section.  The following logarithmic linear transformations are related to the geometric means GX and  G1−X (see § Geometric Mean):
{\displaystyle {\begin{aligned}\operatorname {E} [\ln X]&=\psi (\alpha )-\psi (\alpha +\beta )=-\operatorname {E} \left[\ln {\frac {1}{X}}\right],\\\operatorname {E} [\ln(1-X)]&=\psi (\beta )-\psi (\alpha +\beta )=-\operatorname {E} \left[\ln {\frac {1}{1-X}}\right].\end{aligned}}}

Where the digamma function ψ(α) is defined as the logarithmic derivative of the gamma function:[18]
{\displaystyle \psi (\alpha )={\frac {d}{d\alpha }}\ln \Gamma (\alpha )}

Logit transformations are interesting,[24] as they usually transform various shapes (including J-shapes) into (usually skewed) bell-shaped densities over the logit variable, and they may remove the end singularities over the original variable:
{\displaystyle {\begin{aligned}\operatorname {E} \left[\ln {\frac {X}{1-X}}\right]&=\psi (\alpha )-\psi (\beta )=\operatorname {E} [\ln X]+\operatorname {E} \left[\ln {\frac {1}{1-X}}\right],\\\operatorname {E} \left[\ln {\frac {1-X}{X}}\right]&=\psi (\beta )-\psi (\alpha )=-\operatorname {E} \left[\ln {\frac {X}{1-X}}\right].\end{aligned}}}

Johnson[25]  considered the distribution of the logit – transformed variable ln(X/1 − X), including its moment generating function and approximations for large values of the shape parameters.  This transformation extends the finite support [0, 1] based on the original variable X to infinite support in both directions of the real line (−∞, +∞). The logit of a beta variate has the logistic-beta distribution.
Higher order logarithmic moments can be derived by using the representation of a beta distribution as a proportion of two gamma distributions and differentiating through the integral. They can be expressed in terms of higher order poly-gamma functions as follows:
{\displaystyle {\begin{aligned}\operatorname {E} \left[\ln ^{2}(X)\right]&=(\psi (\alpha )-\psi (\alpha +\beta ))^{2}+\psi _{1}(\alpha )-\psi _{1}(\alpha +\beta ),\\\operatorname {E} \left[\ln ^{2}(1-X)\right]&=(\psi (\beta )-\psi (\alpha +\beta ))^{2}+\psi _{1}(\beta )-\psi _{1}(\alpha +\beta ),\\\operatorname {E} \left[\ln(X)\ln(1-X)\right]&=(\psi (\alpha )-\psi (\alpha +\beta ))(\psi (\beta )-\psi (\alpha +\beta ))-\psi _{1}(\alpha +\beta ).\end{aligned}}}

therefore the variance of the logarithmic variables and covariance of ln(X) and ln(1−X) are:
{\displaystyle {\begin{aligned}\operatorname {cov} [\ln X,\ln(1-X)]&=\operatorname {E} \left[\ln X\ln(1-X)\right]-\operatorname {E} [\ln X]\operatorname {E} [\ln(1-X)]\\&=-\psi _{1}(\alpha +\beta )\\&\\\operatorname {var} [\ln X]&=\operatorname {E} [\ln ^{2}X]-(\operatorname {E} [\ln X])^{2}\\&=\psi _{1}(\alpha )-\psi _{1}(\alpha +\beta )\\&=\psi _{1}(\alpha )+\operatorname {cov} [\ln X,\ln(1-X)]\\&\\\operatorname {var} [\ln(1-X)]&=\operatorname {E} [\ln ^{2}(1-X)]-(\operatorname {E} [\ln(1-X)])^{2}\\&=\psi _{1}(\beta )-\psi _{1}(\alpha +\beta )\\&=\psi _{1}(\beta )+\operatorname {cov} [\ln X,\ln(1-X)]\end{aligned}}}

where the trigamma function, denoted ψ1(α), is the second of the polygamma functions, and is defined as the derivative of the digamma function:
{\displaystyle \psi _{1}(\alpha )={\frac {d^{2}\ln \Gamma (\alpha )}{d\alpha ^{2}}}={\frac {d\psi (\alpha )}{d\alpha }}.}

The variances and covariance of the logarithmically transformed variables X and (1 − X) are different, in general, because the logarithmic transformation destroys the mirror-symmetry of the original variables X and (1 − X), as the logarithm approaches negative infinity for the variable approaching zero.
These logarithmic variances and covariance are the elements of the Fisher information matrix for the beta distribution.  They are also a measure of the curvature of the log likelihood function (see section on Maximum likelihood estimation).
The variances of the log inverse variables are identical to the variances of the log variables:
{\displaystyle {\begin{aligned}\operatorname {var} \left[\ln {\frac {1}{X}}\right]&=\operatorname {var} [\ln X]=\psi _{1}(\alpha )-\psi _{1}(\alpha +\beta ),\\\operatorname {var} \left[\ln {\frac {1}{1-X}}\right]&=\operatorname {var} [\ln(1-X)]=\psi _{1}(\beta )-\psi _{1}(\alpha +\beta ),\\\operatorname {cov} \left[\ln {\frac {1}{X}},\,\ln {\frac {1}{1-X}}\right]&=\operatorname {cov} [\ln X,\ln(1-X)]=-\psi _{1}(\alpha +\beta ).\end{aligned}}}

It also follows that the variances of the logit-transformed variables are
{\displaystyle {\begin{aligned}\operatorname {var} \left[\ln {\frac {X}{1-X}}\right]&=\operatorname {var} \left[\ln {\frac {1-X}{X}}\right]\\&=-\operatorname {cov} \left[\ln {\frac {X}{1-X}},\,\ln {\frac {1-X}{X}}\right]\\[1ex]&=\psi _{1}(\alpha )+\psi _{1}(\beta ).\end{aligned}}}

Quantities of information (entropy)[edit]
Given a beta distributed random variable, X ~ Beta(α, β), the differential entropy of X is (measured in nats),[26] the expected value of the negative of the logarithm of the probability density function:
{\displaystyle {\begin{aligned}h(X)&=\operatorname {E} \left[-\ln f(X;\alpha ,\beta )\right]\\[4pt]&=\int _{0}^{1}-f(x;\alpha ,\beta )\ln f(x;\alpha ,\beta )\,dx\\[4pt]&=\ln \mathrm {B} (\alpha ,\beta )-(\alpha -1)\psi (\alpha )-(\beta -1)\psi (\beta )+(\alpha +\beta -2)\psi (\alpha +\beta )\end{aligned}}}

where f(x; α, β) is the probability density function of the beta distribution:
{\displaystyle f(x;\alpha ,\beta )={\frac {x^{\alpha -1}\left(1-x\right)^{\beta -1}}{\mathrm {B} (\alpha ,\beta )}}}

The digamma function ψ appears in the formula for the differential entropy as a consequence of Euler's integral formula for the harmonic numbers which follows from the integral:
{\displaystyle \int _{0}^{1}{\frac {1-x^{\alpha -1}}{1-x}}\,dx=\psi (\alpha )-\psi (1)}

The differential entropy of the beta distribution is negative for all values of α and β greater than zero, except at α = β = 1 (for which values the beta distribution is the same as the uniform distribution), where the differential entropy reaches its maximum value of zero.  It is to be expected that the maximum entropy should take place when the beta distribution becomes equal to the uniform distribution, since uncertainty is maximal when all possible events are equiprobable.
For α or β approaching zero, the differential entropy approaches its minimum value of negative infinity. For (either or both) α or β approaching zero, there is a maximum amount of order: all the probability density is concentrated at the ends, and there is zero probability density at points located between the ends. Similarly for (either or both) α or β approaching infinity, the differential entropy approaches its minimum value of negative infinity, and a maximum amount of order.  If either α or β approaches infinity (and the other is finite) all the probability density is concentrated at an end, and the probability density is zero everywhere else.  If both shape parameters are equal (the symmetric case), α = β, and they approach infinity simultaneously, the probability density becomes a spike (Dirac delta function) concentrated at the middle x = 1/2, and hence there is 100% probability at the middle x = 1/2 and zero probability everywhere else.

The (continuous case) differential entropy was introduced by Shannon in his original paper (where he named it the "entropy of a continuous distribution"), as the concluding part of the same paper where he defined the discrete entropy.[27]  It is known since then that the differential entropy may differ from the infinitesimal limit of the discrete entropy by an infinite offset, therefore the differential entropy can be negative (as it is for the beta distribution). What really matters is the relative value of entropy.
Given two beta distributed random variables, X1 ~ Beta(α, β) and X2 ~ Beta(α′, β′), the cross-entropy is (measured in nats)[28]
{\displaystyle {\begin{aligned}H(X_{1},X_{2})&=\int _{0}^{1}-f(x;\alpha ,\beta )\ln f(x;\alpha ',\beta ')\,dx\\[4pt]&=\ln \mathrm {B} (\alpha ',\beta ')-(\alpha '-1)\psi (\alpha )-(\beta '-1)\psi (\beta )+\left(\alpha '+\beta '-2\right)\psi (\alpha +\beta ).\end{aligned}}}

The cross entropy has been used as an error metric to measure the distance between two hypotheses.[29][30]  Its absolute value is minimum when the two distributions are identical. It is the information measure most closely related to the log maximum likelihood [28](see section on "Parameter estimation. Maximum likelihood estimation")).
The relative entropy, or Kullback–Leibler divergence DKL(X1 || X2), is a measure of the inefficiency of assuming that the distribution is X2 ~ Beta(α′, β′)  when the distribution is really X1 ~ Beta(α, β). It is defined as follows (measured in nats).
{\displaystyle {\begin{aligned}D_{\mathrm {KL} }(X_{1}\parallel X_{2})&=\int _{0}^{1}f(x;\alpha ,\beta )\,\ln {\frac {f(x;\alpha ,\beta )}{f(x;\alpha ',\beta ')}}\,dx\\[4pt]&=\left(\int _{0}^{1}f(x;\alpha ,\beta )\ln f(x;\alpha ,\beta )\,dx\right)-\left(\int _{0}^{1}f(x;\alpha ,\beta )\ln f(x;\alpha ',\beta ')\,dx\right)\\[4pt]&=-h(X_{1})+H(X_{1},X_{2})\\[4pt]&=\ln {\frac {\mathrm {B} (\alpha ',\beta ')}{\mathrm {B} (\alpha ,\beta )}}+\left(\alpha -\alpha '\right)\psi (\alpha )+\left(\beta -\beta '\right)\psi (\beta )+\left(\alpha '-\alpha +\beta '-\beta \right)\psi (\alpha +\beta ).\end{aligned}}}

The relative entropy, or Kullback–Leibler divergence, is always non-negative.  A few numerical examples follow:

X1 ~ Beta(1, 1) and X2 ~ Beta(3, 3); DKL(X1 || X2) = 0.598803; DKL(X2 || X1) = 0.267864; h(X1) = 0; h(X2) = −0.267864
X1 ~ Beta(3, 0.5) and X2 ~ Beta(0.5, 3); DKL(X1 || X2) = 7.21574; DKL(X2 || X1) = 7.21574; h(X1) = −1.10805; h(X2) = −1.10805.
The Kullback–Leibler divergence is not symmetric DKL(X1 || X2) ≠ DKL(X2 || X1)  for the case in which the individual beta distributions Beta(1, 1) and Beta(3, 3) are symmetric, but have different entropies h(X1) ≠ h(X2). The value of the Kullback divergence depends on the direction traveled: whether going from a higher (differential) entropy to a lower (differential) entropy or the other way around. In the numerical example above, the Kullback divergence measures the inefficiency of assuming that the distribution is (bell-shaped) Beta(3, 3), rather than (uniform) Beta(1, 1). The "h" entropy of Beta(1, 1) is higher than the "h" entropy of Beta(3, 3) because the uniform distribution Beta(1, 1) has a maximum amount of disorder. The Kullback divergence is more than two times higher (0.598803 instead of 0.267864) when measured in the direction of decreasing entropy: the direction that assumes that the (uniform) Beta(1, 1) distribution is (bell-shaped) Beta(3, 3) rather than the other way around. In this restricted sense, the Kullback divergence is consistent with the second law of thermodynamics.
The Kullback–Leibler divergence is symmetric DKL(X1 || X2) = DKL(X2 || X1) for the skewed cases Beta(3, 0.5) and Beta(0.5, 3) that have equal differential entropy h(X1) = h(X2).
The symmetry condition:

D

K
L

(

X

1

∥

X

2

)
=

D

K
L

(

X

2

∥

X

1

)
,

 if 

h
(

X

1

)
=
h
(

X

2

)
,

 for (skewed) 
{\displaystyle D_{\mathrm {KL} }(X_{1}\parallel X_{2})=D_{\mathrm {KL} }(X_{2}\parallel X_{1}),{\text{ if }}h(X_{1})=h(X_{2}),{\text{ for (skewed) }}\alpha \neq \beta }

follows from the above definitions and the mirror-symmetry f(x; α, β) = f(1 − x; α, β) enjoyed by the beta distribution.

Relationships between statistical measures[edit]
Mean, mode and median relationship[edit]
If 1 < α < β then mode ≤ median ≤ mean.[10] Expressing the mode (only for α, β > 1), and the mean in terms of α and β:

α
−
1

α
+
β
−
2

≤

median
{\displaystyle {\frac {\alpha -1}{\alpha +\beta -2}}\leq {\text{median}}\leq {\frac {\alpha }{\alpha +\beta }},}

If 1 < β < α then the order of the inequalities are reversed. For α, β > 1 the absolute distance between the mean and the median is less than 5% of the distance between the maximum and minimum values of x. On the other hand, the absolute distance between the mean and the mode can reach 50% of the distance between the maximum and minimum values of x, for the (pathological) case of α = 1 and β = 1, for which values the beta distribution approaches the uniform distribution and the differential entropy approaches its maximum value, and hence maximum "disorder".
For example, for α = 1.0001 and β = 1.00000001:

mode   = 0.9999;   PDF(mode) = 1.00010
mean   = 0.500025; PDF(mean) = 1.00003
median = 0.500035; PDF(median) = 1.00003
mean − mode   = −0.499875
mean − median = −9.65538 × 10−6
where PDF stands for the value of the probability density function.

Mean, geometric mean and harmonic mean relationship[edit]
:Mean, median, geometric mean and harmonic mean for beta distribution with 0 < α = β < 5
It is known from the inequality of arithmetic and geometric means that the geometric mean is lower than the mean.  Similarly, the harmonic mean is lower than the geometric mean.  The accompanying plot shows that for α = β, both the mean and the median are exactly equal to 1/2, regardless of the value of α = β, and the mode is also equal to 1/2 for α = β > 1, however the geometric and harmonic means are lower than 1/2 and they only approach this value asymptotically as α = β → ∞.

Kurtosis bounded by the square of the skewness[edit]
Beta distribution α and β parameters vs. excess kurtosis and squared skewness
As remarked by Feller,[5] in the Pearson system the beta probability density appears as type I (any difference between the beta distribution and Pearson's type I distribution is only superficial and it makes no difference for the following discussion regarding the relationship between kurtosis and skewness). Karl Pearson showed, in Plate 1 of his paper [21]  published in 1916,  a graph with the kurtosis as the vertical axis (ordinate) and the square of the skewness as the horizontal axis (abscissa), in which a number of distributions were displayed.[31]  The region occupied by the beta distribution is bounded by the following two lines in the (skewness2,kurtosis) plane, or the (skewness2,excess kurtosis) plane:

(

skewness

)

2

+
1
<

kurtosis

<

3
2

(

skewness
{\displaystyle ({\text{skewness}})^{2}+1<{\text{kurtosis}}<{\frac {3}{2}}({\text{skewness}})^{2}+3}

or, equivalently,

(

skewness

)

2

−
2
<

excess kurtosis

<

3
2

(

skewness
{\displaystyle ({\text{skewness}})^{2}-2<{\text{excess kurtosis}}<{\frac {3}{2}}({\text{skewness}})^{2}}

At a time when there were no powerful digital computers, Karl Pearson accurately computed further boundaries,[32][21] for example, separating the "U-shaped" from the "J-shaped" distributions. The lower boundary line (excess kurtosis + 2 − skewness2 = 0) is produced by skewed "U-shaped" beta distributions with both values of shape parameters α and β close to zero.  The upper boundary line (excess kurtosis − (3/2) skewness2 = 0) is produced by extremely skewed distributions with very large values of one of the parameters and very small values of the other parameter.  Karl Pearson showed[21] that this upper boundary line (excess kurtosis − (3/2) skewness2 = 0) is also the intersection with Pearson's distribution III, which has unlimited support in one direction (towards positive infinity), and can be bell-shaped or J-shaped. His son, Egon Pearson, showed[31] that the region (in the kurtosis/squared-skewness plane) occupied by the beta distribution (equivalently, Pearson's distribution I) as it approaches this boundary (excess kurtosis − (3/2) skewness2 = 0) is shared with the noncentral chi-squared distribution.  Karl Pearson[33] (Pearson 1895, pp. 357, 360, 373–376) also showed that the gamma distribution is a Pearson type III distribution. Hence this boundary line for Pearson's type III distribution is known as the gamma line. (This can be shown from the fact that the excess kurtosis of the gamma distribution is 6/k and the square of the skewness is 4/k, hence (excess kurtosis − (3/2) skewness2 = 0) is identically satisfied by the gamma distribution regardless of the value of the parameter "k"). Pearson later noted that the chi-squared distribution is a special case of Pearson's type III and also shares this boundary line (as it is apparent from the fact that for the chi-squared distribution the excess kurtosis is 12/k and the square of the skewness is 8/k, hence (excess kurtosis − (3/2) skewness2 = 0) is identically satisfied regardless of the value of the parameter "k"). This is to be expected, since the chi-squared distribution X ~ χ2(k) is a special case of the gamma distribution, with parametrization X ~ Γ(k/2, 1/2) where k is a positive integer that specifies the "number of degrees of freedom" of the chi-squared distribution.
An example of a beta distribution near the upper boundary (excess kurtosis − (3/2) skewness2 = 0) is given by α = 0.1, β = 1000, for which the ratio (excess kurtosis)/(skewness2) = 1.49835 approaches the upper limit of 1.5 from below. An example of a beta distribution near the lower boundary (excess kurtosis + 2 − skewness2 = 0) is given by α= 0.0001, β = 0.1, for which values the expression (excess kurtosis + 2)/(skewness2) = 1.01621 approaches the lower limit of 1 from above. In the infinitesimal limit for both α and β approaching zero symmetrically, the excess kurtosis reaches its minimum value at −2.  This minimum value occurs at the point at which the lower boundary line intersects the vertical axis (ordinate). (However, in Pearson's original chart, the ordinate is kurtosis, instead of excess kurtosis, and it increases downwards rather than upwards).
Values for the skewness and excess kurtosis below the lower boundary (excess kurtosis + 2 − skewness2 = 0) cannot occur for any distribution, and hence Karl Pearson appropriately called the region below this boundary the "impossible region". The boundary for this "impossible region" is determined by (symmetric or skewed) bimodal U-shaped distributions for which the parameters α and β approach zero and hence all the probability density is concentrated at the ends: x = 0, 1 with practically nothing in between them. Since for α ≈ β ≈ 0 the probability density is concentrated at the two ends x = 0 and x = 1, this "impossible boundary" is determined by a Bernoulli distribution, where the two only possible outcomes occur with respective probabilities p and q = 1 − p. For cases approaching this limit boundary with symmetry α = β, skewness ≈ 0, excess kurtosis ≈ −2 (this is the lowest excess kurtosis possible for any distribution), and the probabilities are p ≈ q ≈ 1/2.  For cases approaching this limit boundary with skewness, excess kurtosis ≈ −2 + skewness2, and the probability density is concentrated more at one end than the other end (with practically nothing in between), with probabilities 
{\displaystyle p={\tfrac {\beta }{\alpha +\beta }}}

 at the left end x = 0 and 
{\displaystyle q=1-p={\tfrac {\alpha }{\alpha +\beta }}}

 at the right end x = 1.

Symmetry[edit]
All statements are conditional on α, β > 0:

Probability density function reflection symmetry 
{\displaystyle f(x;\alpha ,\beta )=f(1-x;\beta ,\alpha )}

Cumulative distribution function reflection symmetry plus unitary translation 
{\displaystyle F(x;\alpha ,\beta )=I_{x}(\alpha ,\beta )=1-F(1-x;\beta ,\alpha )=1-I_{1-x}(\beta ,\alpha )}

Mode reflection symmetry plus unitary translation 

mode
⁡
(

B

(
α
,
β
)
)
=
1
−
mode
{\displaystyle \operatorname {mode} (\mathrm {B} (\alpha ,\beta ))=1-\operatorname {mode} (\mathrm {B} (\beta ,\alpha )),{\text{ if }}\mathrm {B} (\beta ,\alpha )\neq \mathrm {B} (1,1)}

Median reflection symmetry plus unitary translation 

median
⁡
(

B

(
α
,
β
)
)
=
1
−
median
{\displaystyle \operatorname {median} (\mathrm {B} (\alpha ,\beta ))=1-\operatorname {median} (\mathrm {B} (\beta ,\alpha ))}

Mean reflection symmetry plus unitary translation 
{\displaystyle \mu (\mathrm {B} (\alpha ,\beta ))=1-\mu (\mathrm {B} (\beta ,\alpha ))}

Geometric means each is individually asymmetric, the following symmetry applies between the geometric mean based on X and the geometric mean based on its reflection 1−X 
{\displaystyle G_{X}(\mathrm {B} (\alpha ,\beta ))=G_{1-X}(\mathrm {B} (\beta ,\alpha ))}

Harmonic means each is individually asymmetric, the following symmetry applies between the harmonic mean based on X and the harmonic mean based on its reflection 1−X 
{\displaystyle H_{X}(\mathrm {B} (\alpha ,\beta ))=H_{1-X}(\mathrm {B} (\beta ,\alpha )){\text{ if }}\alpha ,\beta >1.}

Variance symmetry 
{\displaystyle \operatorname {var} (\mathrm {B} (\alpha ,\beta ))=\operatorname {var} (\mathrm {B} (\beta ,\alpha ))}

Geometric variances each is individually asymmetric, the following symmetry applies between the log geometric variance based on X and the log geometric variance based on its reflection 1−X 
{\displaystyle \ln(\operatorname {var} _{GX}(\mathrm {B} (\alpha ,\beta )))=\ln(\operatorname {var} _{G(1-X)}(\mathrm {B} (\beta ,\alpha )))}

Geometric covariance symmetry 
{\displaystyle \ln \operatorname {cov} _{GX,(1-X)}(\mathrm {B} (\alpha ,\beta ))=\ln \operatorname {cov} _{GX,(1-X)}(\mathrm {B} (\beta ,\alpha ))}

Mean absolute deviation around the mean symmetry 
{\displaystyle \operatorname {E} [|X-E[X]|](\mathrm {B} (\alpha ,\beta ))=\operatorname {E} [|X-E[X]|](\mathrm {B} (\beta ,\alpha ))}

Skewness skew-symmetry 

skewness
⁡
(

B

(
α
,
β
)
)
=
−
skewness
{\displaystyle \operatorname {skewness} (\mathrm {B} (\alpha ,\beta ))=-\operatorname {skewness} (\mathrm {B} (\beta ,\alpha ))}

Excess kurtosis symmetry 

excess kurtosis

(

B

(
α
,
β
)
)
=

excess kurtosis
{\displaystyle {\text{excess kurtosis}}(\mathrm {B} (\alpha ,\beta ))={\text{excess kurtosis}}(\mathrm {B} (\beta ,\alpha ))}

Characteristic function symmetry of Real part (with respect to the origin of variable "t") 
{\displaystyle {\text{Re}}[{}_{1}F_{1}(\alpha ;\alpha +\beta ;it)]={\text{Re}}[{}_{1}F_{1}(\alpha ;\alpha +\beta ;-it)]}

Characteristic function skew-symmetry of Imaginary part (with respect to the origin of variable "t") 
{\displaystyle {\text{Im}}[{}_{1}F_{1}(\alpha ;\alpha +\beta ;it)]=-{\text{Im}}[{}_{1}F_{1}(\alpha ;\alpha +\beta ;-it)]}

Characteristic function symmetry of Absolute value (with respect to the origin of variable "t") 
{\displaystyle {\text{Abs}}[{}_{1}F_{1}(\alpha ;\alpha +\beta ;it)]={\text{Abs}}[{}_{1}F_{1}(\alpha ;\alpha +\beta ;-it)]}

Differential entropy symmetry 
{\displaystyle h(\mathrm {B} (\alpha ,\beta ))=h(\mathrm {B} (\beta ,\alpha ))}

Relative entropy (also called Kullback–Leibler divergence) symmetry 

D

K
L

(

X

1

∥

X

2

)
=

D

K
L

(

X

2

∥

X

1

)
,

 if 

h
(

X

1

)
=
h
(

X

2

)

, for (skewed) 
{\displaystyle D_{\mathrm {KL} }(X_{1}\parallel X_{2})=D_{\mathrm {KL} }(X_{2}\parallel X_{1}),{\text{ if }}h(X_{1})=h(X_{2}){\text{, for (skewed) }}\alpha \neq \beta }

Fisher information matrix symmetry 
{\displaystyle {\mathcal {I}}_{i,j}={\mathcal {I}}_{j,i}}

Geometry of the probability density function[edit]
Inflection points[edit]
Inflection point location versus α and β showing regions with one inflection point
Inflection point location versus α and β showing region with two inflection points
For certain values of the shape parameters α and β, the probability density function has inflection points, at which the curvature changes sign.  The position of these inflection points can be useful as a measure of the dispersion or spread of the distribution.
Defining the following quantity:
{\displaystyle \kappa ={\frac {\sqrt {\frac {(\alpha -1)(\beta -1)}{\alpha +\beta -3}}}{\alpha +\beta -2}}}

Points of inflection occur,[1][8][9][20] depending on the value of the shape parameters α and β, as follows:

(α > 2, β > 2) The distribution is bell-shaped (symmetric for α = β and skewed otherwise), with two inflection points, equidistant from the mode:

x
=

mode
{\displaystyle x={\text{mode}}\pm \kappa ={\frac {\alpha -1\pm {\sqrt {\frac {(\alpha -1)(\beta -1)}{\alpha +\beta -3}}}}{\alpha +\beta -2}}}

(α = 2, β > 2) The distribution is unimodal, positively skewed, right-tailed, with one inflection point, located to the right of the mode:

x
=

mode
{\displaystyle x={\text{mode}}+\kappa ={\frac {2}{\beta }}}

(α > 2, β = 2) The distribution is unimodal, negatively skewed, left-tailed, with one inflection point, located to the left of the mode:

x
=

mode
{\displaystyle x={\text{mode}}-\kappa =1-{\frac {2}{\alpha }}}

(1 < α < 2, β > 2, α + β > 2) The distribution is unimodal, positively skewed, right-tailed, with one inflection point, located to the right of the mode:

x
=

mode
{\displaystyle x={\text{mode}}+\kappa ={\frac {\alpha -1+{\sqrt {\frac {(\alpha -1)(\beta -1)}{\alpha +\beta -3}}}}{\alpha +\beta -2}}}

(0 < α < 1, 1 < β < 2) The distribution has a mode at the left end x = 0 and it is positively skewed, right-tailed. There is one inflection point, located to the right of the mode:
{\displaystyle x={\frac {\alpha -1+{\sqrt {\frac {(\alpha -1)(\beta -1)}{\alpha +\beta -3}}}}{\alpha +\beta -2}}}

(α > 2, 1 < β < 2) The distribution is unimodal negatively skewed, left-tailed, with one inflection point, located to the left of the mode:

x
=

mode
{\displaystyle x={\text{mode}}-\kappa ={\frac {\alpha -1-{\sqrt {\frac {(\alpha -1)(\beta -1)}{\alpha +\beta -3}}}}{\alpha +\beta -2}}}

(1 < α < 2,  0 < β < 1) The distribution has a mode at the right end x = 1 and it is negatively skewed, left-tailed. There is one inflection point, located to the left of the mode:
{\displaystyle x={\frac {\alpha -1-{\sqrt {\frac {(\alpha -1)(\beta -1)}{\alpha +\beta -3}}}}{\alpha +\beta -2}}}

There are no inflection points in the remaining (symmetric and skewed) regions: U-shaped: (α, β < 1) upside-down-U-shaped: (1 < α < 2, 1 < β < 2), reverse-J-shaped (α < 1, β > 2) or J-shaped: (α > 2, β < 1)
The accompanying plots show the inflection point locations (shown vertically, ranging from 0 to 1) versus α and β (the horizontal axes ranging from 0 to 5). There are large cuts at surfaces intersecting the lines α = 1, β = 1, α = 2, and β = 2 because at these values the beta distribution change from 2 modes, to 1 mode to no mode.

Shapes[edit]
PDF for symmetric beta distribution vs. x and α = β from 0 to 30
PDF for symmetric beta distribution vs. x and α = β from 0 to 2
PDF for skewed beta distribution vs. x and β = 2.5α from 0 to 9
PDF for skewed beta distribution vs. x and β = 5.5α from 0 to 9
PDF for skewed beta distribution vs. x and β = 8α from 0 to 10
The beta density function can take a wide variety of different shapes depending on the values of the two parameters α and β.  The ability of the beta distribution to take this great diversity of shapes (using only two parameters) is partly responsible for finding wide application for modeling actual measurements:

Symmetric (α = β)[edit]
the density function is symmetric about 1/2 (blue & teal plots).
median = mean = 1/2.
skewness  = 0.
variance = 1/(4(2α + 1))
α = β < 1
U-shaped (blue plot).
bimodal: left mode = 0,  right mode =1, anti-mode = 1/2
1/12 < var(X) < 1/4[1]
−2 < excess kurtosis(X) < −6/5
α = β = 1/2 is the arcsine distribution
var(X) = 1/8
excess kurtosis(X) = −3/2
CF = Rinc (t) [34]
α = β → 0 is a 2-point Bernoulli distribution with equal probability 1/2 at each Dirac delta function end x = 0 and x = 1 and zero probability everywhere else. A coin toss: one face of the coin being x = 0 and the other face being x = 1.
{\displaystyle \lim _{\alpha =\beta \to 0}\operatorname {var} (X)={\tfrac {1}{4}}}
{\displaystyle \lim _{\alpha =\beta \to 0}\operatorname {excess\ kurtosis} (X)=-2}

  a lower value than this is impossible for any distribution to reach.
The differential entropy approaches a minimum value of −∞
α = β = 1
the uniform [0, 1] distribution
no mode
var(X) = 1/12
excess kurtosis(X) = −6/5
The (negative anywhere else) differential entropy reaches its maximum value of zero
CF = Sinc (t)
α = β > 1
symmetric unimodal
mode = 1/2.
0 < var(X) < 1/12[1]
−6/5 < excess kurtosis(X) < 0
α = β = 3/2 is a semi-elliptic [0, 1] distribution, see: Wigner semicircle distribution[35]
var(X) = 1/16.
excess kurtosis(X) = −1
CF = 2 Jinc (t)
α = β = 2 is the parabolic [0, 1] distribution
var(X) = 1/20
excess kurtosis(X) = −6/7
CF = 3 Tinc (t) [36]
α = β > 2 is bell-shaped, with inflection points located to either side of the mode
0 < var(X) < 1/20
−6/7 < excess kurtosis(X) < 0
α = β → ∞ is a 1-point Degenerate distribution with a Dirac delta function spike at the midpoint x = 1/2 with probability 1, and zero probability everywhere else. There is 100% probability (absolute certainty) concentrated at the single point x = 1/2.
{\displaystyle \lim _{\alpha =\beta \to \infty }\operatorname {var} (X)=0}
{\displaystyle \lim _{\alpha =\beta \to \infty }\operatorname {excess\ kurtosis} (X)=0}

The differential entropy approaches a minimum value of −∞
Skewed (α ≠ β)[edit]
The density function is skewed.  An interchange of parameter values yields the mirror image (the reverse) of the initial curve, some more specific cases:

α < 1, β < 1
U-shaped
Positive skew for α < β, negative skew for α > β.
bimodal: left mode = 0, right mode = 1,  anti-mode = 
{\displaystyle {\tfrac {\alpha -1}{\alpha +\beta -2}}}

0 < median < 1.
0 < var(X) < 1/4
α > 1, β > 1
unimodal (magenta & cyan plots),
Positive skew for α < β, negative skew for α > β.

mode
{\displaystyle {\text{mode}}={\tfrac {\alpha -1}{\alpha +\beta -2}}}

0 < median < 1
0 < var(X) < 1/12
α < 1, β ≥ 1
reverse J-shaped with a right tail,
positively skewed,
strictly decreasing, convex
mode = 0
0 < median < 1/2.
{\displaystyle 0<\operatorname {var} (X)<{\tfrac {-11+5{\sqrt {5}}}{2}},}

 (maximum variance occurs for 
{\displaystyle \alpha ={\tfrac {-1+{\sqrt {5}}}{2}},\beta =1}

, or α = Φ the golden ratio conjugate)
α ≥ 1, β < 1
J-shaped with a left tail,
negatively skewed,
strictly increasing, convex
mode = 1
1/2 < median < 1
{\displaystyle 0<\operatorname {var} (X)<{\tfrac {-11+5{\sqrt {5}}}{2}},}

 (maximum variance occurs for 
{\displaystyle \alpha =1,\beta ={\tfrac {-1+{\sqrt {5}}}{2}}}

, or β = Φ the golden ratio conjugate)
α = 1, β > 1
positively skewed,
strictly decreasing (red plot),
a reversed (mirror-image) power function distribution
mean = 1 / (β + 1)
median = 1 - 1/21/β
mode = 0
α = 1, 1 < β < 2
concave

1
−

1

2

<

median
{\displaystyle 1-{\tfrac {1}{\sqrt {2}}}<{\text{median}}<{\tfrac {1}{2}}}

1/18 < var(X) < 1/12.
α = 1, β = 2
a straight line with slope −2, the right-triangular distribution with right angle at the left end, at x = 0

median
{\displaystyle {\text{median}}=1-{\tfrac {1}{\sqrt {2}}}}

var(X) = 1/18
α = 1, β > 2
reverse J-shaped with a right tail,
convex

0
<

median
{\displaystyle 0<{\text{median}}<1-{\tfrac {1}{\sqrt {2}}}}

0 < var(X) < 1/18
α > 1, β = 1
negatively skewed,
strictly increasing (green plot),
the power function distribution[9]
mean = α / (α + 1)
median = 1/21/α 
mode = 1
2 > α > 1, β = 1
concave

1
2

<

median
{\displaystyle {\tfrac {1}{2}}<{\text{median}}<{\tfrac {1}{\sqrt {2}}}}

1/18 < var(X) < 1/12
α = 2, β = 1
a straight line with slope +2, the right-triangular distribution with right angle at the right end, at x = 1

median
{\displaystyle {\text{median}}={\tfrac {1}{\sqrt {2}}}}

var(X) = 1/18
α > 2, β = 1
J-shaped with a left tail, convex

1

2

<

median
{\displaystyle {\tfrac {1}{\sqrt {2}}}<{\text{median}}<1}

0 < var(X) < 1/18
Related distributions[edit]
Transformations[edit]
If X ~ Beta(α, β) then 1 − X ~ Beta(β, α) mirror-image symmetry
If X ~ Beta(α, β) then 
{\displaystyle {\tfrac {X}{1-X}}\sim {\beta '}(\alpha ,\beta )}

. The beta prime distribution, also called "beta distribution of the second kind".
If 

X
∼

Beta
{\displaystyle X\sim {\text{Beta}}(\alpha ,\beta )}

, then 
{\displaystyle Y=\log {\frac {X}{1-X}}}

 has a generalized logistic distribution, with density 
{\displaystyle {\frac {\sigma (y)^{\alpha }\sigma (-y)^{\beta }}{B(\alpha ,\beta )}}}

, where 

σ

{\displaystyle \sigma }

 is the logistic sigmoid.
If X ~ Beta(α, β) then 
{\displaystyle {\tfrac {1}{X}}-1\sim {\beta '}(\beta ,\alpha )}

.
If 

X
∼

Beta
{\displaystyle X\sim {\text{Beta}}(\alpha _{1},\beta _{1})}

 and 

Y
∼

Beta
{\displaystyle Y\sim {\text{Beta}}(\alpha _{2},\beta _{2})}

 then 
{\displaystyle Z={\tfrac {X}{Y}}}

 has density 
{\displaystyle {\tfrac {B(\alpha _{1}+\alpha _{2},\beta _{2})z^{\alpha _{1}-1}{}_{2}F_{1}(\alpha _{1}+\alpha _{2},1-\beta _{1};\alpha _{1}+\alpha _{2}+\beta _{2};z)}{B(\alpha _{1},\beta _{1})B(\alpha _{2},\beta _{2})}}}
{\displaystyle 0<z\leq 1}
{\displaystyle {\tfrac {B(\alpha _{1}+\alpha _{2},\beta _{1})z^{-(\alpha _{2}+1)}{}_{2}F_{1}(\alpha _{1}+\alpha _{2},1-\beta _{2};\alpha _{1}+\alpha _{2}+\beta _{1};{\tfrac {1}{z}})}{B(\alpha _{1},\beta _{1})B(\alpha _{2},\beta _{2})}}}
{\displaystyle z\geq 1}

, where 
{\displaystyle {}_{2}F_{1}(a,b;c;x)}

 is the Hypergeometric function.[37]
If X ~ Beta(n/2, m/2) then 
{\displaystyle {\tfrac {mX}{n(1-X)}}\sim F(n,m)}

 (assuming n > 0 and m > 0), the Fisher–Snedecor F distribution.
If 

X
∼
Beta
{\displaystyle X\sim \operatorname {Beta} \left(1+\lambda {\tfrac {m-\min }{\max -\min }},1+\lambda {\tfrac {\max -m}{\max -\min }}\right)}

 then min + X(max − min) ~ PERT(min, max, m, λ) where PERT denotes a PERT distribution used in PERT analysis, and m=most likely value.[38] Traditionally[39] λ = 4 in PERT analysis.
If X ~ Beta(1, β) then X ~ Kumaraswamy distribution with parameters (1, β)
If X ~ Beta(α, 1) then X ~ Kumaraswamy distribution with parameters (α, 1)
If X ~ Beta(α, 1) then −ln(X) ~ Exponential(α)
Special and limiting cases[edit]
Example of eight realizations of a random walk in one dimension starting at 0: the probability for the time of the last visit to the origin is distributed as Beta(1/2, 1/2)
Beta(1/2, 1/2): The arcsine distribution probability density was proposed by Harold Jeffreys to represent uncertainty for a Bernoulli or a binomial distribution in Bayesian inference, and is now commonly referred to as Jeffreys prior: p−1/2(1 − p)−1/2. This distribution also appears in several random walk fundamental theorems
Beta(1, 1) ~ U(0, 1) with density 1 on that interval.
Beta(n, 1) ~ Maximum of n independent rvs. with U(0, 1), sometimes called a a standard power function distribution with density n xn–1 on that interval.
Beta(1, n) ~ Minimum of n independent rvs. with U(0, 1) with density n(1 − x)n−1 on that interval.
If X ~ Beta(3/2, 3/2) and r > 0 then 2rX − r ~ Wigner semicircle distribution.
Beta(1/2, 1/2) is equivalent to the arcsine distribution. This distribution is also Jeffreys prior probability for the Bernoulli and  binomial distributions.

lim

n
→
∞

n
Beta
⁡
(
1
,
n
)
=
Exponential
{\displaystyle \lim _{n\to \infty }n\operatorname {Beta} (1,n)=\operatorname {Exponential} (1)}

  the exponential distribution.

lim

n
→
∞

n
Beta
⁡
(
k
,
n
)
=
Gamma
{\displaystyle \lim _{n\to \infty }n\operatorname {Beta} (k,n)=\operatorname {Gamma} (k,1)}

 the gamma distribution.
For large 

n

{\displaystyle n}

, 

Beta
{\displaystyle \operatorname {Beta} (\alpha n,\beta n)\to {\mathcal {N}}\left({\frac {\alpha }{\alpha +\beta }},{\frac {\alpha \beta }{(\alpha +\beta )^{3}}}{\frac {1}{n}}\right)}

 the normal distribution. More precisely, if 

X

n

∼
Beta
{\displaystyle X_{n}\sim \operatorname {Beta} (\alpha n,\beta n)}

 then  
{\displaystyle {\sqrt {n}}\left(X_{n}-{\tfrac {\alpha }{\alpha +\beta }}\right)}

 converges in distribution to a normal distribution with mean 0 and variance 
{\displaystyle {\tfrac {\alpha \beta }{(\alpha +\beta )^{3}}}}

 as n increases.
Derived from other distributions[edit]
The kth order statistic of a sample of size n from the uniform distribution is a beta random variable, U(k) ~ Beta(k, n+1−k).[40]
Gamma distribution: If X ~ Gamma(α, θ) and Y ~ Gamma(β, θ) are independent, then 

X

X
+
Y

∼
Beta
{\displaystyle {\tfrac {X}{X+Y}}\sim \operatorname {Beta} (\alpha ,\beta )\,}

.
Chi-squared distribution: If 
{\displaystyle X\sim \chi ^{2}(\alpha )\,}
{\displaystyle Y\sim \chi ^{2}(\beta )\,}

 are independent, then 

X

X
+
Y

∼
Beta
{\displaystyle {\tfrac {X}{X+Y}}\sim \operatorname {Beta} ({\tfrac {\alpha }{2}},{\tfrac {\beta }{2}})}

.
The power transformation for the uniform distribution: If X ~ U(0, 1) and α > 0 then X1/α ~ Beta(α, 1).
Cauchy distribution: If X ~ Cauchy(0, 1) then 

1

1
+

X

2

∼
Beta
{\displaystyle {\tfrac {1}{1+X^{2}}}\sim \operatorname {Beta} \left({\tfrac {1}{2}},{\tfrac {1}{2}}\right)\,}

Combination with other distributions[edit]
X ~ Beta(α, β) and Y ~ F(2β,2α) then  
{\displaystyle \Pr(X\leq {\tfrac {\alpha }{\alpha +\beta x}})=\Pr(Y\geq x)\,}

 for all x > 0.
Compounding with other distributions[edit]
If p ~ Beta(α, β) and X ~ Bin(k, p) then X ~ beta-binomial distribution
If p ~ Beta(α, β) and X ~ NB(r, p) then X ~ beta negative binomial distribution
Generalisations[edit]
The generalization to multiple variables, i.e. a multivariate Beta distribution, is called a Dirichlet distribution. Univariate marginals of the Dirichlet distribution have a beta distribution.  The beta distribution is conjugate to the binomial and Bernoulli distributions in exactly the same way as the Dirichlet distribution is conjugate to the multinomial distribution and categorical distribution.
The Pearson type I distribution is identical to the beta distribution (except for arbitrary shifting and re-scaling that can also be accomplished with the four parameter parametrization of the beta distribution).
The beta distribution is the special case of the noncentral beta distribution where 
{\displaystyle \lambda =0}

: 

Beta
⁡
(
α
,
β
)
=
NonCentralBeta
{\displaystyle \operatorname {Beta} (\alpha ,\beta )=\operatorname {NonCentralBeta} (\alpha ,\beta ,0)}

.
The generalized beta distribution is a five-parameter distribution family which has the beta distribution as a special case.
The matrix variate beta distribution is a distribution for positive-definite matrices.
Statistical inference[edit]
Parameter estimation[edit]
Method of moments[edit]
Two unknown parameters[edit]
Two unknown parameters (
{\displaystyle ({\hat {\alpha }},{\hat {\beta }})}

  of a beta distribution supported in the [0,1] interval) can be estimated, using the method of moments, with the first two moments (sample mean and sample variance) as follows.  Let:

sample mean(X)
{\displaystyle {\text{sample mean(X)}}={\bar {x}}={\frac {1}{N}}\sum _{i=1}^{N}X_{i}}

be the sample mean estimate and

sample variance(X)
{\displaystyle {\text{sample variance(X)}}={\bar {v}}={\frac {1}{N-1}}\sum _{i=1}^{N}\left(X_{i}-{\bar {x}}\right)^{2}}

be the sample variance estimate.  The method-of-moments estimates of the parameters are
{\displaystyle {\hat {\alpha }}={\bar {x}}\left({\frac {{\bar {x}}(1-{\bar {x}})}{\bar {v}}}-1\right)\ {\text{if}}\ {\bar {v}}<{\bar {x}}(1-{\bar {x}}),}
{\displaystyle {\hat {\beta }}=(1-{\bar {x}})\left({\frac {{\bar {x}}(1-{\bar {x}})}{\bar {v}}}-1\right)\ {\text{if}}\ {\bar {v}}<{\bar {x}}(1-{\bar {x}}).}

When the distribution is required over a known interval other than [0, 1] with random variable X, say [a, c] with random variable Y, then replace 
{\displaystyle {\bar {x}}}

 with 
{\displaystyle {\frac {{\bar {y}}-a}{c-a}},}
{\displaystyle {\bar {v}}}

 with 
{\displaystyle {\frac {\bar {v_{Y}}}{(c-a)^{2}}}}

 in the above couple of equations for the shape parameters (see the "Four unknown parameters" section below),[41] where:

sample mean(Y)
{\displaystyle {\text{sample mean(Y)}}={\bar {y}}={\frac {1}{N}}\sum _{i=1}^{N}Y_{i}}

sample variance(Y)
{\displaystyle {\text{sample variance(Y)}}={\bar {v}}_{Y}={\frac {1}{N-1}}\sum _{i=1}^{N}\left(Y_{i}-{\bar {y}}\right)^{2}}

Four unknown parameters[edit]
Solutions for parameter estimates vs. (sample) excess Kurtosis and (sample) squared Skewness Beta distribution
All four parameters (
{\displaystyle {\hat {\alpha }},{\hat {\beta }},{\hat {a}},{\hat {c}}}

 of a beta distribution supported in the [a, c] interval, see section "Alternative parametrizations, Four parameters") can be estimated, using the method of moments developed by Karl Pearson, by equating sample and population values of the first four central moments (mean, variance, skewness and excess kurtosis).[1][42][43] The excess kurtosis was expressed in terms of the square of the skewness, and the sample size ν = α + β, (see previous section "Kurtosis") as follows:

excess kurtosis

=

6

3
+
ν

(

(
2
+
ν
)

4

(

skewness

)

2

−
1

)

 if (skewness)

2

−
2
<

excess kurtosis

<

3
2

(

skewness
{\displaystyle {\text{excess kurtosis}}={\frac {6}{3+\nu }}\left({\frac {(2+\nu )}{4}}({\text{skewness}})^{2}-1\right){\text{ if (skewness)}}^{2}-2<{\text{excess kurtosis}}<{\tfrac {3}{2}}({\text{skewness}})^{2}}

One can use this equation to solve for the sample size ν= α + β in terms of the square of the skewness and the excess kurtosis as follows:[42]

ν
^

=

α
^

+

β
^

=
3

(

sample excess kurtosis

)
−
(

sample skewness

)

2

+
2

3
2

(

sample skewness

)

2

−

(sample excess kurtosis)

{\displaystyle {\hat {\nu }}={\hat {\alpha }}+{\hat {\beta }}=3{\frac {({\text{sample excess kurtosis}})-({\text{sample skewness}})^{2}+2}{{\frac {3}{2}}({\text{sample skewness}})^{2}-{\text{(sample excess kurtosis)}}}}}

 if (sample skewness)

2

−
2
<

sample excess kurtosis

<

3
2

(

sample skewness
{\displaystyle {\text{ if (sample skewness)}}^{2}-2<{\text{sample excess kurtosis}}<{\tfrac {3}{2}}({\text{sample skewness}})^{2}}

This is the ratio (multiplied by a factor of 3) between the previously derived limit boundaries for the beta distribution in a space (as originally done by Karl Pearson[21]) defined with coordinates of the square of the skewness in one axis and the excess kurtosis in the other axis (see § Kurtosis bounded by the square of the skewness):
The case of zero skewness, can be immediately solved because for zero skewness, α = β and hence ν = 2α = 2β, therefore α = β = ν/2

α
^

=

β
^

=

ν
^

2

=

3
2

(

sample excess kurtosis

)
+
3

−

(sample excess kurtosis)

{\displaystyle {\hat {\alpha }}={\hat {\beta }}={\frac {\hat {\nu }}{2}}={\frac {{\frac {3}{2}}({\text{sample excess kurtosis}})+3}{-{\text{(sample excess kurtosis)}}}}}

 if sample skewness

=
0

 and 

−
2
<

sample excess kurtosis
{\displaystyle {\text{ if sample skewness}}=0{\text{ and }}-2<{\text{sample excess kurtosis}}<0}

(Excess kurtosis is negative for the beta distribution with zero skewness, ranging from -2 to 0, so that 
{\displaystyle {\hat {\nu }}}

 -and therefore the sample shape parameters- is positive, ranging from zero when the shape parameters approach zero and the excess kurtosis approaches -2, to infinity when the shape parameters approach infinity and the excess kurtosis approaches zero).
For non-zero sample skewness one needs to solve a system of two coupled equations. Since the skewness and the excess kurtosis are independent of the parameters 
{\displaystyle {\hat {a}},{\hat {c}}}

, the parameters 
{\displaystyle {\hat {\alpha }},{\hat {\beta }}}

 can be uniquely determined from the sample skewness and the sample excess kurtosis, by solving the coupled equations with two known variables (sample skewness and sample excess kurtosis) and two unknowns (the shape parameters):

(

sample skewness
{\displaystyle ({\text{sample skewness}})^{2}={\frac {4\left({\hat {\beta }}-{\hat {\alpha }}\right)^{2}\left(1+{\hat {\alpha }}+{\hat {\beta }}\right)}{{\hat {\alpha }}{\hat {\beta }}\left(2+{\hat {\alpha }}+{\hat {\beta }}\right)^{2}}}}

sample excess kurtosis

=

6

3
+

α
^

+

β
^

(

(
2
+

α
^

+

β
^

)

4

(

sample skewness
{\displaystyle {\text{sample excess kurtosis}}={\frac {6}{3+{\hat {\alpha }}+{\hat {\beta }}}}\left({\frac {(2+{\hat {\alpha }}+{\hat {\beta }})}{4}}({\text{sample skewness}})^{2}-1\right)}

 if (sample skewness)

2

−
2
<

sample excess kurtosis

<

3
2

(

sample skewness
{\displaystyle {\text{ if (sample skewness)}}^{2}-2<{\text{sample excess kurtosis}}<{\tfrac {3}{2}}({\text{sample skewness}})^{2}}

resulting in the following solution:[42]

α
^

,

β
^

=

ν
^

2

(

1
±

1

1
+

16
(

ν
^

+
1
)

(

ν
^

+
2

)

2

(

sample skewness
{\displaystyle {\hat {\alpha }},{\hat {\beta }}={\frac {\hat {\nu }}{2}}\left(1\pm {\frac {1}{\sqrt {1+{\frac {16({\hat {\nu }}+1)}{({\hat {\nu }}+2)^{2}({\text{sample skewness}})^{2}}}}}}\right)}

 if sample skewness

≠
0

 and 

(

sample skewness

)

2

−
2
<

sample excess kurtosis

<

3
2

(

sample skewness
{\displaystyle {\text{ if sample skewness}}\neq 0{\text{    and   }}({\text{sample skewness}})^{2}-2<{\text{sample excess kurtosis}}<{\tfrac {3}{2}}({\text{sample skewness}})^{2}}

Where one should take the solutions as follows: 
{\displaystyle {\hat {\alpha }}>{\hat {\beta }}}

 for (negative) sample skewness < 0, and 
{\displaystyle {\hat {\alpha }}<{\hat {\beta }}}

 for (positive) sample skewness > 0.
The accompanying plot shows these two solutions as surfaces in a space with horizontal axes of (sample excess kurtosis) and (sample squared skewness) and the shape parameters as the vertical axis. The surfaces are constrained by the condition that the sample excess kurtosis must be bounded by the sample squared skewness as stipulated in the above equation.  The two surfaces meet at the right edge defined by zero skewness. Along this right edge, both parameters are equal and the distribution is symmetric U-shaped for α = β < 1, uniform for α = β = 1, upside-down-U-shaped for 1 < α = β < 2 and bell-shaped for α = β > 2.  The surfaces also meet at the front (lower) edge defined by "the impossible boundary" line (excess kurtosis + 2 - skewness2 = 0). Along this front (lower) boundary both shape parameters approach zero, and the probability density is concentrated more at one end than the other end (with practically nothing in between), with probabilities 
{\displaystyle p={\tfrac {\beta }{\alpha +\beta }}}

 at the left end x = 0 and 
{\displaystyle q=1-p={\tfrac {\alpha }{\alpha +\beta }}}

 at the right end x = 1.  The two surfaces become further apart towards the rear edge.  At this rear edge the surface parameters are quite different from each other.  As remarked, for example, by Bowman and Shenton,[44] sampling in the neighborhood of the line (sample excess kurtosis - (3/2)(sample skewness)2 = 0) (the just-J-shaped portion of the rear edge where blue meets beige), "is dangerously near to chaos", because at that line the denominator of the expression above for the estimate ν = α + β becomes zero and hence ν approaches infinity as that line is approached.  Bowman and Shenton [44] write that "the higher moment parameters (kurtosis and skewness) are extremely fragile (near that line). However, the mean and standard deviation are fairly reliable." Therefore, the problem is for the case of four parameter estimation for very skewed distributions such that the excess kurtosis approaches (3/2) times the square of the skewness.  This boundary line is produced by extremely skewed distributions with very large values of one of the parameters and very small values of the other parameter.  See § Kurtosis bounded by the square of the skewness for a numerical example and further comments about this rear edge boundary line (sample excess kurtosis - (3/2)(sample skewness)2 = 0).  As remarked by Karl Pearson himself [45] this issue may not be of much practical importance as this trouble arises only for very skewed J-shaped (or mirror-image J-shaped) distributions with very different values of shape parameters that are unlikely to occur much in practice).  The usual skewed-bell-shape distributions that occur in practice do not have this parameter estimation problem.
The remaining two parameters 
{\displaystyle {\hat {a}},{\hat {c}}}

 can be determined using the sample mean and the sample variance using a variety of equations.[1][42]  One alternative is to calculate the support interval range 
{\displaystyle ({\hat {c}}-{\hat {a}})}

 based on the sample variance and the sample kurtosis.  For this purpose one can solve, in terms of the range 
{\displaystyle ({\hat {c}}-{\hat {a}})}

, the equation expressing the excess kurtosis in terms of the sample variance, and the sample size ν (see § Kurtosis and § Alternative parametrizations, four parameters):

sample excess kurtosis

=

6

(
3
+

ν
^

)
(
2
+

ν
^

)

(

(

c
^

−

a
^

)

2

(sample variance)
{\displaystyle {\text{sample excess kurtosis}}={\frac {6}{(3+{\hat {\nu }})(2+{\hat {\nu }})}}{\bigg (}{\frac {({\hat {c}}-{\hat {a}})^{2}}{\text{(sample variance)}}}-6-5{\hat {\nu }}{\bigg )}}

to obtain:

(

c
^

−

a
^

)
=

(sample variance)

6
+
5

ν
^

+

(
2
+

ν
^

)
(
3
+

ν
^

)

6

(sample excess kurtosis)

{\displaystyle ({\hat {c}}-{\hat {a}})={\sqrt {\text{(sample variance)}}}{\sqrt {6+5{\hat {\nu }}+{\frac {(2+{\hat {\nu }})(3+{\hat {\nu }})}{6}}{\text{(sample excess kurtosis)}}}}}

Another alternative is to calculate the support interval range 
{\displaystyle ({\hat {c}}-{\hat {a}})}

 based on the sample variance and the sample skewness.[42]  For this purpose one can solve, in terms of the range 
{\displaystyle ({\hat {c}}-{\hat {a}})}

, the equation expressing the squared skewness in terms of the sample variance, and the sample size ν (see section titled "Skewness" and "Alternative parametrizations, four parameters"):

(

sample skewness

)

2

=

4

(
2
+

ν
^

)

2

(

(

c
^

−

a
^

)

2

(sample variance)
{\displaystyle ({\text{sample skewness}})^{2}={\frac {4}{(2+{\hat {\nu }})^{2}}}{\bigg (}{\frac {({\hat {c}}-{\hat {a}})^{2}}{\text{(sample variance)}}}-4(1+{\hat {\nu }}){\bigg )}}

to obtain:[42]

(

c
^

−

a
^

)
=

(sample variance)

2

(
2
+

ν
^

)

2

(

sample skewness
{\displaystyle ({\hat {c}}-{\hat {a}})={\frac {\sqrt {\text{(sample variance)}}}{2}}{\sqrt {(2+{\hat {\nu }})^{2}({\text{sample skewness}})^{2}+16(1+{\hat {\nu }})}}}

The remaining parameter can be determined from the sample mean and the previously obtained parameters: 
{\displaystyle ({\hat {c}}-{\hat {a}}),{\hat {\alpha }},{\hat {\nu }}={\hat {\alpha }}+{\hat {\beta }}}

:

a
^

=
(

sample mean
{\displaystyle {\hat {a}}=({\text{sample mean}})-\left({\frac {\hat {\alpha }}{\hat {\nu }}}\right)({\hat {c}}-{\hat {a}})}

and finally, 
{\displaystyle {\hat {c}}=({\hat {c}}-{\hat {a}})+{\hat {a}}}

.
In the above formulas one may take, for example, as estimates of the sample moments:

sample mean

=

y
¯

=

1
N

∑

i
=
1

N

Y

i

sample variance

=

v
¯

Y

=

1

N
−
1

∑

i
=
1

N

(

Y

i

−

y
¯

)

2

sample skewness

=

G

1

=

N

(
N
−
1
)
(
N
−
2
)

∑

i
=
1

N

(

Y

i

−

y
¯

)

3

v
¯

Y

3
2

sample excess kurtosis
{\displaystyle {\begin{aligned}{\text{sample mean}}&={\overline {y}}={\frac {1}{N}}\sum _{i=1}^{N}Y_{i}\\{\text{sample variance}}&={\overline {v}}_{Y}={\frac {1}{N-1}}\sum _{i=1}^{N}(Y_{i}-{\overline {y}})^{2}\\{\text{sample skewness}}&=G_{1}={\frac {N}{(N-1)(N-2)}}{\frac {\sum _{i=1}^{N}(Y_{i}-{\overline {y}})^{3}}{{\overline {v}}_{Y}^{\frac {3}{2}}}}\\{\text{sample excess kurtosis}}&=G_{2}={\frac {N(N+1)}{(N-1)(N-2)(N-3)}}{\frac {\sum _{i=1}^{N}(Y_{i}-{\overline {y}})^{4}}{{\overline {v}}_{Y}^{2}}}-{\frac {3(N-1)^{2}}{(N-2)(N-3)}}\end{aligned}}}

The estimators G1 for sample skewness and G2 for sample kurtosis are used by DAP/SAS, PSPP/SPSS, and Excel.  However, they are not used by BMDP and (according to [46]) they were not used by MINITAB in 1998. Actually, Joanes and Gill in their 1998 study[46]  concluded that the skewness and kurtosis estimators used in BMDP and in MINITAB (at that time) had smaller variance and mean-squared error in normal samples, but the skewness and kurtosis estimators used in  DAP/SAS, PSPP/SPSS, namely G1 and G2, had smaller mean-squared error in samples from a very skewed distribution.  It is for this reason that we have spelled out "sample skewness", etc., in the above formulas, to make it explicit that the user should choose the best estimator according to the problem at hand, as the best estimator for skewness and kurtosis depends on the amount of skewness (as shown by Joanes and Gill[46]).

Maximum likelihood[edit]
Two unknown parameters[edit]
Max (joint log likelihood/N) for beta distribution maxima at α = β = 2
Max (joint log likelihood/N) for Beta distribution maxima at α = β ∈ {0.25,0.5,1,2,4,6,8}
As is also the case for maximum likelihood estimates for the gamma distribution, the maximum likelihood estimates for the beta distribution do not have a general closed form solution for arbitrary values of the shape parameters. If X1, ..., XN are independent random variables each having a beta distribution, the joint log likelihood function for N iid observations is:
{\displaystyle {\begin{aligned}\ln \,{\mathcal {L}}(\alpha ,\beta \mid X)&=\sum _{i=1}^{N}\ln {\mathcal {L}}_{i}(\alpha ,\beta \mid X_{i})\\&=\sum _{i=1}^{N}\ln f(X_{i};\alpha ,\beta )\\&=\sum _{i=1}^{N}\ln {\frac {X_{i}^{\alpha -1}(1-X_{i})^{\beta -1}}{\mathrm {B} (\alpha ,\beta )}}\\&=(\alpha -1)\sum _{i=1}^{N}\ln X_{i}+(\beta -1)\sum _{i=1}^{N}\ln(1-X_{i})-N\ln \mathrm {B} (\alpha ,\beta )\end{aligned}}}

Finding the maximum with respect to a shape parameter involves taking the partial derivative with respect to the shape parameter and setting the expression equal to zero yielding the maximum likelihood estimator of the shape parameters:
{\displaystyle {\frac {\partial \ln {\mathcal {L}}(\alpha ,\beta \mid X)}{\partial \alpha }}=\sum _{i=1}^{N}\ln X_{i}-N{\frac {\partial \ln \mathrm {B} (\alpha ,\beta )}{\partial \alpha }}=0}
{\displaystyle {\frac {\partial \ln {\mathcal {L}}(\alpha ,\beta \mid X)}{\partial \beta }}=\sum _{i=1}^{N}\ln(1-X_{i})-N{\frac {\partial \ln \mathrm {B} (\alpha ,\beta )}{\partial \beta }}=0}

where:
{\displaystyle {\begin{aligned}{\frac {\partial \ln \mathrm {B} (\alpha ,\beta )}{\partial \alpha }}&=-{\frac {\partial \ln \Gamma (\alpha +\beta )}{\partial \alpha }}+{\frac {\partial \ln \Gamma (\alpha )}{\partial \alpha }}+{\frac {\partial \ln \Gamma (\beta )}{\partial \alpha }}\\[1ex]&=-\psi (\alpha +\beta )+\psi (\alpha )+0\end{aligned}}}
{\displaystyle {\begin{aligned}{\frac {\partial \ln \mathrm {B} (\alpha ,\beta )}{\partial \beta }}&=-{\frac {\partial \ln \Gamma (\alpha +\beta )}{\partial \beta }}+{\frac {\partial \ln \Gamma (\alpha )}{\partial \beta }}+{\frac {\partial \ln \Gamma (\beta )}{\partial \beta }}\\[1ex]&=-\psi (\alpha +\beta )+0+\psi (\beta )\end{aligned}}}

since the digamma function denoted ψ(α) is defined as the logarithmic derivative of the gamma function:[18]
{\displaystyle \psi (\alpha )={\frac {\partial \ln \Gamma (\alpha )}{\partial \alpha }}}

To ensure that the values with zero tangent slope are indeed a maximum (instead of a saddle-point or a minimum) one has to also satisfy the condition that the curvature is negative.  This amounts to satisfying that the second partial derivative with respect to the shape parameters is negative
{\displaystyle {\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta \mid X)}{\partial \alpha ^{2}}}=-N{\frac {\partial ^{2}\ln \mathrm {B} (\alpha ,\beta )}{\partial \alpha ^{2}}}<0}
{\displaystyle {\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta \mid X)}{\partial \beta ^{2}}}=-N{\frac {\partial ^{2}\ln \mathrm {B} (\alpha ,\beta )}{\partial \beta ^{2}}}<0}

using the previous equations, this is equivalent to:
{\displaystyle {\frac {\partial ^{2}\ln \mathrm {B} (\alpha ,\beta )}{\partial \alpha ^{2}}}=\psi _{1}(\alpha )-\psi _{1}(\alpha +\beta )>0}
{\displaystyle {\frac {\partial ^{2}\ln \mathrm {B} (\alpha ,\beta )}{\partial \beta ^{2}}}=\psi _{1}(\beta )-\psi _{1}(\alpha +\beta )>0}

where the trigamma function, denoted ψ1(α), is the second of the polygamma functions, and is defined as the derivative of the digamma function:
{\displaystyle \psi _{1}(\alpha )={\frac {\partial ^{2}\ln \Gamma (\alpha )}{\partial \alpha ^{2}}}=\,{\frac {\partial \,\psi (\alpha )}{\partial \alpha }}.}

These conditions are equivalent to stating that the variances of the logarithmically transformed variables are positive, since:
{\displaystyle \operatorname {var} [\ln(X)]=\operatorname {E} [\ln ^{2}(X)]-(\operatorname {E} [\ln(X)])^{2}=\psi _{1}(\alpha )-\psi _{1}(\alpha +\beta )}
{\displaystyle \operatorname {var} [\ln(1-X)]=\operatorname {E} [\ln ^{2}(1-X)]-(\operatorname {E} [\ln(1-X)])^{2}=\psi _{1}(\beta )-\psi _{1}(\alpha +\beta )}

Therefore, the condition of negative curvature at a maximum is equivalent to the statements:
{\displaystyle \operatorname {var} [\ln(X)]>0}
{\displaystyle \operatorname {var} [\ln(1-X)]>0}

Alternatively, the condition of negative curvature at a maximum is also equivalent to stating that the following logarithmic derivatives of the geometric means GX and G(1−X) are positive, since:
{\displaystyle \psi _{1}(\alpha )-\psi _{1}(\alpha +\beta )={\frac {\partial \ln G_{X}}{\partial \alpha }}>0}
{\displaystyle \psi _{1}(\beta )-\psi _{1}(\alpha +\beta )={\frac {\partial \ln G_{(1-X)}}{\partial \beta }}>0}

While these slopes are indeed positive, the other slopes are negative:
{\displaystyle {\frac {\partial \,\ln G_{X}}{\partial \beta }},{\frac {\partial \ln G_{1-X}}{\partial \alpha }}<0.}

The slopes of the mean and the median with respect to α and β display similar sign behavior.
From the condition that at a maximum, the partial derivative with respect to the shape parameter equals zero, we obtain the following system of coupled maximum likelihood estimate equations (for the average log-likelihoods) that needs to be inverted to obtain the  (unknown) shape parameter estimates 
{\displaystyle {\hat {\alpha }},{\hat {\beta }}}

 in terms of the (known) average of logarithms of the samples X1, ..., XN:[1]
{\displaystyle {\begin{aligned}{\hat {\operatorname {E} }}[\ln(X)]&=\psi ({\hat {\alpha }})-\psi ({\hat {\alpha }}+{\hat {\beta }})={\frac {1}{N}}\sum _{i=1}^{N}\ln X_{i}=\ln {\hat {G}}_{X}\\{\hat {\operatorname {E} }}[\ln(1-X)]&=\psi ({\hat {\beta }})-\psi ({\hat {\alpha }}+{\hat {\beta }})={\frac {1}{N}}\sum _{i=1}^{N}\ln(1-X_{i})=\ln {\hat {G}}_{1-X}\end{aligned}}}

where we recognize 
{\displaystyle \log {\hat {G}}_{X}}

 as the logarithm of the sample geometric mean and 
{\displaystyle \log {\hat {G}}_{1-X}}

 as the logarithm of the sample geometric mean based on (1 − X), the mirror-image of X. For 
{\displaystyle {\hat {\alpha }}={\hat {\beta }}}

, it follows that  
{\displaystyle {\hat {G}}_{X}={\hat {G}}_{1-X}}
{\displaystyle {\begin{aligned}{\hat {G}}_{X}&=\prod _{i=1}^{N}(X_{i})^{1/N}\\{\hat {G}}_{1-X}&=\prod _{i=1}^{N}(1-X_{i})^{1/N}\end{aligned}}}

These coupled equations containing digamma functions of the shape parameter estimates 
{\displaystyle {\hat {\alpha }},{\hat {\beta }}}

 must be solved by numerical methods as done, for example, by Beckman et al.[47] Gnanadesikan et al. give numerical solutions for a few cases.[48] N.L.Johnson and S.Kotz[1] suggest that for "not too small" shape parameter estimates 
{\displaystyle {\hat {\alpha }},{\hat {\beta }}}

, the logarithmic approximation to the digamma function 
{\displaystyle \psi ({\hat {\alpha }})\approx \ln({\hat {\alpha }}-{\tfrac {1}{2}})}

 may be used to obtain initial values for an iterative solution, since the equations resulting from this approximation can be solved exactly:
{\displaystyle \ln {\frac {{\hat {\alpha }}-{\frac {1}{2}}}{{\hat {\alpha }}+{\hat {\beta }}-{\frac {1}{2}}}}\approx \ln {\hat {G}}_{X}}
{\displaystyle \ln {\frac {{\hat {\beta }}-{\frac {1}{2}}}{{\hat {\alpha }}+{\hat {\beta }}-{\frac {1}{2}}}}\approx \ln {\hat {G}}_{1-X}}

which leads to the following solution for the initial values (of the estimate shape parameters in terms of the sample geometric means) for an iterative solution:
{\displaystyle {\hat {\alpha }}\approx {\frac {1}{2}}+{\frac {{\hat {G}}_{X}}{2\left(1-{\hat {G}}_{X}-{\hat {G}}_{1-X}\right)}}{\text{ if }}{\hat {\alpha }}>1}
{\displaystyle {\hat {\beta }}\approx {\frac {1}{2}}+{\frac {{\hat {G}}_{1-X}}{2\left(1-{\hat {G}}_{X}-{\hat {G}}_{1-X}\right)}}{\text{ if }}{\hat {\beta }}>1}

Alternatively, the estimates provided by the method of moments can instead be used as initial values for an iterative solution of the maximum likelihood coupled equations in terms of the digamma functions.
When the distribution is required over a known interval other than [0, 1]  with random variable X, say [a, c] with random variable Y, then replace ln(Xi) in the first equation with
{\displaystyle \ln {\frac {Y_{i}-a}{c-a}},}

and replace ln(1−Xi) in the second equation with
{\displaystyle \ln {\frac {c-Y_{i}}{c-a}}}

(see "Alternative parametrizations, four parameters" section below).
If one of the shape parameters is known, the problem is considerably simplified.  The following logit transformation can be used to solve for the unknown shape parameter (for skewed cases such that 
{\displaystyle {\hat {\alpha }}\neq {\hat {\beta }}}

, otherwise, if symmetric, both -equal- parameters are known when one is known):
{\displaystyle {\hat {\operatorname {E} }}\left[\ln {\frac {X}{1-X}}\right]=\psi ({\hat {\alpha }})-\psi ({\hat {\beta }})={\frac {1}{N}}\sum _{i=1}^{N}\ln {\frac {X_{i}}{1-X_{i}}}=\ln {\hat {G}}_{X}-\ln {\hat {G}}_{1-X}}

This logit transformation is the logarithm of the transformation that divides the variable X by its mirror-image (X/(1 - X) resulting in the "inverted beta distribution"  or beta prime distribution (also known as beta distribution of the second kind or Pearson's Type VI) with support [0, +∞). As previously discussed in the section "Moments of logarithmically transformed random variables," the logit transformation 
{\displaystyle \ln {\frac {X}{1-X}}}

, studied by Johnson,[25] extends the finite support [0, 1] based on the original variable X to infinite support in both directions of the real line (−∞, +∞).
If, for example, 
{\displaystyle {\hat {\beta }}}

 is known, the unknown parameter 
{\displaystyle {\hat {\alpha }}}

 can be obtained in terms of the inverse[49] digamma function of the right hand side of this equation:
{\displaystyle \psi ({\hat {\alpha }})={\frac {1}{N}}\sum _{i=1}^{N}\ln {\frac {X_{i}}{1-X_{i}}}+\psi ({\hat {\beta }})}
{\displaystyle {\hat {\alpha }}=\psi ^{-1}\left(\ln {\hat {G}}_{X}-\ln {\hat {G}}_{(1-X)}+\psi ({\hat {\beta }})\right)}

In particular, if one of the shape parameters has a value of unity, for example for 
{\displaystyle {\hat {\beta }}=1}

 (the power function distribution with bounded support [0,1]), using the identity ψ(x + 1) = ψ(x) + 1/x in the equation 
{\displaystyle \psi ({\hat {\alpha }})-\psi ({\hat {\alpha }}+{\hat {\beta }})=\ln {\hat {G}}_{X}}

, the maximum likelihood estimator for the unknown parameter 
{\displaystyle {\hat {\alpha }}}

 is,[1] exactly:
{\displaystyle {\hat {\alpha }}=-{\frac {1}{{\frac {1}{N}}\sum _{i=1}^{N}\ln X_{i}}}=-{\frac {1}{\ln {\hat {G}}_{X}}}}

The beta has support [0, 1], therefore 
{\displaystyle {\hat {G}}_{X}<1}

, and hence 
{\displaystyle (-\ln {\hat {G}}_{X})>0}

, and therefore 
{\displaystyle {\hat {\alpha }}>0.}

In conclusion, the maximum likelihood estimates of the shape parameters of a beta distribution are (in general) a complicated function of the sample geometric mean, and of the sample geometric mean based on (1−X)), the mirror-image of X.  One may ask, if the variance (in addition to the mean) is necessary to estimate two shape parameters with the method of moments, why is the (logarithmic or geometric) variance not necessary to estimate two shape parameters with the maximum likelihood method, for which only the geometric means suffice?  The answer is because the mean does not provide as much information as the geometric mean.  For a beta distribution with equal shape parameters α = β, the mean is exactly 1/2, regardless of the value of the shape parameters, and therefore regardless of the value of the statistical dispersion (the variance).  On the other hand, the geometric mean of a beta distribution with equal shape parameters α = β, depends on the value of the shape parameters, and therefore it contains more information.  Also, the geometric mean of a beta distribution does not satisfy the symmetry conditions satisfied by the mean, therefore, by employing both the geometric mean based on X and geometric mean based on (1 − X), the maximum likelihood method is able to provide best estimates for both parameters α = β, without need of employing the variance.
One can express the joint log likelihood per N iid observations in terms of the sufficient statistics (the sample geometric means) as follows:
{\displaystyle {\frac {\ln {\mathcal {L}}(\alpha ,\beta \mid X)}{N}}=(\alpha -1)\ln {\hat {G}}_{X}+(\beta -1)\ln {\hat {G}}_{(1-X)}-\ln \mathrm {B} (\alpha ,\beta ).}

We can plot the joint log likelihood per N observations for fixed values of the sample geometric means to see the behavior of the likelihood function as a function of the shape parameters α and β. In such a plot, the shape parameter estimators 
{\displaystyle {\hat {\alpha }},{\hat {\beta }}}

 correspond to the maxima of the likelihood function. See the accompanying graph that shows that all the likelihood functions intersect at α = β = 1, which corresponds to the values of the shape parameters that give the maximum entropy (the maximum entropy occurs for shape parameters equal to unity: the uniform distribution).  It is evident from the plot that the likelihood function gives sharp peaks for values of the shape parameter estimators close to zero, but that for values of the shape parameters estimators greater than one, the likelihood function becomes quite flat, with less defined peaks.  Obviously, the maximum likelihood parameter estimation method for the beta distribution becomes less acceptable for larger values of the shape parameter estimators, as the uncertainty in the peak definition increases with the value of the shape parameter estimators.  One can arrive at the same conclusion by noticing that the expression for the curvature of the likelihood function is in terms of the geometric variances
{\displaystyle {\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta \mid X)}{\partial \alpha ^{2}}}=-\operatorname {var} [\ln X]}
{\displaystyle {\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta \mid X)}{\partial \beta ^{2}}}=-\operatorname {var} [\ln(1-X)]}

These variances (and therefore the curvatures) are much larger for small values of the shape parameter α and β. However, for shape parameter values α, β > 1, the variances (and therefore the curvatures) flatten out.  Equivalently, this result follows from the Cramér–Rao bound, since the Fisher information matrix components for the beta distribution are these logarithmic variances. The Cramér–Rao bound states that the variance of any unbiased estimator 
{\displaystyle {\hat {\alpha }}}

 of α is bounded by the reciprocal of the Fisher information:
{\displaystyle \mathrm {var} ({\hat {\alpha }})\geq {\frac {1}{\operatorname {var} [\ln X]}}\geq {\frac {1}{\psi _{1}({\hat {\alpha }})-\psi _{1}({\hat {\alpha }}+{\hat {\beta }})}}}
{\displaystyle \mathrm {var} ({\hat {\beta }})\geq {\frac {1}{\operatorname {var} [\ln(1-X)]}}\geq {\frac {1}{\psi _{1}({\hat {\beta }})-\psi _{1}({\hat {\alpha }}+{\hat {\beta }})}}}

so the variance of the estimators increases with increasing α and β, as the logarithmic variances decrease.
Also one can express the joint log likelihood per N iid observations in terms of the digamma function expressions for the logarithms of the sample geometric means as follows:
{\displaystyle {\frac {\ln \,{\mathcal {L}}(\alpha ,\beta \mid X)}{N}}=(\alpha -1)(\psi ({\hat {\alpha }})-\psi ({\hat {\alpha }}+{\hat {\beta }}))+(\beta -1)(\psi ({\hat {\beta }})-\psi ({\hat {\alpha }}+{\hat {\beta }}))-\ln \mathrm {B} (\alpha ,\beta )}

this expression is identical to the negative of the cross-entropy (see section on "Quantities of information (entropy)").  Therefore, finding the maximum of the joint log likelihood of the shape parameters, per N iid observations, is identical to finding the minimum of the cross-entropy for the beta distribution, as a function of the shape parameters.
{\displaystyle {\begin{aligned}{\frac {\ln {\mathcal {L}}(\alpha ,\beta \mid X)}{N}}&=-H=-h-D_{\mathrm {KL} }\\&=-\ln \mathrm {B} (\alpha ,\beta )+(\alpha -1)\psi ({\hat {\alpha }})+(\beta -1)\psi ({\hat {\beta }})-(\alpha +\beta -2)\psi ({\hat {\alpha }}+{\hat {\beta }})\end{aligned}}}

with the cross-entropy defined as follows:
{\displaystyle H=\int _{0}^{1}-f(X;{\hat {\alpha }},{\hat {\beta }})\ln(f(X;\alpha ,\beta ))\,{\rm {d}}X}

Four unknown parameters[edit]
The procedure is similar to the one followed in the two unknown parameter case. If Y1, ..., YN are independent random variables each having a beta distribution with four parameters, the joint log likelihood function for N iid observations is:
{\displaystyle {\begin{aligned}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)&=\sum _{i=1}^{N}\ln \,{\mathcal {L}}_{i}(\alpha ,\beta ,a,c\mid Y_{i})\\&=\sum _{i=1}^{N}\ln f(Y_{i};\alpha ,\beta ,a,c)\\&=\sum _{i=1}^{N}\ln {\frac {(Y_{i}-a)^{\alpha -1}(c-Y_{i})^{\beta -1}}{(c-a)^{\alpha +\beta -1}\mathrm {B} (\alpha ,\beta )}}\\&=(\alpha -1)\sum _{i=1}^{N}\ln(Y_{i}-a)+(\beta -1)\sum _{i=1}^{N}\ln(c-Y_{i})-N\ln \mathrm {B} (\alpha ,\beta )-N(\alpha +\beta -1)\ln(c-a)\end{aligned}}}

Finding the maximum with respect to a shape parameter involves taking the partial derivative with respect to the shape parameter and setting the expression equal to zero yielding the maximum likelihood estimator of the shape parameters:
{\displaystyle {\frac {\partial \ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \alpha }}=\sum _{i=1}^{N}\ln(Y_{i}-a)-N(-\psi (\alpha +\beta )+\psi (\alpha ))-N\ln(c-a)=0}
{\displaystyle {\frac {\partial \ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \beta }}=\sum _{i=1}^{N}\ln(c-Y_{i})-N(-\psi (\alpha +\beta )+\psi (\beta ))-N\ln(c-a)=0}
{\displaystyle {\frac {\partial \ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial a}}=-(\alpha -1)\sum _{i=1}^{N}{\frac {1}{Y_{i}-a}}\,+N(\alpha +\beta -1){\frac {1}{c-a}}=0}
{\displaystyle {\frac {\partial \ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial c}}=(\beta -1)\sum _{i=1}^{N}{\frac {1}{c-Y_{i}}}\,-N(\alpha +\beta -1){\frac {1}{c-a}}=0}

these equations can be re-arranged as the following system of four coupled equations (the first two equations are geometric means and the second two equations are the harmonic means) in terms of the maximum likelihood estimates for the four parameters 
{\displaystyle {\hat {\alpha }},{\hat {\beta }},{\hat {a}},{\hat {c}}}
{\displaystyle {\frac {1}{N}}\sum _{i=1}^{N}\ln {\frac {Y_{i}-{\hat {a}}}{{\hat {c}}-{\hat {a}}}}=\psi ({\hat {\alpha }})-\psi ({\hat {\alpha }}+{\hat {\beta }})=\ln {\hat {G}}_{X}}
{\displaystyle {\frac {1}{N}}\sum _{i=1}^{N}\ln {\frac {{\hat {c}}-Y_{i}}{{\hat {c}}-{\hat {a}}}}=\psi ({\hat {\beta }})-\psi ({\hat {\alpha }}+{\hat {\beta }})=\ln {\hat {G}}_{1-X}}
{\displaystyle {\frac {1}{{\frac {1}{N}}\sum _{i=1}^{N}{\frac {{\hat {c}}-{\hat {a}}}{Y_{i}-{\hat {a}}}}}}={\frac {{\hat {\alpha }}-1}{{\hat {\alpha }}+{\hat {\beta }}-1}}={\hat {H}}_{X}}
{\displaystyle {\frac {1}{{\frac {1}{N}}\sum _{i=1}^{N}{\frac {{\hat {c}}-{\hat {a}}}{{\hat {c}}-Y_{i}}}}}={\frac {{\hat {\beta }}-1}{{\hat {\alpha }}+{\hat {\beta }}-1}}={\hat {H}}_{1-X}}

with sample geometric means:
{\displaystyle {\hat {G}}_{X}=\prod _{i=1}^{N}\left({\frac {Y_{i}-{\hat {a}}}{{\hat {c}}-{\hat {a}}}}\right)^{\frac {1}{N}}}
{\displaystyle {\hat {G}}_{(1-X)}=\prod _{i=1}^{N}\left({\frac {{\hat {c}}-Y_{i}}{{\hat {c}}-{\hat {a}}}}\right)^{\frac {1}{N}}}

The parameters 
{\displaystyle {\hat {a}},{\hat {c}}}

 are embedded inside the geometric mean expressions in a nonlinear way (to the power 1/N).  This precludes, in general, a closed form solution, even for an initial value approximation for iteration purposes.  One alternative is to use as initial values for iteration the values obtained from the method of moments solution for the four parameter case.  Furthermore, the expressions for the harmonic means are well-defined only for 
{\displaystyle {\hat {\alpha }},{\hat {\beta }}>1}

, which precludes a maximum likelihood solution for shape parameters less than unity in the four-parameter case. Fisher's information matrix for the four parameter case is positive-definite only for α, β > 2 (for further discussion, see section on Fisher information matrix, four parameter case), for bell-shaped (symmetric or unsymmetric) beta distributions, with inflection points located to either side of the mode. The following Fisher information components (that represent the expectations of the curvature of the log likelihood function) have singularities at the following values:
{\displaystyle \alpha =2:\quad \operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial a^{2}}}\right]={\mathcal {I}}_{a,a}}
{\displaystyle \beta =2:\quad \operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial c^{2}}}\right]={\mathcal {I}}_{c,c}}
{\displaystyle \alpha =2:\quad \operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \alpha \partial a}}\right]={\mathcal {I}}_{\alpha ,a}}
{\displaystyle \beta =1:\quad \operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \beta \partial c}}\right]={\mathcal {I}}_{\beta ,c}}

(for further discussion see section on Fisher information matrix). Thus, it is not possible to strictly carry on the maximum likelihood estimation for some well known distributions belonging to the four-parameter beta distribution family, like the uniform distribution (Beta(1, 1, a, c)), and the arcsine distribution (Beta(1/2, 1/2, a, c)).  N.L.Johnson and S.Kotz[1] ignore the equations for the harmonic means and instead suggest "If a and c are unknown, and maximum likelihood estimators of a, c, α and β are required, the above procedure (for the two unknown parameter case, with X transformed as X = (Y − a)/(c − a)) can be repeated using a succession of trial values of a and c, until the pair (a, c) for which maximum likelihood (given a and c) is as great as possible, is attained" (where, for the purpose of clarity, their notation for the parameters has been translated into the present notation).

Fisher information matrix[edit]
Let a random variable X have a probability density f(x;α). The partial derivative with respect to the (unknown, and to be estimated) parameter α of the log likelihood function is called the score.  The second moment of the score is called the Fisher information:
{\displaystyle {\mathcal {I}}(\alpha )=\operatorname {E} \left[\left({\frac {\partial }{\partial \alpha }}\ln {\mathcal {L}}(\alpha \mid X)\right)^{2}\right],}

The expectation of the score is zero, therefore the Fisher information is also the second moment centered on the mean of the score: the variance of the score.
If the log likelihood function is twice differentiable with respect to the parameter α, and under certain regularity conditions,[50] then the Fisher information may also be written as follows (which is often a more convenient form for calculation purposes):
{\displaystyle {\mathcal {I}}(\alpha )=-\operatorname {E} \left[{\frac {\partial ^{2}}{\partial \alpha ^{2}}}\ln {\mathcal {L}}(\alpha \mid X)\right].}

Thus, the Fisher information is the negative of the expectation of the second derivative  with respect to the parameter α of the log likelihood function. Therefore, Fisher information is a measure of the curvature of the log likelihood function of α. A low curvature (and therefore high radius of curvature), flatter log likelihood function curve has low Fisher information; while a log likelihood function curve with large curvature (and therefore low radius of curvature) has high Fisher information. When the Fisher information matrix is computed at the evaluates of the parameters ("the observed Fisher information matrix") it is equivalent to the replacement of the true log likelihood surface by a Taylor's series approximation, taken as far as the quadratic terms.[51]  The word information, in the context of Fisher information, refers to information about the parameters. Information such as: estimation, sufficiency and properties of variances of estimators.  The Cramér–Rao bound states that the inverse of the Fisher information is a lower bound on the variance of any estimator of a parameter α:
{\displaystyle \operatorname {var} [{\hat {\alpha }}]\geq {\frac {1}{{\mathcal {I}}(\alpha )}}.}

The precision to which one can estimate the estimator of a parameter α is limited by the Fisher Information of the log likelihood function. The Fisher information is a measure of the minimum error involved in estimating a parameter of a distribution and it can be viewed as a measure of the resolving power of an experiment needed to discriminate between two alternative hypothesis of a parameter.[52]
When there are N parameters
{\displaystyle {\begin{bmatrix}\theta _{1}\\\theta _{2}\\\vdots \\\theta _{N}\end{bmatrix}},}

then the Fisher information takes the form of an N×N positive semidefinite symmetric matrix, the Fisher information matrix, with typical element:
{\displaystyle ({\mathcal {I}}(\theta ))_{i,j}=\operatorname {E} \left[{\frac {\partial \ln {\mathcal {L}}}{\partial \theta _{i}}}\cdot {\frac {\partial \ln {\mathcal {L}}}{\partial \theta _{j}}}\right].}

Under certain regularity conditions,[50] the Fisher Information Matrix may also be written in the following form, which is often more convenient for computation:
{\displaystyle ({\mathcal {I}}(\theta ))_{i,j}=-\operatorname {E} \left[{\frac {\partial ^{2}\ln {\mathcal {L}}}{\partial \theta _{i}\,\partial \theta _{j}}}\right]\,.}

With X1, ..., XN iid random variables, an N-dimensional "box" can be constructed with sides X1, ..., XN. Costa and Cover[53]  show that the (Shannon) differential entropy h(X) is related to the volume of the typical set (having the sample entropy close to the true entropy), while the Fisher information is related to the surface of this typical set.

Two parameters[edit]
For X1, ..., XN independent random variables each having a beta distribution parametrized with shape parameters α and β, the joint log likelihood function for N iid observations is:
{\displaystyle \ln {\mathcal {L}}(\alpha ,\beta \mid X)=(\alpha -1)\sum _{i=1}^{N}\ln X_{i}+(\beta -1)\sum _{i=1}^{N}\ln(1-X_{i})-N\ln \mathrm {B} (\alpha ,\beta )}

therefore the joint log likelihood function per N iid observations is
{\displaystyle {\frac {1}{N}}\ln {\mathcal {L}}(\alpha ,\beta \mid X)=(\alpha -1){\frac {1}{N}}\sum _{i=1}^{N}\ln X_{i}+(\beta -1){\frac {1}{N}}\sum _{i=1}^{N}\ln(1-X_{i})-\,\ln \mathrm {B} (\alpha ,\beta ).}

For the two parameter case, the Fisher information has 4 components: 2 diagonal and 2 off-diagonal. Since the Fisher information matrix is symmetric, one of these off diagonal components is independent. Therefore, the Fisher information matrix has 3 independent components (2 diagonal and 1 off diagonal).
Aryal and Nadarajah[54] calculated Fisher's information matrix for the four-parameter case, from which the two parameter case can be obtained as follows:
{\displaystyle -{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta \mid X)}{N\partial \alpha ^{2}}}=\operatorname {var} [\ln(X)]=\psi _{1}(\alpha )-\psi _{1}(\alpha +\beta )={\mathcal {I}}_{\alpha ,\alpha }=\operatorname {E} \left[-{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta \mid X)}{N\partial \alpha ^{2}}}\right]=\ln \operatorname {var} _{GX}}
{\displaystyle -{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta \mid X)}{N\,\partial \beta ^{2}}}=\operatorname {var} [\ln(1-X)]=\psi _{1}(\beta )-\psi _{1}(\alpha +\beta )={\mathcal {I}}_{\beta ,\beta }=\operatorname {E} \left[-{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta \mid X)}{N\partial \beta ^{2}}}\right]=\ln \operatorname {var} _{G(1-X)}}
{\displaystyle -{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta \mid X)}{N\,\partial \alpha \,\partial \beta }}=\operatorname {cov} [\ln X,\ln(1-X)]=-\psi _{1}(\alpha +\beta )={\mathcal {I}}_{\alpha ,\beta }=\operatorname {E} \left[-{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta \mid X)}{N\,\partial \alpha \,\partial \beta }}\right]=\ln \operatorname {cov} _{G{X,(1-X)}}}

Since the Fisher information matrix is symmetric
{\displaystyle {\mathcal {I}}_{\alpha ,\beta }={\mathcal {I}}_{\beta ,\alpha }=\ln \operatorname {cov} _{G{X,(1-X)}}}

The Fisher information components are equal to the log geometric variances and log geometric covariance. Therefore, they can be expressed as trigamma functions, denoted ψ1(α),  the second of the polygamma functions, defined as the derivative of the digamma function:
{\displaystyle \psi _{1}(\alpha )={\frac {d^{2}\ln \Gamma (\alpha )}{\partial \alpha ^{2}}}=\,{\frac {\partial \psi (\alpha )}{\partial \alpha }}.}

These derivatives are also derived in the § Two unknown parameters and plots of the log likelihood function are also shown in that section.  § Geometric variance and covariance contains plots and further discussion of the Fisher information matrix components: the log geometric variances and log geometric covariance as a function of the shape parameters α and β.  § Moments of logarithmically transformed random variables contains formulas for moments of logarithmically transformed random variables. Images for the Fisher information components 
{\displaystyle {\mathcal {I}}_{\alpha ,\alpha },{\mathcal {I}}_{\beta ,\beta }}
{\displaystyle {\mathcal {I}}_{\alpha ,\beta }}

 are shown in § Geometric variance.
The determinant of Fisher's information matrix is of interest (for example for the calculation of Jeffreys prior probability).  From the expressions for the individual components of the Fisher information matrix, it follows that the determinant of Fisher's (symmetric) information matrix for the beta distribution is:
{\displaystyle {\begin{aligned}\det({\mathcal {I}}(\alpha ,\beta ))&={\mathcal {I}}_{\alpha ,\alpha }{\mathcal {I}}_{\beta ,\beta }-{\mathcal {I}}_{\alpha ,\beta }{\mathcal {I}}_{\alpha ,\beta }\\[4pt]&=(\psi _{1}(\alpha )-\psi _{1}(\alpha +\beta ))(\psi _{1}(\beta )-\psi _{1}(\alpha +\beta ))-(-\psi _{1}(\alpha +\beta ))(-\psi _{1}(\alpha +\beta ))\\[4pt]&=\psi _{1}(\alpha )\psi _{1}(\beta )-(\psi _{1}(\alpha )+\psi _{1}(\beta ))\psi _{1}(\alpha +\beta )\\[4pt]\lim _{\alpha \to 0}\det({\mathcal {I}}(\alpha ,\beta ))&=\lim _{\beta \to 0}\det({\mathcal {I}}(\alpha ,\beta ))=\infty \\[4pt]\lim _{\alpha \to \infty }\det({\mathcal {I}}(\alpha ,\beta ))&=\lim _{\beta \to \infty }\det({\mathcal {I}}(\alpha ,\beta ))=0\end{aligned}}}

From Sylvester's criterion (checking whether the diagonal elements are all positive), it follows that the Fisher information matrix for the two parameter case is positive-definite (under the standard condition that the shape parameters are positive α > 0 and β > 0).

Four parameters[edit]
Fisher Information I(a,a) for α = β vs range (c − a) and exponent α = β
Fisher Information I(α,a) for α = β, vs. range (c − a) and exponent α = β
If Y1, ..., YN are independent random variables each having a beta distribution with four parameters: the exponents α and β, and also a (the minimum of the distribution range), and c (the maximum of the distribution range) (section titled "Alternative parametrizations", "Four parameters"), with probability density function:
{\displaystyle f(y;\alpha ,\beta ,a,c)={\frac {f(x;\alpha ,\beta )}{c-a}}={\frac {\left({\frac {y-a}{c-a}}\right)^{\alpha -1}\left({\frac {c-y}{c-a}}\right)^{\beta -1}}{(c-a)B(\alpha ,\beta )}}={\frac {(y-a)^{\alpha -1}(c-y)^{\beta -1}}{(c-a)^{\alpha +\beta -1}B(\alpha ,\beta )}}.}

the joint log likelihood function per N iid observations is:
{\displaystyle {\frac {1}{N}}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)={\frac {\alpha -1}{N}}\sum _{i=1}^{N}\ln(Y_{i}-a)+{\frac {\beta -1}{N}}\sum _{i=1}^{N}\ln(c-Y_{i})-\ln \mathrm {B} (\alpha ,\beta )-(\alpha +\beta -1)\ln(c-a)}

For the four parameter case, the Fisher information has 4*4=16 components.  It has 12 off-diagonal components = (4×4 total − 4 diagonal). Since the Fisher information matrix is symmetric, half of these components (12/2=6) are independent. Therefore, the Fisher information matrix has 6 independent off-diagonal + 4 diagonal = 10 independent components.  Aryal and Nadarajah[54] calculated Fisher's information matrix for the four parameter case as follows:
{\displaystyle -{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \alpha ^{2}}}=\operatorname {var} [\ln(X)]=\psi _{1}(\alpha )-\psi _{1}(\alpha +\beta )={\mathcal {I}}_{\alpha ,\alpha }=\operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \alpha ^{2}}}\right]=\ln(\operatorname {var_{GX}} )}
{\displaystyle -{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \beta ^{2}}}=\operatorname {var} [\ln(1-X)]=\psi _{1}(\beta )-\psi _{1}(\alpha +\beta )={\mathcal {I}}_{\beta ,\beta }=\operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \beta ^{2}}}\right]=\ln(\operatorname {var_{G(1-X)}} )}
{\displaystyle -{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \alpha \,\partial \beta }}=\operatorname {cov} [\ln X,(1-X)]=-\psi _{1}(\alpha +\beta )={\mathcal {I}}_{\alpha ,\beta }=\operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \alpha \,\partial \beta }}\right]=\ln(\operatorname {cov} _{G{X,(1-X)}})}

In the above expressions, the use of X instead of Y in the expressions var[ln(X)] = ln(varGX) is not an error. The expressions in terms of the log geometric variances and log geometric covariance occur as functions of the two parameter X ~ Beta(α, β) parametrization because when taking the partial derivatives with respect to the exponents (α, β) in the four parameter case, one obtains the identical expressions as for the two parameter case: these terms of the four parameter Fisher information matrix are independent of the minimum a and maximum c of the distribution's range. The only non-zero term upon double differentiation of the log likelihood function with respect to the exponents α and β is the second derivative of the log of the beta function: ln(B(α, β)). This term is independent of the minimum a and maximum c of the distribution's range. Double differentiation of this term results in trigamma functions.  The sections titled "Maximum likelihood", "Two unknown parameters" and "Four unknown parameters" also show this fact.
The Fisher information for N i.i.d. samples is N times the individual Fisher information (eq. 11.279, page 394 of Cover and Thomas[28]).  (Aryal and Nadarajah[54] take a single observation, N = 1, to calculate the following components of the Fisher information, which leads to the same result as considering the derivatives of the log likelihood per N observations. Moreover, below the erroneous expression for 
{\displaystyle {\mathcal {I}}_{a,a}}

 in Aryal and Nadarajah has been corrected.)
{\displaystyle {\begin{aligned}\alpha >2:\quad \operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial a^{2}}}\right]&={\mathcal {I}}_{a,a}={\frac {\beta (\alpha +\beta -1)}{(\alpha -2)(c-a)^{2}}}\\\beta >2:\quad \operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial c^{2}}}\right]&={\mathcal {I}}_{c,c}={\frac {\alpha (\alpha +\beta -1)}{(\beta -2)(c-a)^{2}}}\\\operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial a\,\partial c}}\right]&={\mathcal {I}}_{a,c}={\frac {(\alpha +\beta -1)}{(c-a)^{2}}}\\\alpha >1:\quad \operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \alpha \,\partial a}}\right]&={\mathcal {I}}_{\alpha ,a}={\frac {\beta }{(\alpha -1)(c-a)}}\\\operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \alpha \,\partial c}}\right]&={\mathcal {I}}_{\alpha ,c}={\frac {1}{(c-a)}}\\\operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \beta \,\partial a}}\right]&={\mathcal {I}}_{\beta ,a}=-{\frac {1}{(c-a)}}\\\beta >1:\quad \operatorname {E} \left[-{\frac {1}{N}}{\frac {\partial ^{2}\ln {\mathcal {L}}(\alpha ,\beta ,a,c\mid Y)}{\partial \beta \,\partial c}}\right]&={\mathcal {I}}_{\beta ,c}=-{\frac {\alpha }{(\beta -1)(c-a)}}\end{aligned}}}

The lower two diagonal entries of the Fisher information matrix, with respect to the parameter a (the minimum of the distribution's range): 
{\displaystyle {\mathcal {I}}_{a,a}}

, and with respect to the parameter c (the maximum of the distribution's range): 
{\displaystyle {\mathcal {I}}_{c,c}}

 are only defined for exponents α > 2 and β > 2 respectively. The Fisher information matrix component 
{\displaystyle {\mathcal {I}}_{a,a}}

 for the minimum a approaches infinity for exponent α approaching 2 from above, and the Fisher information matrix component 
{\displaystyle {\mathcal {I}}_{c,c}}

 for the maximum c approaches infinity for exponent β approaching 2 from above.
The Fisher information matrix for the four parameter case does not depend on the individual values of the minimum a and the maximum c, but only on the total range (c − a).  Moreover, the components of the Fisher information matrix that depend on the range (c − a), depend only through its inverse (or the square of the inverse), such that the Fisher information decreases for increasing range (c − a).
The accompanying images show the Fisher information components 
{\displaystyle {\mathcal {I}}_{a,a}}
{\displaystyle {\mathcal {I}}_{\alpha ,a}}

. Images for the Fisher information components 
{\displaystyle {\mathcal {I}}_{\alpha ,\alpha }}
{\displaystyle {\mathcal {I}}_{\beta ,\beta }}

 are shown in  § Geometric variance.  All these Fisher information components look like a basin, with the "walls" of the basin being located at low values of the parameters.
The following four-parameter-beta-distribution Fisher information components can be expressed in terms of the two-parameter: X ~ Beta(α, β) expectations of the transformed ratio ((1 − X)/X) and of its mirror image (X/(1 − X)), scaled by the range (c − a), which may be helpful for interpretation:
{\displaystyle {\mathcal {I}}_{\alpha ,a}={\frac {\operatorname {E} \left[{\frac {1-X}{X}}\right]}{c-a}}={\frac {\beta }{(\alpha -1)(c-a)}}{\text{ if }}\alpha >1}
{\displaystyle {\mathcal {I}}_{\beta ,c}=-{\frac {\operatorname {E} \left[{\frac {X}{1-X}}\right]}{c-a}}=-{\frac {\alpha }{(\beta -1)(c-a)}}{\text{ if }}\beta >1}

These are also the expected values of the "inverted beta distribution" or beta prime distribution (also known as beta distribution of the second kind or Pearson's Type VI) [1] and its mirror image, scaled by the range (c − a).
Also, the following Fisher information components can be expressed in terms of the harmonic (1/X) variances or of variances based on the ratio transformed variables ((1-X)/X) as follows:
{\displaystyle {\begin{aligned}\alpha >2:\quad {\mathcal {I}}_{a,a}&=\operatorname {var} \left[{\frac {1}{X}}\right]\left({\frac {\alpha -1}{c-a}}\right)^{2}=\operatorname {var} \left[{\frac {1-X}{X}}\right]\left({\frac {\alpha -1}{c-a}}\right)^{2}={\frac {\beta (\alpha +\beta -1)}{(\alpha -2)(c-a)^{2}}}\\\beta >2:\quad {\mathcal {I}}_{c,c}&=\operatorname {var} \left[{\frac {1}{1-X}}\right]\left({\frac {\beta -1}{c-a}}\right)^{2}=\operatorname {var} \left[{\frac {X}{1-X}}\right]\left({\frac {\beta -1}{c-a}}\right)^{2}={\frac {\alpha (\alpha +\beta -1)}{(\beta -2)(c-a)^{2}}}\\{\mathcal {I}}_{a,c}&=\operatorname {cov} \left[{\frac {1}{X}},{\frac {1}{1-X}}\right]{\frac {(\alpha -1)(\beta -1)}{(c-a)^{2}}}=\operatorname {cov} \left[{\frac {1-X}{X}},{\frac {X}{1-X}}\right]{\frac {(\alpha -1)(\beta -1)}{(c-a)^{2}}}={\frac {(\alpha +\beta -1)}{(c-a)^{2}}}\end{aligned}}}

See section "Moments of linearly transformed, product and inverted random variables" for these expectations.
The determinant of Fisher's information matrix is of interest (for example for the calculation of Jeffreys prior probability).  From the expressions for the individual components, it follows that the determinant of Fisher's (symmetric) information matrix for the beta distribution with four parameters is:
{\displaystyle {\begin{aligned}\det({\mathcal {I}}(\alpha ,\beta ,a,c))={}&-{\mathcal {I}}_{a,c}^{2}{\mathcal {I}}_{\alpha ,a}{\mathcal {I}}_{\alpha ,\beta }+{\mathcal {I}}_{a,a}{\mathcal {I}}_{a,c}{\mathcal {I}}_{\alpha ,c}{\mathcal {I}}_{\alpha ,\beta }+{\mathcal {I}}_{a,c}^{2}{\mathcal {I}}_{\alpha ,\beta }^{2}-{\mathcal {I}}_{a,a}{\mathcal {I}}_{c,c}{\mathcal {I}}_{\alpha ,\beta }^{2}\\&{}-{\mathcal {I}}_{a,c}{\mathcal {I}}_{\alpha ,a}{\mathcal {I}}_{\alpha ,c}{\mathcal {I}}_{\beta ,a}+{\mathcal {I}}_{a,c}^{2}{\mathcal {I}}_{\alpha ,\alpha }{\mathcal {I}}_{\beta ,a}+2{\mathcal {I}}_{c,c}{\mathcal {I}}_{\alpha ,a}{\mathcal {I}}_{\alpha ,\beta }{\mathcal {I}}_{\beta ,a}\\&{}-2{\mathcal {I}}_{a,c}{\mathcal {I}}_{\alpha ,c}{\mathcal {I}}_{\alpha ,\beta }{\mathcal {I}}_{\beta ,a}+{\mathcal {I}}_{\alpha ,c}^{2}{\mathcal {I}}_{\beta ,a}^{2}-{\mathcal {I}}_{c,c}{\mathcal {I}}_{\alpha ,\alpha }{\mathcal {I}}_{\beta ,a}^{2}+{\mathcal {I}}_{a,c}{\mathcal {I}}_{\alpha ,a}^{2}{\mathcal {I}}_{\beta ,c}\\&{}-{\mathcal {I}}_{a,a}{\mathcal {I}}_{a,c}{\mathcal {I}}_{\alpha ,\alpha }{\mathcal {I}}_{\beta ,c}-{\mathcal {I}}_{a,c}{\mathcal {I}}_{\alpha ,a}{\mathcal {I}}_{\alpha ,\beta }{\mathcal {I}}_{\beta ,c}+{\mathcal {I}}_{a,a}{\mathcal {I}}_{\alpha ,c}{\mathcal {I}}_{\alpha ,\beta }{\mathcal {I}}_{\beta ,c}\\&{}-{\mathcal {I}}_{\alpha ,a}{\mathcal {I}}_{\alpha ,c}{\mathcal {I}}_{\beta ,a}{\mathcal {I}}_{\beta ,c}+{\mathcal {I}}_{a,c}{\mathcal {I}}_{\alpha ,\alpha }{\mathcal {I}}_{\beta ,a}{\mathcal {I}}_{\beta ,c}-{\mathcal {I}}_{c,c}{\mathcal {I}}_{\alpha ,a}^{2}{\mathcal {I}}_{\beta ,\beta }\\&{}+2{\mathcal {I}}_{a,c}{\mathcal {I}}_{\alpha ,a}{\mathcal {I}}_{\alpha ,c}{\mathcal {I}}_{\beta ,\beta }-{\mathcal {I}}_{a,a}{\mathcal {I}}_{\alpha ,c}^{2}{\mathcal {I}}_{\beta ,\beta }-{\mathcal {I}}_{a,c}^{2}{\mathcal {I}}_{\alpha ,\alpha }{\mathcal {I}}_{\beta ,\beta }+{\mathcal {I}}_{a,a}{\mathcal {I}}_{c,c}{\mathcal {I}}_{\alpha ,\alpha }{\mathcal {I}}_{\beta ,\beta }{\text{ if }}\alpha ,\beta >2\end{aligned}}}

Using Sylvester's criterion (checking whether the diagonal elements are all positive), and since diagonal components 
{\displaystyle {\mathcal {I}}_{a,a}}
{\displaystyle {\mathcal {I}}_{c,c}}

 have singularities at α=2 and β=2 it follows that the Fisher information matrix for the four parameter case is positive-definite for α>2 and β>2.  Since for α > 2 and β > 2 the beta distribution is (symmetric or unsymmetric) bell shaped, it follows that the Fisher information matrix is positive-definite only for bell-shaped (symmetric or unsymmetric) beta distributions, with inflection points located to either side of the mode. Thus, important well known distributions belonging to the four-parameter beta distribution family, like the parabolic distribution (Beta(2,2,a,c)) and the uniform distribution (Beta(1,1,a,c)) have Fisher information components (
{\displaystyle {\mathcal {I}}_{a,a},{\mathcal {I}}_{c,c},{\mathcal {I}}_{\alpha ,a},{\mathcal {I}}_{\beta ,c}}

) that blow up (approach infinity) in the four-parameter case (although their Fisher information components are all defined for the two parameter case).  The four-parameter Wigner semicircle distribution (Beta(3/2,3/2,a,c)) and arcsine distribution (Beta(1/2,1/2,a,c)) have negative Fisher information determinants for the four-parameter case.

Bayesian inference[edit]
Main article: Bayesian inference
{\displaystyle Beta(1,1)}

: The uniform distribution probability density was proposed by Thomas Bayes to represent ignorance of prior probabilities in Bayesian inference.
The use of Beta distributions in Bayesian inference is due to the fact that they provide a family of conjugate prior probability distributions for binomial (including Bernoulli) and geometric distributions.  The domain of the beta distribution can be viewed as a probability, and in fact the beta distribution is often used to describe the distribution of a probability value p:[24]
{\displaystyle P(p;\alpha ,\beta )={\frac {p^{\alpha -1}(1-p)^{\beta -1}}{\mathrm {B} (\alpha ,\beta )}}.}

Examples of beta distributions used as prior probabilities to represent ignorance of prior parameter values in Bayesian inference are Beta(1,1), Beta(0,0) and Beta(1/2,1/2).

Rule of succession[edit]
Main article: Rule of succession
A classic application of the beta distribution is the rule of succession, introduced in the 18th century by Pierre-Simon Laplace[55]  in the course of treating the sunrise problem.  It states that, given s successes in n conditionally independent Bernoulli trials with probability p, that the estimate of the expected value in the next trial is 
{\displaystyle {\frac {s+1}{n+2}}}

.  This estimate is the expected value of the posterior distribution over p, namely Beta(s+1, n−s+1), which is given by Bayes' rule if one assumes a uniform prior probability over p (i.e., Beta(1, 1)) and then observes that p generated s successes in n trials.  Laplace's rule of succession has been criticized by prominent scientists.  R. T. Cox described Laplace's application of the rule of succession to the sunrise problem ([56] p. 89) as "a travesty of the proper use of the principle".  Keynes remarks  ([57] Ch.XXX, p. 382)  "indeed this is so foolish a theorem that to entertain it is discreditable".  Karl Pearson[58]  showed that the probability that the next (n + 1) trials will be successes, after n successes in n trials, is only 50%, which has been considered too low by scientists like Jeffreys and unacceptable as a representation of the scientific process of experimentation to test a proposed scientific law.  As pointed out by Jeffreys ([59] p. 128) (crediting C. D. Broad[60] ) Laplace's rule of succession establishes a high probability of success ((n+1)/(n+2)) in the next trial, but only a moderate probability (50%) that a further sample (n+1) comparable in size will be equally successful.  As pointed out by Perks,[61] "The rule of succession itself is hard to accept. It assigns a probability to the next trial which implies the assumption that the actual run observed is an average run and that we are always at the end of an average run. It would, one would think, be more reasonable to assume that we were in the middle of an average run. Clearly a higher value for both probabilities is necessary if they are to accord with reasonable belief." These problems with Laplace's rule of succession motivated Haldane, Perks, Jeffreys and others to search for other forms of prior probability (see the next § Bayesian inference).  According to Jaynes,[52] the main problem with the rule of succession is that it is not valid when s=0 or s=n (see rule of succession, for an analysis of its validity).

Bayes–Laplace prior probability (Beta(1,1))[edit]
The beta distribution achieves maximum differential entropy for Beta(1,1): the uniform probability density, for which all values in the domain of the distribution have equal density.  This uniform distribution Beta(1,1) was suggested ("with a great deal of doubt") by Thomas Bayes[62] as the prior probability distribution to express ignorance about the correct prior distribution. This prior distribution was adopted (apparently, from his writings, with little sign of doubt[55]) by Pierre-Simon Laplace, and hence it was also known as the "Bayes–Laplace rule" or the "Laplace rule" of "inverse probability" in publications of the first half of the 20th century. In the later part of the 19th century and early part of the 20th century, scientists realized that the assumption of uniform "equal" probability density depended on the actual functions (for example whether a linear or a logarithmic scale was most appropriate) and parametrizations used.  In particular, the behavior near the ends of distributions with finite support (for example near x = 0, for a distribution with initial support at x = 0) required particular attention. Keynes ([57] Ch.XXX, p. 381) criticized the use of Bayes's uniform prior probability (Beta(1,1)) that all values between zero and one are equiprobable, as follows: "Thus experience, if it shows anything, shows that there is a very marked clustering of statistical ratios in the neighborhoods of zero and unity, of those for positive theories and for correlations between positive qualities in the neighborhood of zero, and of those for negative theories and for correlations between negative qualities in the neighborhood of unity. "

Haldane's prior probability (Beta(0,0))[edit]
{\displaystyle Beta(0,0)}

: The Haldane prior probability expressing total ignorance about prior information, where we are not even sure whether it is physically possible for an experiment to yield either a success or a failure. As α, β → 0, the beta distribution approaches a two-point Bernoulli distribution with all probability density concentrated at each end, at 0 and 1, and nothing in between. A coin-toss: one face of the coin being at 0 and the other face being at 1. 
The Beta(0,0) distribution was proposed by J.B.S. Haldane,[63] who suggested that the prior probability representing complete uncertainty should be proportional to p−1(1−p)−1. The function p−1(1−p)−1 can be viewed as the limit of the numerator of the beta distribution as both shape parameters approach zero: α, β → 0. The Beta function (in the denominator of the beta distribution) approaches infinity, for both parameters approaching zero, α, β → 0. Therefore, p−1(1−p)−1 divided by the Beta function approaches a 2-point Bernoulli distribution with equal probability 1/2 at each end, at 0 and 1, and nothing in between, as α, β → 0. A coin-toss: one face of the coin being at 0 and the other face being at 1.  The Haldane prior probability distribution Beta(0,0) is an "improper prior" because its integration (from 0 to 1) fails to strictly converge to 1 due to the singularities at each end. However, this is not an issue for computing posterior probabilities unless the sample size is very small.  Furthermore, Zellner[64] points out that on the log-odds scale, (the logit transformation 
{\displaystyle \log(p/(1-p))}

), the Haldane prior is the uniformly flat prior. The fact that a uniform prior probability on the logit transformed variable ln(p/1 − p) (with domain (−∞, ∞)) is equivalent to the Haldane prior on the domain [0, 1] was pointed out by Harold Jeffreys in the first edition (1939) of his book Theory of Probability ([59] p. 123).  Jeffreys writes "Certainly if we take the Bayes–Laplace rule right up to the extremes we are led to results that do not correspond to anybody's way of thinking. The (Haldane) rule dx/(x(1 − x)) goes too far the other way.  It would lead to the conclusion that if a sample is of one type with respect to some property there is a probability 1 that the whole population is of that type."  The fact that "uniform" depends on the parametrization, led Jeffreys to seek a form of prior that would be invariant under different parametrizations.

Jeffreys' prior probability (Beta(1/2,1/2) for a Bernoulli or for a binomial distribution)[edit]
Main article: Jeffreys prior
Jeffreys prior probability for the beta distribution: the square root of the determinant of Fisher's information matrix: 
{\displaystyle \scriptstyle {\sqrt {\det({\mathcal {I}}(\alpha ,\beta ))}}={\sqrt {\psi _{1}(\alpha )\psi _{1}(\beta )-(\psi _{1}(\alpha )+\psi _{1}(\beta ))\psi _{1}(\alpha +\beta )}}}

 is a function of the trigamma function ψ1 of shape parameters α, β
Posterior Beta densities with samples having success = "s", failure = "f" of s/(s + f) = 1/2, and s + f = {3,10,50}, based on 3 different prior probability functions: Haldane (Beta(0,0), Jeffreys (Beta(1/2,1/2)) and Bayes (Beta(1,1)). The image shows that there is little difference between the priors for the posterior with sample size of 50 (with more pronounced peak near p = 1/2). Significant differences appear for very small sample sizes (the flatter distribution for sample size of 3)
Posterior Beta densities with samples having success = "s", failure = "f" of s/(s + f) = 1/4, and s + f ∈ {3,10,50}, based on three different prior probability functions: Haldane (Beta(0,0), Jeffreys (Beta(1/2,1/2)) and Bayes (Beta(1,1)). The image shows that there is little difference between the priors for the posterior with sample size of 50 (with more pronounced peak near p = 1/4).  Significant differences appear for very small sample sizes (the very skewed distribution for the degenerate case of sample size = 3, in this degenerate and unlikely case the Haldane prior results in a reverse "J" shape with mode at p = 0 instead of p = 1/4.  If there is sufficient sampling data, the three priors of Bayes (Beta(1,1)), Jeffreys (Beta(1/2,1/2)) and Haldane (Beta(0,0)) should yield similar posterior probability densities.
Posterior Beta densities with samples having success = s, failure = f of s/(s + f) = 1/4, and s + f ∈ {4,12,40}, based on three different prior probability functions: Haldane (Beta(0,0), Jeffreys (Beta(1/2,1/2)) and Bayes (Beta(1,1)). The image shows that there is little difference between the priors for the posterior with sample size of 40 (with more pronounced peak near p = 1/4). Significant differences appear for very small sample sizes
Harold Jeffreys[59][65] proposed to use an uninformative prior probability measure that should be invariant under reparameterization: proportional to the square root of the determinant of Fisher's information matrix.  For the Bernoulli distribution, this can be shown as follows: for a coin that is "heads" with probability p ∈ [0, 1] and is "tails" with probability 1 − p, for a given (H,T) ∈ {(0,1), (1,0)} the probability is pH(1 − p)T.  Since T = 1 − H, the Bernoulli distribution is pH(1 − p)1 − H. Considering p as the only parameter, it follows that the log likelihood for the Bernoulli distribution is
{\displaystyle \ln {\mathcal {L}}(p\mid H)=H\ln p+(1-H)\ln(1-p).}

The Fisher information matrix has only one component (it is a scalar, because there is only one parameter: p), therefore:
{\displaystyle {\begin{aligned}{\sqrt {{\mathcal {I}}(p)}}&={\sqrt {\operatorname {E} \!\left[\left({\frac {d}{dp}}\ln {\mathcal {L}}(p\mid H)\right)^{2}\right]}}\\[6pt]&={\sqrt {\operatorname {E} \!\left[\left({\frac {H}{p}}-{\frac {1-H}{1-p}}\right)^{2}\right]}}\\[6pt]&={\sqrt {p^{1}(1-p)^{0}\left({\frac {1}{p}}-{\frac {0}{1-p}}\right)^{2}+p^{0}(1-p)^{1}\left({\frac {0}{p}}-{\frac {1}{1-p}}\right)^{2}}}\\&={\frac {1}{\sqrt {p(1-p)}}}.\end{aligned}}}

Similarly, for the Binomial distribution with n Bernoulli trials, it can be shown that
{\displaystyle {\sqrt {{\mathcal {I}}(p)}}={\sqrt {\frac {n}{p(1-p)}}}.}

Thus, for the Bernoulli, and Binomial distributions, Jeffreys prior is proportional to 
{\displaystyle \scriptstyle {\frac {1}{\sqrt {p(1-p)}}}}

, which happens to be proportional to a beta distribution with domain variable x = p, and shape parameters α = β = 1/2, the arcsine distribution:

Beta
{\displaystyle \operatorname {Beta} ({\tfrac {1}{2}},{\tfrac {1}{2}})={\frac {1}{\pi {\sqrt {p(1-p)}}}}.}

It will be shown in the next section that the normalizing constant for Jeffreys prior is immaterial to the final result because the normalizing constant cancels out in Bayes' theorem for the posterior probability.  Hence Beta(1/2,1/2) is used as the Jeffreys prior for both Bernoulli and binomial distributions. As shown in the next section, when using this expression as a prior probability times the likelihood in Bayes' theorem, the posterior probability turns out to be a beta distribution. It is important to realize, however, that Jeffreys prior is proportional to 

1

p
(
1
−
p
)

{\textstyle {\frac {1}{\sqrt {p(1-p)}}}}

 for the Bernoulli and binomial distribution, but not for the beta distribution.  Jeffreys prior for the beta distribution is given by the determinant of Fisher's information for the beta distribution, which, as shown in the § Fisher information matrix  is a function of the trigamma function ψ1 of shape parameters α and β as follows:
{\displaystyle {\begin{aligned}{\sqrt {\det({\mathcal {I}}(\alpha ,\beta ))}}&={\sqrt {\psi _{1}(\alpha )\psi _{1}(\beta )-(\psi _{1}(\alpha )+\psi _{1}(\beta ))\psi _{1}(\alpha +\beta )}}\\\lim _{\alpha \to 0}{\sqrt {\det({\mathcal {I}}(\alpha ,\beta ))}}&=\lim _{\beta \to 0}{\sqrt {\det({\mathcal {I}}(\alpha ,\beta ))}}=\infty \\\lim _{\alpha \to \infty }{\sqrt {\det({\mathcal {I}}(\alpha ,\beta ))}}&=\lim _{\beta \to \infty }{\sqrt {\det({\mathcal {I}}(\alpha ,\beta ))}}=0\end{aligned}}}

As previously discussed, Jeffreys prior for the Bernoulli and binomial distributions is proportional to the arcsine distribution Beta(1/2,1/2), a one-dimensional curve that looks like a basin as a function of the parameter p of the Bernoulli and binomial distributions. The walls of the basin are formed by p approaching the singularities at the ends p → 0 and p → 1, where Beta(1/2,1/2) approaches infinity. Jeffreys prior for the beta distribution is a 2-dimensional surface (embedded in a three-dimensional space) that looks like a basin with only two of its walls meeting at the corner α = β = 0 (and missing the other two walls) as a function of the shape parameters α and β of the beta distribution. The two adjoining walls of this 2-dimensional surface are formed by the shape parameters α and β approaching the singularities (of the trigamma function) at α, β → 0. It has no walls for α, β → ∞ because in this case the determinant of Fisher's information matrix for the beta distribution approaches zero.
It will be shown in the next section that Jeffreys prior probability results in posterior probabilities (when multiplied by the binomial likelihood function) that are intermediate between the posterior probability results of the Haldane and Bayes prior probabilities.
Jeffreys prior may be difficult to obtain analytically, and for some cases it just doesn't exist (even for simple distribution functions like the asymmetric triangular distribution). Berger, Bernardo and Sun, in a 2009 paper[66]  defined a reference prior probability distribution that (unlike Jeffreys prior) exists for the asymmetric triangular distribution. They cannot obtain a closed-form expression for their reference prior, but numerical calculations show it to be nearly perfectly fitted by the (proper) prior

Beta
{\displaystyle \operatorname {Beta} ({\tfrac {1}{2}},{\tfrac {1}{2}})\sim {\frac {1}{\sqrt {\theta (1-\theta )}}}}

where θ is the vertex variable for the asymmetric triangular distribution with support [0, 1] (corresponding to the following parameter values in Wikipedia's article on the triangular distribution: vertex c = θ, left end a = 0, and right end b = 1). Berger et al. also give a heuristic argument that Beta(1/2,1/2) could indeed be the exact Berger–Bernardo–Sun reference prior for the asymmetric triangular distribution. Therefore, Beta(1/2,1/2) not only is Jeffreys prior for the Bernoulli and binomial distributions, but also seems to be the Berger–Bernardo–Sun reference prior for the asymmetric triangular distribution (for which the Jeffreys prior does not exist), a distribution used in project management and PERT analysis to describe the cost and duration of project tasks.
Clarke and Barron[67] prove that, among continuous positive priors, Jeffreys prior (when it exists) asymptotically maximizes Shannon's mutual information between a sample of size n and the parameter, and therefore Jeffreys prior is the most uninformative prior (measuring information as Shannon information). The proof rests on an examination of the Kullback–Leibler divergence between probability density functions for iid random variables.

Effect of different prior probability choices on the posterior beta distribution[edit]
If samples are drawn from the population of a random variable X that result in s successes and f failures in n Bernoulli trials n = s + f, then the likelihood function for parameters s and f given x = p (the notation x = p in the expressions below will emphasize that the domain x stands for the value of the parameter p in the binomial distribution), is the following binomial distribution:
{\displaystyle {\mathcal {L}}(s,f\mid x=p)={s+f \choose s}x^{s}(1-x)^{f}={n \choose s}x^{s}(1-x)^{n-s}.}

If beliefs about prior probability information are reasonably well approximated by a beta distribution with parameters α Prior and β Prior, then:

PriorProbability

(
x
=
p
;
α
Prior
,
β
Prior
)
=

x

α
Prior
−
1

(
1
−
x

)

β
Prior
−
1

B

(
α
Prior
,
β
Prior
)

{\displaystyle {\operatorname {PriorProbability} }(x=p;\alpha \operatorname {Prior} ,\beta \operatorname {Prior} )={\frac {x^{\alpha \operatorname {Prior} -1}(1-x)^{\beta \operatorname {Prior} -1}}{\mathrm {B} (\alpha \operatorname {Prior} ,\beta \operatorname {Prior} )}}}

According to Bayes' theorem for a continuous event space, the posterior probability density is given by the product of the prior probability and the likelihood function (given the evidence s and f = n − s), normalized so that the area under the curve equals one, as follows:

posterior probability density

(
x
=
p
∣
s
,
n
−
s
)

=

priorprobabilitydensity
⁡
(
x
=
p
;
α
prior
,
β
prior
)

L

(
s
,
f
∣
x
=
p
)

∫

0

1

prior probability density

(
x
=
p
;
α
prior
,
β
prior
)

L

(
s
,
f
∣
x
=
p
)

d
x

=

(

n
s

)

x

s
+
α
prior
−
1

(
1
−
x

)

n
−
s
+
β
prior
−
1

/

B

(
α
prior
,
β
prior
)

∫

0

1

(

(

n
s

)

x

s
+
α
prior
−
1

(
1
−
x

)

n
−
s
+
β
prior
−
1

/

B

(
α
prior
,
β
prior
)

)

d
x

=

x

s
+
α
prior
−
1

(
1
−
x

)

n
−
s
+
β
prior
−
1

∫

0

1

(

x

s
+
α
prior
−
1

(
1
−
x

)

n
−
s
+
β
prior
−
1

)

d
x

=

x

s
+
α
prior
−
1

(
1
−
x

)

n
−
s
+
β
prior
−
1

B

(
s
+
α
prior
,
n
−
s
+
β
prior
{\displaystyle {\begin{aligned}&{\text{posterior probability density}}(x=p\mid s,n-s)\\[6pt]={}&{\frac {\operatorname {priorprobabilitydensity} (x=p;\alpha \operatorname {prior} ,\beta \operatorname {prior} ){\mathcal {L}}(s,f\mid x=p)}{\int _{0}^{1}{\text{prior probability density}}(x=p;\alpha \operatorname {prior} ,\beta \operatorname {prior} ){\mathcal {L}}(s,f\mid x=p)\,dx}}\\[6pt]={}&{\frac {{n \choose s}x^{s+\alpha \operatorname {prior} -1}(1-x)^{n-s+\beta \operatorname {prior} -1}/\mathrm {B} (\alpha \operatorname {prior} ,\beta \operatorname {prior} )}{\int _{0}^{1}\left({n \choose s}x^{s+\alpha \operatorname {prior} -1}(1-x)^{n-s+\beta \operatorname {prior} -1}/\mathrm {B} (\alpha \operatorname {prior} ,\beta \operatorname {prior} )\right)\,dx}}\\[6pt]={}&{\frac {x^{s+\alpha \operatorname {prior} -1}(1-x)^{n-s+\beta \operatorname {prior} -1}}{\int _{0}^{1}\left(x^{s+\alpha \operatorname {prior} -1}(1-x)^{n-s+\beta \operatorname {prior} -1}\right)\,dx}}\\[6pt]={}&{\frac {x^{s+\alpha \operatorname {prior} -1}(1-x)^{n-s+\beta \operatorname {prior} -1}}{\mathrm {B} (s+\alpha \operatorname {prior} ,n-s+\beta \operatorname {prior} )}}.\end{aligned}}}

The binomial coefficient
{\displaystyle {s+f \choose s}={n \choose s}={\frac {(s+f)!}{s!f!}}={\frac {n!}{s!(n-s)!}}}

appears both in the numerator and the denominator of the posterior probability, and it does not depend on the integration variable x, hence it cancels out, and it is irrelevant to the final result.  Similarly the normalizing factor for the prior probability, the beta function B(αPrior,βPrior) cancels out and it is immaterial to the final result. The same posterior probability result can be obtained if one uses an un-normalized prior

x

α
prior
−
1

(
1
−
x

)

β
prior
−
1

{\displaystyle x^{\alpha \operatorname {prior} -1}(1-x)^{\beta \operatorname {prior} -1}}

because the normalizing factors all cancel out. Several authors (including Jeffreys himself) thus use an un-normalized prior formula since the normalization constant cancels out.  The numerator of the posterior probability ends up being just the (un-normalized) product of the prior probability and the likelihood function, and the denominator is its integral from zero to one. The beta function in the denominator, B(s + α Prior, n − s + β Prior), appears as a normalization constant to ensure that the total posterior probability integrates to unity.
The ratio s/n of the number of successes to the total number of trials is a sufficient statistic in the binomial case, which is relevant for the following results.
For the Bayes' prior probability (Beta(1,1)), the posterior probability is:

posteriorprobability
⁡
(
p
=
x
∣
s
,
f
)
=

x

s

(
1
−
x

)

n
−
s

B

(
s
+
1
,
n
−
s
+
1
)

,

 with mean 

=

s
+
1

n
+
2

,

 (and mode
{\displaystyle \operatorname {posteriorprobability} (p=x\mid s,f)={\frac {x^{s}(1-x)^{n-s}}{\mathrm {B} (s+1,n-s+1)}},{\text{ with mean }}={\frac {s+1}{n+2}},{\text{ (and mode}}={\frac {s}{n}}{\text{ if }}0<s<n).}

For the Jeffreys' prior probability (Beta(1/2,1/2)), the posterior probability is:

posteriorprobability
⁡
(
p
=
x
∣
s
,
f
)
=

x

s
−

1
2

(
1
−
x

)

n
−
s
−

1
2

B

(
s
+

1
2

,
n
−
s
+

1
2

)

,

 with mean

=

s
+

1
2

n
+
1

,

 (and mode
{\displaystyle \operatorname {posteriorprobability} (p=x\mid s,f)={x^{s-{\tfrac {1}{2}}}(1-x)^{n-s-{\frac {1}{2}}} \over \mathrm {B} (s+{\tfrac {1}{2}},n-s+{\tfrac {1}{2}})},{\text{ with mean}}={\frac {s+{\tfrac {1}{2}}}{n+1}},{\text{ (and mode}}={\frac {s-{\tfrac {1}{2}}}{n-1}}{\text{ if }}{\tfrac {1}{2}}<s<n-{\tfrac {1}{2}}).}

and for the Haldane prior probability (Beta(0,0)), the posterior probability is:

posteriorprobability
⁡
(
p
=
x
∣
s
,
f
)
=

x

s
−
1

(
1
−
x

)

n
−
s
−
1

B

(
s
,
n
−
s
)

,

 with mean

=

s
n

,

 (and mode
{\displaystyle \operatorname {posteriorprobability} (p=x\mid s,f)={\frac {x^{s-1}(1-x)^{n-s-1}}{\mathrm {B} (s,n-s)}},{\text{ with mean}}={\frac {s}{n}},{\text{ (and mode}}={\frac {s-1}{n-2}}{\text{ if }}1<s<n-1).}

From the above expressions it follows that for s/n = 1/2) all the above three prior probabilities result in the identical location for the posterior probability mean = mode = 1/2.  For s/n < 1/2, the mean of the posterior probabilities, using the following priors, are such that: mean for Bayes prior > mean for Jeffreys prior > mean for Haldane prior. For s/n > 1/2 the order of these inequalities is reversed such that the Haldane prior probability results in the largest posterior mean. The Haldane prior probability Beta(0,0) results in a posterior probability density with mean (the expected value for the probability of success in the "next" trial) identical to the ratio s/n of the number of successes to the total number of trials. Therefore, the Haldane prior results in a posterior probability with expected value in the next trial equal to the maximum likelihood. The Bayes prior probability Beta(1,1) results in a posterior probability density with mode identical to the ratio s/n (the maximum likelihood).
In the case that 100% of the trials have been successful s = n, the Bayes prior probability Beta(1,1) results in a posterior expected value equal to the rule of succession (n + 1)/(n + 2), while the Haldane prior Beta(0,0) results in a posterior expected value of 1 (absolute certainty of success in the next trial).  Jeffreys prior probability results in a posterior expected value equal to (n + 1/2)/(n + 1). Perks[61] (p. 303) points out: "This provides a new rule of succession and expresses a 'reasonable' position to take up, namely, that after an unbroken run of n successes we assume a probability for the next trial equivalent to the assumption that we are about half-way through an average run, i.e. that we expect a failure once in (2n + 2) trials. The Bayes–Laplace rule implies that we are about at the end of an average run or that we expect a failure once in (n + 2) trials. The comparison clearly favours the new result (what is now called Jeffreys prior) from the point of view of 'reasonableness'."
Conversely, in the case that 100% of the trials have resulted in failure (s = 0), the Bayes prior probability Beta(1,1) results in a posterior expected value for success in the next trial equal to 1/(n + 2), while the Haldane prior Beta(0,0) results in a posterior expected value of success in the next trial of 0 (absolute certainty of failure in the next trial). Jeffreys prior probability results in a posterior expected value for success in the next trial equal to (1/2)/(n + 1), which Perks[61] (p. 303) points out: "is a much more reasonably remote result than the Bayes–Laplace result 1/(n + 2)".
Jaynes[52] questions (for the uniform prior Beta(1,1)) the use of these formulas for the cases s = 0 or s = n because the integrals do not converge (Beta(1,1) is an improper prior for s = 0 or s = n). In practice, the conditions 0<s<n necessary for a mode to exist between both ends for the Bayes prior are usually met, and therefore the Bayes prior (as long as 0 < s < n) results in a posterior mode located between both ends of the domain.
As remarked in the section on the rule of succession, K. Pearson showed that after n successes in n trials the posterior probability (based on the Bayes Beta(1,1) distribution as the prior probability) that the next (n + 1) trials will all be successes is exactly 1/2, whatever the value of n. Based on the Haldane Beta(0,0) distribution as the prior probability, this posterior probability is 1 (absolute certainty that after n successes in n trials the next (n + 1) trials will all be successes). Perks[61] (p. 303) shows that, for what is now known as the Jeffreys prior, this probability is ((n + 1/2)/(n + 1))((n + 3/2)/(n + 2))...(2n + 1/2)/(2n + 1), which for n = 1, 2, 3 gives 15/24, 315/480, 9009/13440; rapidly approaching a limiting value of 

1

/

2

=
0.70710678
…

{\displaystyle 1/{\sqrt {2}}=0.70710678\ldots }

 as n tends to infinity.  Perks remarks that what is now known as the Jeffreys prior: "is clearly more 'reasonable' than either the Bayes–Laplace result or the result on the (Haldane) alternative rule rejected by Jeffreys which gives certainty as the probability. It clearly provides a very much better correspondence with the process of induction. Whether it is 'absolutely' reasonable for the purpose, i.e. whether it is yet large enough, without the absurdity of reaching unity, is a matter for others to decide. But it must be realized that the result depends on the assumption of complete indifference and absence of knowledge prior to the sampling experiment."
Following are the variances of the posterior distribution obtained with these three prior probability distributions:
for the Bayes' prior probability (Beta(1,1)), the posterior variance is:

variance

=

(
n
−
s
+
1
)
(
s
+
1
)

(
3
+
n
)
(
2
+
n

)

2

,

 which for 

s
=

n
2

 results in variance
{\displaystyle {\text{variance}}={\frac {(n-s+1)(s+1)}{(3+n)(2+n)^{2}}},{\text{ which for  }}s={\frac {n}{2}}{\text{ results in variance}}={\frac {1}{12+4n}}}

for the Jeffreys' prior probability (Beta(1/2,1/2)), the posterior variance is:

variance

=

(
n
−
s
+

1
2

)
(
s
+

1
2

)

(
2
+
n
)
(
1
+
n

)

2

,

 which for 

s
=

n
2

 results in var
{\displaystyle {\text{variance}}={\frac {(n-s+{\frac {1}{2}})(s+{\frac {1}{2}})}{(2+n)(1+n)^{2}}},{\text{ which for }}s={\frac {n}{2}}{\text{ results in var}}={\frac {1}{8+4n}}}

and for the Haldane prior probability (Beta(0,0)), the posterior variance is:

variance

=

(
n
−
s
)
s

(
1
+
n
)

n

2

,

 which for 

s
=

n
2

 results in variance
{\displaystyle {\text{variance}}={\frac {(n-s)s}{(1+n)n^{2}}},{\text{ which for  }}s={\frac {n}{2}}{\text{ results in variance}}={\frac {1}{4+4n}}}

So, as remarked by Silvey,[50] for large n, the variance is small and hence the posterior distribution is highly concentrated, whereas the assumed prior distribution was very diffuse.  This is in accord with what one would hope for, as vague prior knowledge is transformed (through Bayes' theorem) into a more precise posterior knowledge by an informative experiment.  For small n the Haldane Beta(0,0) prior results in the largest posterior variance while the Bayes Beta(1,1) prior results in the more concentrated posterior.  Jeffreys prior Beta(1/2,1/2) results in a posterior variance in between the other two.  As n increases, the variance rapidly decreases so that the posterior variance for all three priors converges to approximately the same value (approaching zero variance as n → ∞). Recalling the previous result that the Haldane prior probability Beta(0,0) results in a posterior probability density with mean (the expected value for the probability of success in the "next" trial) identical to the ratio s/n of the number of successes to the total number of trials, it follows from the above expression that also the Haldane prior Beta(0,0) results in a posterior with variance identical to the variance expressed in terms of the max. likelihood estimate s/n and sample size (in § Variance):

variance
{\displaystyle {\text{variance}}={\frac {\mu (1-\mu )}{1+\nu }}={\frac {(n-s)s}{(1+n)n^{2}}}}

with the mean μ = s/n and the sample size ν = n.
In Bayesian inference, using a prior distribution Beta(αPrior,βPrior) prior to a binomial distribution is equivalent to adding (αPrior − 1) pseudo-observations of "success" and (βPrior − 1) pseudo-observations of "failure" to the actual number of successes and failures observed, then estimating the parameter p of the binomial distribution by the proportion of successes over both real- and pseudo-observations.  A uniform prior Beta(1,1) does not add (or subtract) any pseudo-observations since for Beta(1,1) it follows that (αPrior − 1) = 0 and (βPrior − 1) = 0. The Haldane prior Beta(0,0) subtracts one pseudo observation from each and Jeffreys prior Beta(1/2,1/2) subtracts 1/2 pseudo-observation of success and an equal number of failure. This subtraction has the effect of smoothing out the posterior distribution.  If the proportion of successes is not 50% (s/n ≠ 1/2) values of αPrior and βPrior less than 1 (and therefore negative (αPrior − 1) and (βPrior − 1)) favor sparsity, i.e. distributions where the parameter p is closer to either 0 or 1.  In effect, values of αPrior and βPrior between 0 and 1, when operating together, function as a concentration parameter.
The accompanying plots show the posterior probability density functions for sample sizes n ∈ {3,10,50}, successes s ∈ {n/2,n/4} and Beta(αPrior,βPrior) ∈ {Beta(0,0),Beta(1/2,1/2),Beta(1,1)}. Also shown are the cases for n = {4,12,40}, success s = {n/4} and Beta(αPrior,βPrior) ∈ {Beta(0,0),Beta(1/2,1/2),Beta(1,1)}. The first plot shows the symmetric cases, for successes s ∈ {n/2}, with mean = mode = 1/2 and the second plot shows the skewed cases s ∈ {n/4}.  The images show that there is little difference between the priors for the posterior with sample size of 50 (characterized by a more pronounced peak near p = 1/2). Significant differences appear for very small sample sizes (in particular for the flatter distribution for the degenerate case of sample size = 3). Therefore, the skewed cases, with successes s = {n/4}, show a larger effect from the choice of prior, at small sample size, than the symmetric cases.  For symmetric distributions, the Bayes prior Beta(1,1) results in the most "peaky" and highest posterior distributions and the Haldane prior Beta(0,0) results in the flattest and lowest peak distribution.  The Jeffreys prior Beta(1/2,1/2) lies in between them.  For nearly symmetric, not too skewed distributions the effect of the priors is similar.  For very small sample size (in this case for a sample size of 3) and skewed distribution (in this example for s ∈ {n/4}) the Haldane prior can result in a reverse-J-shaped distribution with a singularity at the left end.  However, this happens only in degenerate cases (in this example n = 3 and hence s = 3/4 < 1, a degenerate value because s should be greater than unity in order for the posterior of the Haldane prior to have a mode located between the ends, and because s = 3/4 is not an integer number, hence it violates the initial assumption of a binomial distribution for the likelihood) and it is not an issue in generic cases of reasonable sample size (such that the condition 1 < s < n − 1, necessary for a mode to exist between both ends, is fulfilled).
In Chapter 12 (p. 385) of his book, Jaynes[52] asserts that the Haldane prior Beta(0,0) describes a prior state of knowledge of complete ignorance, where we are not even sure whether it is physically possible for an experiment to yield either a success or a failure, while the Bayes (uniform) prior Beta(1,1) applies if one knows that both binary outcomes are possible. Jaynes states: "interpret the Bayes–Laplace (Beta(1,1)) prior as describing not a state of complete ignorance, but the state of knowledge in which we have observed one success and one failure...once we have seen at least one success and one failure, then we know that the experiment is a true binary one, in the sense of physical possibility." Jaynes [52] does not specifically discuss Jeffreys prior Beta(1/2,1/2) (Jaynes discussion of "Jeffreys prior" on pp. 181, 423 and on chapter 12 of Jaynes book[52] refers instead to the improper, un-normalized, prior "1/p dp" introduced by Jeffreys in the 1939 edition of his book,[59] seven years before he introduced what is now known as Jeffreys' invariant prior: the square root of the determinant of Fisher's information matrix. "1/p" is Jeffreys' (1946) invariant prior for the exponential distribution, not for the Bernoulli or binomial distributions). However, it follows from the above discussion that Jeffreys Beta(1/2,1/2) prior represents a state of knowledge in between the Haldane Beta(0,0) and Bayes Beta (1,1) prior.
Similarly, Karl Pearson in his 1892 book The Grammar of Science[68][69] (p. 144 of 1900 edition)  maintained that the Bayes (Beta(1,1) uniform prior was not a complete ignorance prior, and that it should be used when prior information justified to "distribute our ignorance equally"".  K. Pearson wrote: "Yet the only supposition that we appear to have made is this: that, knowing nothing of nature, routine and anomy (from the Greek ανομία, namely: a- "without", and nomos "law") are to be considered as equally likely to occur.  Now we were not really justified in making even this assumption, for it involves a knowledge that we do not possess regarding nature.  We use our experience of the constitution and action of coins in general to assert that heads and tails are equally probable, but we have no right to assert before experience that, as we know nothing of nature, routine and breach are equally probable. In our ignorance we ought to consider before experience that nature may consist of all routines, all anomies (normlessness), or a mixture of the two in any proportion whatever, and that all such are equally probable. Which of these constitutions after experience is the most probable must clearly depend on what that experience has been like."
If there is sufficient sampling data, and the posterior probability mode is not located at one of the extremes of the domain (x = 0 or x = 1), the three priors of Bayes (Beta(1,1)), Jeffreys (Beta(1/2,1/2)) and Haldane (Beta(0,0)) should yield similar posterior probability densities.  Otherwise, as Gelman et al.[70] (p. 65) point out, "if so few data are available that the choice of noninformative prior distribution makes a difference, one should put relevant information into the prior distribution", or as Berger[4] (p. 125) points out "when different reasonable priors yield substantially different answers, can it be right to state that there is a single answer? Would it not be better to admit that there is scientific uncertainty, with the conclusion depending on prior beliefs?."

Occurrence and applications[edit]
Order statistics[edit]
Main article: Order statistic
The beta distribution has an important application in the theory of order statistics. A basic result is that the distribution of the kth smallest of a sample of size n from a continuous uniform distribution has a beta distribution.[40] This result is summarized as

U

(
k
)

∼
Beta
{\displaystyle U_{(k)}\sim \operatorname {Beta} (k,n+1-k).}

From this, and application of the theory related to the probability integral transform, the distribution of any individual order statistic from any continuous distribution can be derived.[40]

Subjective logic[edit]
Main article: Subjective logic
In standard logic, propositions are considered to be either true or false. In contradistinction, subjective logic assumes that humans cannot determine with absolute certainty whether a proposition about the real world is absolutely true or false. In subjective logic the posteriori probability estimates of binary events can be represented by beta distributions.[71]

Wavelet analysis[edit]
Main article: Beta wavelet
A wavelet is a wave-like oscillation with an amplitude that starts out at zero, increases, and then decreases back to zero. It can typically be visualized as a "brief oscillation" that promptly decays. Wavelets can be used to extract information from many different kinds of data, including – but certainly not limited to – audio signals and images. Thus, wavelets are purposefully crafted to have specific properties that make them useful for signal processing. Wavelets are localized in both time and frequency whereas the standard Fourier transform is only localized in frequency. Therefore, standard Fourier Transforms are only applicable to stationary processes, while wavelets are applicable to non-stationary processes.  Continuous wavelets can be constructed based on the beta distribution. Beta wavelets[72] can be viewed as a soft variety of Haar wavelets whose shape is fine-tuned by two shape parameters α and β.

Population genetics[edit]
Main article: Balding–Nichols model
Further information: F-statistics, Fixation index, and Coefficient of relationship
The Balding–Nichols model is a two-parameter parametrization of the beta distribution used in population genetics.[73]  It is a statistical description of the allele frequencies in the components of a sub-divided population:
{\displaystyle {\begin{aligned}\alpha &=\mu \nu ,\\\beta &=(1-\mu )\nu ,\end{aligned}}}

where 
{\displaystyle \nu =\alpha +\beta ={\frac {1-F}{F}}}
{\displaystyle 0<F<1}

; here F is (Wright's) genetic distance between two populations.

Project management: task cost and schedule modeling[edit]
The beta distribution can be used to model events which are constrained to take place within an interval defined by a minimum and maximum value. For this reason, the beta distribution — along with the triangular distribution — is used extensively in PERT, critical path method (CPM), Joint Cost Schedule Modeling (JCSM) and other project management/control systems to describe the time to completion and the cost of a task. In project management, shorthand computations are widely used to estimate the mean and standard deviation of the beta distribution:[39]
{\displaystyle {\begin{aligned}\mu (X)&={\frac {a+4b+c}{6}}\\[8pt]\sigma (X)&={\frac {c-a}{6}}\end{aligned}}}

where a is the minimum, c is the maximum, and b is the most likely value (the mode for α > 1 and β > 1).
The above estimate for the mean 
{\displaystyle \mu (X)={\frac {a+4b+c}{6}}}

 is known as the PERT three-point estimation and it is exact for either of the following values of β (for arbitrary α within these ranges):

β = α > 1 (symmetric case) with standard deviation 
{\displaystyle \sigma (X)={\frac {c-a}{2{\sqrt {1+2\alpha }}}}}

, skewness = 0, and excess kurtosis = 
{\displaystyle {\frac {-6}{3+2\alpha }}}

or

β = 6 − α for 5 > α > 1 (skewed case) with standard deviation
{\displaystyle \sigma (X)={\frac {(c-a){\sqrt {\alpha (6-\alpha )}}}{6{\sqrt {7}}}},}

skewness
{\displaystyle {}={\frac {(3-\alpha ){\sqrt {7}}}{2{\sqrt {\alpha (6-\alpha )}}}}}

, and excess kurtosis
{\displaystyle {}={\frac {21}{\alpha (6-\alpha )}}-3}

The above estimate for the standard deviation σ(X) = (c − a)/6 is exact for either of the following values of α and β:

α = β = 4 (symmetric) with skewness = 0, and excess kurtosis = −6/11.
{\displaystyle \alpha =3-{\sqrt {2}}}

 (right-tailed, positive skew) with skewness
{\displaystyle {}={\frac {1}{\sqrt {2}}}}

, and excess kurtosis = 0
{\displaystyle \alpha =3+{\sqrt {2}}}

 (left-tailed, negative skew) with skewness
{\displaystyle {}={\frac {-1}{\sqrt {2}}}}

, and excess kurtosis = 0

Otherwise, these can be poor approximations for beta distributions with other values of α and β, exhibiting average errors of 40% in the mean and 549% in the variance.[74][75][76]

Random variate generation[edit]
Further information: Non-uniform random variate generation
If X and Y are independent, with 
{\displaystyle X\sim \Gamma (\alpha ,\theta )}
{\displaystyle Y\sim \Gamma (\beta ,\theta )}

 then
{\displaystyle {\frac {X}{X+Y}}\sim \mathrm {B} (\alpha ,\beta ).}

So one algorithm for generating beta variates is to generate 
{\displaystyle {\frac {X}{X+Y}}}

, where X is a gamma variate with parameters (α, 1) and Y is an independent gamma variate with parameters (β, 1).[77]  In fact, here 
{\displaystyle {\frac {X}{X+Y}}}
{\displaystyle X+Y}

 are independent, and 
{\displaystyle X+Y\sim \Gamma (\alpha +\beta ,\theta )}
{\displaystyle Z\sim \Gamma (\gamma ,\theta )}
{\displaystyle Z}

 is independent of 

X

{\displaystyle X}
{\displaystyle Y}

, then 
{\displaystyle {\frac {X+Y}{X+Y+Z}}\sim \mathrm {B} (\alpha +\beta ,\gamma )}
{\displaystyle {\frac {X+Y}{X+Y+Z}}}

 is independent of 
{\displaystyle {\frac {X}{X+Y}}}

. This shows that the product of independent 
{\displaystyle \mathrm {B} (\alpha ,\beta )}
{\displaystyle \mathrm {B} (\alpha +\beta ,\gamma )}

 random variables is a 
{\displaystyle \mathrm {B} (\alpha ,\beta +\gamma )}

 random variable.
Also, the kth order statistic of n uniformly distributed variates is 
{\displaystyle \mathrm {B} (k,n+1-k)}

, so an alternative if α and β are small integers is to generate α + β − 1 uniform variates and choose the α-th smallest.[40]
Another way to generate the Beta distribution is by Pólya urn model. According to this method, one starts with an "urn" with α "black" balls and β "white" balls and draws uniformly with replacement. Every trial an additional ball is added according to the color of the last ball which was drawn. Asymptotically, the proportion of black and white balls will be distributed according to the Beta distribution, where each repetition of the experiment will produce a different value.
It is also possible to use the inverse transform sampling.

Normal approximation to the Beta distribution[edit]
A beta distribution 
{\displaystyle \mathrm {B} (\alpha ,\beta )}

  with α ~ β and α and β >> 1 is approximately normal with mean 1/2 and variance 1/(4(2α + 1)). If α ≥ β the normal approximation can be improved by taking the cube-root of the logarithm of the reciprocal of 
{\displaystyle \mathrm {B} (\alpha ,\beta )}

[78][79]

History[edit]
Thomas Bayes, in a posthumous paper [62] published in 1763 by Richard Price, obtained a beta distribution as the density of the probability of success in Bernoulli trials (see § Applications, Bayesian inference), but the paper does not analyze any of the moments of the beta distribution or discuss any of its properties.

Karl Pearson analyzed the beta distribution as the solution Type I of Pearson distributions 
The first systematic modern discussion of the beta distribution is probably due to Karl Pearson.[80][81] In Pearson's papers[21][33] the beta distribution is couched as a solution of a differential equation: Pearson's Type I distribution which it is essentially identical to except for arbitrary shifting and re-scaling (the beta and Pearson Type I distributions can always be equalized by proper choice of parameters). In fact, in several English books and journal articles in the few decades prior to World War II, it was common to refer to the beta distribution as Pearson's Type I distribution.  William P. Elderton in his 1906 monograph "Frequency curves and correlation"[42] further analyzes the beta distribution as Pearson's Type I distribution, including a full discussion of the method of moments for the four parameter case, and diagrams of (what Elderton describes as) U-shaped, J-shaped, twisted J-shaped, "cocked-hat" shapes, horizontal and angled straight-line cases.  Elderton wrote "I am chiefly indebted to Professor Pearson, but the indebtedness is of a kind for which it is impossible to offer formal thanks."  Elderton in his 1906 monograph [42] provides an impressive amount of information on the beta distribution, including equations for the origin of the distribution chosen to be the mode, as well as for other Pearson distributions: types I through VII. Elderton also included a number of appendixes, including one appendix ("II") on the beta and gamma functions. In later editions, Elderton added equations for the origin of the distribution chosen to be the mean, and analysis of Pearson distributions VIII through XII.
As remarked by Bowman and Shenton[44] "Fisher and Pearson had a difference of opinion in the approach to (parameter) estimation, in particular relating to (Pearson's method of) moments and (Fisher's method of) maximum likelihood in the case of the Beta distribution." Also according to Bowman and Shenton, "the case of a Type I (beta distribution) model being the center of the controversy was pure serendipity. A more difficult model of 4 parameters would have been hard to find." The long running public conflict of Fisher with Karl Pearson can be followed in a number of articles in prestigious journals.  For example, concerning the estimation of the four parameters for the beta distribution, and Fisher's criticism of Pearson's method of moments as being arbitrary, see Pearson's article "Method of moments and method of maximum likelihood" [45] (published three years after his retirement from University College, London, where his position had been divided between Fisher and Pearson's son Egon) in which Pearson writes "I read (Koshai's paper in the Journal of the Royal Statistical Society, 1933) which as far as I am aware is the only case at present published of the application of Professor Fisher's method. To my astonishment that method depends on first working out the constants of the frequency curve by the (Pearson) Method of Moments and then superposing on it, by what Fisher terms "the Method of Maximum Likelihood" a further approximation to obtain, what he holds, he will thus get, 'more efficient values' of the curve constants".
David and Edwards's treatise on the history of statistics[82] cites the first modern treatment of the beta distribution, in 1911,[83]  using the beta designation that has become standard, due to Corrado Gini, an Italian statistician, demographer, and sociologist, who developed the Gini coefficient. N.L.Johnson and S.Kotz, in their comprehensive and very informative monograph[84]  on leading historical personalities in statistical sciences credit Corrado Gini[85]  as "an early Bayesian...who dealt with the problem of eliciting the parameters of an initial Beta distribution, by singling out techniques which anticipated the advent of the so-called empirical Bayes approach."
