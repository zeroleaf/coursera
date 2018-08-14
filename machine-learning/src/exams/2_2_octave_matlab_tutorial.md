# Octave/Matlab Tutorial

// TBD 添加题目

## 1

> Suppose I first execute the following in Octave/Matlab:
> ```matlab
> A = [1 2; 3 4; 5 6];
> B = [1 2 3; 4 5 6];
> ```
> Which of the following are then valid commands? Check all that apply.
> (Hint: A' denotes the transpose of A.)
>  
>  
> - [x] C = A' + B;
> - [x] C = B * A;
> - [ ] C = A + B;
> - [ ] C = B' * A;

### 解析

A  为 3 x 2 的矩阵; B  为 2 x 3 的矩阵; 从而  
A' 为 2 x 3 的矩阵; B' 为 3 x 2 的矩阵

只有维度相同的矩阵才能相加, 从而 选项1 ✅ 选项3 ❌;  
只有前矩阵的列数与后矩阵的行数相同时才能相乘, 从而 选项2 ✅ 选项4 ❌

## 2

> - [x] B = A(:, 1:2);
> - [x] B = A(1:4, 1:2);
> - [ ] B = A(0:2, 0:4)
> - [ ] B = A(1:2, 1:4);

## 3

> - [x] v = A * x;
> - [ ] v = Ax;
> - [ ] v = A .* x;
> - [ ] v = sum (A * x);

## 4

> - [x] z = sum (v .* w);
> - [x] z = w' * v;
> - [ ] z = v * w;
> - [ ] z = w * v;

##

> - [x] C = X + 1;
> - [x] D = X / 4;
> - [x] B = X .^ 2;
> - [ ] B = X ^ 2;
