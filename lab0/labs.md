# Lab & Homework Instructions

### Reference Documentation

#### Flask
	+ [Flask App documentation](https://flask.palletsprojects.com/en/2.0.x/)
	+ [Jinja Template documentation](https://jinja.palletsprojects.com/en/3.0.x/)

#### Heroku
	+ [Getting Started with Heroku and Python](https://devcenter.heroku.com/articles/getting-started-with-python)
	+ [Flask and Heroku](https://devcenter.heroku.com/articles/flask-memcache)
	+ [Deploying to Heroku with Git](https://devcenter.heroku.com/articles/git)

For every lab/homework going unless otherwise indicated, these are the steps every student needs to take:

## A. Before you start labs (before class begins):
	1. Change to the course git repo: `cd <course repo>`
	2. In the course git repository directory, git pull to get the latest assignment/lab code. `git pull`
	3. Change to your git repository directory: `cd <your repo>`
		+ **NOTE: _DO NOT CREATE A NEW GITHUB REPO!!!_**
	4. In your existing git repository directory, copy the new lab code: `cp -r <path to course repo>/<new code dir> .`
	5. Add the new code to your repository: `git add <newly copied code>`
	6. Commit the new code: `git commit -m <added lab n code>`
	7. Push the new (unedited) code to your repo: `git push`
	8. At this point, you will need to create a **new** heroku app for your new assignment, and make sure you can deploy! To do that, you need to remove the old heroku **repo** from the previous assignment: `git remote remove heroku`
	9. Create a new heroku app: `heroku create`
	10. Confirm that the new heroku repo was created: `git remote -v` 
		+ That should show you two remotes: one for GitHub and one for heroku
		
## B. When you start the labs (follow along with the video):
	1. ACTIVATE YOUR CONDA ENVIRONMENT: `conda activate <your lab environment>`
	2. Enter the lab current lab directory: `cd <current lab>`
	3. Complete the lab work, but **do not do your homework assignment(s)**.
	4. Test your work in Flask: `flask run`
	5. Create your requirements.txt file in your lab directory: `pipreqs --force .`
	6. Create/edit your Procfile, it should contain: `gunicorn --pythonpath <lab directory> app:app`
	7. Copy both files to the top level directory: `cd <your repo>; cp <lab directory>/requirements.txt <lab directory>/Procfile .`
	8. Add all new files to your GitHub repo, and stage files for commit: `git add requirements.txt Procfile <lab directory>`
	9. Commit the files: `git commit -m "finished lab <n>"`
	10. Push the files: `git push`
	11. Publish your app to heroku: `git push heroku master`
		＋　Make sure the app works with just the lab code. 
		＋　If you get an error: ｀heroku logs --tail｀ and watch the logs as you use the app. If you get errors, address them. The most likely errors are:
			1. You forgot to activate your environment, so you’re publishing packages that cant be found or are too big
			2. There is a problem with file paths in your app. See the [Flask Application API Reference](https://flask.palletsprojects.com/en/2.0.x/api/#application-object)
			3. You’re out of memory (if this happens, bring it up in OH, or slack the TFs right away to resolve)

## After class
	1. Now, do your homework.
	2. Repeat steps B1-B11 and submit your homework on canvas.
		+ Put the heroku url in the url box. (Looks like: https://beverly-hills-90210.herokuapp.com)
		+ Put the GitHub url in the comment box.(Looks like: https://github.com/Harvard-DCE-BIWADA/S14A2021)
		+ If you are submitting right before the deadline and did not finish, note what errors you were receiving that got you stuck.

## REMEMBER:
	+ Perform steps 1-10 before we start the labs on Monday & Wednesdays.
	+ **We don’t offer feedback or support on submission days**, so start early or follow along in class and you’ll already be at step B21.
	+ Use the public slack channel to find answers first, then ask questions there. The TFs monitor the public channels. You can also direct message your teammates to see if they’ve had your same issue.
	+ If you have an issue that you’ve solved, **tell everyone about it and what you did to fix the problem.** From experience if one person is having a problem, someone else is too!
