# Dirichlet distribution

Probability distribution

| Dirichlet distribution |
| --- |
| Probability density function |
| Parameters | K ≥ 2 {\displaystyle K\geq 2} number of categories (integer) α = ( α 1 , … , α K ) {\displaystyle {\boldsymbol {\alpha }}=(\alpha _{1},\ldots ,\alpha _{K})} concentration parameters, where α i > 0 {\displaystyle \alpha _{i}>0} ${\displaystyle K\geq 2}$ ${\displaystyle {\boldsymbol {\alpha }}=(\alpha _{1},\ldots ,\alpha _{K})}$ ${\displaystyle \alpha _{i}>0}$ |
| Support | x 1 , … , x K {\displaystyle x_{1},\ldots ,x_{K}} where x i ∈ [ 0 , 1 ] {\displaystyle x_{i}\in [0,1]} and ∑ i = 1 K x i = 1 {\displaystyle \sum _{i=1}^{K}x_{i}=1} (i.e. a K − 1 {\displaystyle K-1} simplex) ${\displaystyle x_{1},\ldots ,x_{K}}$ ${\displaystyle x_{i}\in [0,1]}$ ${\displaystyle \sum _{i=1}^{K}x_{i}=1}$ ${\displaystyle K-1}$ |
| PDF | 1 B ( α ) ∏ i = 1 K x i α i − 1 {\displaystyle {\frac {1}{\mathrm {B} ({\boldsymbol {\alpha }})}}\prod _{i=1}^{K}x_{i}^{\alpha _{i}-1}} where B ( α ) = ∏ i = 1 K Γ ( α i ) Γ ( α 0 ) {\displaystyle \mathrm {B} ({\boldsymbol {\alpha }})={\frac {\prod _{i=1}^{K}\Gamma (\alpha _{i})}{\Gamma {\bigl (}\alpha _{0}{\bigr )}}}} where α 0 = ∑ i = 1 K α i {\displaystyle \alpha _{0}=\sum _{i=1}^{K}\alpha _{i}} ${\displaystyle {\frac {1}{\mathrm {B} ({\boldsymbol {\alpha }})}}\prod _{i=1}^{K}x_{i}^{\alpha _{i}-1}}$ ${\displaystyle \mathrm {B} ({\boldsymbol {\alpha }})={\frac {\prod _{i=1}^{K}\Gamma (\alpha _{i})}{\Gamma {\bigl (}\alpha _{0}{\bigr )}}}}$ ${\displaystyle \alpha _{0}=\sum _{i=1}^{K}\alpha _{i}}$ |
| Mean | E ⁡ [ X i ] = α i α 0 {\displaystyle \operatorname {E} [X_{i}]={\frac {\alpha _{i}}{\alpha _{0}}}} E ⁡ [ ln ⁡ X i ] = ψ ( α i ) − ψ ( α 0 ) {\displaystyle \operatorname {E} [\ln X_{i}]=\psi (\alpha _{i})-\psi (\alpha _{0})} (where ψ {\displaystyle \psi } is the digamma function) ${\displaystyle \operatorname {E} [X_{i}]={\frac {\alpha _{i}}{\alpha _{0}}}}$ ${\displaystyle \operatorname {E} [\ln X_{i}]=\psi (\alpha _{i})-\psi (\alpha _{0})}$ ${\displaystyle \psi }$ |
| Mode | x i = α i − 1 α 0 − K , α i > 1. {\displaystyle x_{i}={\frac {\alpha _{i}-1}{\alpha _{0}-K}},\quad \alpha _{i}>1.} ${\displaystyle x_{i}={\frac {\alpha _{i}-1}{\alpha _{0}-K}},\quad \alpha _{i}>1.}$ |
| Variance | Var ⁡ [ X i ] = α ~ i ( 1 − α ~ i ) α 0 + 1 , {\displaystyle \operatorname {Var} [X_{i}]={\frac {{\tilde {\alpha }}_{i}(1-{\tilde {\alpha }}_{i})}{\alpha _{0}+1}},} Cov ⁡ [ X i , X j ] = δ i j α ~ i − α ~ i α ~ j α 0 + 1 {\displaystyle \operatorname {Cov} [X_{i},X_{j}]={\frac {\delta _{ij}\,{\tilde {\alpha }}_{i}-{\tilde {\alpha }}_{i}{\tilde {\alpha }}_{j}}{\alpha _{0}+1}}} where α ~ i = α i α 0 {\displaystyle {\tilde {\alpha }}_{i}={\frac {\alpha _{i}}{\alpha _{0}}}} , and δ i j {\displaystyle \delta _{ij}} is the Kronecker delta ${\displaystyle \operatorname {Var} [X_{i}]={\frac {{\tilde {\alpha }}_{i}(1-{\tilde {\alpha }}_{i})}{\alpha _{0}+1}},}$ ${\displaystyle \operatorname {Cov} [X_{i},X_{j}]={\frac {\delta _{ij}\,{\tilde {\alpha }}_{i}-{\tilde {\alpha }}_{i}{\tilde {\alpha }}_{j}}{\alpha _{0}+1}}}$ ${\displaystyle {\tilde {\alpha }}_{i}={\frac {\alpha _{i}}{\alpha _{0}}}}$ ${\displaystyle \delta _{ij}}$ |
| Entropy | H ( X ) = log ⁡ B ( α ) {\displaystyle H(X)=\log \mathrm {B} ({\boldsymbol {\alpha }})} + ( α 0 − K ) ψ ( α 0 ) − {\displaystyle +(\alpha _{0}-K)\psi (\alpha _{0})-} ∑ j = 1 K ( α j − 1 ) ψ ( α j ) {\displaystyle \sum _{j=1}^{K}(\alpha _{j}-1)\psi (\alpha _{j})} with α 0 {\displaystyle \alpha _{0}} defined as for variance, above; and ψ {\displaystyle \psi } is the digamma function ${\displaystyle H(X)=\log \mathrm {B} ({\boldsymbol {\alpha }})}$ ${\displaystyle +(\alpha _{0}-K)\psi (\alpha _{0})-}$ ${\displaystyle \sum _{j=1}^{K}(\alpha _{j}-1)\psi (\alpha _{j})}$ ${\displaystyle \alpha _{0}}$ ${\displaystyle \psi }$ |
| Method of moments | α i = E [ X i ] ( E [ X j ] ( 1 − E [ X j ] ) V [ X j ] − 1 ) {\displaystyle \alpha _{i}=E[X_{i}]\left({\frac {E[X_{j}](1-E[X_{j}])}{V[X_{j}]}}-1\right)} where j is any index, possibly i itself ${\displaystyle \alpha _{i}=E[X_{i}]\left({\frac {E[X_{j}](1-E[X_{j}])}{V[X_{j}]}}-1\right)}$ |

In probability and statistics, the Dirichlet distribution (after Peter Gustav Lejeune Dirichlet), often denoted 
{\displaystyle \operatorname {Dir} ({\boldsymbol {\alpha }})}

, is a family of continuous multivariate probability distributions parameterized by a vector α of positive reals. It is a multivariate generalization of the beta distribution,[1] hence its alternative name of multivariate beta distribution (MBD).[2]  Dirichlet distributions are commonly used as prior distributions in Bayesian statistics, and in fact, the Dirichlet distribution is the conjugate prior of the categorical distribution and multinomial distribution. ${\displaystyle \operatorname {Dir} ({\boldsymbol {\alpha }})}$

The infinite-dimensional generalization of the Dirichlet distribution is the Dirichlet process.

Definitions[edit]
Probability density function[edit]
Illustrating how the log of the density function changes when 
{\displaystyle K=3}

 as we change the vector 

α

{\displaystyle {\boldsymbol {\alpha }}}

 from 
{\displaystyle {\boldsymbol {\alpha }}=(0.3,0.3,0.3)}
{\displaystyle (2.0,2.0,2.0)}

, keeping all the individual 
{\displaystyle \alpha _{i}}

's equal to each other.
The Dirichlet distribution of order 
{\displaystyle K\geq 2}

 with parameters 
{\displaystyle \alpha _{1},\ldots ,\alpha _{K}>0}

 has a probability density function given by
{\displaystyle f\left(x_{1},\ldots ,x_{K};\alpha _{1},\ldots ,\alpha _{K}\right)={\frac {1}{\mathrm {B} ({\boldsymbol {\alpha }})}}\prod _{i=1}^{K}x_{i}^{\alpha _{i}-1}}

where 

x

i

∈

[

0
,
1

]

 for all 
{\displaystyle x_{i}\in \left[0,1\right]{\mbox{ for all }}i\in \{1,\dots ,K\}{\mbox{ and }}\sum _{i=1}^{K}x_{i}=1\,.}

That is, the probability density function is defined on the standard 
{\displaystyle K-1}

 simplex embedded in ⁠

K

{\displaystyle K}

⁠-dimensional Euclidean space, 
{\displaystyle \mathbb {R} ^{K}}

.
The normalizing constant is the multivariate beta function, which can be expressed in terms of the gamma function:
{\displaystyle \mathrm {B} ({\boldsymbol {\alpha }})={\frac {\prod \limits _{i=1}^{K}\Gamma (\alpha _{i})}{\Gamma \left(\sum \limits _{i=1}^{K}\alpha _{i}\right)}},\qquad {\boldsymbol {\alpha }}=(\alpha _{1},\ldots ,\alpha _{K}).}

Support[edit]
The support of the Dirichlet distribution is the set of K-dimensional vectors x whose entries are real numbers in the interval [0,1] such that 
{\displaystyle \|{\boldsymbol {x}}\|_{1}=1}

, i.e. the sum of the coordinates is equal to 1.  These can be viewed as the probabilities of a K-way categorical event. Another way to express this is that the domain of the Dirichlet distribution is itself a set of probability distributions, specifically the set of K-dimensional discrete distributions. The technical term for the set of points in the support of a K-dimensional Dirichlet distribution is the open standard (K − 1)-simplex,[3] which is a generalization of a triangle, embedded in the next-higher dimension.  For example, with K = 3, the support is an equilateral triangle embedded in a downward-angle fashion in three-dimensional space, with vertices at (1,0,0), (0,1,0) and (0,0,1), i.e. touching each of the coordinate axes at a point 1 unit away from the origin.

Special cases[edit]
A common special case is the symmetric Dirichlet distribution, where all of the elements making up the parameter vector α have the same value.  The symmetric case might be useful, for example, when a Dirichlet prior over components is called for, but there is no prior knowledge favoring one component over another.  Since all elements of the parameter vector have the same value, the symmetric Dirichlet distribution can be parametrized by a single scalar value α, called the concentration parameter. In terms of α, the density function has the form
{\displaystyle f(x_{1},\dots ,x_{K};\alpha )={\frac {\Gamma (\alpha K)}{\Gamma (\alpha )^{K}}}\prod _{i=1}^{K}x_{i}^{\alpha -1}.}

When α = 1,[1] the symmetric Dirichlet distribution is equivalent to a uniform distribution over the open standard (K−1)-simplex, i.e. it is uniform over all points in its support. This particular distribution is known as the flat Dirichlet distribution. Values of the concentration parameter above 1 prefer variates that are dense, evenly distributed distributions, i.e. all the values within a single sample are similar to each other.  Values of the concentration parameter below 1 prefer sparse distributions, i.e. most of the values within a single sample will be close to 0, and the vast majority of the mass will be concentrated in a few of the values.
When α = 1/2, the distribution is the same as would be obtained by choosing a point uniformly at random from the surface of a (K−1)-dimensional unit hypersphere and squaring each coordinate.  The α = 1/2 distribution is the Jeffreys prior for the Dirichlet distribution.
More generally, the parameter vector is sometimes written as the product 
{\displaystyle \alpha {\boldsymbol {n}}}

 of a (scalar) concentration parameter α and a (vector) base measure 
{\displaystyle {\boldsymbol {n}}=(n_{1},\dots ,n_{K})}

 where n lies within the (K − 1)-simplex (i.e.: its coordinates 
{\displaystyle n_{i}}

 sum to one). The concentration parameter in this case is larger by a factor of K than the concentration parameter for a symmetric Dirichlet distribution described above. This construction ties in with concept of a base measure when discussing Dirichlet processes and is often used in the topic modelling literature.

^  If we define the concentration parameter as the sum of the Dirichlet parameters for each dimension, the Dirichlet distribution with concentration parameter K, the dimension of the distribution, is the uniform distribution on the (K − 1)-simplex.

Properties[edit]
Moments[edit]
{\displaystyle X=(X_{1},\ldots ,X_{K})\sim \operatorname {Dir} ({\boldsymbol {\alpha }})}
{\displaystyle \alpha _{0}=\sum _{i=1}^{K}\alpha _{i}.}

Then[4][5]
{\displaystyle \operatorname {E} [X_{i}]={\frac {\alpha _{i}}{\alpha _{0}}},}
{\displaystyle \operatorname {Var} [X_{i}]={\frac {\alpha _{i}(\alpha _{0}-\alpha _{i})}{\alpha _{0}^{2}(\alpha _{0}+1)}}.}

Furthermore, if 
{\displaystyle i\neq j}
{\displaystyle \operatorname {Cov} [X_{i},X_{j}]={\frac {-\alpha _{i}\alpha _{j}}{\alpha _{0}^{2}(\alpha _{0}+1)}}.}

The covariance matrix is singular.
More generally, moments of Dirichlet-distributed random variables can be expressed in the following way. For 
{\displaystyle {\boldsymbol {t}}=(t_{1},\dotsc ,t_{K})\in \mathbb {R} ^{K}}

, denote by 
{\displaystyle {\boldsymbol {t}}^{\circ i}=(t_{1}^{i},\dotsc ,t_{K}^{i})}

 its i-th Hadamard power. Then,[6]
{\displaystyle \operatorname {E} \left[({\boldsymbol {t}}\cdot {\boldsymbol {X}})^{n}\right]={\frac {n!\,\Gamma (\alpha _{0})}{\Gamma (\alpha _{0}+n)}}\sum {\frac {{t_{1}}^{k_{1}}\cdots {t_{K}}^{k_{K}}}{k_{1}!\cdots k_{K}!}}\prod _{i=1}^{K}{\frac {\Gamma (\alpha _{i}+k_{i})}{\Gamma (\alpha _{i})}}={\frac {n!\,\Gamma (\alpha _{0})}{\Gamma (\alpha _{0}+n)}}Z_{n}({\boldsymbol {t}}^{\circ 1}\cdot {\boldsymbol {\alpha }},\cdots ,{\boldsymbol {t}}^{\circ n}\cdot {\boldsymbol {\alpha }}),}

where the sum is over non-negative integers 
{\displaystyle k_{1},\ldots ,k_{K}}

 with 
{\displaystyle n=k_{1}+\cdots +k_{K}}

, and 
{\displaystyle Z_{n}}

 is the cycle index polynomial of the Symmetric group of degree n.
We have the special case 
{\displaystyle \operatorname {E} \left[{\boldsymbol {t}}\cdot {\boldsymbol {X}}\right]={\frac {{\boldsymbol {t}}\cdot {\boldsymbol {\alpha }}}{\alpha _{0}}}.}

The multivariate analogue 

E
⁡

[

(

t

1

⋅

X

)

n

1

⋯
(

t

q

⋅

X

)

n

q

]

{\textstyle \operatorname {E} \left[({\boldsymbol {t}}_{1}\cdot {\boldsymbol {X}})^{n_{1}}\cdots ({\boldsymbol {t}}_{q}\cdot {\boldsymbol {X}})^{n_{q}}\right]}

 for vectors 
{\displaystyle {\boldsymbol {t}}_{1},\dotsc ,{\boldsymbol {t}}_{q}\in \mathbb {R} ^{K}}

 can be expressed[7] in terms of a color pattern of the exponents 
{\displaystyle n_{1},\dotsc ,n_{q}}

 in the sense of the Pólya enumeration theorem.
Particular cases include the simple computation[8]
{\displaystyle \operatorname {E} \left[\prod _{i=1}^{K}X_{i}^{\beta _{i}}\right]={\frac {B\left({\boldsymbol {\alpha }}+{\boldsymbol {\beta }}\right)}{B\left({\boldsymbol {\alpha }}\right)}}={\frac {\Gamma \left(\sum \limits _{i=1}^{K}\alpha _{i}\right)}{\Gamma \left[\sum \limits _{i=1}^{K}(\alpha _{i}+\beta _{i})\right]}}\times \prod _{i=1}^{K}{\frac {\Gamma (\alpha _{i}+\beta _{i})}{\Gamma (\alpha _{i})}}.}

Mode[edit]
The mode of the distribution is[9] the vector (x1, ..., xK) with
{\displaystyle x_{i}={\frac {\alpha _{i}-1}{\alpha _{0}-K}},\qquad \alpha _{i}>1.}

Marginal distributions[edit]
The marginal distributions are beta distributions:[10]

X

i

∼
Beta
{\displaystyle X_{i}\sim \operatorname {Beta} (\alpha _{i},\alpha _{0}-\alpha _{i}).}

Also see § Related distributions below.

Conjugate to categorical or multinomial[edit]
The Dirichlet distribution is the conjugate prior distribution of the categorical distribution (a generic discrete probability distribution with a given number of possible outcomes) and multinomial distribution (the distribution over observed counts of each possible category in a set of categorically distributed observations).  This means that if a data point has either a categorical or multinomial distribution, and the prior distribution of the distribution's parameter (the vector of probabilities that generates the data point) is distributed as a Dirichlet, then the posterior distribution of the parameter is also a Dirichlet.  Intuitively, in such a case, starting from what we know about the parameter prior to observing the data point, we then can update our knowledge based on the data point and end up with a new distribution of the same form as the old one.  This means that we can successively update our knowledge of a parameter by incorporating new observations one at a time, without running into mathematical difficulties.
Formally, this can be expressed as follows.  Given a model

α

=

(

α

1

,
…
,

α

K

)

=

concentration hyperparameter
{\displaystyle {\begin{array}{rcccl}{\boldsymbol {\alpha }}&=&\left(\alpha _{1},\ldots ,\alpha _{K}\right)&=&{\text{concentration hyperparameter}}\\\mathbf {p} \mid {\boldsymbol {\alpha }}&=&\left(p_{1},\ldots ,p_{K}\right)&\sim &\operatorname {Dir} (K,{\boldsymbol {\alpha }})\\\mathbb {X} \mid \mathbf {p} &=&\left(\mathbf {x} _{1},\ldots ,\mathbf {x} _{K}\right)&\sim &\operatorname {Cat} (K,\mathbf {p} )\end{array}}}

then the following holds:

c

=

(

c

1

,
…
,

c

K

)

=

number of occurrences of category 
{\displaystyle {\begin{array}{rcccl}\mathbf {c} &=&\left(c_{1},\ldots ,c_{K}\right)&=&{\text{number of occurrences of category }}i\\\mathbf {p} \mid \mathbb {X} ,{\boldsymbol {\alpha }}&\sim &\operatorname {Dir} (K,\mathbf {c} +{\boldsymbol {\alpha }})&=&\operatorname {Dir} \left(K,c_{1}+\alpha _{1},\ldots ,c_{K}+\alpha _{K}\right)\end{array}}}

This relationship is used in Bayesian statistics to estimate the underlying parameter p of a categorical distribution given a collection of N samples. Intuitively, we can view the hyperprior vector α as pseudocounts, i.e. as representing the number of observations in each category that we have already seen.  Then we simply add in the counts for all the new observations (the vector c) in order to derive the posterior distribution.
In Bayesian mixture models and other hierarchical Bayesian models with mixture components, Dirichlet distributions are commonly used as the prior distributions for the categorical variables appearing in the models.  See the section on applications below for more information.

Relation to Dirichlet-multinomial distribution[edit]
In a model where a Dirichlet prior distribution is placed over a set of categorical-valued observations, the marginal joint distribution of the observations (i.e. the joint distribution of the observations, with the prior parameter marginalized out) is a Dirichlet-multinomial distribution.  This distribution plays an important role in hierarchical Bayesian models, because when doing inference over such models using methods such as Gibbs sampling or variational Bayes, Dirichlet prior distributions are often marginalized out.  See the article on this distribution for more details.

Entropy[edit]
If X is a 
{\displaystyle \operatorname {Dir} ({\boldsymbol {\alpha }})}

 random variable, the differential entropy of X (in nat units) is[11]
{\displaystyle h({\boldsymbol {X}})=\operatorname {E} [-\ln f({\boldsymbol {X}})]=\ln \operatorname {B} ({\boldsymbol {\alpha }})+(\alpha _{0}-K)\psi (\alpha _{0})-\sum _{j=1}^{K}(\alpha _{j}-1)\psi (\alpha _{j})}

where 

ψ

{\displaystyle \psi }

 is the digamma function.
The following formula for 
{\displaystyle \operatorname {E} [\ln(X_{i})]}

 can be used to derive the differential entropy above. Since the functions 
{\displaystyle \ln(X_{i})}

 are the sufficient statistics of the Dirichlet distribution, the exponential family differential identities can be used to get an analytic expression for the expectation of 
{\displaystyle \ln(X_{i})}

 (see equation (2.62) in [12]) and its associated covariance matrix:
{\displaystyle \operatorname {E} [\ln(X_{i})]=\psi (\alpha _{i})-\psi (\alpha _{0})}
{\displaystyle \operatorname {Cov} [\ln(X_{i}),\ln(X_{j})]=\psi '(\alpha _{i})\delta _{ij}-\psi '(\alpha _{0})}

where 

ψ

{\displaystyle \psi }

 is the digamma function, 
{\displaystyle \psi '}

 is the trigamma function, and 
{\displaystyle \delta _{ij}}

 is the Kronecker delta.
The spectrum of Rényi information for values other than 
{\displaystyle \lambda =1}

 is given by[13]
{\displaystyle F_{R}(\lambda )=(1-\lambda )^{-1}\left(-\lambda \log \mathrm {B} ({\boldsymbol {\alpha }})+\sum _{i=1}^{K}\log \Gamma (\lambda (\alpha _{i}-1)+1)-\log \Gamma (\lambda (\alpha _{0}-K)+K)\right)}

and the information entropy is the limit as 

λ

{\displaystyle \lambda }

 goes to 1.
Another related interesting measure is the entropy of a discrete categorical (one-of-K binary) vector Z with probability-mass distribution X, i.e.,  
{\displaystyle P(Z_{i}=1,Z_{j\neq i}=0|{\boldsymbol {X}})=X_{i}}

. The conditional information entropy of Z, given X is
{\displaystyle S({\boldsymbol {X}})=H({\boldsymbol {Z}}|{\boldsymbol {X}})=\operatorname {E} _{\boldsymbol {Z}}[-\log P({\boldsymbol {Z}}|{\boldsymbol {X}})]=\sum _{i=1}^{K}-X_{i}\log X_{i}}

This function of X is a scalar random variable. If X has a symmetric Dirichlet distribution with all 
{\displaystyle \alpha _{i}=\alpha }

, the expected value of the entropy (in nat units) is[14]
{\displaystyle \operatorname {E} [S({\boldsymbol {X}})]=\sum _{i=1}^{K}\operatorname {E} [-X_{i}\ln X_{i}]=\psi (K\alpha +1)-\psi (\alpha +1)}

Kullback–Leibler divergence[edit]
The Kullback–Leibler (KL) divergence between two Dirichlet distributions, 
{\displaystyle {\text{Dir}}({\boldsymbol {\alpha }})}
{\displaystyle {\text{Dir}}({\boldsymbol {\beta }})}

, over the same simplex is:[15]
{\displaystyle {\begin{aligned}D_{\mathrm {KL} }{\big (}\mathrm {Dir} ({\boldsymbol {\alpha }})\,\|\,\mathrm {Dir} ({\boldsymbol {\beta }}){\big )}&=\log {\frac {\Gamma \left(\sum _{i=1}^{K}\alpha _{i}\right)}{\Gamma \left(\sum _{i=1}^{K}\beta _{i}\right)}}+\sum _{i=1}^{K}\left[\log {\frac {\Gamma (\beta _{i})}{\Gamma (\alpha _{i})}}+(\alpha _{i}-\beta _{i})\left(\psi (\alpha _{i})-\psi \left(\sum _{j=1}^{K}\alpha _{j}\right)\right)\right]\end{aligned}}}

Aggregation[edit]
{\displaystyle X=(X_{1},\ldots ,X_{K})\sim \operatorname {Dir} (\alpha _{1},\ldots ,\alpha _{K})}

then, if the random variables with subscripts i and j are dropped from the vector and replaced by their sum,
{\displaystyle X'=(X_{1},\ldots ,X_{i}+X_{j},\ldots ,X_{K})\sim \operatorname {Dir} (\alpha _{1},\ldots ,\alpha _{i}+\alpha _{j},\ldots ,\alpha _{K}).}

This aggregation property may be used to derive the marginal distribution of 
{\displaystyle X_{i}}

 mentioned above.

Neutrality[edit]
Main article: Neutral vector
{\displaystyle X=(X_{1},\ldots ,X_{K})\sim \operatorname {Dir} ({\boldsymbol {\alpha }})}

, then the vector X is said to be neutral[16] in the sense that XK is independent of 
{\displaystyle X^{(-K)}}

[3] where
{\displaystyle X^{(-K)}=\left({\frac {X_{1}}{1-X_{K}}},{\frac {X_{2}}{1-X_{K}}},\ldots ,{\frac {X_{K-1}}{1-X_{K}}}\right),}

and similarly for removing any of 
{\displaystyle X_{2},\ldots ,X_{K-1}}

. Observe that any permutation of X is also neutral (a property not possessed by samples drawn from a generalized Dirichlet distribution).[17]
Combining this with the property of aggregation it follows that Xj + ... + XK is independent of 
{\displaystyle \left({\frac {X_{1}}{X_{1}+\cdots +X_{j-1}}},{\frac {X_{2}}{X_{1}+\cdots +X_{j-1}}},\ldots ,{\frac {X_{j-1}}{X_{1}+\cdots +X_{j-1}}}\right)}

. In fact it is true, further, for the Dirichlet distribution, that for 
{\displaystyle 3\leq j\leq K-1}

, the pair 
{\displaystyle \left(X_{1}+\cdots +X_{j-1},X_{j}+\cdots +X_{K}\right)}

, and the two vectors 
{\displaystyle \left({\frac {X_{1}}{X_{1}+\cdots +X_{j-1}}},{\frac {X_{2}}{X_{1}+\cdots +X_{j-1}}},\ldots ,{\frac {X_{j-1}}{X_{1}+\cdots +X_{j-1}}}\right)}
{\displaystyle \left({\frac {X_{j}}{X_{j}+\cdots +X_{K}}},{\frac {X_{j+1}}{X_{j}+\cdots +X_{K}}},\ldots ,{\frac {X_{K}}{X_{j}+\cdots +X_{K}}}\right)}

, viewed as triple of normalised random vectors, are mutually independent. The analogous result is true for partition of the indices {1, 2, ..., K} into any other pair of non-singleton subsets.

Characteristic function[edit]
The characteristic function of the Dirichlet distribution is a confluent form of the Lauricella hypergeometric series.  It is given by Phillips as[18]
{\displaystyle CF\left(s_{1},\ldots ,s_{K-1}\right)=\operatorname {E} \left(e^{i\left(s_{1}X_{1}+\cdots +s_{K-1}X_{K-1}\right)}\right)=\Psi ^{\left[K-1\right]}(\alpha _{1},\ldots ,\alpha _{K-1};\alpha _{0};is_{1},\ldots ,is_{K-1})}

where
{\displaystyle \Psi ^{[m]}(a_{1},\ldots ,a_{m};c;z_{1},\ldots z_{m})=\sum {\frac {(a_{1})_{k_{1}}\cdots (a_{m})_{k_{m}}\,z_{1}^{k_{1}}\cdots z_{m}^{k_{m}}}{(c)_{k}\,k_{1}!\cdots k_{m}!}}.}

The sum is over non-negative integers 
{\displaystyle k_{1},\ldots ,k_{m}}
{\displaystyle k=k_{1}+\cdots +k_{m}}

.  Phillips goes on to state that this form is "inconvenient for numerical calculation" and gives an alternative in terms of a complex path integral:
{\displaystyle \Psi ^{[m]}={\frac {\Gamma (c)}{2\pi i}}\int _{L}e^{t}\,t^{a_{1}+\cdots +a_{m}-c}\,\prod _{j=1}^{m}(t-z_{j})^{-a_{j}}\,dt}

where L denotes any path in the complex plane originating at 
{\displaystyle -\infty }

, encircling in the positive direction all the singularities of the integrand and returning to 
{\displaystyle -\infty }

.

Inequality[edit]
Probability density function 
{\displaystyle f\left(x_{1},\ldots ,x_{K-1};\alpha _{1},\ldots ,\alpha _{K}\right)}

 plays a key role in a multifunctional inequality which implies various bounds for the Dirichlet distribution.[19]
Another inequality relates the moment-generating function of the Dirichlet distribution to the convex conjugate of the scaled reversed Kullback-Leibler divergence:[20]
{\displaystyle \log \operatorname {E} \left(\exp {\sum _{i=1}^{K}s_{i}X_{i}}\right)\leq \sup _{p}\sum _{i=1}^{K}\left(p_{i}s_{i}-\alpha _{i}\log \left({\frac {\alpha _{i}}{\alpha _{0}p_{i}}}\right)\right),}

where the supremum is taken over p spanning the (K − 1)-simplex.

Related distributions[edit]
When 
{\displaystyle {\boldsymbol {X}}=(X_{1},\ldots ,X_{K})\sim \operatorname {Dir} \left(\alpha _{1},\ldots ,\alpha _{K}\right)}

, the marginal distribution of each component 

X

i

∼
Beta
{\displaystyle X_{i}\sim \operatorname {Beta} (\alpha _{i},\alpha _{0}-\alpha _{i})}

, a Beta distribution. In particular, if K = 2 then 

X

1

∼
Beta
{\displaystyle X_{1}\sim \operatorname {Beta} (\alpha _{1},\alpha _{2})}

 is equivalent to 
{\displaystyle {\boldsymbol {X}}=(X_{1},1-X_{1})\sim \operatorname {Dir} \left(\alpha _{1},\alpha _{2}\right)}

.  
For K independently distributed Gamma distributions:

Y

1

∼
Gamma
⁡
(

α

1

,
θ
)
,
…
,

Y

K

∼
Gamma
{\displaystyle Y_{1}\sim \operatorname {Gamma} (\alpha _{1},\theta ),\ldots ,Y_{K}\sim \operatorname {Gamma} (\alpha _{K},\theta )}

we have:[21]: 402 

V
=

∑

i
=
1

K

Y

i

∼
Gamma
{\displaystyle V=\sum _{i=1}^{K}Y_{i}\sim \operatorname {Gamma} \left(\alpha _{0},\theta \right),}
{\displaystyle X=(X_{1},\ldots ,X_{K})=\left({\frac {Y_{1}}{V}},\ldots ,{\frac {Y_{K}}{V}}\right)\sim \operatorname {Dir} \left(\alpha _{1},\ldots ,\alpha _{K}\right).}

Although the Xis are not independent from one another, they can be seen to be generated from a set of K independent gamma random variables.[21]: 594  Unfortunately, since the sum V is lost in forming X (in fact it can be shown that V is stochastically independent of X), it is not possible to recover the original gamma random variables from these values alone. Nevertheless, because independent random variables are simpler to work with, this reparametrization can still be useful for proofs about properties of the Dirichlet distribution.

Conjugate prior of the Dirichlet distribution[edit]
Because the Dirichlet distribution is an exponential family distribution it has a conjugate prior.
The conjugate prior is of the form:[22]
{\displaystyle \operatorname {CD} ({\boldsymbol {\alpha }}\mid {\boldsymbol {v}},\eta )\propto \left({\frac {1}{\operatorname {B} ({\boldsymbol {\alpha }})}}\right)^{\eta }\exp \left(-\sum _{k}v_{k}\alpha _{k}\right).}

Here 

v

{\displaystyle {\boldsymbol {v}}}

 is a K-dimensional real vector and 

η

{\displaystyle \eta }

 is a scalar parameter.  The domain of 
{\displaystyle ({\boldsymbol {v}},\eta )}

 is restricted to the set of parameters for which the above unnormalized density function can be normalized. The (necessary and sufficient) condition is:[23]
{\displaystyle \forall k\;\;v_{k}>0\;\;\;\;{\text{ and }}\;\;\;\;\eta >-1\;\;\;\;{\text{ and }}\;\;\;\;(\eta \leq 0\;\;\;\;{\text{ or }}\;\;\;\;\sum _{k}\exp -{\frac {v_{k}}{\eta }}<1)}

The conjugation property can be expressed as

if [prior: 
{\displaystyle {\boldsymbol {\alpha }}\sim \operatorname {CD} (\cdot \mid {\boldsymbol {v}},\eta )}

] and [observation: 

x

∣

α

∼
Dirichlet
{\displaystyle {\boldsymbol {x}}\mid {\boldsymbol {\alpha }}\sim \operatorname {Dirichlet} (\cdot \mid {\boldsymbol {\alpha }})}

] then [posterior: 
{\displaystyle {\boldsymbol {\alpha }}\mid {\boldsymbol {x}}\sim \operatorname {CD} (\cdot \mid {\boldsymbol {v}}-\log {\boldsymbol {x}},\eta +1)}

].
In the published literature there is no practical algorithm to efficiently generate samples from 
{\displaystyle \operatorname {CD} ({\boldsymbol {\alpha }}\mid {\boldsymbol {v}},\eta )}

.

Generalization by scaling and translation of log-probabilities[edit]
As noted above, Dirichlet variates can be generated by normalizing independent gamma variates. If instead one normalizes generalized gamma variates, one obtains variates from the simplicial generalized beta distribution (SGB).[24] On the other hand, SGB variates can also be obtained by applying the softmax function to scaled and translated logarithms of Dirichlet variates. Specifically, let 
{\displaystyle \mathbf {x} =(x_{1},\ldots ,x_{K})\sim \operatorname {Dir} ({\boldsymbol {\alpha }})}

 and let 
{\displaystyle \mathbf {y} =(y_{1},\ldots ,y_{K})}

, where applying the logarithm elementwise:

y

=
softmax
⁡
(

a

−
1

log
⁡

x

+
log
⁡

b

)

⟺

x

=
softmax
{\displaystyle \mathbf {y} =\operatorname {softmax} (a^{-1}\log \mathbf {x} +\log \mathbf {b} )\;\iff \;\mathbf {x} =\operatorname {softmax} (a\log \mathbf {y} -a\log \mathbf {b} )}
{\displaystyle y_{k}={\frac {b_{k}x_{k}^{1/a}}{\sum _{i=1}^{K}b_{i}x_{i}^{1/a}}}\;\iff \;x_{k}={\frac {(y_{k}/b_{k})^{a}}{\sum _{i=1}^{K}(y_{i}/b_{i})^{a}}}}

where 
{\displaystyle a>0}
{\displaystyle \mathbf {b} =(b_{1},\ldots ,b_{K})}

, with all 
{\displaystyle b_{k}>0}

, then 
{\displaystyle \mathbf {y} \sim \operatorname {SGB} (a,\mathbf {b} ,{\boldsymbol {\alpha }})}

. The SGB density function can be derived by noting that the transformation 
{\displaystyle \mathbf {x} \mapsto \mathbf {y} }

, which is a bijection from the simplex to itself, induces a differential volume change factor[25] of:
{\displaystyle R(\mathbf {y} ,a,\mathbf {b} )=a^{1-K}\prod _{k=1}^{K}{\frac {y_{k}}{x_{k}}}}

where it is understood that 

x

{\displaystyle \mathbf {x} }

 is recovered as a function of 

y

{\displaystyle \mathbf {y} }

, as shown above. This facilitates writing the SGB density in terms of the Dirichlet density, as:
{\displaystyle f_{\text{SGB}}(\mathbf {y} \mid a,\mathbf {b} ,{\boldsymbol {\alpha }})={\frac {f_{\text{Dir}}(\mathbf {x} \mid {\boldsymbol {\alpha }})}{R(\mathbf {y} ,a,\mathbf {b} )}}}

This generalization of the Dirichlet density, via a change of variables, is closely related to a normalizing flow, while it must be noted that the differential volume change is not given by the Jacobian determinant of 
{\displaystyle \mathbf {x} \mapsto \mathbf {y} :\mathbb {R} ^{K}\to \mathbb {R} ^{K}}

 which is zero, but by the Jacobian determinant of 
{\displaystyle (x_{1},\ldots ,x_{K-1})\mapsto \mathbf {(} y_{1},\ldots ,y_{K-1})}

, as explained in more detail at Normalizing flow § Simplex flow.
For further insight into the interaction between the Dirichlet shape parameters 

α

{\displaystyle {\boldsymbol {\alpha }}}

, and the transformation parameters 
{\displaystyle a,\mathbf {b} }

, it may be helpful to consider the logarithmic marginals, 
{\displaystyle \log {\frac {x_{k}}{1-x_{k}}}}

, which follow the logistic-beta distribution, 
{\displaystyle B_{\sigma }(\alpha _{k},\sum _{i\neq k}\alpha _{i})}

. See in particular the sections on tail behaviour and generalization with location and scale parameters.      

Application[edit]
When 
{\displaystyle b_{1}=b_{2}=\cdots =b_{K}}

, then the transformation simplifies to 

x

↦
softmax
{\displaystyle \mathbf {x} \mapsto \operatorname {softmax} (a^{-1}\log \mathbf {x} )}

, which is known as temperature scaling in machine learning, where it is used as a calibration transform for multiclass probabilistic classifiers.[26] Traditionally the temperature parameter (

a

{\displaystyle a}

 here) is learnt discriminatively by minimizing multiclass cross-entropy over a supervised calibration data set with known class labels. But the above PDF transformation mechanism can be used to facilitate also the design of generatively trained calibration models with a temperature scaling component.

Occurrence and applications[edit]
Bayesian models[edit]
Dirichlet distributions are most commonly used as the prior distribution of categorical variables or multinomial variables in Bayesian mixture models and other hierarchical Bayesian models. (In many fields, such as in natural language processing, categorical variables are often imprecisely called "multinomial variables".  Such a usage is unlikely to cause confusion, just as when Bernoulli distributions and binomial distributions are commonly conflated.)
Inference over hierarchical Bayesian models is often done using Gibbs sampling, and in such a case, instances of the Dirichlet distribution are typically marginalized out of the model by integrating out the Dirichlet random variable.  This causes the various categorical variables drawn from the same Dirichlet random variable to become correlated, and the joint distribution over them assumes a Dirichlet-multinomial distribution, conditioned on the hyperparameters of the Dirichlet distribution (the concentration parameters).  One of the reasons for doing this is that Gibbs sampling of the Dirichlet-multinomial distribution is extremely easy; see that article for more information.

Intuitive interpretations of the parameters[edit]
The concentration parameter[edit]
Dirichlet distributions are very often used as prior distributions in Bayesian inference.  The simplest and perhaps most common type of Dirichlet prior is the symmetric Dirichlet distribution, where all parameters are equal.  This corresponds to the case where you have no prior information to favor one component over any other.  As described above, the single value α to which all parameters are set is called the concentration parameter.  If the sample space of the Dirichlet distribution is interpreted as a discrete probability distribution, then intuitively the concentration parameter can be thought of as determining how "concentrated" the probability mass of the Dirichlet distribution to its center, leading to samples with mass dispersed almost equally among all components, i.e., with a value much less than 1, the mass will be highly concentrated in a few components, and all the rest will have almost no mass, and with a value much greater than 1, the mass will be dispersed almost equally among all the components.  See the article on the concentration parameter for further discussion.

String cutting[edit]
One example use of the Dirichlet distribution is if one wanted to cut strings (each of initial length 1.0) into K pieces with different lengths, where each piece had a designated average length, but allowing some variation in the relative sizes of the pieces. Recall that 
{\displaystyle \alpha _{0}=\sum _{i=1}^{K}\alpha _{i}.}
{\displaystyle \alpha _{i}/\alpha _{0}}

 values specify the mean lengths of the cut pieces of string resulting from the distribution.  The variance around this mean varies inversely with 
{\displaystyle \alpha _{0}}

.

Example of Dirichlet(1/2,1/3,1/6) distribution
Pólya's urn[edit]
Consider an urn containing balls of K different colors. Initially, the urn contains α1 balls of color 1, α2 balls of color 2, and so on. Now perform N draws from the urn, where after each draw, the ball is placed back into the urn with an additional ball of the same color. In the limit as N approaches infinity, the proportions of different colored balls in the urn will be distributed as Dir(α1, ..., αK).[27]
For a formal proof, note that the proportions of the different colored balls form a bounded [0,1]K-valued martingale, hence by the martingale convergence theorem, these proportions converge almost surely and in mean to a limiting random vector. To see that this limiting vector has the above Dirichlet distribution, check that all mixed moments agree.
Each draw from the urn modifies the probability of drawing a ball of any one color from the urn in the future. This modification diminishes with the number of draws, since the relative effect of adding a new ball to the urn diminishes as the urn accumulates increasing numbers of balls.

Random variate generation[edit]
Further information: Non-uniform random variate generation
From gamma distribution[edit]
With a source of Gamma-distributed random variates, one can easily sample a random vector 
{\displaystyle x=(x_{1},\ldots ,x_{K})}

 from the K-dimensional Dirichlet distribution with parameters 
{\displaystyle (\alpha _{1},\ldots ,\alpha _{K})}

 . First, draw K independent random samples 
{\displaystyle y_{1},\ldots ,y_{K}}

 from Gamma distributions each with density

Gamma
{\displaystyle \operatorname {Gamma} (\alpha _{i},1)={\frac {y_{i}^{\alpha _{i}-1}\;e^{-y_{i}}}{\Gamma (\alpha _{i})}},\!}

and then set
{\displaystyle x_{i}={\frac {y_{i}}{\sum _{j=1}^{K}y_{j}}}.}

[Proof]
The joint distribution of the independently sampled gamma variates, 
{\displaystyle \{y_{i}\}}

, is given by the product:
{\displaystyle e^{-\sum _{i}y_{i}}\prod _{i=1}^{K}{\frac {y_{i}^{\alpha _{i}-1}}{\Gamma (\alpha _{i})}}}

Next, one uses a change of variables, parametrising 
{\displaystyle \{y_{i}\}}

 in terms of 
{\displaystyle y_{1},y_{2},\ldots ,y_{K-1}}
{\displaystyle \sum _{i=1}^{K}y_{i}}

 , and performs a change of variables from  
{\displaystyle y\to x}

 such that 
{\displaystyle {\bar {x}}=\textstyle \sum _{i=1}^{K}y_{i},x_{1}={\frac {y_{1}}{\bar {x}}},x_{2}={\frac {y_{2}}{\bar {x}}},\ldots ,x_{K-1}={\frac {y_{K-1}}{\bar {x}}}}

. Each of the variables 
{\displaystyle 0\leq x_{1},x_{2},\ldots ,x_{k-1}\leq 1}

 and likewise 
{\displaystyle 0\leq \textstyle \sum _{i=1}^{K-1}x_{i}\leq 1}

. One must then use the change of variables formula, 
{\displaystyle P(x)=P(y(x)){\bigg |}{\frac {\partial y}{\partial x}}{\bigg |}}

 in which 
{\displaystyle {\bigg |}{\frac {\partial y}{\partial x}}{\bigg |}}

 is the transformation Jacobian. Writing y explicitly as a function of x, one obtains 
{\displaystyle y_{1}={\bar {x}}x_{1},y_{2}={\bar {x}}x_{2}\ldots y_{K-1}={\bar {x}}x_{K-1},y_{K}={\bar {x}}(1-\textstyle \sum _{i=1}^{K-1}x_{i})}

The Jacobian now looks like
{\displaystyle {\begin{vmatrix}{\bar {x}}&0&\ldots &x_{1}\\0&{\bar {x}}&\ldots &x_{2}\\\vdots &\vdots &\ddots &\vdots \\-{\bar {x}}&-{\bar {x}}&\ldots &1-\sum _{i=1}^{K-1}x_{i}\end{vmatrix}}}

The determinant can be evaluated by noting that it remains unchanged if multiples of a row are added to another row, and adding each of the first K-1 rows to the bottom row to obtain
{\displaystyle {\begin{vmatrix}{\bar {x}}&0&\ldots &x_{1}\\0&{\bar {x}}&\ldots &x_{2}\\\vdots &\vdots &\ddots &\vdots \\0&0&\ldots &1\end{vmatrix}}}

which can be expanded about the bottom row to obtain the determinant value 
{\displaystyle {\bar {x}}^{K-1}}

. Substituting for x in the joint pdf and including the Jacobian determinant, one obtains:
{\displaystyle {\begin{aligned}&{\frac {\left[\prod _{i=1}^{K-1}({\bar {x}}x_{i})^{\alpha _{i}-1}\right]\left[{\bar {x}}(1-\sum _{i=1}^{K-1}x_{i})\right]^{\alpha _{K}-1}}{\prod _{i=1}^{K}\Gamma (\alpha _{i})}}{\bar {x}}^{K-1}e^{-{\bar {x}}}\\=&{\frac {\Gamma ({\bar {\alpha }})\left[\prod _{i=1}^{K-1}(x_{i})^{\alpha _{i}-1}\right]\left[1-\sum _{i=1}^{K-1}x_{i}\right]^{\alpha _{K}-1}}{\prod _{i=1}^{K}\Gamma (\alpha _{i})}}\times {\frac {{\bar {x}}^{{\bar {\alpha }}-1}e^{-{\bar {x}}}}{\Gamma ({\bar {\alpha }})}}\end{aligned}}}

where 
{\displaystyle {\bar {\alpha }}=\textstyle \sum _{i=1}^{K}\alpha _{i}}

. The right-hand side can be recognized as the product of a Dirichlet pdf for the 
{\displaystyle x_{i}}

 and a gamma pdf for 
{\displaystyle {\bar {x}}}

. The product form shows the Dirichlet and gamma variables are independent, so the latter can be integrated out by simply omitting it, to obtain:
{\displaystyle x_{1},x_{2},\ldots ,x_{K-1}\sim {\frac {(1-\sum _{i=1}^{K-1}x_{i})^{\alpha _{K}-1}\prod _{i=1}^{K-1}x_{i}^{\alpha _{i}-1}}{B({\boldsymbol {\alpha }})}}}

Which is equivalent to
{\displaystyle {\frac {\prod _{i=1}^{K}x_{i}^{\alpha _{i}-1}}{B({\boldsymbol {\alpha }})}}}

 with support 
{\displaystyle \sum _{i=1}^{K}x_{i}=1}

Below is example Python code to draw the sample:

params = [a1, a2, ..., ak]
sample = [random.gammavariate(a, 1) for a in params]
sample = [v / sum(sample) for v in sample]

This formulation is correct regardless of how the Gamma distributions are parameterized (shape/scale vs. shape/rate) because they are equivalent when scale and rate equal 1.0.

From marginal beta distributions[edit]
A less efficient algorithm[28] relies on the univariate marginal and conditional distributions being beta and proceeds as follows.  Simulate 
{\displaystyle x_{1}}

 from

Beta
{\displaystyle {\textrm {Beta}}\left(\alpha _{1},\sum _{i=2}^{K}\alpha _{i}\right)}

Then simulate 
{\displaystyle x_{2},\ldots ,x_{K-1}}

 in order, as follows.  For 
{\displaystyle j=2,\ldots ,K-1}

, simulate 
{\displaystyle \phi _{j}}

 from

Beta
{\displaystyle {\textrm {Beta}}\left(\alpha _{j},\sum _{i=j+1}^{K}\alpha _{i}\right),}

and let
{\displaystyle x_{j}=\left(1-\sum _{i=1}^{j-1}x_{i}\right)\phi _{j}.}

Finally, set
{\displaystyle x_{K}=1-\sum _{i=1}^{K-1}x_{i}.}

This iterative procedure corresponds closely to the "string cutting" intuition described above.
Below is example Python code to draw the sample:

params = [a1, a2, ..., ak]
xs = [random.betavariate(params[0], sum(params[1:]))]
for j in range(1, len(params) - 1):
    phi = random.betavariate(params[j], sum(params[j + 1 :]))
    xs.append((1 - sum(xs)) * phi)
xs.append(1 - sum(xs))

When each alpha is 1[edit]
When α1 = ... = αK = 1, a sample from the distribution can be found by randomly drawing a set of K − 1 values independently and uniformly from the interval [0, 1], adding the values 0 and 1 to the set to make it have K + 1 values, sorting the set, and computing the difference between each pair of order-adjacent values, to give x1, ..., xK.

When each alpha is 1/2 and relationship to the hypersphere[edit]
When α1 = ... = αK = 1/2, a sample from the distribution can be found by randomly drawing K values independently from the standard normal distribution, squaring these values, and normalizing them by dividing by their sum, to give x1, ..., xK.
A point (x1, ..., xK) can be drawn uniformly at random from the (K−1)-dimensional unit hypersphere (which is the surface of a K-dimensional hyperball) via a similar procedure.  Randomly draw K values independently from the standard normal distribution and normalize these coordinate values by dividing each by the constant that is the square root of the sum of their squares.
