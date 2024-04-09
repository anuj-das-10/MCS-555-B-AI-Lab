# MCS-555-(B): <br> Artificial Intelligence LAB

Anuj Das <br>
Class Roll Number: 13 <br>
MCS - 8<sup>th</sup> Semester <br>
Department of Computer Science <br>
Assam University, Silchar <br>

[Visit my Swi-Prolog Notebook](https://swish.swi-prolog.org/p/MCS-555-B:%20AI-Lab.swinb)📖

#

**1. Given the following facts:**
>- Steve only likes easy course.
>- Science course are hard.
>- All the courses in the basket weaving department are easy.
>- BK301 is a basket weaving course.

Write a program to find “What course would Steve like?”

```prolog
% Define likes predicate for Steve based on easy courses
likes(steve, Course):- easy_course(Course).

% Define predicate for science courses being hard
hard_course(science_course).

% Define predicate for courses in the basket weaving department being easy
easy_course(Course):- basket_weaving_course(Course).

% Define BK301 as a basket weaving course
basket_weaving_course(bk301).
```

- [ See Solution in Prolog](prolog-solutions/Q-01.pl)✅ 
- Query - `likes(steve, X).`
 

<br>
<br>
<br>
 

**2. Given the following facts:**
>- Sam likes all Indian mild food.
>- Sam likes all Chinese food.
>- Sam likes all Italian food.
>- Sam likes chips.
>- Curry, dal, tandoori, kurma are Indian food.
>- Dal, tandoori, kurma are Indian mild food.
>- Chowmein, chopsuey, sweetandsour are Chinese food.
>- Pizza and spaghetti are Italian food.
 
Write a program to find: <br>
&nbsp; &nbsp; &nbsp; a) What foods does Sam like? <br>
&nbsp; &nbsp; &nbsp; b) Does Sam like Curry? <br>
&nbsp; &nbsp; &nbsp; c) Does Sam like Chips?

```prolog
% Define likes predicate for Sam based on different types of food.

% Sam likes all Indian mild food
likes(sam, Food):- indian_mild_food(Food).

% Sam likes all Chinese food
likes(sam, Food):- chinese_food(Food).

% Sam likes all Italian food
likes(sam, Food):- italian_food(Food).

% Sam likes chips
likes(sam, chips).

% Define Indian food items
indian_food(curry).
indian_food(dal).
indian_food(tandoori).
indian_food(kurma).

% Define Indian mild food items and curry is not considered mild.
indian_mild_food(Food):- indian_food(Food), Food \= curry. 

% Define Chinese food items
chinese_food(chowmein).
chinese_food(chopsuey).
chinese_food(sweetandsour).

% Define Italian food items
italian_food(pizza).
italian_food(spaghetti).
```

- [ See Solution in Prolog](prolog-solutions/Q-02.pl)✅ 
- Query - `likes(sam, X).`
- Query - `likes(sam, curry).`
- Query - `likes(sam, chips).`

 

<br>
<br>
<br>
 

**3. Given the following facts:**
>- John likes all food.
>- Apples are food.
>- Chicken is food.
>- Anything anyone eats and isn’t killed by is food.
>- Bill eats Peanuts and is still alive.
>- Sue eats everything Bill eats.
 
&nbsp; &nbsp; &nbsp; a) Write a Program to prove that “John likes peanuts”. <br>
&nbsp; &nbsp; &nbsp; b) Find “what food does Sue eat?”

```prolog
% Define likes predicate for John based on food
likes(john, X):- food(X).

% Define what constitutes food
food(apple).
food(chicken).
food(peanuts).

% Directive to handle non-consecutive clauses for eats/2 predicate
:- discontiguous eats/2.

% Define food predicate based on what is eaten and not killed by
food(X):- eats(A, X), alive(A, X).

% Define who eats peanuts
eats(bill, peanuts).

% Define that Bill is alive after eating peanuts
alive(bill, peanuts).

% Define what Sue eats based on what Bill eats
eats(sue, X) :- eats(bill, X).
```

- [ See Solution in Prolog](prolog-solutions/Q-03.pl)✅ 
- Query - `likes(john, peanuts).`
- Query - `eats(sue, X).`


<br>
<br>
<br>
 

**4. Given the following facts:**
>- All people who are not poor and are smart are happy.
>- Those people who read are not stupid but smart.
>- John could read and is wealthy.
>- Happy people have exciting lives.
 
Write a Program to prove “John has an exciting life”.

```prolog
% Define predicate for reading
reads(john).

% Define predicate for wealth
wealthy(john).

% Define predicate for intelligence
smart(X):- reads(X).

% Define predicate for happiness
happy(X):- not(poor(X)), smart(X).

% Define predicate for being stupid
stupid(X):- not(smart(X)).

% Define predicate for exciting lives
exciting_life(X):- happy(X).

% Define predicate for being poor(assuming all those not wealthy are poor)
poor(X):- not(wealthy(X)).
```

- [ See Solution in Prolog](prolog-solutions/Q-04.pl)✅ 
- Query - `exciting_life(john).`

 
<br>
<br>
<br>
 

**5. Write a program to perform the following arithmetic operations on two numbers:** <br>
&nbsp; &nbsp; &nbsp; a) Addition  <br>
&nbsp; &nbsp; &nbsp; b) Subtraction  <br>
&nbsp; &nbsp; &nbsp; c) Multiplication  <br>
&nbsp; &nbsp; &nbsp; d) Division 

```prolog
% Predicate to print an arithmetic operation and its result
print(X, Operator, Y, Result):- 
    write(X), write(' '), 
    write(Operator), 
    write(' '), 
    write(Y), 
    write(' = '), 
    write(Result), nl.

% Addition Predicate
add(X, Y):- Z is X + Y, print(X, "+", Y, Z).

% Subtraction Predicate
subtract(X, Y):- Z is X - Y, print(X, "-", Y, Z).

% Multiplication Predicate
multiply(X, Y):- Z is X * Y, print(X, "X", Y, Z).

% Division Predicate
divide(_, Y):- Y = 0, write("Exception: Division by zero!"), nl, !, fail.
divide(X, Y):- Z is X / Y, print(X, "/", Y, Z).ss
```
 
- [ See Solution in Prolog](prolog-solutions/Q-05.pl)✅ 
- Query - `add(6, 4).`
- Query - `subtract(12, 4).`
- Query - `multiply(14, 5).`
- Query - `divide(625, 0).`
- Query - `divide(625, 25).`



<br>
<br>
<br>
 

**6. Write a program to compute the factorial of a non-negative integer.**

```prolog
factorial:-
    write('Enter a non-negative integer: '),	% Prompt user for input
    read(N),	% Read input from user
    % Check if input is an integer and non-negative
    (   integer(N), 
    	% If condition is true, calculate factorial	
   		N >= 0 ->
        calculate_factorial(N, Result),
        % Format and print the factorial result
        format("Factorial of ~d is ~d.~n", [N, Result])
    ;   % If condition is false, print error message
        writeln("Error: Input must be a non-negative integer."), fail
    ).

calculate_factorial(0, 1) :- !. 	% Base case: factorial of 0 is 1
calculate_factorial(N, Result) :-	% Recursive predicate to calculate factorial
    N > 0,
    N1 is N - 1,
    calculate_factorial(N1, SubFactorial),
    Result is N * SubFactorial.
```
 
- [ See Solution in Prolog](prolog-solutions/Q-06.pl)✅ 
- Query - `factorial.`
 

<br>
<br>
<br>
 

**7. Write a program to generate Fibonacci Series upto n-th terms.**

```prolog
fibonacci(N) :-
    calculate_next_term(N, 0, 1), !.

% Helper predicate to generate Fibonacci series recursively
calculate_next_term(0, _, _).
calculate_next_term(N, A, B) :-
    N > 0,
    NextTerm is A + B,
    write(A), write(', '), 		% Print the current Fibonacci number
    N1 is N - 1,
    calculate_next_term(N1, B, NextTerm).
```
 
- [ See Solution in Prolog](prolog-solutions/Q-07.pl)✅ 
- Query - `fibonacci(1).`
- Query - `fibonacci(12).`


