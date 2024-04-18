# This will cover the following material:
- Variables
- Data Types
- Conditionals

## Variables and Data Types 

| Data Type     | Description                                   |
|---------------|-----------------------------------------------|
| bool          | Represents a Boolean value (`true` or `false`)|
| byte          | Represents an unsigned 8-bit integer          |
| sbyte         | Represents a signed 8-bit integer            |
| short         | Represents a signed 16-bit integer           |
| ushort        | Represents an unsigned 16-bit integer        |
| int           | Represents a signed 32-bit integer           |
| uint          | Represents an unsigned 32-bit integer        |
| long          | Represents a signed 64-bit integer           |
| ulong         | Represents an unsigned 64-bit integer        |
| float         | Represents a single-precision floating point number |
| double        | Represents a double-precision floating point number |
| decimal       | Represents a decimal floating point number   |
| char          | Represents a Unicode character               |
| string        | Represents a sequence of characters          |
| object        | Represents any type of object                |


We will use the variable `A` and the variable `B`
- `A` will be equal to 40
- `B` will be equal to 60
- Run the program and see what happens

Notice you have errors with the name A and B doesnt exist. To correct this we
will have to assign them a data type.
- Before the Variable we will have to give it a data type
- Lets give the variable `A` the data type of `double`
- Lets make `B` a `int`
- Run the program and see what happens

The program runs! However nothing happens. The key things to take away is Variables
have to have a type. We also learned where the error panel is. We saw a failed
run and a successful run.

Lets add the variables `A` and `B` together
- make a variable `sum`
- have it adding the values stored in variables A and B.
- Run the program and see what happens

What data type did assign the variable `sum`? If you didn't use the data type double
you will notice you got an error. This is because in C#, when you perform arithmetic
operations between different numeric types (such as double and int), the result is
automatically promoted to the larger type to maintain precision and avoid loss of data.


---

## Operators and Conditional Statements 


| Category             | Operator | Description                                                |
|----------------------|----------|------------------------------------------------------------|
| Arithmetic Operators | `+`      | Addition                                                   |
|                      | `-`      | Subtraction                                                |
|                      | `*`      | Multiplication                                             |
|                      | `/`      | Division                                                   |
|                      | `%`      | Modulus (Remainder)                                        |
| Assignment Operators | `=`      | Assigns a value to a variable                              |
|                      | `+=`     | Adds right operand to the left operand and assigns         |
|                      | `-=`     | Subtracts right operand from the left operand and assigns  |
|                      | `*=`     | Multiplies right operand with the left operand and assigns |
|                      | `/=`     | Divides left operand by right operand and assigns          |
|                      | `%=`     | Computes modulus of the left operand with the right operand and assigns |
| Comparison Operators | `==`     | Equality                                                   |
|                      | `!=`     | Inequality                                                 |
|                      | `>`      | Greater than                                               |
|                      | `<`      | Less than                                                  |
|                      | `>=`     | Greater than or equal to                                   |
|                      | `<=`     | Less than or equal to                                      |
| Logical Operators    | `&&`     | Logical AND                                                |
|                      | `||`     | Logical OR                                                 |
|                      | `!`      | Logical NOT                                                |
| Bitwise Operators    | `&`      | Bitwise AND                                                |
|                      | `|`      | Bitwise OR                                                 |
|                      | `^`      | Bitwise XOR (Exclusive OR)                                 |
|                      | `~`      | Bitwise NOT (One's complement)                             |
|                      | `<<`     | Left shift                                                 |
|                      | `>>`     | Right shift                                                |
| Conditional Operator | `? :`    | Ternary conditional operator                               |




| Conditional Statement | Description                                                                           |
|-----------------------|---------------------------------------------------------------------------------------|
| `if`                  | Executes a block of code if the specified condition is true.                          |
| `else`                | Executes a block of code if the preceding `if` condition is false.                     |
| `else if`             | Allows you to specify a new condition if the preceding `if` condition is false.        |
| `switch`              | Evaluates an expression and executes code blocks based on matching cases.              |
| `case`                | Specifies a value or expression that matches the value of the `switch` expression.     |
| `default`             | Specifies the code block to be executed if no `case` matches the `switch` expression.  |
| `?:` (ternary)        | Provides a compact way to write conditional expressions.                               |


Conditionals will be important in the program logic. We will get started with
some basic conditionals using our variables from above.

- Let's write an `if` statement to check if A is greater than B
- Remember, an `if` statement begins with the `if` keyword, followed by a
condition in parentheses, and then the code block you want to execute if the
condition is true, enclosed in curly braces
- Start with `if` then write 'A > B' inside the parentheses
- I want to print 'A is greater than B'. So, I'll write
`Console.WriteLine("A is greater than B");` inside the curly braces
- run the code

**If the code has an error google if statement syntax in C#**

What happened when you ran the code?
- You should have noticed nothing was printed. This is because `A` isn't greater
than `B`.

-Now copy your code that you wrote and flip the variable. Be sure to edit the
print statement.

- Now we get a console message that tells us B is greater than A!

Lets now comment out our 2 `if` statements. Highlight both if statement and then
hit control & ? (on mac command & ?). This will add `//` to the beginning of the
line making it so the code no longer runs.
- We are going to combine both if statement adding a else clause to the code.
- Take the first if statement and copy it below.
- at the end of it on a new line add `else`
- add a new set of curly braces
- Then put `Console.WriteLine("B is greater than A");` in between them

When you run the code now it should just print "B is greater than A"
- This is cleaner than having 2 seperate sets of logic working to solve the same
problem.
- We need to add one more condition to this code.
- add a `else if` condition between the `if` and `else`
- our new condition needs to address if `A` is equal `==` to `B`
- run the code and veriy no errors.

# Recap What We learned
Here's an overview of what we learned from this code:

- Variable Declaration and Initialization: We learned how to declare and
initialize variables in C#. In this code, A is declared as a double and
initialized with the value 40, while B is declared as an int and initialized
with the value 60.
- Arithmetic Operations: We learned how to perform arithmetic operations in C#.
Specifically, we saw how to add two variables together using the + operator.
- Output to Console: We learned how to output text to the console using the
Console.WriteLine() method. In this code, we printed the sum of variables A and
B to the console.
- Conditional Statements: We learned about conditional statements in C# using
if, else if, and else. These statements allow us to execute different blocks of
code based on different conditions. In this code, we used conditional statements
to determine whether A is greater than B, equal to B, or less than B, and
printed the corresponding message to the console based on the result.
- Code Commenting: We learned about code commenting in C#. Comments are used to
document and explain code. In this code, we saw how to comment out sections of
code using // to temporarily disable them.

Overall, this code provided a hands-on introduction to basic C# concepts such as
variables, arithmetic operations, output to console, and conditional statements.
It also demonstrated the importance of code commenting for clarity and
maintainability.





