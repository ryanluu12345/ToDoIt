#Loads dependencies from Python
from flask import Flask,request,render_template,redirect,url_for
from twilio.rest import Client
import datetime
import json


#Instantiates the application and assigns it the name of the file
app=Flask(__name__)

#Creates a route and a corresponding function that will perform actions when the route is called
@app.route("/",methods=["POST","GET"])
def main():
    
    #Checks to see which button was pressed and redirects to corresponding pages based on action
    if request.method=="POST":

        #Checks the value in the form which has the name "submit"
        if request.form["submit"]=="at":
            return redirect(url_for("add_tasks")) #Takes in the function name and variables (function name, variables)

        elif request.form["submit"]=="vt":
            return redirect(url_for("view_tasks"))

        elif request.form["submit"]=="ap":
            return redirect(url_for("add_people"))

        elif request.form["submit"]=="rg":
            return redirect(url_for("remind_group"))
        

    #By defaultrenders specific template from the template folder
    return render_template("index.html")

@app.route("/add_tasks",methods=["POST","GET"])
def add_tasks():
    #Initializes a dictionary that will contain data about the task extracted from the page
    task={}

    #Checks method to ensure that it was post. Takes action following that condition
    if request.method=="POST":

        #Checks to see if the user wants the fields cleared or updated
        if request.form["submit"]=="clear":
            return render_template("add_tasks.html")

        elif request.form["submit"]=="view_tasks":
            return redirect(url_for("view_tasks"))

        else:
            #Retrieves data from user input on the "add_tasks.html" view
            task_description=request.form["description"]
            person_responsible=request.form["person_responsible"]
            due_date=request.form["due_date"]

            #Adds task to the dictionary previously created
            task["description"]=task_description
            task["person_responsible"]=person_responsible
            task["due_date"]=due_date
            task["timestamp"]=str(datetime.datetime.now())

            #Calls method that will save task data
            save_task(task)
    
    return render_template("add_tasks.html")


'''TODO: Make sure to check templating to make sure that it renders correctly '''
@app.route("/view_tasks",methods=["POST","GET"])
def view_tasks():

    task_history=None
    #Checks to see if user submitted a get request to endpoint
    if request.method=="GET":
        with open("tasks.json","r") as json_file:
            task_history=json.load(json_file)
    
    return render_template("view_tasks.html",task_history=task_history)

@app.route("/add_people",methods=["POST","GET"])
def add_people():
    person={}
    if request.method=="POST":
        #Checks to see if the user wants the fields cleared or updated
        if request.form["submit"]=="clear":
            return render_template("add_people.html")

        elif request.form["submit"]=="remind_group":
            return redirect(url_for("remind_group"))

        else:
            #Retrieves data from user input on the "add_tasks.html" view
            name=request.form["name"]
            phone_number=request.form["phone_number"]
            email=request.form["email"]

            #Adds task to the dictionary previously created
            person["name"]=name
            person["phone_number"]=phone_number
            person["email"]=email

            #Calls method that will save task data
            save_person(person)
        
    return render_template("add_people.html")

@app.route("/remindGroup",methods=["POST","GET"])
def remind_group():
    group=None
    notif=None
    
    with open("people.json","r") as json_file:
        group=json.load(json_file)

    if request.method=="POST":
        #Gathers phone numbers from the dictionary object
        phone_numbers=[member["phone_number"] for member in group]

        #Method that handles messaging
        send_message(phone_numbers)
        
        #Alert of notification that messages have been sent
        notif="Your group has been notified"
    
    return render_template("remind_group.html",group=group,notif=notif)

#Helper function that uses Twilio to text users
def send_message(numbers):

    with open("credentials.json","r") as json_file:
        user_credentials=json.load(json_file)
    
    #Initializes API client
    client=Client(user_credentials["account_sid"],user_credentials["auth_token"])

    #Loops through phone numbers and sends messages to each person involved
    for number in numbers:
        client.api.account.messages.create(to=number,from_=user_credentials["sender"],body="Hello! Remember to check the task sheet for your tasks")
    

#Helper function that saves task data in JSON format
def save_task(task):
    #Opens up the json file and extracts list 
    with open("tasks.json","r") as json_file:
        task_data=json.load(json_file)
        task_data.append(task)
   
    #Saves the new data
    with open("tasks.json","w") as json_file:
        json.dump(task_data,json_file)

#Helper function that saves people data in JSON format
def save_person(person):
    #Opens up the json file and extracts list 
    with open("people.json","r") as json_file:
        people_data=json.load(json_file)
        people_data.append(person)
   
    #Saves the new data
    with open("people.json","w") as json_file:
        json.dump(people_data,json_file)


#Used for debugging
if __name__=="__main__":
    app.run()
