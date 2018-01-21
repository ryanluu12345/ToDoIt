# ToDoIt

# Final Product: A simple task tracking application that allows one to add tasks, view tasks, add group members, and remind members of tasks. This simple application is used to teach basic concepts of Flask.

# What you will learn about:
- Declaring and setting routes using Flask as a backend
- Handling different requests within routes
- Creating Jinjas/HTML templates to allow for interactive interfaces
- Simply persisting data using JSON files
- Command line basics 
- Deploying your web application to Heroku using the Heroku CLI

# Extended instructions for deploying to Heroku
1. Make sure to download the Heroku command line interface: https://devcenter.heroku.com/articles/heroku-cli

2. Make sure to download the git command line tool: https://git-scm.com/download/win

3. Now that those two are downloaded, enter your command prompt or terminal as a root user (Run as administrator if you are on Windows/Use sudo before commands if on Linux/Type "su" if you are on Mac and it should allow you to enter a password to log in as root)

4. Navigate to your file directory

5. Create a new file called "Procfile". (Make sure that you do not have the ".txt" extension. Otherwise, Heroku will not detect the command in the Procfile.)

6. Inside of Procfile enter this line: "web gunicorn app:app". This command will start our server through gunicorn.

7. Create a new file called "requirements.txt" if there is not a file named that already. Inside of it, place these dependencies with a line break in between each one: 
flask
gunicorn
twilio

8. In terminal enter the commands as follows:
git init
git add --all
git commmit -m "init"
heroku apps:create <replace_with_your_app_name>
git push heroku master

Explanation: 
- "git init" initializes the folder you are in as a git folder/directory, meaning that is eligible for version control 
- "git add --all" adds all files in the directory, including all files in sub-directories
- "git commit -m" is used to commit changes and give a message describing changes
- "heroku apps:create" is used to create a heroku application
- "git push heroku master" is used to send your application to heroku so that it can build your app and deploy it

