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