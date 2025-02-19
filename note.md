CS 163 Data Science Senior Project
San Jose State University

# Before Class
1. Create a Python environment (Use Python 3.10.x)
2. Install pandas and [dash](https://dash.plotly.com/installation)
3. Redeem the Google cloud coupon (check the Canvas page) and activate your Google cloud account
4. Install [the gcloud CLI](https://cloud.google.com/sdk/docs/install) on your machine (You can follow the instructions till STEP 5. You do NOT need to do STEP 6 with ```gcloud init```. Just make sure that ```gcloud --help``` gives you the help page to check the installation.)
<!--
1. Create an account (free) on [PythonAnywhere](https://www.pythonanywhere.com/) Note: Your account name will be revealed to the public as a part of a URL when you host a website. Please carefully choose the user name so it will be appropriate as a part of your public data science portfolio.
-->

---

# 1. HTML basics
- [reference](https://dash.plotly.com/dash-html-components)
- Check ```app2.py```
- What is HTML?
- How do they work?
- Web server, IP address, and port number
- HTML and style

# 2. Adding Data
- [reference](https://dash.plotly.com/datatable)
- Check ```app3.py```
- Data location: https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv
- ```'records'``` option specifies the format of the conversion


# 3. Visualizing Data
- [reference](https://dash.plotly.com/dash-core-components/graph) (Check other components too!)
- Check ```app3.py```
- [Histogram details](https://plotly.com/python/histograms/?_gl=1*1kv743e*_gcl_au*MTkwMDUxMzMyLjE3MjExNTkxMzI.*_ga*MTAzNzExMjIzMi4xNzIxMTU5MTMy*_ga_6G7EE0JNSC*MTcyMTE1OTEzMS4xLjEuMTcyMTE2Mzk3Mi4zMy4wLjA.)
- [Other charts](https://plotly.com/python/?_gl=1*vegk6e*_gcl_au*MTkwMDUxMzMyLjE3MjExNTkxMzI.*_ga*MTAzNzExMjIzMi4xNzIxMTU5MTMy*_ga_6G7EE0JNSC*MTcyMTE1OTEzMS4xLjEuMTcyMTE2MzUwNi41OC4wLjA.)

# 4. Interactive Website
- Check ```app4.py```
- ```@callback```: By writing this decorator, we're telling Dash to call this function for us whenever the value of the "input" component (the text box) changes in order to update the children of the "output" component on the page (the HTML div).
- Your callbacks should never modify variables outside of their scope.
- ```component_id``` will be used by the callback to identify the components.

# Class 1 - Tasks
- Import another dataset (of your choice)
- Try adding more features to a histogram
- Also, try two other types of plots (Check the examples on the "other charts" link)

---
<!--
# 5. Hosting a Dash app on a Public Web Server
- Push your app to your cs163 repo (or you can use ```src_sample```)
- Open a bash console
  - Install pandas and dash
  - (Or you can use venv)
- Clone your cs163 repo to your home dir (Remember the location of your source file.)
- Create a web app (You need to manually configure the settings.)
  - Select Python 3.10
  - Edit ```WSGI configuration file``` based on the example under ```cs163/src_example```
- Click the "Reload xxx.pythonanywhere.com" button
- Go to your webpage (xxx.pythonanywhere.com)
-->

# 5. Preparing Google App Engine
- What is Google App Engine?
1. Create a new project 
2. ```gcloud projects list``` should return a list of projects
3. ```gcloud billing accounts list``` gives you a list of billing accounts
4. Connect a billing account to your project ```gcloud billing projects link <your project name> --billing-account <XXXXXX-XXXXXX-XXXXXX>``` ([reference](https://cloud.google.com/sdk/gcloud/reference/billing))
5. (On Google Cloud Console,) Enable the App Engine Admin API ([See the Before you begin section](https://cloud.google.com/build/docs/deploying-builds/deploy-appengine))
6. Initialize the CLI ```gcloud init``` and select the project.

# 6. Preparing an Dash app for Google App Engine
1. Create a git-managed directory
2. Put a sample Dash app (app4.py) into the directory
3. The app code should have: ```server = app.server```
    - ```app.server``` refers to the underlying Flask server instance that Dash uses to run the application
    - Many WSGI servers (e.g., Gunicorn) with which we use to deploy the app expect a server object 
    - Command example: ```gunicorn my_dash_app:server```([reference](https://docs.gunicorn.org/en/stable/run.html#commands))

# 7. Python 3 Runtime Environment in App Engine
- [reference](https://cloud.google.com/appengine/docs/standard/python3/runtime)
- The Python runtime for App Engine in the standard environment is declared in [the ```app.yaml``` file](https://cloud.google.com/appengine/docs/standard/python3/configuring-your-app-with-app-yaml)
  - ```runtime: python310```
- The runtime starts your app by running the command you specify in the entrypoint field in your ```app.yaml``` file.
  - ```entrypoint: gunicorn -b :$PORT main:app```
- App Engine provides default values for all other settings, including the F1 instance class, which determines the memory and CPU resources that are available to your app, and automatic scaling, which controls how and when new instances of your app are created.
  - [app.yaml file reference](https://cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=python)
  - [scaling elements](https://cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=python#scaling_elements)
- During deployment, App Engine uses the Python package manager ```pip``` to install dependencies defined in the ```requirements.txt``` metadata file located in your project's root directory.
  - If you have configured a Gunicorn web server entrypoint in the ```app.yaml``` file, you must also add ```gunicorn``` to your ```requirements.txt``` file.
- When you have all three files (```app4.py```, ```app.yaml```, and ```requirements.txt```), you can deploy the website on Google App Engine
  - ```gcloud app deploy``` on the repository root
- If you want to disable the app, check [this reference](https://cloud.google.com/appengine/docs/standard/python3/building-app/cleaning-up)

# Reference
- [Deploying Dash Apps](https://dash.plotly.com/deployment)
- [My slides on web hosting](https://docs.google.com/presentation/d/1B5WKCexRrfNJI83NlAdh-dnm7kZdMGQkv6sla4aeTec/edit?usp=sharing)

# Note: Google Cloud Free Program
- [App Engine Free Tier](https://cloud.google.com/free/docs/free-cloud-features#app-engine)
  - If we only use one F1 instance, it will be in the free tier (max_instances)
  - The instance needs to be the standard environment

# Note: More Discussions on App Engine
- ```gcloud app``` commands
  - [reference](https://cloud.google.com/sdk/gcloud/reference/app)
- On web console, App Engine > Dashboard > Versions (Split traffic)
  - Or ```gcloud app versions list```

# 8. Multi-Page App
- [reference](https://dash.plotly.com/urls)
- Check ```app5-multi```
- path: We call ```dash.register_page``` on each children page in our app. When we call ```dash.register_page``` for ```home.py```, we do set the path property. For ```home.py``` we set the path property because we don't want the content to be displayed when the user goes to ```/home```, but when the user goes to the homepage: ```/```.
- ```page_registry```: Pages that include a call to ```dash.register_page``` are added to the page registry for our app. This is an OrderedDict that we can extract information from about our app's pages. 
- ```page_container``` is where page content is displayed when a user navigates to that page's path.
- Note: In Python, ```__name__``` is a built-in variable which evaluates to the name of the current module.

# 9. More Interactions with Graphs
- Check ```app6.py```
- The ```dcc.Graph``` component has four attributes that can change through user-interaction: ```hoverData```, ```clickData```, ```selectedData```, and ```relayoutData```.
- These properties update when you hover over points, click on points, or select regions of points in a graph.

# 10. Sharing Data Between Callbacks
- [reference](https://dash.plotly.com/sharing-data-between-callbacks)
- In some apps, you may have multiple callbacks that depend on expensive data processing tasks like making database queries, running simulations, or downloading data.
- Rather than have each callback run the same expensive task, you can have one callback run the task and then share the results to the other callbacks.
- There are three places you can store this data:
    - In the user's browser session, using ```dcc.Store```
    - On the disk (e.g. in a file or database)
    - In server-side memory (RAM) shared across processes and servers such as a Redis database. Dash Enterprise includes onboard, one-click Redis databases for this purpose.
  - Check the ```dcc.Store``` example in the reference
  - ```dcc.Store``` can be used to store the processed data as an intermediate value that can then be used as an input in multiple callbacks to generate different outputs


# Class 2 - Tasks
- Understand more about callbacks. Look at the callback with multiple inputs and chained callbacks in this [reference](https://dash.plotly.com/basic-callbacks). Run some examples and/or modify your app.
- Check the "Update Graphs on Hover" section in this [reference](https://dash.plotly.com/interactive-graphing). This functionality can provide very informative and rich experience to show more details of the datasets. Try this example. Modify it for your application.

---

# 11. Additional Topics on Design
- [dash_bootstrap_templates](https://pypi.org/project/dash-bootstrap-templates/)
- [dash_bootstrap_components](https://dash-bootstrap-components.opensource.faculty.ai/)
- check ```app7.py``` for the style template
- check ```app8.py``` for the layout setup

# Class 3 - Tasks
- Create a multi page app template for your final project
- Apply some designs (basic styles, external css)
- Plot a few diagrams to show the basic properties of your datasets