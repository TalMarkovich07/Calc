This project is a complex calculator.

The calculator has the regular functions: +, -, *, /, ^, %, !, but also some unregular functions: $ - maximum, & - minimum, @ - average, ~ - negative, and # - sum. 

Here is an explanation to how the calculator work:
The user enters an expression. The expression gets sent to 'run_calculator' function.
This function as a main list which contains lists of every binary operator's level.
the 'run_calculator' searches for the first operand and the first operator.
After finding an operand and operator, they are added to the list in the list that suits the operator's level.
After that, there is while loop that finds the next duo of operand and operator, and if the operator's
level is lower than the one before him, it calulates the expression before and adds the calculation and the operator to the list.
otherwise just the operand and operator are added to the list.
we are adding a +0 at the end so in the last itteration, everything will pop out and be calculated.

the program uses the functions:
semi_in_num() - to make sure the number has 0 or 1 ~.
find_num() - to find the number in a given expression.
calculate_num() - to calculate the unary functions in the given number.
op_level() - to get an operator's level.
calculate_exp() - to calculate a binary expression given two operands and a binary operator.
pop_until() - to remove and calculate everything from the list of lists until a given level.
handle_brackets() - to get the index of the closing bracket and to make sure all brackets are closed.
run_calculator() - uses all of the above functions to calculate an expression
