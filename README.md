<h2>TechNote with Django and API with Django Rest Framework</h2>

<p>Tech Notes is an Web application, that lets user to take notes. User can take notes,
add them, edit them delete them, search them and even can share them with other users for view only, that is
user can share their notes to other user to view.</p>

<h3>Requirements</h3>
<ul>
    <li>Python 3.5 or above</li>
    <li>Django 3.1.5</li>
    <li>Django Rest Framework</li>
</ul>

<h3>Install Dependencies</h3>

<p>Create a virtual environment using pip/pip3 before installing dependencies </p>

<code>pip3 install virtualenv</code><br>
<code>virtualenv venv</code><br>

<p>Activate the virtual environment 'venv'</p>

<code>source venv/bin/activate</code>

<p>Install all dependency from <code>requirements</code> folder</p>

<code>pip install -r requirements.txt</code>

<h3>Database Setup</h3>
You can use any database you want, but in this project SQLite has been used. You can use mysql if you uncomment the database section in <code>settings.py</code>
<p>Once a database is created and connected, migrate the models</p>

<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code>

<p>Create and configure the <code>.env</code> file.
Put all essential configuration in this file, like SECRET_KEY, Database credentials, Allowed hosts, etc.
</p>
<p>
Now, run the project with </p>

<code>python manage.py runserver</code>

<p>Create a superuser to get access to admin</p>

<code>python manage.py createsuperuser</code>

<p>Check the urls.py inside 'technotes' folder and navigate to the urls to view the API outputs.</p>

<h3>Project Description</h3>
<h5>Feature list</h5>
<ul>
<li>User can create account</li>
<li>User can login</li>
<li>User can create note</li>
<li>User can update note</li>
<li>User can view note</li>
<li>User can see note list</li>
<li>User can share note with other user</li>
<li>User can see the note list that has been shared with that user</li>
</ul>
<p>All the feature list item available in both API and Web section</p>
<p>User can share their note from note view page in web section</p>
