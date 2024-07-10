## 1. Palindrome

Approach - 1:

```prolog
% One Liner!
palindrome(List) :- reverse(List, List).
```

Approach - 2:

```prolog
palindrome([]).
palindrome([_]).

palindrome(List):-
    append([Head|Tail], [Head], List),
    palindrome(Tail).
```

Query: `palindrome([1,2,2,1]).`

<br/>

## 2. Tower of Hanoi

```prolog
move(1,X,Y,_):- 
    write('Move top disk from:  '), write(X), write(' to '), write(Y), nl.

move(N,X,Y,Z):- N > 1, M is N - 1,
    			move(M, X, Z, Y),
    			move(1, X, Y, _),
    			move(M, Z, Y, X).

hanoi(N):- move(N,left,right,center).
```

Query: `hanoi(3).`

<br/>

## 3. Monkey Banana

```prolog
perform(grasp, 
        state(middle, middle, onbox, hasnot), 
        state(middle, middle, onbox, has)).

perform(climb, 
        state(MP, BP, onfloor, H), 
        state(MP, BP, onbox, H)).

perform(push(P1, P2), 
        state(P1, P1, onfloor, H), 
        state(P2, P2, onfloor, H)).

perform(walk(P1, P2), 
        state(P1, BP, onfloor, H), 
        state(P2, BP, onfloor, H)).

getfood(state(_, _, _, has)).

getfood(State1) :- perform(Action, State1, State2), nl, 
    			   write('In '), write(State1), nl,
    			   write('Trying '), write(Action), nl,
    			   getfood(State2).
```

Query: `getfood(state(atdoor, nearwindow, onfloor, hasnot)).`

<br/>

## 4. Quick Sort using Cut

```prolog
quick_sort([], []).
quick_sort([X], [X]).

quick_sort([Pivot|Rest], SortedList):-
    		partition(Rest, Pivot, Less, Greater),
    		quick_sort(Less, SortedLess),
    		quick_sort(Greater, SortedGreater),
    		append(SortedLess, [Pivot|SortedGreater], SortedList).

partition([], _, [], []).

partition([X|Rest], Pivot, [X|Less], Greater):- 
                    X =< Pivot, !,
    				partition(Rest, Pivot, Less, Greater).

partition([X|Rest], Pivot, Less, [X|Greater]):- 
                    X > Pivot, !,
    				partition(Rest, Pivot, Less, Greater).
```

Query: `quick_sort([3,6,8,10,1,2,1], SortedList).`

<br/>

## 5. Binary Tree Traversal

```prolog
tree(A):- A = tree(1, 
                   tree(2, 
                        tree(4, nil, nil), 
                        tree(5, nil, nil)), 
                   tree(3, 
                        tree(6, nil, nil), 
                        tree(7, nil, nil))).

% Inorder traversal: Left, Root, Right
inorder(nil, []).
inorder(tree(Value, Left, Right), Result) :-
    inorder(Left, LeftResult),
    inorder(Right, RightResult),
    append(LeftResult, [Value|RightResult], Result).

% Preorder traversal: Root, Left, Right
preorder(nil, []).
preorder(tree(Value, Left, Right), [Value|Result]) :-
    preorder(Left, LeftResult),
    preorder(Right, RightResult),
    append(LeftResult, RightResult, Result).

% Postorder traversal: Left, Right, Root
postorder(nil, []).
postorder(tree(Value, Left, Right), Result) :-
    postorder(Left, LeftResult),
    postorder(Right, RightResult),
    append(LeftResult, RightResult, Subtrees),
    append(Subtrees, [Value], Result).
```

Query: `tree(T), inorder(T, Result).` <br>
Query: `tree(T), preorder(T, Result).` <br>
Query: `tree(T), postorder(T, Result).`

<br/>

## 6. Breadth First Search (BFS)

```prolog
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).

bfs(Start, Goal, Path):- bfs_queue([[Start]], Goal, Path).

bfs_queue([[Goal|Visited]|_], Goal, [Goal|Visited]).

bfs_queue([[Node|Visited]|Rest], Goal, Path):-
        Node \== Goal,              				
        findall([Next,Node|Visited], (edge(Node, Next), \+ member(Next, Visited)), NextPaths),
        append(Rest, NextPaths, NewPaths),
        bfs_queue(NewPaths, Goal, Path).

bf_search(Start, Goal):- 
        bfs(Start, Goal, Path), 
        reverse(Path, Solution), 
    	write('Path from '), write(Start), 
    	write(' to '), write(Goal), write(': '), 
    	write(Solution).
```

Query: `bf_search(a, g).`

<br/>

## 7. Depth First Search (DFS)

```prolog
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).

dfs(Start, Goal, Path):- dfs_helper(Start, Goal, [], Path).

dfs_helper(Goal, Goal, _, [Goal]).

dfs_helper(Node, Goal, Visited, [Node|Path]):-
    Node \== Goal,                         
    edge(Node, Next),                     
    \+ member(Next, Visited),             
    dfs_helper(Next, Goal, [Node|Visited], Path). 

df_search(Start, Goal):- dfs(Start, Goal, Path), 
    					 write('Path from '), write(Start), 
    					 write(' to '), write(Goal), 
    					 write(': '), write(Path).
```

Query: `df_search(a, g).`

<br>

### [Knowledge Base Related](../README.md)
