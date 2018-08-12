"""
1.

Suppose m=4 students have taken some class, and the class had a midterm exam and a final exam.
You have collected a dataset of their scores on the two exams, which is as follows:

midterm exam    (midterm exam)^2    final exam
89              7921                96
72              5184                74
94              8836                87
69              4761                78
You'd like to use polynomial regression to predict a student's final exam score
from their midterm exam score. Concretely, suppose you want to fit a model of the
form

h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2h

θ(x)=θ0 + θ1x1 + θ2x2,

where x_1 x1 is the midterm score and x_2 is (midterm score)^2.
Further, you plan to use both feature scaling (dividing by the "max-min", or range,
of a feature) and mean normalization.

What is the normalized feature x_2^{(4)}x2(4) ?
(Hint: midterm = 69, final = 78 is training example 4.)
Please round off your answer to two decimal places and enter in the text box below.
"""
# 求解
x2_list = [7921, 5184, 8836, 4761]

x2_min = min(x2_list)
x2_max = max(x2_list)
x2_avg = sum(x2_list) / len(x2_list)

x_2_4 = (x2_list[3] - x2_avg) / (x2_max - x2_min)

print("x_2_4 is ", round(x_2_4, 2))
# -0.47


"""
2.


You run gradient descent for 15 iterations
with \alpha = 0.3 α=0.3 and compute
J(\theta)J(θ) after each iteration. You find that the
value of J(\theta)J(θ) decreases slowly and is still
decreasing after 15 iterations. Based on this, which of the
following conclusions seems most plausible?

忘记黏贴选项了, o(╯□╰)o

解析:

根据题意, 梯度下降执行了15次之后, J(Θ) 仍旧 **缓慢减小**, 
说明当前的 α 值太小, 应该适度的增大 α 值.
"""


"""
3.

Suppose you have m = 23 training examples with n = 5 features 
(excluding the additional all-ones feature for the intercept term, which you should add). 
The normal equation is 

\theta = (X^TX)^{-1}X^Tyθ=(X^TX)^−1X^Ty. 

For the given values of mm and nn, what are the dimensions of 
\thetaθ, XX, and yy in this equation?

  - [ ] X is 23\times623×6, yy is 23\times623×6, \thetaθ is 6\times66×6
  - [ ] X is 23\times523×5, yy is 23\times123×1, \thetaθ is 5\times55×5
  - [x] X is 23\times623×6, yy is 23\times123×1, \thetaθ is 6\times16×1
  - [ ] X is 23\times523×5, yy is 23\times123×1, \thetaθ is 5\times15×1
  
解析:

根据题意, 我们总共有 n = 5 个特征值, 同时我们需要增加一个特殊的 x0 = 1 的特征值,
因此, 结果 Θ 是一个 6 x 1 的列向量, 据此可以直接判断结果为 3.

同时, 
y 表示的是目标值, 我们总共有 m = 23 个训练样本, 因此 y 为 23 x 1 的列向量;
X 表示的是当前的训练样本, 加上特殊的特征值 x0, 则 X 为 23 x 6 的矩阵
"""


"""
4.

Suppose you have a dataset with m = 50 examples and n = 15 features for each example. 
You want to use multivariate linear regression to fit the parameters θ to our data. 
Should you prefer gradient descent or the normal equation?

  - [ ] Gradient descent, since (X^TX)^{-1}(X^TX)^−1 will be very slow to compute in the normal equation.
  - [ ] The normal equation, since gradient descent might be unable to find the optimal \thetaθ.
  - [ ] Gradient descent, since it will always converge to the optimal \thetaθ.
  - [x] The normal equation, since it provides an efficient way to directly find the solution.
  
解析:

由于 n = 15 是个很小的值(课程中介绍的参考临界值为 10000), 因此我们选择正规方程.
选项2关于正规方程的描述是错误的, 只要选定合适的 α 值, 梯度下降同样可以找到最优的 θ.
相较于正规方程, 梯度下降在特征值比较小的情况下, 执行速度相对较慢.
"""


"""
5.

Which of the following are reasons for using feature scaling?

  - [ ] It speeds up solving for θ using the normal equation.
  - [x] It speeds up gradient descent by making it require fewer iterations to get to a good solution.
  - [ ] It is necessary to prevent gradient descent from getting stuck in local optima.
  - [ ] It prevents the matrix X^TX (used in the normal equation) from being non-invertable (singular/degenerate).
  
解析:

特征缩放的目的是为了标准化特征值, 从而加速梯度下降法的收敛过程. 因此选项2正确.

选项1: 特征缩放只用到了特征值的平均值, 最大/最小值, 并没有使用正规方程求解, 因此错误.
选项3: 特征缩放仅仅是起到了加速求解的过程, 并不能防止梯度下降求解到局部最优解.
选项4: 特征缩放跟正规方程无关.
"""