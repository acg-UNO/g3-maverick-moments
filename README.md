# g3-maverick-moments
Group project for event management company

# Setting up your environment (for group members)
### 1. Remember to create your own virtual environment with Python 3.11
### 2. ALWAYS ACTIVATE YOUR VIRTUAL ENVIRONMENT BEFORE DOING ANYTHING   (something like: venvFolderName\Scripts\activate )
### 3. Then run "pip install -r requirements.txt" 
make sure that requirements.txt is in your current directory
this installs the packages needed for the application and is specific to your computer's virtual environment. 
### 4. Add the name of your venv folder to the .gitignore so that it doesn't get pushed! (cuz everyones is different)
mine is named 'env' and the default name 'venv' is already in the .gitignore
### 5. Run migrations real quick
    python manage.py makemigrations
    python manage.py migrate
### 6. Add any new packages to your environment
    pip install -r requirements.txt
Now you're good to go

Run server:
    python manage.py runserver