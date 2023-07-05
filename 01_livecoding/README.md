Mini Project - Build and Deploy Your Streamlit App
========================

You'll be working with the [MPG dataset](https://ggplot2.tidyverse.org/reference/mpg.html) that contains the subset of the fuel economy data. 

Let's create a Streamlit app which runs locally on your computer and explore how you can get it into the cloud.
If you don't have your own app ready, you can download this [template streamlit app](app.py) and the dataset [mpg.csv](https://drive.google.com/file/d/1w_udatZPqdyrIdtM1FBZgbMt0VouiqPz/view?usp=sharing) and try out the deployment with these files.

Streamlit Cloud will fetch all the files required for the app deployment from Github, so first of all, we need to ensure that everything is available in a public repo.
The instructions below are adapted from the official [Streamlit documentation](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app).

## 1) Set up your Github repo ##


**Note**: This first part is only relevant, if you haven't created a Github repo for this mini project yet.

- If you do not have a git folder set up yet, create a new directory and save your app script (``app.py``) and the data file(s) in this folder. ``cd`` into it and initialize a git folder:

```bash
    mkdir my-first-streamlitapp
    cd my-first-streamlitapp
    git init
```

- If you haven't already done so, create a public Github repo for your app (suggested name: my-first-streamlitapp). Connect this repo to your local git folder and push the files to Github.

```bash
    git add app.py mpg.csv
    git commit -m "first commit"
    git remote add origin git@github.com:<user_name>/<repo_name>.git
    git push
```

## 2) Create and test the requirements file ##

- Use a text editor to create a file named `requirements.txt`, which will contain information on all the packages required to run your project. For example, if you're using the template streamlit app, write the lines below in it and save it in your git folder.

```bash
    streamlit~=1.24.0
    numpy~=1.25.0
    pandas~=2.0.3
    plotly~=5.15.0
    seaborn~=0.11.2
    matplotlib~=3.7.1
```

- Test if your app runs in a new environment, with only the packages listed in your requirements file: Create a new conda environment, activate it and type the following lines (though you may need to change the path to your app.py file). This will first install your required packages in the new environment and then check if everything is working properly.

```
    conda create --name app_test python">=3.9"
    conda activate app_test
    conda install pip
    pip install -r requirements.txt
    streamlit run app.py
```

- Once everything works fine, commit and push the new/modified files to Github.

**Note**: If you're working with a `.gitignore` file, make sure that the data files required for your app also get pushed to Github.
The app will not run without them. (Github currently has a file size limit of 2 GB for free accounts.)


## 3) Deploy the app to the Streamlit Cloud ##


- Log in to Streamlit with your Github account [here](https://share.streamlit.io/).

- Click on the button ``New app`` and enter the repository name, branch and main file path (to your app.py file).

- Go to ``Advanced settings...`` and choose the Python version that you need for your app.

- Click ``Deploy!`` and watch your app launch. It is now hosted in the cloud so you can share the assigned streamlit link with others.


## 4) Optional: Showcase your app ##


- Brush up the Github repo to make it more attractive and understandable: Adapt the README file to explain your work, add a screenshot of your app, etc.

- Get acquainted with the vibrant online data visualization community by posting about your app. Include a screenshot of your app and a link to your Github repo. Feel free to tag [COLearning](https://www.linkedin.com/school/constructor-learning/), [@Women++](https://www.linkedin.com/company/womenplusplus/), [Hack&Lead](https://www.linkedin.com/company/hackandlead/) and [@streamlit](https://twitter.com/streamlit?lang=en).
