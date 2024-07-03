## 1. **Facts and Rules**

In Prolog, facts and rules are used to represent knowledge and define logical relationships.

**FACTS**
>Facts are unconditional statements that represent known information about the problem domain. They are written in the form:

```prolog
fact_name(argument1, argument2, ...).
```

Example:
```prolog
parent(john, alice).    % John is the parent of Alice
```

<br>
<br>

**RULES**
>Rules are conditional statements that define relationships or logical implications. They are written in the form:

```prolog
rule_name(argument1, argument2, ...) :- premise1, premise2, ..., premiseN.
```

The part before the `:-` is called the "head" of the rule, and the part after is called the "body". The body consists of one or more premises (goals) that must be satisfied for the rule to be true.

Example:
```prolog
ancestor(X, Y) :- parent(X, Y).                    % X is an ancestor of Y if X is a parent of Y
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).    % X is an ancestor of Y if X is a parent of Z, and Z is an ancestor of Y
```

In this example, the `ancestor/2` predicate is defined using two rules. The first rule states that if `X` is a parent of `Y`, then `X` is an ancestor of `Y`. The second rule states that if `X` is a parent of `Z`, and `Z` is an ancestor of `Y`, then `X` is also an ancestor of `Y`.

<br>
<br>

Facts and rules are the fundamental building blocks of knowledge representation in Prolog. They are used to define relationships, express constraints, and reason about the problem domain.