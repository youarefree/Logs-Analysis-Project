#THIS IS THE README FILE OF MY IMPLEMENTATION OF THE LOGS ANALYSIS PROJECT

The project can be run by executing the "Logs Analysis".py file which brings out four options.
The first three options represent the task that needed to be fulfilled for the project to be successful.
And the fourth exits the program.

Everything about the implementation can be seen in the source code itself. Just to clarify:
The three options run on a similar manner. I am connecting to the 'news' database using the psycopg2 library
and in each of the methods I am using a cursor to go through the records of the database. The difference between the
three of them is the sql query that is being executed and the formatted output at the end.