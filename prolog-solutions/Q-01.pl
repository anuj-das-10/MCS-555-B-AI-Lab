% Define likes predicate for Steve based on easy courses
likes(steve, Course):- easy_course(Course).

% Define predicate for science courses being hard
hard_course(science_course).

% Define predicate for courses in the basket weaving department being easy
easy_course(Course):- basket_weaving_course(Course).

% Define BK301 as a basket weaving course
basket_weaving_course(bk301).