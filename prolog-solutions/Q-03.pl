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