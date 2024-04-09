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