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