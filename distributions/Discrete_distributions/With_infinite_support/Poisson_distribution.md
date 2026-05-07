# Poisson distribution

Discrete probability distribution

| Poisson distribution |
| --- |
| Probability mass functionThe horizontal axis is the index k, the number of occurrences. λ is the expected rate of occurrences. The vertical axis is the probability of k occurrences given λ. The function is defined only at integer values of k; the connecting lines are only guides for the eye. |
| Cumulative distribution functionThe horizontal axis is the index k, the number of occurrences. The CDF is discontinuous at the integers of k and flat everywhere else because a variable that is Poisson distributed takes on only integer values. |
| Notation | Pois ⁡ ( λ ) {\displaystyle \operatorname {Pois} (\lambda )} ${\displaystyle \operatorname {Pois} (\lambda )}$ |
| Parameters | λ ∈ ( 0 , ∞ ) {\displaystyle \lambda \in (0,\infty )} (rate) ${\displaystyle \lambda \in (0,\infty )}$ |
| Support | k ∈ N 0 {\displaystyle k\in \mathbb {N} _{0}} (Natural numbers starting from 0) ${\displaystyle k\in \mathbb {N} _{0}}$ |
| PMF | λ k e − λ k ! {\displaystyle {\frac {\lambda ^{k}e^{-\lambda }}{k!}}} ${\displaystyle {\frac {\lambda ^{k}e^{-\lambda }}{k!}}}$ |
| CDF | Γ ( ⌊ k + 1 ⌋ , λ ) ⌊ k ⌋ ! , {\displaystyle {\frac {\Gamma (\lfloor k+1\rfloor ,\lambda )}{\lfloor k\rfloor !}},} or e − λ ∑ j = 0 ⌊ k ⌋ λ j j ! , {\displaystyle e^{-\lambda }\sum _{j=0}^{\lfloor k\rfloor }{\frac {\lambda ^{j}}{j!}},} or Q ( ⌊ k + 1 ⌋ , λ ) {\displaystyle Q(\lfloor k+1\rfloor ,\lambda )} (for k ≥ 0 , {\displaystyle k\geq 0,} where Γ ( x , y ) {\displaystyle \Gamma (x,y)} is the upper incomplete gamma function, ⌊ k ⌋ {\displaystyle \lfloor k\rfloor } is the floor function, and Q {\displaystyle Q} is the regularized gamma function) ${\displaystyle {\frac {\Gamma (\lfloor k+1\rfloor ,\lambda )}{\lfloor k\rfloor !}},}$ ${\displaystyle e^{-\lambda }\sum _{j=0}^{\lfloor k\rfloor }{\frac {\lambda ^{j}}{j!}},}$ ${\displaystyle Q(\lfloor k+1\rfloor ,\lambda )}$ ${\displaystyle k\geq 0,}$ ${\displaystyle \Gamma (x,y)}$ ${\displaystyle \lfloor k\rfloor }$ ${\displaystyle Q}$ |
| Mean | λ {\displaystyle \lambda } ${\displaystyle \lambda }$ |
| Median | ≈ ⌊ λ + 1 3 − 1 50 λ ⌋ {\displaystyle \approx \left\lfloor \lambda +{\frac {1}{3}}-{\frac {1}{50\lambda }}\right\rfloor } ${\displaystyle \approx \left\lfloor \lambda +{\frac {1}{3}}-{\frac {1}{50\lambda }}\right\rfloor }$ |
| Mode | ⌈ λ ⌉ − 1 , ⌊ λ ⌋ {\displaystyle \left\lceil \lambda \right\rceil -1,\left\lfloor \lambda \right\rfloor } ${\displaystyle \left\lceil \lambda \right\rceil -1,\left\lfloor \lambda \right\rfloor }$ |
| Variance | λ {\displaystyle \lambda } ${\displaystyle \lambda }$ |
| Skewness | 1 λ {\displaystyle {\frac {1}{\sqrt {\lambda }}}} ${\displaystyle {\frac {1}{\sqrt {\lambda }}}}$ |
| Excess kurtosis | 1 λ {\displaystyle {\frac {1}{\lambda }}} ${\displaystyle {\frac {1}{\lambda }}}$ |
| Entropy | λ [ 1 − log ⁡ ( λ ) ] + e − λ ∑ k = 0 ∞ λ k log ⁡ ( k ! ) k ! {\displaystyle \lambda {\Bigl [}1-\log(\lambda ){\Bigr ]}+e^{-\lambda }\sum _{k=0}^{\infty }{\frac {\lambda ^{k}\log(k!)}{k!}}} or for large λ {\displaystyle \lambda } ≈ 1 2 log ⁡ ( 2 π e λ ) − 1 12 λ − 1 24 λ 2 − 19 360 λ 3 + O ( 1 λ 4 ) {\displaystyle {\begin{aligned}\approx {\frac {1}{2}}\log \left(2\pi e\lambda \right)-{\frac {1}{12\lambda }}-{\frac {1}{24\lambda ^{2}}}\\-{\frac {19}{360\lambda ^{3}}}+{\mathcal {O}}\left({\frac {1}{\lambda ^{4}}}\right)\end{aligned}}} ${\displaystyle \lambda {\Bigl [}1-\log(\lambda ){\Bigr ]}+e^{-\lambda }\sum _{k=0}^{\infty }{\frac {\lambda ^{k}\log(k!)}{k!}}}$ ${\displaystyle \lambda }$ ${\displaystyle {\begin{aligned}\approx {\frac {1}{2}}\log \left(2\pi e\lambda \right)-{\frac {1}{12\lambda }}-{\frac {1}{24\lambda ^{2}}}\\-{\frac {19}{360\lambda ^{3}}}+{\mathcal {O}}\left({\frac {1}{\lambda ^{4}}}\right)\end{aligned}}}$ |
| MGF | exp ⁡ [ λ ( e t − 1 ) ] {\displaystyle \exp \left[\lambda \left(e^{t}-1\right)\right]} ${\displaystyle \exp \left[\lambda \left(e^{t}-1\right)\right]}$ |
| CF | exp ⁡ [ λ ( e i t − 1 ) ] {\displaystyle \exp \left[\lambda \left(e^{it}-1\right)\right]} ${\displaystyle \exp \left[\lambda \left(e^{it}-1\right)\right]}$ |
| PGF | exp ⁡ [ λ ( z − 1 ) ] {\displaystyle \exp \left[\lambda \left(z-1\right)\right]} ${\displaystyle \exp \left[\lambda \left(z-1\right)\right]}$ |
| Fisher information | 1 λ {\displaystyle {\frac {1}{\lambda }}} ${\displaystyle {\frac {1}{\lambda }}}$ |

In probability theory and statistics, the Poisson distribution (/ˈpwɑːsɒn/) is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time if these events occur with a known constant mean rate and independently of the time since the last event.[1] It can also be used for the number of events in other types of intervals than time, and in dimension greater than 1 (e.g., number of events in a given area or volume).
The Poisson distribution is named after French mathematician Siméon Denis Poisson. It plays an important role for discrete-stable distributions.

Under a Poisson distribution with the expectation of λ events in a given interval, the probability of k events in the same interval is:[2]: 60 
{\displaystyle {\frac {\lambda ^{k}e^{-\lambda }}{k!}}.}

For instance, consider a call center which receives an average of λ = 3 calls per minute at all times of day. If the number of calls received in any two given disjoint time intervals is independent, then the number k of calls received during any minute has a Poisson probability distribution. Receiving  k = 1 to 4 calls then has a probability of about 0.77, while receiving 0 or at least 5 calls has a probability of about 0.23. ${\displaystyle {\frac {\lambda ^{k}e^{-\lambda }}{k!}}.}$

A classic example used to motivate the Poisson distribution is the number of radioactive decay events during a fixed observation period.[3]

History
The distribution was first introduced by Siméon Denis Poisson (1781–1840) and published together with his probability theory in his work Recherches sur la probabilité des jugements en matière criminelle et en matière civile (1837).[4]: 205-207  The work theorized about the number of wrongful convictions in a given country by focusing on certain random variables N that count, among other things, the number of discrete occurrences (sometimes called "events" or "arrivals") that take place during a time-interval of given length. The result had already been given in 1711 by Abraham de Moivre in De Mensura Sortis seu; de Probabilitate Eventuum in Ludis a Casu Fortuito Pendentibus .[5]: 219 [6]: 14-15 [7]: 193 [8]: 157  This makes it an example of Stigler's law and it has prompted some authors to argue that the Poisson distribution should bear the name of de Moivre.[9][10]
In 1860, Simon Newcomb fitted the Poisson distribution to the number of stars found in a unit of space.[11]
A further practical application was made by Ladislaus Bortkiewicz in 1898. Bortkiewicz showed that the frequency with which soldiers in the Prussian army were accidentally killed by horse kicks could be well modeled by a Poisson distribution.[12]: 23-25 .

Definitions
Probability mass function
A discrete random variable X is said to have a Poisson distribution with parameter 
{\displaystyle \lambda >0}

 if it has a probability mass function given by:[2]: 60 
{\displaystyle f(k;\lambda )=\Pr(X{=}k)={\frac {\lambda ^{k}e^{-\lambda }}{k!}},}

where

k is the number of occurrences (
{\displaystyle k=0,1,2,\ldots }

)
e is Euler's number (

e
=
2.71828
…

{\displaystyle e=2.71828\ldots }

)
k! = k(k–1) ··· (3)(2)(1) is the factorial.
The positive real number λ is equal to the expected value of X and also to its variance.[13]
{\displaystyle \lambda =\operatorname {E} (X)=\operatorname {Var} (X).}

The Poisson distribution can be applied to systems with a large number of possible events, each of which is rare. The number of such events that occur during a fixed time interval is, under the right circumstances, a random number with a Poisson distribution.
The equation can be adapted if, instead of the average number of events 
{\displaystyle \lambda ,}

 we are given the average rate 

r

{\displaystyle r}

 at which events occur. Then 
{\displaystyle \lambda =rt,}

 and:[14]

P
(
k

 events in interval 
{\displaystyle P(k{\text{ events in interval }}t)={\frac {(rt)^{k}e^{-rt}}{k!}}.}

Examples
Chewing gum on a sidewalk. The number of pieces on a single tile is approximately Poisson distributed.
The Poisson distribution may be useful to model events such as:

the number of meteorites greater than one-meter diameter that strike Earth in a year;
the number of laser photons hitting a detector in a particular time interval;
the number of students achieving a low and high mark in an exam; and
locations of defects and dislocations in materials.
Examples of the occurrence of random points in space are: the locations of asteroid impacts with earth (2-dimensional), the locations of imperfections in a material (3-dimensional), and the locations of trees in a forest (2-dimensional).[15]

Assumptions and validity
The Poisson distribution is an appropriate model if the following assumptions are true:

k, a nonnegative integer, is the number of times an event occurs in an interval.
The occurrence of one event does not affect the probability of a second event.
The average rate at which events occur is independent of any occurrences.
Two events cannot occur at exactly the same instant.
If these conditions are true, then k is a Poisson random variable; the distribution of k is a Poisson distribution.
The Poisson distribution is also the limit of a binomial distribution, for which the probability of success for each trial is 
{\displaystyle p={\frac {\lambda }{n}}}

, where 

λ

{\displaystyle \lambda }

 is the expectation and 

n

{\displaystyle n}

 is the number of trials, in the limit that 
{\displaystyle n\to \infty }

 with 

λ

{\displaystyle \lambda }

 kept constant
[16][17] (see Related distributions):
{\displaystyle \lim _{n\to \infty }{\dbinom {n}{k}}\left({\frac {\lambda }{n}}\right)^{k}\,\left(1-{\frac {\lambda }{n}}\right)^{n-k}={\frac {\lambda ^{k}}{k!}}\,e^{-\lambda }}

The Poisson distribution may also be derived from the differential equations[18][19][20]
{\displaystyle {\frac {d\,P_{k}(t)}{dt}}=\lambda \,{\Big (}P_{k-1}(t)-P_{k}(t){\Big )}}

with initial conditions 
{\displaystyle P_{k}(0)=\delta _{k0}}

 and evaluated at 
{\displaystyle t=1}

Examples of probability for Poisson distributions

On a particular river, overflow floods occur once every 100 years on average. Calculate the probability of k = 0, 1, 2, 3, 4, 5, or 6 overflow floods in a 100-year interval, assuming the Poisson model is appropriate.
Because the average event rate is one overflow flood per 100 years, λ = 1

P
(
k

 overflow floods in 100 years

)

=

λ

k

e

−
λ

k
!

=

1

k

e

−
1

k
!

P
(
k
=
0

 overflow floods in 100 years

)

=

1

0

e

−
1

0
!

=

e

−
1

1

≈
0.368

P
(
k
=
1

 overflow flood in 100 years

)

=

1

1

e

−
1

1
!

=

e

−
1

1

≈
0.368

P
(
k
=
2

 overflow floods in 100 years

)

=

1

2

e

−
1

2
!

=

e

−
1

2

≈
0.184

{\displaystyle {\begin{aligned}P(k{\text{ overflow floods in 100 years}})&={\frac {\lambda ^{k}e^{-\lambda }}{k!}}={\frac {1^{k}e^{-1}}{k!}}\\P(k=0{\text{ overflow floods in 100 years}})&={\frac {1^{0}e^{-1}}{0!}}={\frac {e^{-1}}{1}}\approx 0.368\\P(k=1{\text{ overflow flood in 100 years}})&={\frac {1^{1}e^{-1}}{1!}}={\frac {e^{-1}}{1}}\approx 0.368\\P(k=2{\text{ overflow floods in 100 years}})&={\frac {1^{2}e^{-1}}{2!}}={\frac {e^{-1}}{2}}\approx 0.184\end{aligned}}}

k
P(k overflow floods in 100 years)

0
0.368

1
0.368

2
0.184

3
0.061

4
0.015

5
0.003

6
0.0005

The probability for 0 to 6 overflow floods in a 100-year period.

In this example, it is reported that the average number of goals in a World Cup soccer match is approximately 2.5 and the Poisson model is appropriate.[21]
Because the average event rate is 2.5 goals per match, λ = 2.5.

P
(
k

 goals in a match

)

=

2.5

k

e

−
2.5

k
!

P
(
k
=
0

 goals in a match

)

=

2.5

0

e

−
2.5

0
!

=

e

−
2.5

1

≈
0.082

P
(
k
=
1

 goal in a match

)

=

2.5

1

e

−
2.5

1
!

=

2.5

e

−
2.5

1

≈
0.205

P
(
k
=
2

 goals in a match

)

=

2.5

2

e

−
2.5

2
!

=

6.25

e

−
2.5

2

≈
0.257

{\displaystyle {\begin{aligned}P(k{\text{ goals in a match}})&={\frac {2.5^{k}e^{-2.5}}{k!}}\\P(k=0{\text{ goals in a match}})&={\frac {2.5^{0}e^{-2.5}}{0!}}={\frac {e^{-2.5}}{1}}\approx 0.082\\P(k=1{\text{ goal in a match}})&={\frac {2.5^{1}e^{-2.5}}{1!}}={\frac {2.5e^{-2.5}}{1}}\approx 0.205\\P(k=2{\text{ goals in a match}})&={\frac {2.5^{2}e^{-2.5}}{2!}}={\frac {6.25e^{-2.5}}{2}}\approx 0.257\end{aligned}}}

k
P(k goals in a World Cup soccer match)

0
0.082

1
0.205

2
0.257

3
0.213

4
0.133

5
0.067

6
0.028

7
0.010

The probability for 0 to 7 goals in a match.

Examples that violate the Poisson assumptions
The number of students who arrive at the student union per minute will likely not follow a Poisson distribution, because the rate is not constant (low rate during class time, high rate between class times) and the arrivals of individual students are not independent (students tend to come in groups). The non-constant arrival rate may be modeled as a mixed Poisson distribution, and the arrival of groups rather than individual students as a compound Poisson process.
The number of magnitude 5 earthquakes per year in a country may not follow a Poisson distribution if one large earthquake increases the probability of aftershocks of similar magnitude.
Examples in which at least one event is guaranteed are not Poisson distributed; but may be modeled using a zero-truncated Poisson distribution.
Count distributions in which the number of intervals with zero events is higher than predicted by a Poisson model may be modeled using a zero-inflated model.

Properties
Descriptive statistics
The expected value of a Poisson random variable is λ.
The variance of a Poisson random variable is also λ.
The coefficient of variation is 

λ

−
1

/

2

,

{\textstyle \lambda ^{-1/2},}

 while the index of dispersion is 1.[8]: 163 
The mean absolute deviation about the mean is[8]: 163  
{\displaystyle \operatorname {E} [\ |X-\lambda |\ ]={\frac {2\lambda ^{\lfloor \lambda \rfloor +1}e^{-\lambda }}{\lfloor \lambda \rfloor !}}.}

The mode of a Poisson-distributed random variable with non-integer λ is equal to 
{\displaystyle \lfloor \lambda \rfloor ,}

 which is the largest integer less than or equal to λ. This is also written as floor(λ). When λ is a positive integer, the modes are λ and λ − 1.
All of the cumulants of the Poisson distribution are equal to the expected value λ. The n-th factorial moment of the Poisson distribution is λn.
The expected value of a Poisson process is sometimes decomposed into the product of intensity and exposure (or more generally expressed as the integral of an "intensity function" over time or space, sometimes described as "exposure").[22]
Median
Bounds for the median (

ν

{\displaystyle \nu }

) of the distribution are known and are sharp:[23]
{\displaystyle \lambda -\ln 2\leq \nu <\lambda +{\frac {1}{3}}.}

Higher moments
The higher non-centered moments mk of the Poisson distribution are Touchard polynomials in λ:
{\displaystyle m_{k}=\sum _{i=0}^{k}\lambda ^{i}{\begin{Bmatrix}k\\i\end{Bmatrix}},}

 where the braces { } denote Stirling numbers of the second kind.[24][1]: 6  In other words,
{\displaystyle E[X]=\lambda ,\quad E[X(X-1)]=\lambda ^{2},\quad E[X(X-1)(X-2)]=\lambda ^{3},\cdots }

When the expected value is set to λ = 1, Dobinski's formula implies that the n‑th moment is equal to the number of partitions of a set of size n.
A simple upper bound is:[25]
{\displaystyle m_{k}=E[X^{k}]\leq \left({\frac {k}{\log(k/\lambda +1)}}\right)^{k}\leq \lambda ^{k}\exp \left({\frac {k^{2}}{2\lambda }}\right).}

Sums of Poisson-distributed random variables
If 

X

i

∼
Pois
{\displaystyle X_{i}\sim \operatorname {Pois} (\lambda _{i})}
{\displaystyle i=1,\dotsc ,n}

 are independent, then 

∑

i
=
1

n

X

i

∼
Pois
⁡

(

∑

i
=
1

n

λ

i

)

.

{\textstyle \sum _{i=1}^{n}X_{i}\sim \operatorname {Pois} \left(\sum _{i=1}^{n}\lambda _{i}\right).}

[26]: 65  A converse is Raikov's theorem, which says that if the sum of two independent random variables is Poisson-distributed, then so are each of those two independent random variables.[27][28]

Maximum entropy
It is a maximum-entropy distribution among the set of generalized binomial distributions 
{\displaystyle B_{n}(\lambda )}

 with mean 

λ

{\displaystyle \lambda }
{\displaystyle n\to \infty }

,[29] where a generalized binomial distribution is defined as a distribution of the sum of N independent but not identically distributed Bernoulli variables.

Other properties
The Poisson distributions are infinitely divisible probability distributions.[30]: 233 [8]: 164 
The directed Kullback–Leibler divergence of 

P
=
Pois
{\displaystyle P=\operatorname {Pois} (\lambda )}

 from 

P

0

=
Pois
{\displaystyle P_{0}=\operatorname {Pois} (\lambda _{0})}

 is given by
{\displaystyle \operatorname {D} _{\text{KL}}(P\parallel P_{0})=\lambda _{0}-\lambda +\lambda \log {\frac {\lambda }{\lambda _{0}}}.}
{\displaystyle \lambda \geq 1}

 is an integer, then 

Y
∼
Pois
{\displaystyle Y\sim \operatorname {Pois} (\lambda )}

 satisfies 
{\displaystyle \Pr(Y\geq E[Y])\geq {\frac {1}{2}}}
{\displaystyle \Pr(Y\leq E[Y])\geq {\frac {1}{2}}.}

[31][failed verification – see discussion]
Bounds for the tail probabilities of a Poisson random variable 

X
∼
Pois
{\displaystyle X\sim \operatorname {Pois} (\lambda )}

 can be derived using a Chernoff bound argument.[32]: 97-98  
{\displaystyle {\begin{aligned}P(X\geq x)&\leq {\frac {\left(e\lambda \right)^{x}e^{-\lambda }}{x^{x}}},&{\text{ for }}x>\lambda ,\\[1ex]P(X\leq x)&\leq {\frac {\left(e\lambda \right)^{x}e^{-\lambda }}{x^{x}}},&{\text{ for }}x<\lambda .\end{aligned}}}

The upper tail probability can be tightened (by a factor of at least two) as follows:[33]
{\displaystyle P(X\geq x)\leq {\frac {e^{-\operatorname {D} _{\text{KL}}(Q\parallel P)}}{\max {(2,{\sqrt {4\pi \operatorname {D} _{\text{KL}}(Q\parallel P)}}})}},{\text{ for }}x>\lambda ,}

 where 
{\displaystyle \operatorname {D} _{\text{KL}}(Q\parallel P)}

 is the Kullback–Leibler divergence of 

Q
=
Pois
{\displaystyle Q=\operatorname {Pois} (x)}

 from 

P
=
Pois
{\displaystyle P=\operatorname {Pois} (\lambda )}

.
Inequalities that relate the distribution function of a Poisson random variable 

X
∼
Pois
{\displaystyle X\sim \operatorname {Pois} (\lambda )}

 to the Standard normal distribution function 
{\displaystyle \Phi (x)}

 are as follows:[34]

Φ

(

sign
⁡
(
k
−
λ
)

2

D

KL

⁡
(

Q

−

∥
P
)

)

<
P
(
X
≤
k
)
<
Φ

(

sign
{\displaystyle \Phi {\left(\operatorname {sign} (k-\lambda ){\sqrt {2\operatorname {D} _{\text{KL}}(Q_{-}\parallel P)}}\right)}<P(X\leq k)<\Phi {\left(\operatorname {sign} (k+1-\lambda ){\sqrt {2\operatorname {D} _{\text{KL}}(Q_{+}\parallel P)}}\right)},{\text{ for }}k>0,}

 where 
{\displaystyle \operatorname {D} _{\text{KL}}(Q_{-}\parallel P)}

 is the Kullback–Leibler divergence of 

Q

−

=
Pois
{\displaystyle Q_{-}=\operatorname {Pois} (k)}

 from 

P
=
Pois
{\displaystyle P=\operatorname {Pois} (\lambda )}
{\displaystyle \operatorname {D} _{\text{KL}}(Q_{+}\parallel P)}

 is the Kullback–Leibler divergence of 

Q

+

=
Pois
{\displaystyle Q_{+}=\operatorname {Pois} (k+1)}

 from 

P

{\displaystyle P}

.

Poisson races
Let 

X
∼
Pois
{\displaystyle X\sim \operatorname {Pois} (\lambda )}

 and 

Y
∼
Pois
{\displaystyle Y\sim \operatorname {Pois} (\mu )}

 be independent random variables, with 
{\displaystyle \lambda <\mu ,}

 then we have that
{\displaystyle {\frac {e^{-({\sqrt {\mu }}-{\sqrt {\lambda }})^{2}}}{(\lambda +\mu )^{2}}}-{\frac {e^{-(\lambda +\mu )}}{2{\sqrt {\lambda \mu }}}}-{\frac {e^{-(\lambda +\mu )}}{4\lambda \mu }}\leq P(X-Y\geq 0)\leq e^{-({\sqrt {\mu }}-{\sqrt {\lambda }})^{2}}}

The upper bound is proved using a standard Chernoff bound.
The lower bound can be proved by noting that 
{\displaystyle P(X-Y\geq 0\mid X+Y=i)}

 is the probability that 

Z
≥

i
2

,

{\textstyle Z\geq {\frac {i}{2}},}

 where 

Z
∼
Bin
⁡

(

i
,

λ

λ
+
μ

)

,

{\textstyle Z\sim \operatorname {Bin} \left(i,{\frac {\lambda }{\lambda +\mu }}\right),}

 which is bounded below by 

1

(
i
+
1

)

2

e

−
i
D

(

0.5
‖

λ

λ
+
μ

)

,

{\textstyle {\frac {1}{(i+1)^{2}}}e^{-iD\left(0.5\|{\frac {\lambda }{\lambda +\mu }}\right)},}

 where 

D

{\displaystyle D}

 is relative entropy (See the entry on bounds on tails of binomial distributions for details). Further noting that 

X
+
Y
∼
Pois
{\displaystyle X+Y\sim \operatorname {Pois} (\lambda +\mu ),}

 and computing a lower bound on the unconditional probability gives the result. More details can be found in the appendix of Kamath et al.[35]

Related distributions
As a Binomial distribution with infinitesimal time-steps
The Poisson distribution can be derived as a limiting case to the binomial distribution as the number of trials goes to infinity and the expected number of successes remains fixed — see law of rare events below. Therefore, it can be used as an approximation of the binomial distribution if n is sufficiently large and p is sufficiently small. The Poisson distribution is a good approximation of the binomial distribution if n is at least 20 and p is smaller than or equal to 0.05, and an excellent approximation if n ≥ 100 and np ≤ 10.[36] Letting 
{\displaystyle F_{\mathrm {B} }}
{\displaystyle F_{\mathrm {P} }}

 be the respective cumulative density functions of the binomial and Poisson distributions, one has:
{\displaystyle F_{\mathrm {B} }(k;n,p)\ \approx \ F_{\mathrm {P} }(k;\lambda =np).}

One derivation of this uses probability-generating functions.[37] Consider a Bernoulli trial (coin-flip) whose probability of one success (or expected number of successes) is 
{\displaystyle \lambda \leq 1}

 within a given interval. Split the interval into n parts, and perform a trial in each subinterval with probability 
{\displaystyle {\tfrac {\lambda }{n}}}

. The probability of k successes out of n trials over the entire interval is then given by the binomial distribution
{\displaystyle p_{k}^{(n)}={\binom {n}{k}}\left({\frac {\lambda }{n}}\right)^{\!k}\left(1{-}{\frac {\lambda }{n}}\right)^{\!n-k},}

whose generating function is:
{\displaystyle P^{(n)}(x)=\sum _{k=0}^{n}p_{k}^{(n)}x^{k}=\left(1-{\frac {\lambda }{n}}+{\frac {\lambda }{n}}x\right)^{n}.}

Taking the limit as n increases to infinity (with x fixed) and applying the product limit definition of the exponential function, this reduces to the generating function of the Poisson distribution:
{\displaystyle \lim _{n\to \infty }P^{(n)}(x)=\lim _{n\to \infty }\left(1{+}{\tfrac {\lambda (x-1)}{n}}\right)^{n}=e^{\lambda (x-1)}=\sum _{k=0}^{\infty }e^{-\lambda }{\frac {\lambda ^{k}}{k!}}x^{k}.}

General
{\displaystyle X_{1}\sim \mathrm {Pois} (\lambda _{1})\,}
{\displaystyle X_{2}\sim \mathrm {Pois} (\lambda _{2})\,}

 are independent, then the difference 
{\displaystyle Y=X_{1}-X_{2}}

 follows a Skellam distribution.
{\displaystyle X_{1}\sim \mathrm {Pois} (\lambda _{1})\,}
{\displaystyle X_{2}\sim \mathrm {Pois} (\lambda _{2})\,}

 are independent, then the distribution of 
{\displaystyle X_{1}}

 conditional on 
{\displaystyle X_{1}+X_{2}}

 is a binomial distribution.  Specifically, if 
{\displaystyle X_{1}+X_{2}=k,}

 then 
{\displaystyle X_{1}|X_{1}+X_{2}=k\sim \mathrm {Binom} (k,\lambda _{1}/(\lambda _{1}+\lambda _{2})).}

  More generally, if X1, X2, ..., Xn are independent Poisson random variables with parameters λ1, λ2, ..., λn then  given 
{\displaystyle \sum _{j=1}^{n}X_{j}=k,}

 it follows that 
{\displaystyle X_{i}{\Big |}\sum _{j=1}^{n}X_{j}=k\sim \mathrm {Binom} \left(k,{\frac {\lambda _{i}}{\sum _{j=1}^{n}\lambda _{j}}}\right).}

 In fact, 
{\displaystyle \{X_{i}\}\sim \mathrm {Multinom} \left(k,\left\{{\frac {\lambda _{i}}{\sum _{j=1}^{n}\lambda _{j}}}\right\}\right).}
{\displaystyle X\sim \mathrm {Pois} (\lambda )\,}

 and the distribution of 

Y

{\displaystyle Y}

 conditional on X = k is a binomial distribution, 
{\displaystyle Y\mid (X=k)\sim \mathrm {Binom} (k,p),}

 then the distribution of Y follows a Poisson distribution 
{\displaystyle Y\sim \mathrm {Pois} (\lambda \cdot p).}

 In fact, if, conditional on 
{\displaystyle \{X=k\},}
{\displaystyle \{Y_{i}\}}

 follows a multinomial distribution, 
{\displaystyle \{Y_{i}\}\mid (X=k)\sim \mathrm {Multinom} \left(k,p_{i}\right),}

 then each 
{\displaystyle Y_{i}}

 follows an independent Poisson distribution 
{\displaystyle Y_{i}\sim \mathrm {Pois} (\lambda \cdot p_{i}),\rho (Y_{i},Y_{j})=0.}

The Poisson distribution is a special case of the discrete compound Poisson distribution (or stuttering Poisson distribution) with only a parameter.[38][39] The discrete compound Poisson distribution can be deduced from the limiting distribution of univariate multinomial distribution. It is also a special case of a compound Poisson distribution.
For sufficiently large values of λ, (say λ > 1000), the normal distribution with mean λ and variance λ (standard deviation 

λ

{\displaystyle {\sqrt {\lambda }}}

) is an excellent approximation to the Poisson distribution. If λ is greater than about 10, then the normal distribution is a good approximation if an appropriate continuity correction is performed, i.e., if P(X ≤ x), where x is a non-negative integer, is replaced by P(X ≤ x + 0.5). 
{\displaystyle F_{\mathrm {Poisson} }(x;\lambda )\approx F_{\mathrm {normal} }(x;\mu =\lambda ,\sigma ^{2}=\lambda )}

Variance-stabilizing transformation: If 
{\displaystyle X\sim \mathrm {Pois} (\lambda ),}

 then[8]: 168  
{\displaystyle Y=2{\sqrt {X}}\approx {\mathcal {N}}(2{\sqrt {\lambda }};1),}

 and[40]: 196  
{\displaystyle Y={\sqrt {X}}\approx {\mathcal {N}}({\sqrt {\lambda }};1/4).}

 Under this transformation, the convergence to normality (as 

λ

{\displaystyle \lambda }

 increases) is far faster than the untransformed variable.[citation needed] Other, slightly more complicated, variance stabilizing transformations are available,[8]: 168  one of which is Anscombe transform.[41] See Data transformation (statistics) for more general uses of transformations.
If for every t > 0 the number of arrivals in the time interval [0, t] follows the Poisson distribution with mean λt, then the sequence of inter-arrival times are independent and identically distributed exponential random variables having mean 1/λ.[42]: 317–319 
The cumulative distribution functions of the Poisson and chi-squared distributions are related in the following ways:[8]: 167  

F

Poisson

(
k
;
λ
)
=
1
−

F

χ

2

(
2
λ
;
2
(
k
+
1
)
)

 integer 
{\displaystyle F_{\text{Poisson}}(k;\lambda )=1-F_{\chi ^{2}}(2\lambda ;2(k+1))\quad \quad {\text{ integer }}k,}

 and[8]: 158  
{\displaystyle P(X=k)=F_{\chi ^{2}}(2\lambda ;2(k+1))-F_{\chi ^{2}}(2\lambda ;2k).}

Poisson approximation
Assume 

X

1

∼
Pois
⁡
(

λ

1

)
,

X

2

∼
Pois
⁡
(

λ

2

)
,
…
,

X

n

∼
Pois
{\displaystyle X_{1}\sim \operatorname {Pois} (\lambda _{1}),X_{2}\sim \operatorname {Pois} (\lambda _{2}),\dots ,X_{n}\sim \operatorname {Pois} (\lambda _{n})}

 where 
{\displaystyle \lambda _{1}+\lambda _{2}+\dots +\lambda _{n}=1,}

 then[43] 
{\displaystyle (X_{1},X_{2},\dots ,X_{n})}

 is multinomially distributed

(

X

1

,

X

2

,
…
,

X

n

)
∼
Mult
{\displaystyle (X_{1},X_{2},\dots ,X_{n})\sim \operatorname {Mult} (N,\lambda _{1},\lambda _{2},\dots ,\lambda _{n})}

 conditioned on 
{\displaystyle N=X_{1}+X_{2}+\dots X_{n}.}

This means[32]: 101-102 , among other things, that for any nonnegative function 
{\displaystyle f(x_{1},x_{2},\dots ,x_{n}),}

if 

(

Y

1

,

Y

2

,
…
,

Y

n

)
∼
Mult
{\displaystyle (Y_{1},Y_{2},\dots ,Y_{n})\sim \operatorname {Mult} (m,\mathbf {p} )}

 is multinomially distributed, then
{\displaystyle \operatorname {E} [f(Y_{1},Y_{2},\dots ,Y_{n})]\leq e{\sqrt {m}}\operatorname {E} [f(X_{1},X_{2},\dots ,X_{n})]}

where 

(

X

1

,

X

2

,
…
,

X

n

)
∼
Pois
{\displaystyle (X_{1},X_{2},\dots ,X_{n})\sim \operatorname {Pois} (\mathbf {p} ).}

The factor of 
{\displaystyle e{\sqrt {m}}}

 can be replaced by 2 if 

f

{\displaystyle f}

 is further assumed to be monotonically increasing or decreasing.

Bivariate Poisson distribution
This distribution has been extended to the bivariate case.[44] The generating function for this distribution is
{\displaystyle g(u,v)=\exp[(\theta _{1}-\theta _{12})(u-1)+(\theta _{2}-\theta _{12})(v-1)+\theta _{12}(uv-1)]}

with
{\displaystyle \theta _{1},\theta _{2}>\theta _{12}>0}

The marginal distributions are Poisson(θ1) and Poisson(θ2) and the correlation coefficient is limited to the range
{\displaystyle 0\leq \rho \leq \min \left\{{\sqrt {\frac {\theta _{1}}{\theta _{2}}}},{\sqrt {\frac {\theta _{2}}{\theta _{1}}}}\right\}}

A simple way to generate a bivariate Poisson distribution 
{\displaystyle X_{1},X_{2}}

 is to take three independent Poisson distributions 
{\displaystyle Y_{1},Y_{2},Y_{3}}

 with means 
{\displaystyle \lambda _{1},\lambda _{2},\lambda _{3}}

 and then set 
{\displaystyle X_{1}=Y_{1}+Y_{3},X_{2}=Y_{2}+Y_{3}.}

 The probability function of the bivariate Poisson distribution is
{\displaystyle \Pr(X_{1}=k_{1},X_{2}=k_{2})=\exp \left(-\lambda _{1}-\lambda _{2}-\lambda _{3}\right){\frac {\lambda _{1}^{k_{1}}}{k_{1}!}}{\frac {\lambda _{2}^{k_{2}}}{k_{2}!}}\sum _{k=0}^{\min(k_{1},k_{2})}{\binom {k_{1}}{k}}{\binom {k_{2}}{k}}k!\left({\frac {\lambda _{3}}{\lambda _{1}\lambda _{2}}}\right)^{k}}

Free Poisson distribution
The free Poisson distribution[45] with jump size 

α

{\displaystyle \alpha }

 and rate 

λ

{\displaystyle \lambda }

 arises in free probability theory as the limit of repeated free convolution
{\displaystyle \left(\left(1-{\frac {\lambda }{N}}\right)\delta _{0}+{\frac {\lambda }{N}}\delta _{\alpha }\right)^{\boxplus N}}

as N → ∞.
In other words, let 
{\displaystyle X_{N}}

 be random variables so that 
{\displaystyle X_{N}}

 has value 

α

{\displaystyle \alpha }

 with probability 

λ
N

{\textstyle {\frac {\lambda }{N}}}

 and value 0 with the remaining probability. Assume also that the family 
{\displaystyle X_{1},X_{2},\ldots }

 are freely independent. Then the limit as 
{\displaystyle N\to \infty }

 of the law of 
{\displaystyle X_{1}+\cdots +X_{N}}

 is given by the Free Poisson law with parameters 
{\displaystyle \lambda ,\alpha .}

This definition is analogous to one of the ways in which the classical Poisson distribution is obtained from a (classical) Poisson process.
The measure associated to the free Poisson law is given by[46]
{\displaystyle \mu ={\begin{cases}(1-\lambda )\delta _{0}+\nu ,&{\text{if }}0\leq \lambda \leq 1\\\nu ,&{\text{if }}\lambda >1,\end{cases}}}

where
{\displaystyle \nu ={\frac {1}{2\pi \alpha t}}{\sqrt {4\lambda \alpha ^{2}-(t-\alpha (1+\lambda ))^{2}}}\,dt}

and has support 
{\displaystyle [\alpha (1-{\sqrt {\lambda }})^{2},\alpha (1+{\sqrt {\lambda }})^{2}].}

This law also arises in random matrix theory as the Marchenko–Pastur law. Its free cumulants are equal to 
{\displaystyle \kappa _{n}=\lambda \alpha ^{n}.}

Some transforms of this law
We give values of some important transforms of the free Poisson law; the computation can be found in e.g. in the book Lectures on the Combinatorics of Free Probability by A. Nica and R. Speicher[47]
The R-transform of the free Poisson law is given by
{\displaystyle R(z)={\frac {\lambda \alpha }{1-\alpha z}}.}

The Cauchy transform (which is the negative of the Stieltjes transformation) is given by
{\displaystyle G(z)={\frac {z+\alpha -\lambda \alpha -{\sqrt {(z-\alpha (1+\lambda ))^{2}-4\lambda \alpha ^{2}}}}{2\alpha z}}}

The S-transform is given by
{\displaystyle S(z)={\frac {1}{z+\lambda }}}

in the case that 
{\displaystyle \alpha =1.}

Statistical inference
See also: Poisson regression
Parameter estimation
Given a sample of n measured values 
{\displaystyle k_{i}\in \{0,1,\dots \},}

 for i = 1, ..., n, we wish to estimate the value of the parameter λ of the Poisson population from which the sample was drawn. The maximum likelihood estimate is[48]
{\displaystyle {\widehat {\lambda }}_{\mathrm {MLE} }={\frac {1}{n}}\sum _{i=1}^{n}k_{i}\ .}

Since each observation has expectation λ, so does the sample mean. Therefore, the maximum likelihood estimate is an unbiased estimator of λ. It is also an efficient estimator since its variance achieves the Cramér–Rao lower bound (CRLB).[49] Hence it is minimum-variance unbiased. Also it can be proven that the sum (and hence the sample mean as it is a one-to-one function of the sum) is a complete and sufficient statistic for λ.
To prove sufficiency we may use the factorization theorem. Consider partitioning the probability mass function of the joint Poisson distribution for the sample into two parts: one that depends solely on the sample 

x

{\displaystyle \mathbf {x} }

, called 
{\displaystyle h(\mathbf {x} )}

, and one that depends on the parameter 

λ

{\displaystyle \lambda }

 and the sample 

x

{\displaystyle \mathbf {x} }

 only through the function 
{\displaystyle T(\mathbf {x} ).}

 Then 
{\displaystyle T(\mathbf {x} )}

 is a sufficient statistic for 
{\displaystyle \lambda .}
{\displaystyle P(\mathbf {x} )=\prod _{i=1}^{n}{\frac {\lambda ^{x_{i}}e^{-\lambda }}{x_{i}!}}={\frac {1}{\prod _{i=1}^{n}x_{i}!}}\times \lambda ^{\sum _{i=1}^{n}x_{i}}e^{-n\lambda }}

The first term 
{\displaystyle h(\mathbf {x} )}

 depends only on 

x

{\displaystyle \mathbf {x} }

. The second term 
{\displaystyle g(T(\mathbf {x} )|\lambda )}

 depends on the sample only through 

T
(

x

)
=

∑

i
=
1

n

x

i

.

{\textstyle T(\mathbf {x} )=\sum _{i=1}^{n}x_{i}.}

 Thus, 
{\displaystyle T(\mathbf {x} )}

 is sufficient.
To find the parameter λ that maximizes the probability function for the Poisson population, we can use the logarithm of the likelihood function:
{\displaystyle {\begin{aligned}\ell (\lambda )&=\ln \prod _{i=1}^{n}f(k_{i}\mid \lambda )\\&=\sum _{i=1}^{n}\ln \!\left({\frac {e^{-\lambda }\lambda ^{k_{i}}}{k_{i}!}}\right)\\&=-n\lambda +\left(\sum _{i=1}^{n}k_{i}\right)\ln(\lambda )-\sum _{i=1}^{n}\ln(k_{i}!).\end{aligned}}}

We take the derivative of 

ℓ

{\displaystyle \ell }

 with respect to λ and compare it to zero:
{\displaystyle {\frac {\mathrm {d} }{\mathrm {d} \lambda }}\ell (\lambda )=0\iff -n+\left(\sum _{i=1}^{n}k_{i}\right){\frac {1}{\lambda }}=0.\!}

Solving for λ gives a stationary point.
{\displaystyle \lambda ={\frac {\sum _{i=1}^{n}k_{i}}{n}}}

So λ is the average of the ki values. Obtaining the sign of the second derivative of L at the stationary point will determine what kind of extreme value λ is.
{\displaystyle {\frac {\partial ^{2}\ell }{\partial \lambda ^{2}}}=-\lambda ^{-2}\sum _{i=1}^{n}k_{i}}

Evaluating the second derivative at the stationary point gives:
{\displaystyle {\frac {\partial ^{2}\ell }{\partial \lambda ^{2}}}=-{\frac {n^{2}}{\sum _{i=1}^{n}k_{i}}}}

which is the negative of n times the reciprocal of the average of the ki. This expression is negative when the average is positive. If this is satisfied, then the stationary point maximizes the probability function.
For completeness, a family of distributions is said to be complete if and only if 
{\displaystyle E(g(T))=0}

 implies that 
{\displaystyle P_{\lambda }(g(T)=0)=1}

 for all 
{\displaystyle \lambda .}

 If the individual 
{\displaystyle X_{i}}

 are iid 
{\displaystyle \mathrm {Po} (\lambda ),}

 then 

T
(

x

)
=

∑

i
=
1

n

X

i

∼

P
o

(
n
λ
)
.

{\textstyle T(\mathbf {x} )=\sum _{i=1}^{n}X_{i}\sim \mathrm {Po} (n\lambda ).}

 Knowing the distribution we want to investigate, it is easy to see that the statistic is complete.
{\displaystyle E(g(T))=\sum _{t=0}^{\infty }g(t){\frac {(n\lambda )^{t}e^{-n\lambda }}{t!}}=0}

For this equality to hold, 
{\displaystyle g(t)}

 must be 0. This follows from the fact that none of the other terms will be 0 for all 

t

{\displaystyle t}

 in the sum and for all possible values of 
{\displaystyle \lambda .}

 Hence, 
{\displaystyle E(g(T))=0}

 for all 

λ

{\displaystyle \lambda }

 implies that 
{\displaystyle P_{\lambda }(g(T)=0)=1,}

 and the statistic has been shown to be complete.

Confidence interval
The confidence interval for the mean of a Poisson distribution can be expressed using the relationship between the cumulative distribution functions of the Poisson and chi-squared distributions. The chi-squared distribution is itself closely related to the gamma distribution, and this leads to an alternative expression. Given an observation k from a Poisson distribution with mean μ, a confidence interval for μ with confidence level 1 – α is
{\displaystyle {\tfrac {1}{2}}\chi ^{2}(\alpha /2;2k)\leq \mu \leq {\tfrac {1}{2}}\chi ^{2}(1-\alpha /2;2k+2),}

or equivalently,
{\displaystyle F^{-1}(\alpha /2;k,1)\leq \mu \leq F^{-1}(1-\alpha /2;k+1,1),}

where 
{\displaystyle \chi ^{2}(p;n)}

 is the quantile function (corresponding to a lower tail area p) of the chi-squared distribution with n degrees of freedom and 
{\displaystyle F^{-1}(p;n,1)}

 is the quantile function of a gamma distribution with shape parameter n and scale parameter 1.[8]: 176-178 [50] This interval is 'exact' in the sense that its coverage probability is never less than the nominal 1 – α.
When quantiles of the gamma distribution are not available, an accurate approximation to this exact interval has been proposed (based on the Wilson–Hilferty transformation):[51]
{\displaystyle k\left(1-{\frac {1}{9k}}-{\frac {z_{\alpha /2}}{3{\sqrt {k}}}}\right)^{3}\leq \mu \leq (k+1)\left(1-{\frac {1}{9(k+1)}}+{\frac {z_{\alpha /2}}{3{\sqrt {k+1}}}}\right)^{3},}

where 
{\displaystyle z_{\alpha /2}}

 denotes the standard normal deviate with upper tail area α / 2.
For application of these formulae in the same context as above (given a sample of n measured values ki each drawn from a Poisson distribution with mean λ), one would set
{\displaystyle k=\sum _{i=1}^{n}k_{i},}

calculate an interval for μ = nλ, and then derive the interval for λ.

Bayesian inference
In Bayesian inference, the conjugate prior for the rate parameter λ of the Poisson distribution is the gamma distribution.[52] Let
{\displaystyle \lambda \sim \mathrm {Gamma} (\alpha ,\beta )}

denote that λ is distributed according to the gamma density g parameterized in terms of a shape parameter α and an inverse scale parameter β:
{\displaystyle g(\lambda \mid \alpha ,\beta )={\frac {\beta ^{\alpha }}{\Gamma (\alpha )}}\;\lambda ^{\alpha -1}\;e^{-\beta \,\lambda }\qquad {\text{ for }}\lambda >0\,\!.}

Then, given the same sample of n measured values ki as before, and a prior of Gamma(α, β), the posterior distribution is
{\displaystyle \lambda \sim \mathrm {Gamma} {\left(\alpha +\sum _{i=1}^{n}k_{i},\beta +n\right)}.}

Note that the posterior mean is linear and is given by 
{\displaystyle E[\lambda \mid k_{1},\ldots ,k_{n}]={\frac {\alpha +\sum _{i=1}^{n}k_{i}}{\beta +n}}.}

It can be shown that gamma distribution is the only prior that induces linearity of the conditional mean. Moreover, a converse result exists which states that if the conditional mean is close to a linear function in the 
{\displaystyle L_{2}}

 distance than the prior distribution of λ must be close to gamma distribution in Levy distance.[53]
The posterior mean E[λ] approaches the maximum likelihood estimate 
{\displaystyle {\widehat {\lambda }}_{\mathrm {MLE} }}

 in the limit as 
{\displaystyle \alpha \to 0,\beta \to 0,}

 which follows immediately from the general expression of the mean of the gamma distribution.
The posterior predictive distribution for a single additional observation is a negative binomial distribution,[54]: 53  sometimes called a gamma–Poisson distribution.

Simultaneous estimation of multiple Poisson means
Suppose 
{\displaystyle X_{1},X_{2},\dots ,X_{p}}

 is a set of independent random variables from a set of 

p

{\displaystyle p}

 Poisson distributions, each with a parameter 
{\displaystyle \lambda _{i},}
{\displaystyle i=1,\dots ,p,}

 and we would like to estimate these parameters. Then, Clevenson and Zidek show that under the normalized squared error loss 

L
(
λ
,

λ
^

)
=

∑

i
=
1

p

λ

i

−
1

(

λ
^

i

−

λ

i

)

2

,

{\textstyle L(\lambda ,{\hat {\lambda }})=\sum _{i=1}^{p}\lambda _{i}^{-1}({\hat {\lambda }}_{i}-\lambda _{i})^{2},}

 when 
{\displaystyle p>1,}

 then, similar as in Stein's example for the Normal means, the MLE estimator 
{\displaystyle {\hat {\lambda }}_{i}=X_{i}}

 is inadmissible.[55]
In this case, a family of minimax estimators is given for any 
{\displaystyle 0<c\leq 2(p-1)}
{\displaystyle b\geq (p-2+p^{-1})}

 as[56]
{\displaystyle {\hat {\lambda }}_{i}=\left(1-{\frac {c}{b+\sum _{i=1}^{p}X_{i}}}\right)X_{i},\qquad i=1,\dots ,p.}

Occurrence and applications
This article needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed.Find sources: "Poisson distribution" – news · newspapers · books · scholar · JSTOR (December 2019) (Learn how and when to remove this message)
Some applications of the Poisson distribution to count data (number of events):[57]

telecommunication: telephone calls arriving in a system,
astronomy: photons arriving at a telescope,
chemistry: the molar mass distribution of a living polymerization,[58]
biology: the number of mutations on a strand of DNA per unit length,
management: customers arriving at a counter or call centre,[59]
finance and insurance: number of losses or claims occurring in a given period of time,
seismology: asymptotic Poisson model of risk for large earthquakes,[60]
radioactivity: decays in a given time interval in a radioactive sample,[61]
optics: number of photons emitted in a single laser pulse (a major vulnerability of quantum key distribution protocols, known as photon number splitting).
More examples of counting events that may be modelled as Poisson processes include:

soldiers killed by horse-kicks each year in each corps in the Prussian cavalry. This example was used in a book by Ladislaus Bortkiewicz (1868–1931),[12]: 23-25 
yeast cells used when brewing Guinness beer. This example was used by William Sealy Gosset (1876–1937),[62][63]
phone calls arriving at a call centre within a minute. This example was described by A.K. Erlang (1878–1929),[64]
goals in sports involving two competing teams,[65]
deaths per year in a given age group,[66]
jumps in a stock price in a given time interval,
times a web server is accessed per minute (under an assumption of homogeneity),
mutations in a given stretch of DNA after a certain amount of radiation,
cells infected at a given multiplicity of infection,
bacteria in a certain amount of liquid,[67]
photons arriving on a pixel circuit at a given illumination over a given time period,[68]
landing of V-1 flying bombs on London during World War II, investigated by R. D. Clarke in 1946.[69]
In probabilistic number theory, Gallagher showed in 1976 that, if a certain version of the unproved prime r-tuple conjecture holds,[70]  then the counts of prime numbers in short intervals would obey a Poisson distribution.[71]

Law of rare events
Main article: Poisson limit theorem
Comparison of the Poisson distribution (black lines) and the binomial distribution with n = 10 (red circles), n = 20 (blue circles), n = 1000 (green circles). All distributions have a mean of 5. The horizontal axis shows the number of events k. As n gets larger, the Poisson distribution becomes an increasingly better approximation for the binomial distribution with the same mean.
The rate of an event is related to the probability of an event occurring in some small subinterval (of time, space or otherwise). In the case of the Poisson distribution, one assumes that there exists a small enough subinterval for which the probability of an event occurring twice is "negligible". With this assumption one can derive the Poisson distribution from the binomial one, given only the information of expected number of total events in the whole interval.
Let the total number of events in the whole interval be denoted by 
{\displaystyle \lambda .}

 Divide the whole interval into 

n

{\displaystyle n}

 subintervals 
{\displaystyle I_{1},\dots ,I_{n}}

 of equal size, such that 
{\displaystyle n>\lambda }

 (since we are interested in only very small portions of the interval this assumption is meaningful). This means that the expected number of events in each of the n subintervals is equal to 
{\displaystyle \lambda /n.}

Now we assume that the occurrence of an event in the whole interval can be seen as a sequence of n Bernoulli trials, where the 

i

{\displaystyle i}

-th Bernoulli trial corresponds to looking whether an event happens at the subinterval 
{\displaystyle I_{i}}

 with probability 
{\displaystyle \lambda /n.}

 The expected number of total events in 

n

{\displaystyle n}

 such trials would be 
{\displaystyle \lambda ,}

 the expected number of total events in the whole interval. Hence for each subdivision of the interval we have approximated the occurrence of the event as a Bernoulli process of the form 
{\displaystyle {\textrm {B}}(n,\lambda /n).}

 As we have noted before we want to consider only very small subintervals. Therefore, we take the limit as 

n

{\displaystyle n}

 goes to infinity.
In this case the binomial distribution converges to what is known as the Poisson distribution by the Poisson limit theorem.
In several of the above examples — such as the number of mutations in a given sequence of DNA — the events being counted are actually the outcomes of discrete trials, and would more precisely be modelled using the binomial distribution, that is
{\displaystyle X\sim {\textrm {B}}(n,p).}

In such cases n is very large and p is very small (and so the expectation np is of intermediate magnitude). Then the distribution may be approximated by the less cumbersome Poisson distribution

X
∼

Pois
{\displaystyle X\sim {\textrm {Pois}}(np).}

This approximation is sometimes known as the law of rare events,[72]: 5  since each of the n individual Bernoulli events rarely occurs.
The name "law of rare events" may be misleading because the total count of success events in a Poisson process need not be rare if the parameter np is not small. For example, the number of telephone calls to a busy switchboard in one hour follows a Poisson distribution with the events appearing frequent to the operator, but they are rare from the point of view of the average member of the population who is very unlikely to make a call to that switchboard in that hour.
The variance of the binomial distribution is 1 − p times that of the Poisson distribution, so almost equal when p is very small.
The word law is sometimes used as a synonym of probability distribution, and convergence in law means convergence in distribution. Accordingly, the Poisson distribution is sometimes called the "law of small numbers" because it is the probability distribution of the number of occurrences of an event that happens rarely but has very many opportunities to happen. The Law of Small Numbers is a book by Ladislaus Bortkiewicz about the Poisson distribution, published in 1898.[12][73]

Poisson point process
Main article: Poisson point process
The Poisson distribution arises as the number of points of a Poisson point process located in some finite region. More specifically, if D is some region space, for example Euclidean space Rd, for which |D|, the area, volume or, more generally, the Lebesgue measure of the region is finite, and if N(D) denotes the number of points in D, then
{\displaystyle P(N(D)=k)={\frac {(\lambda |D|)^{k}e^{-\lambda |D|}}{k!}}.}

Poisson regression and negative binomial regression
Poisson regression and negative binomial regression are useful for analyses where the dependent (response) variable is the count (0, 1, 2, ... ) of the number of events or occurrences in an interval.

Biology
The Luria–Delbrück experiment tested against the hypothesis of Lamarckian evolution, which should result in a Poisson distribution. 
Katz and Miledi measured the membrane potential with and without the presence of acetylcholine (ACh).[74] When ACh is present, ion channels on the membrane would be open randomly at a small fraction of the time. As there are a large number of ion channels each open for a small fraction of the time, the total number of ion channels open at any moment is Poisson distributed. When ACh is not present, effectively no ion channels are open. The membrane potential is 

V
=

N

open

V

ion

+

V

0

+

V

noise

{\displaystyle V=N_{\text{open}}V_{\text{ion}}+V_{0}+V_{\text{noise}}}

. Subtracting the effect of noise, Katz and Miledi found the mean and variance of membrane potential to be 
{\displaystyle 8.5\times 10^{-3}\;\mathrm {V} }

 and 

(
29.2
{\displaystyle (29.2\times 10^{-6}\;\mathrm {V} )^{2}}

 respectively, giving 
{\displaystyle V_{\text{ion}}=10^{-7}\;\mathrm {V} }

. (pp. 94-95[75])
During each cellular replication event, the number of mutations is roughly Poisson distributed.[76] For example, the HIV virus has 10,000 base pairs, and has a mutation rate of about 1 per 30,000 base pairs, meaning the number of mutations per replication event is distributed as 
{\displaystyle \mathrm {Pois} (1/3)}

. (p. 64[75])

Other applications in science
In a Poisson process, the number of observed occurrences fluctuates about its mean λ with a standard deviation 
{\displaystyle \sigma _{k}={\sqrt {\lambda }}.}

 These fluctuations are denoted as Poisson noise or (particularly in electronics) as shot noise.
The correlation of the mean and standard deviation in counting independent discrete occurrences is useful scientifically. By monitoring how the fluctuations vary with the mean signal, one can estimate the contribution of a single occurrence, even if that contribution is too small to be detected directly. For example, the charge e on an electron can be estimated by correlating the magnitude of an electric current with its shot noise. If N electrons pass a point in a given time t on the average, the mean current is 
{\displaystyle I=eN/t}

; since the current fluctuations should be of the order 
{\displaystyle \sigma _{I}=e{\sqrt {N}}/t}

 (i.e., the standard deviation of the Poisson process), the charge 

e

{\displaystyle e}

 can be estimated from the ratio 
{\displaystyle t\sigma _{I}^{2}/I.}

[citation needed]
An everyday example is the graininess that appears as photographs are enlarged; the graininess is due to Poisson fluctuations in the number of reduced silver grains, not to the individual grains themselves. By correlating the graininess with the degree of enlargement, one can estimate the contribution of an individual grain (which is otherwise too small to be seen unaided).[citation needed]
In causal set theory the discrete elements of spacetime follow a Poisson distribution in the volume.
The Poisson distribution also appears in quantum mechanics, especially quantum optics. Namely, for a quantum harmonic oscillator system in a coherent state, the probability of measuring a particular energy level has a Poisson distribution.

Computational methods
The Poisson distribution poses two different tasks for dedicated software libraries: evaluating the distribution 
{\displaystyle P(k;\lambda )}

, and drawing random numbers according to that distribution.

Evaluating the Poisson distribution
Computing 
{\displaystyle P(k;\lambda )}

 for given 

k

{\displaystyle k}
{\displaystyle \lambda }

 is a trivial task that can be accomplished by using the standard definition of 
{\displaystyle P(k;\lambda )}

 in terms of exponential, power, and factorial functions. However, the conventional definition of the Poisson distribution contains two terms that can easily overflow on computers: λk and k!. The fraction of λk to k! can also produce a rounding error that is very large compared to e−λ, and therefore give an erroneous result. For numerical stability the Poisson probability mass function should therefore be evaluated as
{\displaystyle \!f(k;\lambda )=\exp \left[k\ln \lambda -\lambda -\ln \Gamma (k+1)\right],}

which is mathematically equivalent but numerically stable. The natural logarithm of the Gamma function can be obtained using the lgamma function in the C standard library (C99 version) or R, the gammaln function in MATLAB or SciPy, or the log_gamma function in Fortran 2008 and later.
Some computing languages provide built-in functions to evaluate the Poisson distribution, namely

R: function dpois(x, lambda);
Excel: function POISSON( x, mean, cumulative), with a flag to specify the cumulative distribution;
Mathematica: univariate Poisson distribution as PoissonDistribution[

λ

{\displaystyle \lambda }

],[77] bivariate Poisson distribution as MultivariatePoissonDistribution[
{\displaystyle \theta _{12},}
{\displaystyle \theta _{1}-\theta _{12},}
{\displaystyle \theta _{2}-\theta _{12}}

}],.[78]
Random variate generation
Further information: Non-uniform random variate generation
The less trivial task is to draw integer random variate from the Poisson distribution with given 
{\displaystyle \lambda .}

Solutions are provided by:

R: function rpois(n, lambda);
GNU Scientific Library (GSL): function gsl_ran_poisson
A simple algorithm to generate random Poisson-distributed numbers (pseudo-random number sampling) has been given by Knuth:[79]: 137-138 

algorithm poisson random number (Knuth):
    init:
        Let L ← e−λ, k ← 0 and p ← 1.
    do:
        k ← k + 1.
        Generate uniform random number u in [0,1] and let p ← p × u.
    while p > L.
    return k − 1.

The complexity is linear in the returned value k, which is λ on average.  There are many other algorithms to improve this. Some are given in Ahrens & Dieter, see § References below.
For large values of λ, the value of L = e−λ may be so small that it is hard to represent.  This can be solved by a change to the algorithm which uses an additional parameter STEP such that e−STEP does not underflow: [citation needed]

algorithm poisson random number (Junhao, based on Knuth):
    init:
        Let λLeft ← λ, k ← 0 and p ← 1.
    do:
        k ← k + 1.
        Generate uniform random number u in (0,1) and let p ← p × u.
        while p < 1 and λLeft > 0:
            if λLeft > STEP:
                p ← p × eSTEP
                λLeft ← λLeft − STEP
            else:
                p ← p × eλLeft
                λLeft ← 0
    while p > 1.
    return k − 1.

The choice of STEP depends on the threshold of overflow. For double precision floating point format the threshold is near e700, so 500 should be a safe STEP.
Other solutions for large values of λ include rejection sampling and using Gaussian approximation.
Inverse transform sampling is simple and efficient for small values of λ, and requires only one uniform random number u per sample. Cumulative probabilities are examined in turn until one exceeds u.

algorithm Poisson generator based upon the inversion by sequential search:[80]: 505 
    init:
        Let x ← 0, p ← e−λ, s ← p.
        Generate uniform random number u in [0,1].
    while u > s do:
        x ← x + 1.
        p ← p × λ / x.
        s ← s + p.
    return x.

See also

Binomial distribution
Compound Poisson distribution
Conway–Maxwell–Poisson distribution
Erlang distribution
Exponential distribution
Gamma distribution
Hermite distribution
Index of dispersion
Negative binomial distribution
Poisson clumping
Poisson point process
Poisson regression
Poisson sampling
Poisson wavelet
Queueing theory
Renewal theory
Robbins lemma
Skellam distribution
Tweedie distribution
Zero-inflated model
Zero-truncated Poisson distribution

References
Citations

^ a b 
Haight, Frank A. (1967). Handbook of the Poisson Distribution. New York, NY, US: John Wiley & Sons. ISBN 978-0-471-33932-8.

^ a b 
Yates, Roy D.; Goodman, David J. (2014). Probability and Stochastic Processes: A Friendly Introduction for Electrical and Computer Engineers (2nd ed.). Hoboken, NJ: Wiley. ISBN 978-0-471-45259-1.

^ Ross, Sheldon M. (2014). Introduction to Probability Models (11th ed.). Academic Press.

^ 
Poisson, Siméon D. (1837). Probabilité des jugements en matière criminelle et en matière civile, précédées des règles générales du calcul des probabilités [Research on the Probability of Judgments in Criminal and Civil Matters] (in French). Paris, France: Bachelier.

^ 
de Moivre, Abraham (1711). "De mensura sortis, seu, de probabilitate eventuum in ludis a casu fortuito pendentibus" [On the Measurement of Chance, or, on the Probability of Events in Games Depending Upon Fortuitous Chance]. Philosophical Transactions of the Royal Society (in Latin). 27 (329): 213–264. doi:10.1098/rstl.1710.0018.

^ 
de Moivre, Abraham. The Doctrine of Chances: Or, A Method of Calculating the Probability of Events in Play. London, Great Britain: W. Pearson. ISBN 9780598843753.

^ 
de Moivre, Abraham. "Of the Laws of Chance". In Motte, Benjamin (ed.). The Philosophical Transactions from the Year MDCC (where Mr. Lowthorp Ends) to the Year MDCCXX. Abridg'd, and Dispos'd Under General Heads (in Latin). Vol. I. London, Great Britain: R. Wilkin, R. Robinson, S. Ballard, W. and J. Innys, and J. Osborn. pp. 190–219.

^ a b c d e f g h i 
Johnson, Norman L.; Kemp, Adrienne W.; Kotz, Samuel (2005). "Poisson Distribution". Univariate Discrete Distributions (3rd ed.). New York, NY, US: John Wiley & Sons, Inc. pp. 156–207. doi:10.1002/0471715816. ISBN 978-0-471-27246-5.

^ 
Stigler, Stephen M. (1982). "Poisson on the Poisson Distribution". Statistics & Probability Letters. 1 (1): 33–35. doi:10.1016/0167-7152(82)90010-4.

^ 
Hald, Anders; de Moivre, Abraham; McClintock, Bruce (1984). "A. de Moivre: 'De Mensura Sortis' or 'On the Measurement of Chance'". International Statistical Review / Revue Internationale de Statistique. 52 (3): 229–262. doi:10.2307/1403045. JSTOR 1403045.

^ 
Newcomb, Simon (1860). "Notes on the theory of probabilities". The Mathematical Monthly. 2 (4): 134–140.

^ a b c 
von Bortkiewitsch, Ladislaus (1898). Das Gesetz der kleinen Zahlen [The law of small numbers] (in German). Leipzig, Germany: B.G. Teubner. pp. 1, 23–25.
On page 1, Bortkiewicz presents the Poisson distribution.
On pages 23–25, Bortkiewitsch presents his analysis of "4. Beispiel: Die durch Schlag eines Pferdes im preußischen Heere Getöteten." [4. Example: Those killed in the Prussian army by a horse's kick.]

^ For the proof, see:
Proof wiki: expectation and Proof wiki: variance

^ Kardar, Mehran (2007). Statistical Physics of Particles. Cambridge University Press. p. 42. ISBN 978-0-521-87342-0. OCLC 860391091.

^ Dekking, Frederik Michel; Kraaikamp, Cornelis; Lopuhaä, Hendrik Paul; Meester, Ludolf Erwin (2005). A Modern Introduction to Probability and Statistics. Springer Texts in Statistics. p. 167. doi:10.1007/1-84628-168-7. ISBN 978-1-85233-896-1.

^ 
Pitman, Jim (1993). Probability. Springer Texts in Statistics. New York Dordrecht Heidelberg London: Springer. p. 118. ISBN 978-0-387-94594-1.

^ 
Hsu, Hwei P. (1996). Theory and Problems of Probability, Random Variables, and Random Processes. Schaum's Outline Series. New York: McGraw Hill. p. 68. ISBN 0-07-030644-3.

^ 
Arfken, George B.; Weber, Hans J. (2005). Mathematical Methods for Physicists Sixth Edition. Elsevier Academic Press. p. 1131. ISBN 0-12-059876-0.

^ Cowan, Glen (2009). "Derivation of the Poisson distribution" (PDF). 

^ Joyce, D. (2014). "The Poisson process" (PDF). 

^ 
Ugarte, M.D.; Militino, A.F.; Arnholt, A.T. (2016). Probability and Statistics with R (2nd ed.). Boca Raton, FL, US: CRC Press. ISBN 978-1-4665-0439-4.

^ 
Helske, Jouni (2017). "KFAS: Exponential Family State Space Models in R". Journal of Statistical Software. 78 (10). arXiv:1612.01907. doi:10.18637/jss.v078.i10. S2CID 14379617.

^ 
Choi, Kwok P. (1994). "On the medians of gamma distributions and an equation of Ramanujan". Proceedings of the American Mathematical Society. 121 (1): 245–251. doi:10.2307/2160389. JSTOR 2160389.

^ 
Riordan, John (1937). "Moment Recurrence Relations for Binomial, Poisson and Hypergeometric Frequency Distributions" (PDF). Annals of Mathematical Statistics. 8 (2): 103–111. doi:10.1214/aoms/1177732430. JSTOR 2957598.

^ D. Ahle, Thomas (2022). "Sharp and simple bounds for the raw moments of the Binomial and Poisson distributions". Statistics & Probability Letters. 182 109306. arXiv:2103.17027. doi:10.1016/j.spl.2021.109306.

^ 
Lehmann, Erich Leo (1986). Testing Statistical Hypotheses (2nd ed.). New York, NJ, US: Springer Verlag. ISBN 978-0-387-94919-2.

^ 
Raikov, Dmitry (1937). "On the decomposition of Poisson laws". Comptes Rendus de l'Académie des Sciences de l'URSS. 14: 9–11.

^ 
von Mises, Richard. Mathematical Theory of Probability and Statistics. New York: Academic Press. doi:10.1016/C2013-0-12460-9. ISBN 978-1-4832-3213-3.

^ Harremoes, P. (July 2001). "Binomial and Poisson distributions as maximum entropy distributions". IEEE Transactions on Information Theory. 47 (5): 2039–2041. doi:10.1109/18.930936. S2CID 16171405.

^ 
Laha, Radha G.; Rohatgi, Vijay K. (1979). Probability Theory. New York, NJ, US: John Wiley & Sons. ISBN 978-0-471-03262-5.

^ Mitzenmacher, Michael (2017). Probability and computing: Randomization and probabilistic techniques in algorithms and data analysis. Eli Upfal (2nd ed.). Exercise 5.14. ISBN 978-1-107-15488-9. OCLC 960841613.

^ a b 
Mitzenmacher, Michael; Upfal, Eli (2005). Probability and Computing: Randomized Algorithms and Probabilistic Analysis. Cambridge, UK: Cambridge University Press. ISBN 978-0-521-83540-4.

^ Short, Michael (2013). "Improved Inequalities for the Poisson and Binomial Distribution and Upper Tail Quantile Functions". ISRN Probability and Statistics. 2013. Corollary 6. doi:10.1155/2013/412958.

^ Short, Michael (2013). "Improved Inequalities for the Poisson and Binomial Distribution and Upper Tail Quantile Functions". ISRN Probability and Statistics. 2013. Theorem 2. doi:10.1155/2013/412958.

^ 
Kamath, Govinda M.; Şaşoğlu, Eren; Tse, David (14–19 June 2015). Optimal haplotype assembly from high-throughput mate-pair reads. 2015 IEEE International Symposium on Information Theory (ISIT). Hong Kong, China. pp. 914–918. arXiv:1502.01975. doi:10.1109/ISIT.2015.7282588. S2CID 128634.

^ 
Prins, Jack (2012). "6.3.3.1. Counts Control Charts". e-Handbook of Statistical Methods. NIST/SEMATECH. Retrieved 20 September 2019.

^ Feller, William. An Introduction to Probability Theory and its Applications.

^ 
Zhang, Huiming; Liu, Yunxiao; Li, Bo (2014). "Notes on discrete compound Poisson model with applications to risk theory". Insurance: Mathematics and Economics. 59: 325–336. doi:10.1016/j.insmatheco.2014.09.012.

^ 
Zhang, Huiming; Li, Bo (2016). "Characterizations of discrete compound Poisson distributions". Communications in Statistics - Theory and Methods. 45 (22): 6789–6802. doi:10.1080/03610926.2014.901375. S2CID 125475756.

^ 
McCullagh, Peter; Nelder, John (1989). Generalized Linear Models. Monographs on Statistics and Applied Probability. Vol. 37. London, UK: Chapman and Hall. ISBN 978-0-412-31760-6.

^ 
Anscombe, Francis J. (1948). "The transformation of Poisson, binomial and negative binomial data". Biometrika. 35 (3–4): 246–254. doi:10.1093/biomet/35.3-4.246. JSTOR 2332343.

^ 
Ross, Sheldon M. (2010). Introduction to Probability Models (10th ed.). Boston, MA: Academic Press. ISBN 978-0-12-375686-2.

^ "1.7.7 – Relationship between the Multinomial and Poisson | STAT 504". Archived from the original on 6 August 2019. Retrieved 6 August 2019.

^ 
Loukas, Sotirios; Kemp, C. David (1986). "The Index of Dispersion Test for the Bivariate Poisson Distribution". Biometrics. 42 (4): 941–948. doi:10.2307/2530708. JSTOR 2530708.

^ Free Random Variables by D. Voiculescu, K. Dykema, A. Nica, CRM Monograph Series, American Mathematical Society, Providence RI, 1992

^ Alexandru Nica, Roland Speicher: Lectures on the Combinatorics of Free Probability. London Mathematical Society Lecture Note Series, Vol. 335, Cambridge University Press, 2006.

^ Lectures on the Combinatorics of Free Probability by A. Nica and R. Speicher, pp. 203–204, Cambridge Univ. Press 2006

^ Paszek, Ewa. "Maximum likelihood estimation – examples". cnx.org.

^ Van Trees, Harry L. (2013). Detection estimation and modulation theory. Kristine L. Bell, Zhi Tian (Second ed.). ISBN 978-1-299-66515-6. OCLC 851161356.

^ 
Garwood, Frank (1936). "Fiducial Limits for the Poisson Distribution". Biometrika. 28 (3/4): 437–442. doi:10.1093/biomet/28.3-4.437. JSTOR 2333958.

^ 
Breslow, Norman E.; Day, Nick E. (1987). Statistical Methods in Cancer Research. Vol. 2 — The Design and Analysis of Cohort Studies. Lyon, France: International Agency for Research on Cancer. ISBN 978-92-832-0182-3. Archived from the original on 8 August 2018. Retrieved 11 March 2012.

^ 
Fink, Daniel (1997). A Compendium of Conjugate Priors.

^ Dytso, Alex; Poor, H. Vincent (2020). "Estimation in Poisson noise: Properties of the conditional mean estimator". IEEE Transactions on Information Theory. 66 (7): 4304–4323. arXiv:1911.03744. doi:10.1109/TIT.2020.2979978. S2CID 207853178.

^ 
Gelman; Carlin, John B.; Stern, Hal S.; Rubin, Donald B. (2003). Bayesian Data Analysis (2nd ed.). Boca Raton, FL, US: Chapman & Hall/CRC. ISBN 1-58488-388-X.

^ 
Clevenson, M. Lawrence; Zidek, James V. (1975). "Simultaneous estimation of the means of independent Poisson laws". Journal of the American Statistical Association. 70 (351): 698–705. doi:10.1080/01621459.1975.10482497. JSTOR 2285958.

^ 
Berger, James O. (1985). Statistical Decision Theory and Bayesian Analysis. Springer Series in Statistics (2nd ed.). New York, NY: Springer-Verlag. Bibcode:1985sdtb.book.....B. doi:10.1007/978-1-4757-4286-2. ISBN 978-0-387-96098-2.

^ 
Rasch, Georg (1963). The Poisson Process as a Model for a Diversity of Behavioural Phenomena (PDF). 17th International Congress of Psychology. Vol. 2. Washington, DC: American Psychological Association. doi:10.1037/e685262012-108.

^ 
Flory, Paul J. (1940). "Molecular Size Distribution in Ethylene Oxide Polymers". Journal of the American Chemical Society. 62 (6): 1561–1565. Bibcode:1940JAChS..62.1561F. doi:10.1021/ja01863a066.

^ Dwyer, Barry (23 March 2016). Systems Analysis and Synthesis: Bridging Computer Science and Information Technology. Morgan Kaufmann. ISBN 978-0-12-805449-9. Similarly, if candidates arrive at an enrolment center uniformly, the times between their arrivals will be distributed exponentially, and the number of candidates arriving each hour will follow a Poisson distribution.

^ 
Lomnitz, Cinna (1994). Fundamentals of Earthquake Prediction. New York, NY: John Wiley & Sons. ISBN 0-471-57419-8. OCLC 647404423.

^ "Poisson Distribution and Radiological Measurement". www.hko.gov.hk. Retrieved 30 September 2025. The actual number of decays over a period of time is generally described by the Poisson distribution.

^ 
a student (1907). "On the error of counting with a haemacytometer". Biometrika. 5 (3): 351–360. doi:10.2307/2331633. JSTOR 2331633.

^ 
Boland, Philip J. (1984). "A biographical glimpse of William Sealy Gosset". The American Statistician. 38 (3): 179–183. doi:10.1080/00031305.1984.10483195. JSTOR 2683648.

^ 
Erlang, Agner K. (1909). "Sandsynlighedsregning og Telefonsamtaler" [Probability Calculation and Telephone Conversations]. Nyt Tidsskrift for Matematik (in Danish). 20 (B): 33–39. JSTOR 24528622.

^ 
Hornby, Dave (2014). "Football Prediction Model: Poisson Distribution". Sports Betting Online. Retrieved 19 September 2014.

^ Campbell, Michael J.; Jacques, Richard M. (13 February 2023). Statistics at Square Two. John Wiley & Sons. ISBN 978-1-119-40136-0. The expected values are given by the Poisson model.

^ 
Koyama, Kento; Hokunan, Hidekazu; Hasegawa, Mayumi; Kawamura, Shuso; Koseki, Shigenobu (2016). "Do bacterial cell numbers follow a theoretical Poisson distribution? Comparison of experimentally obtained numbers of single cells with random number generation via computer simulation". Food Microbiology. 60: 49–53. doi:10.1016/j.fm.2016.05.019. PMID 27554145.

^ The Senses: A Comprehensive Reference. Academic Press. 30 September 2020. ISBN 978-0-12-805409-3. The division of light into discrete photons means that nominally constant light sources – e.g. a light bulb or a reflecting object in a scene – will produce visual inputs that vary randomly over time. These variations are described by Poisson statistics.

^ 
Clarke, R. D. (1946). "An application of the Poisson distribution" (PDF). Journal of the Institute of Actuaries. 72 (3): 481. doi:10.1017/S0020268100035435.

^ 
Hardy, Godfrey H.; Littlewood, John E. (1923). "On some problems of "partitio numerorum" III: On the expression of a number as a sum of primes". Acta Mathematica. 44: 1–70. doi:10.1007/BF02403921.

^ 
Gallagher, Patrick X. (1976). "On the distribution of primes in short intervals". Mathematika. 23 (1): 4–9. doi:10.1112/s0025579300016442.

^ 
Cameron, A. Colin; Trivedi, Pravin K. (1998). Regression Analysis of Count Data. Cambridge, UK: Cambridge University Press. ISBN 978-0-521-63567-7.

^ 
Edgeworth, F.Y. (1913). "On the use of the theory of probabilities in statistics relating to society". Journal of the Royal Statistical Society. 76 (2): 165–193. doi:10.2307/2340091. JSTOR 2340091.

^ Katz, B.; Miledi, R. (August 1972). "The statistical nature of the acetylcholine potential and its molecular components". The Journal of Physiology. 224 (3): 665–699. doi:10.1113/jphysiol.1972.sp009918. ISSN 0022-3751. PMC 1331515. PMID 5071933.

^ a b Nelson, Philip Charles; Bromberg, Sarina; Hermundstad, Ann; Prentice, Jason (2015). Physical models of living systems. New York, NY: W.H. Freeman & Company, a Macmillan Education Imprint. ISBN 978-1-4641-4029-7. OCLC 891121698.

^ Foster, Patricia L. (1 January 2006), "Methods for Determining Spontaneous Mutation Rates", DNA Repair, Part B, Methods in Enzymology, vol. 409, Academic Press, pp. 195–213, doi:10.1016/S0076-6879(05)09012-9, ISBN 978-0-12-182814-1, PMC 2041832, PMID 16793403

^ "Wolfram Language: PoissonDistribution reference page". wolfram.com. Retrieved 8 April 2016.

^ "Wolfram Language: MultivariatePoissonDistribution reference page". wolfram.com. Retrieved 8 April 2016.

^ 
Knuth, Donald Ervin (1997). Seminumerical Algorithms. The Art of Computer Programming. Vol. 2 (3rd ed.). Addison Wesley. ISBN 978-0-201-89684-8.

^ 
Devroye, Luc (1986). "Discrete Univariate Distributions" (PDF). Non-Uniform Random Variate Generation. New York, NY: Springer-Verlag. pp. 485–553. doi:10.1007/978-1-4613-8643-8_10. ISBN 978-1-4613-8645-2.

Sources

Ahrens, Joachim H.; Dieter, Ulrich (1974). "Computer Methods for Sampling from Gamma, Beta, Poisson and Binomial Distributions". Computing. 12 (3): 223–246. doi:10.1007/BF02293108. S2CID 37484126.
Ahrens, Joachim H.; Dieter, Ulrich (1982). "Computer Generation of Poisson Deviates". ACM Transactions on Mathematical Software. 8 (2): 163–179. doi:10.1145/355993.355997. S2CID 12410131.
Evans, Ronald J.; Boersma, J.; Blachman, N. M.; Jagers, A. A. (1988). "The Entropy of a Poisson Distribution: Problem 87-6". SIAM Review. 30 (2): 314–317. doi:10.1137/1030059.

vteProbability distributions (list)Discrete univariatewith finite support
Benford
Bernoulli
Beta-binomial
Binomial
Categorical
Hypergeometric
Negative
Poisson binomial
Rademacher
Soliton
Discrete uniform
Zipf
Zipf–Mandelbrot
with infinite support
Beta negative binomial
Borel
Conway–Maxwell–Poisson
Discrete phase-type
Delaporte
Extended negative binomial
Flory–Schulz
Gauss–Kuzmin
Geometric
Logarithmic
Mixed Poisson
Negative binomial
Panjer
Parabolic fractal
Poisson
Skellam
Yule–Simon
Zeta
Continuous univariatesupported on a bounded interval
Arcsine
ARGUS
Balding–Nichols
Bates
Beta
Generalized
Beta rectangular
Continuous Bernoulli
Irwin–Hall
Kumaraswamy
Logit-normal
Noncentral beta
PERT
Power function
Raised cosine
Reciprocal
Triangular
U-quadratic
Uniform
Wigner semicircle
supported on a semi-infinite interval
Benini
Benktander 1st kind
Benktander 2nd kind
Beta prime
Burr
Chi
Chi-squared
Noncentral
Inverse
Scaled
Dagum
Davis
Erlang
Hyper
Exponential
Hyperexponential
Hypoexponential
Logarithmic
F
Noncentral
Folded normal
Fréchet
Gamma
Generalized
Inverse
gamma/Gompertz
Gompertz
Shifted
Half-logistic
Half-normal
Hotelling's T-squared
Hartman–Watson
Inverse Gaussian
Generalized
Kolmogorov
Lévy
Log-Cauchy
Log-Laplace
Log-logistic
Log-normal
Log-t
Lomax
Matrix-exponential
Maxwell–Boltzmann
Maxwell–Jüttner
Mittag-Leffler
Nakagami
Pareto
Phase-type
Poly-Weibull
Rayleigh
Relativistic Breit–Wigner
Rice
Truncated normal
type-2 Gumbel
Weibull
Discrete
Wilks's lambda
supported on the whole real line
Cauchy
Exponential power
Fisher's z
Kaniadakis κ-Gaussian
Gaussian q
Generalized hyperbolic
Generalized logistic (logistic-beta)
Generalized normal
Geometric stable
Gumbel
Holtsmark
Hyperbolic secant
Johnson's SU
Landau
Laplace
Asymmetric
Logistic
Noncentral t
Normal (Gaussian)
Normal-inverse Gaussian
Skew normal
Slash
Stable
Student's t
Tracy–Widom
Variance-gamma
Voigt
with support whose type varies
Generalized chi-squared
Generalized extreme value
Generalized Pareto
Marchenko–Pastur
Kaniadakis κ-exponential
Kaniadakis κ-Gamma
Kaniadakis κ-Weibull
Kaniadakis κ-Logistic
Kaniadakis κ-Erlang
q-exponential
q-Gaussian
q-Weibull
Shifted log-logistic
Tukey lambda
Mixed univariatecontinuous-discrete
Rectified Gaussian
Multivariate (joint)
Discrete: 
Ewens
Multinomial
Dirichlet
Negative
Continuous: 
Dirichlet
Generalized
Multivariate Laplace
Multivariate normal
Multivariate stable
Multivariate t
Normal-gamma
Inverse
Matrix-valued: 
LKJ
Matrix beta
Matrix normal
Matrix t
Matrix gamma
Inverse
Wishart
Normal
Inverse
Normal-inverse
Complex
Uniform distribution on a Stiefel manifold
Directional
Univariate (circular) directional
Circular uniform
Univariate von Mises
Wrapped normal
Wrapped Cauchy
Wrapped exponential
Wrapped asymmetric Laplace
Wrapped Lévy
Bivariate (spherical)
Kent
Bivariate (toroidal)
Bivariate von Mises
Multivariate
von Mises–Fisher
Bingham
Degenerate and singular
Degenerate
Dirac delta function
Singular
Cantor
Families
Circular
Compound Poisson
Elliptical
Exponential
Natural exponential
Location–scale
Maximum entropy
Mixture
Pearson
Tweedie
Wrapped

 Category
 Commons

Authority control databases InternationalGNDNationalUnited StatesJapanLatviaIsraelOtherYale LUX ${\displaystyle \lambda >0}$ ${\displaystyle f(k;\lambda )=\Pr(X{=}k)={\frac {\lambda ^{k}e^{-\lambda }}{k!}},}$ ${\displaystyle k=0,1,2,\ldots }$ ${\displaystyle e=2.71828\ldots }$ ${\displaystyle \lambda =\operatorname {E} (X)=\operatorname {Var} (X).}$ ${\displaystyle \lambda ,}$ ${\displaystyle r}$ ${\displaystyle \lambda =rt,}$ ${\displaystyle P(k{\text{ events in interval }}t)={\frac {(rt)^{k}e^{-rt}}{k!}}.}$ ${\displaystyle p={\frac {\lambda }{n}}}$ ${\displaystyle \lambda }$ ${\displaystyle n}$ ${\displaystyle n\to \infty }$ ${\displaystyle \lambda }$ ${\displaystyle \lim _{n\to \infty }{\dbinom {n}{k}}\left({\frac {\lambda }{n}}\right)^{k}\,\left(1-{\frac {\lambda }{n}}\right)^{n-k}={\frac {\lambda ^{k}}{k!}}\,e^{-\lambda }}$ ${\displaystyle {\frac {d\,P_{k}(t)}{dt}}=\lambda \,{\Big (}P_{k-1}(t)-P_{k}(t){\Big )}}$ ${\displaystyle P_{k}(0)=\delta _{k0}}$ ${\displaystyle t=1}$ ${\displaystyle {\begin{aligned}P(k{\text{ overflow floods in 100 years}})&={\frac {\lambda ^{k}e^{-\lambda }}{k!}}={\frac {1^{k}e^{-1}}{k!}}\\P(k=0{\text{ overflow floods in 100 years}})&={\frac {1^{0}e^{-1}}{0!}}={\frac {e^{-1}}{1}}\approx 0.368\\P(k=1{\text{ overflow flood in 100 years}})&={\frac {1^{1}e^{-1}}{1!}}={\frac {e^{-1}}{1}}\approx 0.368\\P(k=2{\text{ overflow floods in 100 years}})&={\frac {1^{2}e^{-1}}{2!}}={\frac {e^{-1}}{2}}\approx 0.184\end{aligned}}}$ ${\displaystyle {\begin{aligned}P(k{\text{ goals in a match}})&={\frac {2.5^{k}e^{-2.5}}{k!}}\\P(k=0{\text{ goals in a match}})&={\frac {2.5^{0}e^{-2.5}}{0!}}={\frac {e^{-2.5}}{1}}\approx 0.082\\P(k=1{\text{ goal in a match}})&={\frac {2.5^{1}e^{-2.5}}{1!}}={\frac {2.5e^{-2.5}}{1}}\approx 0.205\\P(k=2{\text{ goals in a match}})&={\frac {2.5^{2}e^{-2.5}}{2!}}={\frac {6.25e^{-2.5}}{2}}\approx 0.257\end{aligned}}}$ ${\textstyle \lambda ^{-1/2},}$ ${\displaystyle \operatorname {E} [\ |X-\lambda |\ ]={\frac {2\lambda ^{\lfloor \lambda \rfloor +1}e^{-\lambda }}{\lfloor \lambda \rfloor !}}.}$ ${\displaystyle \lfloor \lambda \rfloor ,}$ ${\displaystyle \nu }$ ${\displaystyle \lambda -\ln 2\leq \nu <\lambda +{\frac {1}{3}}.}$ ${\displaystyle m_{k}=\sum _{i=0}^{k}\lambda ^{i}{\begin{Bmatrix}k\\i\end{Bmatrix}},}$ ${\displaystyle E[X]=\lambda ,\quad E[X(X-1)]=\lambda ^{2},\quad E[X(X-1)(X-2)]=\lambda ^{3},\cdots }$ ${\displaystyle m_{k}=E[X^{k}]\leq \left({\frac {k}{\log(k/\lambda +1)}}\right)^{k}\leq \lambda ^{k}\exp \left({\frac {k^{2}}{2\lambda }}\right).}$ ${\displaystyle X_{i}\sim \operatorname {Pois} (\lambda _{i})}$ ${\displaystyle i=1,\dotsc ,n}$ ${\textstyle \sum _{i=1}^{n}X_{i}\sim \operatorname {Pois} \left(\sum _{i=1}^{n}\lambda _{i}\right).}$ ${\displaystyle B_{n}(\lambda )}$ ${\displaystyle \lambda }$ ${\displaystyle n\to \infty }$ ${\displaystyle P=\operatorname {Pois} (\lambda )}$ ${\displaystyle P_{0}=\operatorname {Pois} (\lambda _{0})}$ ${\displaystyle \operatorname {D} _{\text{KL}}(P\parallel P_{0})=\lambda _{0}-\lambda +\lambda \log {\frac {\lambda }{\lambda _{0}}}.}$ ${\displaystyle \lambda \geq 1}$ ${\displaystyle Y\sim \operatorname {Pois} (\lambda )}$ ${\displaystyle \Pr(Y\geq E[Y])\geq {\frac {1}{2}}}$ ${\displaystyle \Pr(Y\leq E[Y])\geq {\frac {1}{2}}.}$ ${\displaystyle X\sim \operatorname {Pois} (\lambda )}$ ${\displaystyle {\begin{aligned}P(X\geq x)&\leq {\frac {\left(e\lambda \right)^{x}e^{-\lambda }}{x^{x}}},&{\text{ for }}x>\lambda ,\\[1ex]P(X\leq x)&\leq {\frac {\left(e\lambda \right)^{x}e^{-\lambda }}{x^{x}}},&{\text{ for }}x<\lambda .\end{aligned}}}$ ${\displaystyle P(X\geq x)\leq {\frac {e^{-\operatorname {D} _{\text{KL}}(Q\parallel P)}}{\max {(2,{\sqrt {4\pi \operatorname {D} _{\text{KL}}(Q\parallel P)}}})}},{\text{ for }}x>\lambda ,}$ ${\displaystyle \operatorname {D} _{\text{KL}}(Q\parallel P)}$ ${\displaystyle Q=\operatorname {Pois} (x)}$ ${\displaystyle P=\operatorname {Pois} (\lambda )}$ ${\displaystyle X\sim \operatorname {Pois} (\lambda )}$ ${\displaystyle \Phi (x)}$ ${\displaystyle \Phi {\left(\operatorname {sign} (k-\lambda ){\sqrt {2\operatorname {D} _{\text{KL}}(Q_{-}\parallel P)}}\right)}<P(X\leq k)<\Phi {\left(\operatorname {sign} (k+1-\lambda ){\sqrt {2\operatorname {D} _{\text{KL}}(Q_{+}\parallel P)}}\right)},{\text{ for }}k>0,}$ ${\displaystyle \operatorname {D} _{\text{KL}}(Q_{-}\parallel P)}$ ${\displaystyle Q_{-}=\operatorname {Pois} (k)}$ ${\displaystyle P=\operatorname {Pois} (\lambda )}$ ${\displaystyle \operatorname {D} _{\text{KL}}(Q_{+}\parallel P)}$ ${\displaystyle Q_{+}=\operatorname {Pois} (k+1)}$ ${\displaystyle P}$ ${\displaystyle X\sim \operatorname {Pois} (\lambda )}$ ${\displaystyle Y\sim \operatorname {Pois} (\mu )}$ ${\displaystyle \lambda <\mu ,}$ ${\displaystyle {\frac {e^{-({\sqrt {\mu }}-{\sqrt {\lambda }})^{2}}}{(\lambda +\mu )^{2}}}-{\frac {e^{-(\lambda +\mu )}}{2{\sqrt {\lambda \mu }}}}-{\frac {e^{-(\lambda +\mu )}}{4\lambda \mu }}\leq P(X-Y\geq 0)\leq e^{-({\sqrt {\mu }}-{\sqrt {\lambda }})^{2}}}$ ${\displaystyle P(X-Y\geq 0\mid X+Y=i)}$ ${\textstyle Z\geq {\frac {i}{2}},}$ ${\textstyle Z\sim \operatorname {Bin} \left(i,{\frac {\lambda }{\lambda +\mu }}\right),}$ ${\textstyle {\frac {1}{(i+1)^{2}}}e^{-iD\left(0.5\|{\frac {\lambda }{\lambda +\mu }}\right)},}$ ${\displaystyle D}$ ${\displaystyle X+Y\sim \operatorname {Pois} (\lambda +\mu ),}$ ${\displaystyle F_{\mathrm {B} }}$ ${\displaystyle F_{\mathrm {P} }}$ ${\displaystyle F_{\mathrm {B} }(k;n,p)\ \approx \ F_{\mathrm {P} }(k;\lambda =np).}$ ${\displaystyle \lambda \leq 1}$ ${\displaystyle {\tfrac {\lambda }{n}}}$ ${\displaystyle p_{k}^{(n)}={\binom {n}{k}}\left({\frac {\lambda }{n}}\right)^{\!k}\left(1{-}{\frac {\lambda }{n}}\right)^{\!n-k},}$ ${\displaystyle P^{(n)}(x)=\sum _{k=0}^{n}p_{k}^{(n)}x^{k}=\left(1-{\frac {\lambda }{n}}+{\frac {\lambda }{n}}x\right)^{n}.}$ ${\displaystyle \lim _{n\to \infty }P^{(n)}(x)=\lim _{n\to \infty }\left(1{+}{\tfrac {\lambda (x-1)}{n}}\right)^{n}=e^{\lambda (x-1)}=\sum _{k=0}^{\infty }e^{-\lambda }{\frac {\lambda ^{k}}{k!}}x^{k}.}$ ${\displaystyle X_{1}\sim \mathrm {Pois} (\lambda _{1})\,}$ ${\displaystyle X_{2}\sim \mathrm {Pois} (\lambda _{2})\,}$ ${\displaystyle Y=X_{1}-X_{2}}$ ${\displaystyle X_{1}\sim \mathrm {Pois} (\lambda _{1})\,}$ ${\displaystyle X_{2}\sim \mathrm {Pois} (\lambda _{2})\,}$ ${\displaystyle X_{1}}$ ${\displaystyle X_{1}+X_{2}}$ ${\displaystyle X_{1}+X_{2}=k,}$ ${\displaystyle X_{1}|X_{1}+X_{2}=k\sim \mathrm {Binom} (k,\lambda _{1}/(\lambda _{1}+\lambda _{2})).}$ ${\displaystyle \sum _{j=1}^{n}X_{j}=k,}$ ${\displaystyle X_{i}{\Big |}\sum _{j=1}^{n}X_{j}=k\sim \mathrm {Binom} \left(k,{\frac {\lambda _{i}}{\sum _{j=1}^{n}\lambda _{j}}}\right).}$ ${\displaystyle \{X_{i}\}\sim \mathrm {Multinom} \left(k,\left\{{\frac {\lambda _{i}}{\sum _{j=1}^{n}\lambda _{j}}}\right\}\right).}$ ${\displaystyle X\sim \mathrm {Pois} (\lambda )\,}$ ${\displaystyle Y}$ ${\displaystyle Y\mid (X=k)\sim \mathrm {Binom} (k,p),}$ ${\displaystyle Y\sim \mathrm {Pois} (\lambda \cdot p).}$ ${\displaystyle \{X=k\},}$ ${\displaystyle \{Y_{i}\}}$ ${\displaystyle \{Y_{i}\}\mid (X=k)\sim \mathrm {Multinom} \left(k,p_{i}\right),}$ ${\displaystyle Y_{i}}$ ${\displaystyle Y_{i}\sim \mathrm {Pois} (\lambda \cdot p_{i}),\rho (Y_{i},Y_{j})=0.}$ ${\displaystyle {\sqrt {\lambda }}}$ ${\displaystyle F_{\mathrm {Poisson} }(x;\lambda )\approx F_{\mathrm {normal} }(x;\mu =\lambda ,\sigma ^{2}=\lambda )}$ ${\displaystyle X\sim \mathrm {Pois} (\lambda ),}$ ${\displaystyle Y=2{\sqrt {X}}\approx {\mathcal {N}}(2{\sqrt {\lambda }};1),}$ ${\displaystyle Y={\sqrt {X}}\approx {\mathcal {N}}({\sqrt {\lambda }};1/4).}$ ${\displaystyle \lambda }$ ${\displaystyle F_{\text{Poisson}}(k;\lambda )=1-F_{\chi ^{2}}(2\lambda ;2(k+1))\quad \quad {\text{ integer }}k,}$ ${\displaystyle P(X=k)=F_{\chi ^{2}}(2\lambda ;2(k+1))-F_{\chi ^{2}}(2\lambda ;2k).}$ ${\displaystyle X_{1}\sim \operatorname {Pois} (\lambda _{1}),X_{2}\sim \operatorname {Pois} (\lambda _{2}),\dots ,X_{n}\sim \operatorname {Pois} (\lambda _{n})}$ ${\displaystyle \lambda _{1}+\lambda _{2}+\dots +\lambda _{n}=1,}$ ${\displaystyle (X_{1},X_{2},\dots ,X_{n})}$ ${\displaystyle (X_{1},X_{2},\dots ,X_{n})\sim \operatorname {Mult} (N,\lambda _{1},\lambda _{2},\dots ,\lambda _{n})}$ ${\displaystyle N=X_{1}+X_{2}+\dots X_{n}.}$ ${\displaystyle f(x_{1},x_{2},\dots ,x_{n}),}$ ${\displaystyle (Y_{1},Y_{2},\dots ,Y_{n})\sim \operatorname {Mult} (m,\mathbf {p} )}$ ${\displaystyle \operatorname {E} [f(Y_{1},Y_{2},\dots ,Y_{n})]\leq e{\sqrt {m}}\operatorname {E} [f(X_{1},X_{2},\dots ,X_{n})]}$ ${\displaystyle (X_{1},X_{2},\dots ,X_{n})\sim \operatorname {Pois} (\mathbf {p} ).}$ ${\displaystyle e{\sqrt {m}}}$ ${\displaystyle f}$ ${\displaystyle g(u,v)=\exp[(\theta _{1}-\theta _{12})(u-1)+(\theta _{2}-\theta _{12})(v-1)+\theta _{12}(uv-1)]}$ ${\displaystyle \theta _{1},\theta _{2}>\theta _{12}>0}$ ${\displaystyle 0\leq \rho \leq \min \left\{{\sqrt {\frac {\theta _{1}}{\theta _{2}}}},{\sqrt {\frac {\theta _{2}}{\theta _{1}}}}\right\}}$ ${\displaystyle X_{1},X_{2}}$ ${\displaystyle Y_{1},Y_{2},Y_{3}}$ ${\displaystyle \lambda _{1},\lambda _{2},\lambda _{3}}$ ${\displaystyle X_{1}=Y_{1}+Y_{3},X_{2}=Y_{2}+Y_{3}.}$ ${\displaystyle \Pr(X_{1}=k_{1},X_{2}=k_{2})=\exp \left(-\lambda _{1}-\lambda _{2}-\lambda _{3}\right){\frac {\lambda _{1}^{k_{1}}}{k_{1}!}}{\frac {\lambda _{2}^{k_{2}}}{k_{2}!}}\sum _{k=0}^{\min(k_{1},k_{2})}{\binom {k_{1}}{k}}{\binom {k_{2}}{k}}k!\left({\frac {\lambda _{3}}{\lambda _{1}\lambda _{2}}}\right)^{k}}$ ${\displaystyle \alpha }$ ${\displaystyle \lambda }$ ${\displaystyle \left(\left(1-{\frac {\lambda }{N}}\right)\delta _{0}+{\frac {\lambda }{N}}\delta _{\alpha }\right)^{\boxplus N}}$ ${\displaystyle X_{N}}$ ${\displaystyle X_{N}}$ ${\displaystyle \alpha }$ ${\textstyle {\frac {\lambda }{N}}}$ ${\displaystyle X_{1},X_{2},\ldots }$ ${\displaystyle N\to \infty }$ ${\displaystyle X_{1}+\cdots +X_{N}}$ ${\displaystyle \lambda ,\alpha .}$ ${\displaystyle \mu ={\begin{cases}(1-\lambda )\delta _{0}+\nu ,&{\text{if }}0\leq \lambda \leq 1\\\nu ,&{\text{if }}\lambda >1,\end{cases}}}$ ${\displaystyle \nu ={\frac {1}{2\pi \alpha t}}{\sqrt {4\lambda \alpha ^{2}-(t-\alpha (1+\lambda ))^{2}}}\,dt}$ ${\displaystyle [\alpha (1-{\sqrt {\lambda }})^{2},\alpha (1+{\sqrt {\lambda }})^{2}].}$ ${\displaystyle \kappa _{n}=\lambda \alpha ^{n}.}$ ${\displaystyle R(z)={\frac {\lambda \alpha }{1-\alpha z}}.}$ ${\displaystyle G(z)={\frac {z+\alpha -\lambda \alpha -{\sqrt {(z-\alpha (1+\lambda ))^{2}-4\lambda \alpha ^{2}}}}{2\alpha z}}}$ ${\displaystyle S(z)={\frac {1}{z+\lambda }}}$ ${\displaystyle \alpha =1.}$ ${\displaystyle k_{i}\in \{0,1,\dots \},}$ ${\displaystyle {\widehat {\lambda }}_{\mathrm {MLE} }={\frac {1}{n}}\sum _{i=1}^{n}k_{i}\ .}$ ${\displaystyle \mathbf {x} }$ ${\displaystyle h(\mathbf {x} )}$ ${\displaystyle \lambda }$ ${\displaystyle \mathbf {x} }$ ${\displaystyle T(\mathbf {x} ).}$ ${\displaystyle T(\mathbf {x} )}$ ${\displaystyle \lambda .}$ ${\displaystyle P(\mathbf {x} )=\prod _{i=1}^{n}{\frac {\lambda ^{x_{i}}e^{-\lambda }}{x_{i}!}}={\frac {1}{\prod _{i=1}^{n}x_{i}!}}\times \lambda ^{\sum _{i=1}^{n}x_{i}}e^{-n\lambda }}$ ${\displaystyle h(\mathbf {x} )}$ ${\displaystyle \mathbf {x} }$ ${\displaystyle g(T(\mathbf {x} )|\lambda )}$ ${\textstyle T(\mathbf {x} )=\sum _{i=1}^{n}x_{i}.}$ ${\displaystyle T(\mathbf {x} )}$ ${\displaystyle {\begin{aligned}\ell (\lambda )&=\ln \prod _{i=1}^{n}f(k_{i}\mid \lambda )\\&=\sum _{i=1}^{n}\ln \!\left({\frac {e^{-\lambda }\lambda ^{k_{i}}}{k_{i}!}}\right)\\&=-n\lambda +\left(\sum _{i=1}^{n}k_{i}\right)\ln(\lambda )-\sum _{i=1}^{n}\ln(k_{i}!).\end{aligned}}}$ ${\displaystyle \ell }$ ${\displaystyle {\frac {\mathrm {d} }{\mathrm {d} \lambda }}\ell (\lambda )=0\iff -n+\left(\sum _{i=1}^{n}k_{i}\right){\frac {1}{\lambda }}=0.\!}$ ${\displaystyle \lambda ={\frac {\sum _{i=1}^{n}k_{i}}{n}}}$ ${\displaystyle {\frac {\partial ^{2}\ell }{\partial \lambda ^{2}}}=-\lambda ^{-2}\sum _{i=1}^{n}k_{i}}$ ${\displaystyle {\frac {\partial ^{2}\ell }{\partial \lambda ^{2}}}=-{\frac {n^{2}}{\sum _{i=1}^{n}k_{i}}}}$ ${\displaystyle E(g(T))=0}$ ${\displaystyle P_{\lambda }(g(T)=0)=1}$ ${\displaystyle \lambda .}$ ${\displaystyle X_{i}}$ ${\displaystyle \mathrm {Po} (\lambda ),}$ ${\textstyle T(\mathbf {x} )=\sum _{i=1}^{n}X_{i}\sim \mathrm {Po} (n\lambda ).}$ ${\displaystyle E(g(T))=\sum _{t=0}^{\infty }g(t){\frac {(n\lambda )^{t}e^{-n\lambda }}{t!}}=0}$ ${\displaystyle g(t)}$ ${\displaystyle t}$ ${\displaystyle \lambda .}$ ${\displaystyle E(g(T))=0}$ ${\displaystyle \lambda }$ ${\displaystyle P_{\lambda }(g(T)=0)=1,}$ ${\displaystyle {\tfrac {1}{2}}\chi ^{2}(\alpha /2;2k)\leq \mu \leq {\tfrac {1}{2}}\chi ^{2}(1-\alpha /2;2k+2),}$ ${\displaystyle F^{-1}(\alpha /2;k,1)\leq \mu \leq F^{-1}(1-\alpha /2;k+1,1),}$ ${\displaystyle \chi ^{2}(p;n)}$ ${\displaystyle F^{-1}(p;n,1)}$ ${\displaystyle k\left(1-{\frac {1}{9k}}-{\frac {z_{\alpha /2}}{3{\sqrt {k}}}}\right)^{3}\leq \mu \leq (k+1)\left(1-{\frac {1}{9(k+1)}}+{\frac {z_{\alpha /2}}{3{\sqrt {k+1}}}}\right)^{3},}$ ${\displaystyle z_{\alpha /2}}$ ${\displaystyle k=\sum _{i=1}^{n}k_{i},}$ ${\displaystyle \lambda \sim \mathrm {Gamma} (\alpha ,\beta )}$ ${\displaystyle g(\lambda \mid \alpha ,\beta )={\frac {\beta ^{\alpha }}{\Gamma (\alpha )}}\;\lambda ^{\alpha -1}\;e^{-\beta \,\lambda }\qquad {\text{ for }}\lambda >0\,\!.}$ ${\displaystyle \lambda \sim \mathrm {Gamma} {\left(\alpha +\sum _{i=1}^{n}k_{i},\beta +n\right)}.}$ ${\displaystyle E[\lambda \mid k_{1},\ldots ,k_{n}]={\frac {\alpha +\sum _{i=1}^{n}k_{i}}{\beta +n}}.}$ ${\displaystyle L_{2}}$ ${\displaystyle {\widehat {\lambda }}_{\mathrm {MLE} }}$ ${\displaystyle \alpha \to 0,\beta \to 0,}$ ${\displaystyle X_{1},X_{2},\dots ,X_{p}}$ ${\displaystyle p}$ ${\displaystyle \lambda _{i},}$ ${\displaystyle i=1,\dots ,p,}$ ${\textstyle L(\lambda ,{\hat {\lambda }})=\sum _{i=1}^{p}\lambda _{i}^{-1}({\hat {\lambda }}_{i}-\lambda _{i})^{2},}$ ${\displaystyle p>1,}$ ${\displaystyle {\hat {\lambda }}_{i}=X_{i}}$ ${\displaystyle 0<c\leq 2(p-1)}$ ${\displaystyle b\geq (p-2+p^{-1})}$ ${\displaystyle {\hat {\lambda }}_{i}=\left(1-{\frac {c}{b+\sum _{i=1}^{p}X_{i}}}\right)X_{i},\qquad i=1,\dots ,p.}$ ${\displaystyle \lambda .}$ ${\displaystyle n}$ ${\displaystyle I_{1},\dots ,I_{n}}$ ${\displaystyle n>\lambda }$ ${\displaystyle \lambda /n.}$ ${\displaystyle i}$ ${\displaystyle I_{i}}$ ${\displaystyle \lambda /n.}$ ${\displaystyle n}$ ${\displaystyle \lambda ,}$ ${\displaystyle {\textrm {B}}(n,\lambda /n).}$ ${\displaystyle n}$ ${\displaystyle X\sim {\textrm {B}}(n,p).}$ ${\displaystyle X\sim {\textrm {Pois}}(np).}$ ${\displaystyle P(N(D)=k)={\frac {(\lambda |D|)^{k}e^{-\lambda |D|}}{k!}}.}$ ${\displaystyle V=N_{\text{open}}V_{\text{ion}}+V_{0}+V_{\text{noise}}}$ ${\displaystyle 8.5\times 10^{-3}\;\mathrm {V} }$ ${\displaystyle (29.2\times 10^{-6}\;\mathrm {V} )^{2}}$ ${\displaystyle V_{\text{ion}}=10^{-7}\;\mathrm {V} }$ ${\displaystyle \mathrm {Pois} (1/3)}$ ${\displaystyle \sigma _{k}={\sqrt {\lambda }}.}$ ${\displaystyle I=eN/t}$ ${\displaystyle \sigma _{I}=e{\sqrt {N}}/t}$ ${\displaystyle e}$ ${\displaystyle t\sigma _{I}^{2}/I.}$ ${\displaystyle P(k;\lambda )}$ ${\displaystyle P(k;\lambda )}$ ${\displaystyle k}$ ${\displaystyle \lambda }$ ${\displaystyle P(k;\lambda )}$ ${\displaystyle \!f(k;\lambda )=\exp \left[k\ln \lambda -\lambda -\ln \Gamma (k+1)\right],}$ ${\displaystyle \lambda }$ ${\displaystyle \theta _{12},}$ ${\displaystyle \theta _{1}-\theta _{12},}$ ${\displaystyle \theta _{2}-\theta _{12}}$ ${\displaystyle \lambda .}$
