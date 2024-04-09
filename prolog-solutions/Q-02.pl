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
 