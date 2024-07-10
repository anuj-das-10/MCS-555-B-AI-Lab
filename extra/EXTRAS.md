**1. Write a program to perform the following arithmetic operations on two numbers:** <br>
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

**2. Write a program to compute the factorial of a non-negative integer.**

```prolog
factorial:-
    write('Enter a non-negative integer: '),	% Prompt user for input
    read(N),	% Read input from user
    % Check if input is an integer and non-negative
    (   integer(N), N >= 0 ->
        calculate_factorial(N, Result),
        format("Factorial of ~d is ~d.~n", [N, Result])
    ;   writeln("Error: Input must be a non-negative integer."), fail
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



**3. Write a program to generate Fibonacci Series upto n-th terms.**

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

<br>
<br>
<br>
