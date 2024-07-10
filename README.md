# MCS-555-(B): <br> Artificial Intelligence LAB

[Visit my Swi-Prolog Notebook](https://swish.swi-prolog.org/p/MCS-555-B:%20AI-Lab.swinb)📖

#

**1. Given the following facts:**
>- Steve only likes easy course.
>- Science course are hard.
>- All the courses in the basket weaving department are easy.
>- BK301 is a basket weaving course.

Write a program to find “What course would Steve like?”

```prolog
likes(steve, X):- easy_course(X).
hard_course(science_course).
easy_course(X):- basket_weaving_course(X).
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
likes(sam, Food):- indian_mild_food(Food).
likes(sam, Food):- chinese_food(Food).
likes(sam, Food):- italian_food(Food).
likes(sam, chips).

indian_food(curry).
indian_food(dal).
indian_food(tandoori).
indian_food(kurma).

indian_mild_food(Food):- indian_food(Food), Food \= curry. 

chinese_food(chowmein).
chinese_food(chopsuey).
chinese_food(sweetandsour).

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
likes(john, X) :- food(X).
food(apple).
food(chicken).

:- discontiguous eats/2.

food(X) :- eats(A, X), alive(A, X).
eats(bill, peanuts).
alive(bill, peanuts).
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
reads(john).
wealthy(john).
smart(X):- reads(X).
happy(X):- not(poor(X)), smart(X).
stupid(X):- not(smart(X)).
exciting_life(X):- happy(X).
poor(X):- not(wealthy(X)).
```

- [ See Solution in Prolog](prolog-solutions/Q-04.pl)✅ 
- Query - `exciting_life(john).`

 
<br>
<br>
<br>


**5. Given the following facts:**
>- Marcus was a man.
>- Marcus was a Pompeian.
>- All Pompeian's were Roman.
>- Caesar was a ruler.
>- All Roman were loyal to Caesar or hated him.
>- Everyone is loyal to someone.
>- People only try to assassinate ruler they are not loyal to.
>- Marcus try to assassinate Caesar.
>- All men are people.
 
Write a Program to find: 

&nbsp; &nbsp; &nbsp; a) Is Marcus loyal to Caesar? <br>
&nbsp; &nbsp; &nbsp; b) Does Marcus hate Caesar?”

```prolog
man(marcus).
pompeian(marcus).
pompeian(X) :- roman(X).
ruler(caesar).

loyal_to(X, Y):- not(try_assassinate(X, Y)).
hates(X, Y):- not(loyal_to(X, Y)).
roman(X):- (loyal_to(X, caesar) ; hates(X, caesar)).

try_assassinate(marcus, caesar).
try_assassinate(X, Y):- person(X), ruler(Y), not(loyal_to(X, Y)).
person(X):- man(X).
```


- Query - `loyal_to(marcus, caesar).`
- Query - `hates(marcus, caesar).`


<br>
<br>
<br>