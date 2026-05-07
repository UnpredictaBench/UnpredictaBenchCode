# Fréchet distribution

Continuous probability distribution

| Fréchet |
| --- |
| Probability density function |
| Cumulative distribution function |
| Parameters | α ∈ ( 0 , ∞ ) {\displaystyle \ \alpha \in (0,\infty )\ } shape. (Optionally, two more parameters) s ∈ ( 0 , ∞ ) {\displaystyle \ s\in (0,\infty )\ } scale (default: s = 1 {\displaystyle \ s=1\ } ) m ∈ ( − ∞ , ∞ ) {\displaystyle \ m\in (-\infty ,\infty )\ } location of minimum (default: m = 0 {\displaystyle \ m=0\ } ) ${\displaystyle \ \alpha \in (0,\infty )\ }$ ${\displaystyle \ s\in (0,\infty )\ }$ ${\displaystyle \ s=1\ }$ ${\displaystyle \ m\in (-\infty ,\infty )\ }$ ${\displaystyle \ m=0\ }$ |
| Support | x > m {\displaystyle \ x>m\ } ${\displaystyle \ x>m\ }$ |
| PDF | α s ( x − m s ) − 1 − α e − ( x − m s ) − α {\displaystyle \ {\frac {\ \alpha \ }{s}}\left({\frac {\ x-m\ }{s}}\right)^{-1-\alpha }~e^{-({\frac {x-m}{s}})^{-\alpha }}\ } ${\displaystyle \ {\frac {\ \alpha \ }{s}}\left({\frac {\ x-m\ }{s}}\right)^{-1-\alpha }~e^{-({\frac {x-m}{s}})^{-\alpha }}\ }$ |
| CDF | e − ( x − m s ) − α {\displaystyle \ e^{-({\frac {x-m}{s}})^{-\alpha }}\ } ${\displaystyle \ e^{-({\frac {x-m}{s}})^{-\alpha }}\ }$ |
| Quantile | m + s [ − ln ⁡ p ] − 1 α {\displaystyle \ m+s\left[\ -\ln p\ \right]^{-{\tfrac {1}{\alpha }}}\ } ${\displaystyle \ m+s\left[\ -\ln p\ \right]^{-{\tfrac {1}{\alpha }}}\ }$ |
| Mean | { m + s Γ ( 1 − 1 α ) for α > 1 ∞ otherwise {\displaystyle {\begin{cases}\ m\ +\ s\ \Gamma \left(1-{\tfrac {1}{\alpha }}\right)~~&{\text{for }}~\alpha >1\\\ \infty &{\text{otherwise}}\end{cases}}} ${\displaystyle {\begin{cases}\ m\ +\ s\ \Gamma \left(1-{\tfrac {1}{\alpha }}\right)~~&{\text{for }}~\alpha >1\\\ \infty &{\text{otherwise}}\end{cases}}}$ |
| Median | m + s ln ⁡ ( 2 ) 1 α {\displaystyle \ m\ +\ {\frac {s}{\ {\ln(2)}^{\tfrac {1}{\alpha }}\ }}} ${\displaystyle \ m\ +\ {\frac {s}{\ {\ln(2)}^{\tfrac {1}{\alpha }}\ }}}$ |
| Mode | m + s ( α 1 + α ) 1 / α {\displaystyle \ m\ +\ s\left({\frac {\alpha }{\ 1+\alpha }}\right)^{1/\alpha \ }} ${\displaystyle \ m\ +\ s\left({\frac {\alpha }{\ 1+\alpha }}\right)^{1/\alpha \ }}$ |
| Variance | { s 2 [ Γ ( 1 − 2 α ) − [ Γ ( 1 − 1 α ) ] 2 ] for α > 2 ∞ otherwise {\displaystyle {\begin{cases}\ s^{2}\left[\ \Gamma \left(1-{\tfrac {2}{\alpha }}\right)-\left[\Gamma \left(1-{\tfrac {1}{\alpha }}\right)\right]^{2}\ \right]~~&{\text{for }}~\alpha >2\\\ \infty &{\text{otherwise}}\end{cases}}} ${\displaystyle {\begin{cases}\ s^{2}\left[\ \Gamma \left(1-{\tfrac {2}{\alpha }}\right)-\left[\Gamma \left(1-{\tfrac {1}{\alpha }}\right)\right]^{2}\ \right]~~&{\text{for }}~\alpha >2\\\ \infty &{\text{otherwise}}\end{cases}}}$ |
| Skewness | { A B 3 for α > 3 ∞ otherwise {\displaystyle {\begin{cases}\ {\frac {\ A\ }{\ {\sqrt {B^{3}\ }}\ }}~~&{\text{for }}~\alpha >3\\\ \infty &{\text{otherwise}}\end{cases}}} where A ≡ Γ ( 1 − 3 α ) − 3 Γ ( 1 − 2 α ) Γ ( 1 − 1 α ) + 2 [ Γ ( 1 − 1 α ) ] 3 {\displaystyle {\begin{aligned}{\text{where}}~~A\ \equiv \ &\Gamma \left(1-{\tfrac {3}{\alpha }}\right)\\&-\ 3\ \Gamma \left(1-{\tfrac {2}{\alpha }}\right)\ \Gamma \left(1-{\tfrac {1}{\alpha }}\right)\\&\quad +\ 2{\Bigl [}\ \Gamma \left(1-{\tfrac {1}{\alpha }}\right)\ {\Bigr ]}^{3}\ \end{aligned}}} and B ≡ Γ ( 1 − 2 α ) − [ Γ ( 1 − 1 α ) ] 2 . {\displaystyle ~\quad {\text{and}}~~B\ \equiv \ \Gamma \left(1-{\tfrac {2}{\alpha }}\right)\ -\ {\Bigr [}\ \Gamma \left(1-{\tfrac {1}{\alpha }}\right)\ {\Bigr ]}^{2}~.} ${\displaystyle {\begin{cases}\ {\frac {\ A\ }{\ {\sqrt {B^{3}\ }}\ }}~~&{\text{for }}~\alpha >3\\\ \infty &{\text{otherwise}}\end{cases}}}$ ${\displaystyle {\begin{aligned}{\text{where}}~~A\ \equiv \ &\Gamma \left(1-{\tfrac {3}{\alpha }}\right)\\&-\ 3\ \Gamma \left(1-{\tfrac {2}{\alpha }}\right)\ \Gamma \left(1-{\tfrac {1}{\alpha }}\right)\\&\quad +\ 2{\Bigl [}\ \Gamma \left(1-{\tfrac {1}{\alpha }}\right)\ {\Bigr ]}^{3}\ \end{aligned}}}$ ${\displaystyle ~\quad {\text{and}}~~B\ \equiv \ \Gamma \left(1-{\tfrac {2}{\alpha }}\right)\ -\ {\Bigr [}\ \Gamma \left(1-{\tfrac {1}{\alpha }}\right)\ {\Bigr ]}^{2}~.}$ |
| Excess kurtosis | { − 6 + C D 2 for α > 4 ∞ otherwise {\displaystyle {\begin{cases}\ -6\ +\ {\frac {\ C\ }{\;D^{2}}}~~&{\text{for }}~\alpha >4\\\ \infty &{\text{otherwise}}\end{cases}}} where C ≡ Γ ( 1 − 4 α ) − 4 Γ ( 1 − 3 α ) Γ ( 1 − 1 α ) + 3 [ Γ ( 1 − 2 α ) ] 2 {\displaystyle {\begin{aligned}{\text{where}}~~C\ \equiv \ &\Gamma \left(1-{\tfrac {4}{\alpha }}\right)\\&-\ 4\ \Gamma \left(1-{\tfrac {3}{\alpha }}\right)\ \Gamma \left(1-{\tfrac {1}{\alpha }}\right)\\&\qquad +\ 3\ {\Bigl [}\ \Gamma \left(1-{\tfrac {2}{\alpha }}\right)\ {\Bigr ]}^{2}\ \end{aligned}}} and D ≡ Γ ( 1 − 2 α ) − [ Γ ( 1 − 1 α ) ] 2 . {\displaystyle ~\quad {\text{and}}~~D\ \equiv \ \Gamma \left(1-{\tfrac {2}{\alpha }}\right)\ -\ {\Bigl [}\ \Gamma \left(1-{\tfrac {1}{\alpha }}\right)\ {\Bigr ]}^{2}~.} ${\displaystyle {\begin{cases}\ -6\ +\ {\frac {\ C\ }{\;D^{2}}}~~&{\text{for }}~\alpha >4\\\ \infty &{\text{otherwise}}\end{cases}}}$ ${\displaystyle {\begin{aligned}{\text{where}}~~C\ \equiv \ &\Gamma \left(1-{\tfrac {4}{\alpha }}\right)\\&-\ 4\ \Gamma \left(1-{\tfrac {3}{\alpha }}\right)\ \Gamma \left(1-{\tfrac {1}{\alpha }}\right)\\&\qquad +\ 3\ {\Bigl [}\ \Gamma \left(1-{\tfrac {2}{\alpha }}\right)\ {\Bigr ]}^{2}\ \end{aligned}}}$ ${\displaystyle ~\quad {\text{and}}~~D\ \equiv \ \Gamma \left(1-{\tfrac {2}{\alpha }}\right)\ -\ {\Bigl [}\ \Gamma \left(1-{\tfrac {1}{\alpha }}\right)\ {\Bigr ]}^{2}~.}$ |
| Entropy | 1 + γ α + γ e + ln ⁡ ( s α ) , {\displaystyle \ 1+{\frac {\gamma }{\alpha }}+\gamma _{e}+\ln \left({\frac {s}{\alpha }}\right)\ ,} where γ e {\displaystyle \ \gamma _{e}\ } is the Euler–Mascheroni constant. ${\displaystyle \ 1+{\frac {\gamma }{\alpha }}+\gamma _{e}+\ln \left({\frac {s}{\alpha }}\right)\ ,}$ ${\displaystyle \ \gamma _{e}\ }$ |
| MGF | [1] Note: Moment k {\displaystyle \ k\ } exists if α > k {\displaystyle \ \alpha >k\ } ${\displaystyle \ k\ }$ ${\displaystyle \ \alpha >k\ }$ |
| CF | [1] |

The Fréchet distribution, also known as inverse Weibull distribution,[2][3] is a special case of the generalized extreme value distribution. It has the cumulative distribution function
{\displaystyle \ \Pr(\ X\leq x\ )=e^{-x^{-\alpha }}~{\text{ if }}~x>0~.} ${\displaystyle \ \Pr(\ X\leq x\ )=e^{-x^{-\alpha }}~{\text{ if }}~x>0~.}$

where  α > 0  is a shape parameter. It can be generalised to include a location parameter m (the minimum) and a scale parameter  s > 0  with the cumulative distribution function
{\displaystyle \ \Pr(\ X\leq x\ )=\exp \left[\ -\left({\tfrac {\ x-m\ }{s}}\right)^{-\alpha }\ \right]~~{\text{ if }}~x>m~.} ${\displaystyle \ \Pr(\ X\leq x\ )=\exp \left[\ -\left({\tfrac {\ x-m\ }{s}}\right)^{-\alpha }\ \right]~~{\text{ if }}~x>m~.}$

Named for Maurice Fréchet who wrote a related paper in 1927,[4] further work was done by Fisher and Tippett in 1928 and by Gumbel in 1958.[5][6]

Characteristics[edit]
The single parameter Fréchet, with parameter 
{\displaystyle \ \alpha \ ,}

 has standardized moment
{\displaystyle \mu _{k}=\int _{0}^{\infty }x^{k}f(x)\ \operatorname {d} x=\int _{0}^{\infty }t^{-{\frac {k}{\alpha }}}e^{-t}\ \operatorname {d} t\ ,}

(with 
{\displaystyle \ t=x^{-\alpha }\ }

) defined only for 
{\displaystyle \ k<\alpha \ :}
{\displaystyle \ \mu _{k}=\Gamma \left(1-{\frac {k}{\alpha }}\right)\ }

where 
{\displaystyle \ \Gamma \left(z\right)\ }

 is the Gamma function.
In particular:
{\displaystyle \alpha >1}

 the expectation is 
{\displaystyle E[X]=\Gamma (1-{\tfrac {1}{\alpha }})}
{\displaystyle \alpha >2}

 the variance is 
{\displaystyle {\text{Var}}(X)=\Gamma (1-{\tfrac {2}{\alpha }})-{\big (}\Gamma (1-{\tfrac {1}{\alpha }}){\big )}^{2}.}

The quantile 
{\displaystyle q_{y}}

 of order 

y

{\displaystyle y}

 can be expressed through the inverse of the distribution,
{\displaystyle q_{y}=F^{-1}(y)=\left(-\log _{e}y\right)^{-{\frac {1}{\alpha }}}}

.
In particular the median is:
{\displaystyle q_{1/2}=(\log _{e}2)^{-{\frac {1}{\alpha }}}.}

The mode of the distribution is 
{\displaystyle \left({\frac {\alpha }{\alpha +1}}\right)^{\frac {1}{\alpha }}.}

Especially for the 3-parameter Fréchet, the first quartile is 
{\displaystyle q_{1}=m+{\frac {s}{\sqrt[{\alpha }]{\log(4)}}}}

 and the third quartile
{\displaystyle q_{3}=m+{\frac {s}{\sqrt[{\alpha }]{\log({\frac {4}{3}})}}}.}

Also the quantiles for the mean and mode are:
{\displaystyle F(mean)=\exp \left(-\Gamma ^{-\alpha }\left(1-{\frac {1}{\alpha }}\right)\right)}
{\displaystyle F(mode)=\exp \left(-{\frac {\alpha +1}{\alpha }}\right).}

Properties[edit]
The Frechet distribution is a max stable distribution
The negative of a random variable having a Frechet distribution is a min stable distribution
Related distributions[edit]
The cumulative distribution function of the Frechet distribution solves the maximum stability postulate equation.
Scaling relations include:
{\displaystyle \ X\sim U(\ 0,1\ )\ }

 (continuous uniform distribution) then 

m
+
s
⋅

(

−

log

e

(
X
)

)

−
1

α

∼

Frechet
{\displaystyle \ m+s\cdot {\Bigl (}-\log _{e}\!(X)\ {\Bigr )}^{\frac {-1\;}{\alpha }}\sim {\textsf {Frechet}}(\alpha ,s,m)\ }

If 

X
∼

Frechet
{\displaystyle \ X\sim {\textsf {Frechet}}(\ \alpha ,s,m=0\ )\ }

 then its reciprocal is Weibull-distributed: 

1

X

∼

Weibull
{\displaystyle \ {\frac {\ 1\ }{X}}\sim {\textsf {Weibull}}\!\left(\ k=\alpha ,\lambda ={\tfrac {1}{s}}\ \right)\ }

If 

X
∼

Frechet
{\displaystyle \ X\sim {\textsf {Frechet}}(\alpha ,s,m)\ }

 then 

k

X
+
b
∼

Frechet
{\displaystyle \ k\ X+b\sim {\textrm {Frechet}}(\ \alpha ,ks,k\ m+b\ )\ }

If 

X

i

∼

Frechet
{\displaystyle \ X_{i}\sim {\textsf {Frechet}}(\ \alpha ,s,m\ )\ }
{\displaystyle \ Y=\max\{\ X_{1},\ldots ,X_{n}\ \}\ }

 then 

Y
∼

Frechet
{\displaystyle \ Y\sim {\textsf {Frechet}}(\ \alpha ,n^{\tfrac {1}{\alpha }}s,m\ )\ }

Applications[edit]
Fitted cumulative Fréchet distribution to extreme one-day rainfalls
Fitted decline curve analysis. Duong model can be thought of as a generalization of the Frechet distribution.
In hydrology, the Fréchet distribution is applied to extreme events such as annually maximum one-day rainfalls and river discharges.[7] This picture illustrates an example of fitting the Fréchet distribution to ranked annually maximum one-day rainfalls in Oman showing also the 90% confidence belt based on the binomial distribution. The cumulative frequencies of the rainfall data are represented by plotting positions as part of the cumulative frequency analysis. However, in most hydrological applications, the distribution fitting is via the generalized extreme value distribution as this avoids imposing the assumption that the distribution does not have a lower bound (as required by the Frechet distribution). [citation needed]
In decline curve analysis, a declining pattern the time series data of oil or gas production rate over time for a well can be described by the Fréchet distribution.[8]
One test to assess whether a multivariate distribution is asymptotically dependent or independent consists of transforming the data into standard Fréchet margins using the transformation 
{\displaystyle Z_{i}=-1/\log F_{i}(X_{i})}

 and then mapping from Cartesian to pseudo-polar coordinates 
{\displaystyle (R,W)=(Z_{1}+Z_{2},Z_{1}/(Z_{1}+Z_{2}))}

. Values of 
{\displaystyle R\gg 1}

 correspond to the extreme data for which at least one component is large while 

W

{\displaystyle W}

 approximately 1 or 0 corresponds to only one component being extreme.
In economics it is used to model the idiosyncratic component of preferences of individuals for different products (Industrial Organization), locations (Urban Economics), or firms (Labor Economics).
