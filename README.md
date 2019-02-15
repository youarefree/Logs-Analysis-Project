#THIS IS THE README FILE OF MY IMPLEMENTATION OF THE LOGS ANALYSIS PROJECT
The project is based on the Python programming language in order to continue and execute it one must first download
and install Python 3 . Here is a link : https://www.python.org/downloads/ . 
I suggest installing python 3.7.1 .

Also, you will need to install a vitrual machine where you would isolate where the project/database will run as on a Linux server
Here is a link : https://www.virtualbox.org/

Another thing you should install is vagrant: Here is a link : https://www.vagrantup.com/downloads.html .
There are different types depending on your OS.

And another thing you need to get the project running is data as like a database. 
Here is a link to download: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
Here's what this command does:

psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql

The database includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles themselves.
The log table includes one entry for each time a user has accessed the site.

After that, you will need to cd into the vagrant directory of your virtual machine so you can get the machine up and running by typing
vagrant up into the terminal and after that use vagrant ssh to connect to it. 

The project can be run by executing the "Logs Analysis".py file which brings out four options. This can happend after you have downloaded 
and set up the virtual machine, vagrant is up and running and you have loaded the database. After those steps are completed you have to 
Execute the python file by typing in the terminal python: python Logs\ Analysis.py

The first three options represent the task that needed to be fulfilled for the project to be successful.
And the fourth exits the program.

Everything about the implementation can be seen in the source code itself. Just to clarify:
The three options run on a similar manner. I am connecting to the 'news' database using the psycopg2 library
and in each of the methods I am using a cursor to go through the records of the database. The difference between the
three of them is the sql query that is being executed and the formatted output at the end.