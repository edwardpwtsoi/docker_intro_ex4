# docker_intro_ex4
This is a "just work" solution to the exercise 4 " Your own PaaS" of introdutcion to docker tutorial.
credit to yetanotherchris/docker-automation.py for the nicelogger module

# usage
pip install -r requirements.txt
EXPORT FLASK=app.py
flask run

visit port localhost:5000/postgres/build_and_run with your favourite browser and you will see a port number of the new created postgres container.

Note: Make sure you have docker installed on you computer.
