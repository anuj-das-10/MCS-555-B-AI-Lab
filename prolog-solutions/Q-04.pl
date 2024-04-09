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