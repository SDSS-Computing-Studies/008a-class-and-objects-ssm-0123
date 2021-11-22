## SDSS Computing Studies Python Assignment
### Assignment #008 Objects and Classes (Total Marks 10)

Objectives:
* Create an Object class
* Describe what instantiation means
* Create object methods and properties

Imagine a car.  We all know what a car looks like, because there is an 
archetypical car.  It has 4 wheels, seats and a steering wheel.  However
we are thinking of the generic car with no particular car in mind.

Now think of your parents car - or your car.  It has some very specific
details.  It has specific brand and size of tires, and the seats are
of a certain fabric and color.  Your car is a specific example of
the generic car archetype.

In programming, we have programs that follow this same example.  There
is an archetype or template.  We call this a "class".  The class has
certain properties, just like a car has basic features.  There are things
that it does when you do certain things, like press the horn.  These
are generic methods or functions that parts of the car can perform

When you think of a specific class and give it some details, we are
thinking about a specific instance of the class. It can now have some
specific details.

Consider a data structure that is used to model a hockey player in a
video game.  This class might contain the stats of the player as well
as some identifying features.  It might have some properties/variables
for:
name
team
age
position
salary
etc.
It might also have properties/variables for things that might make the
game work:
speed
shot_accuracy
passing
puck_handling
agility
fighting
There might be methods/functions that determine things using the stats:
shot_on_net()
accurate_pass()
land_punch()

To create a specific player, we need to instantiate it, or create an
instance.  Today we will work through the basics of defining a class
of objects, as well as instantiating an example.

Review the contents of example1.py to see how a class is defined, and
then instantiated.


### 01 Tasks

##### Task 1
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)



