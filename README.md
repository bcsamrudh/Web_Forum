# Web_Forum

Note: This is still a work in progress.

This is a web application built with Flask, SQLAlchemy, Bootstrap, CSS, and SQLite that allows users to post articles, get weather and news updates, create profiles, enable user authentication, and comment on posts.

## Getting Started

To get started with this project, you'll need to have Python 3 and pip installed on your machine.

1. Clone this repository to your local machine:

```
git clone https://github.com/[your-username]/blog-project.git
```

2. Create a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Create a database and migrate the database schema:

```
flask db init
flask db migrate
flask db upgrade
```

5. Start the development server:

```
flask run
```

The project will now be running on http://localhost:5000.

## Features

- Users can sign up and log in to their accounts.
- Users can create, edit, and delete their own blog posts.
- Users can view weather updates for their location.
- Users can view news updates from various sources.
- Users can comment on blog posts.
- Users can view the profiles of other users.

## Technologies Used

- Flask: A Python web application framework used for building the server-side API.
- SQLAlchemy: A Python library used for working with relational databases.
- Bootstrap: A CSS framework used for styling the user interface.
- CSS: A styling language used for creating the user interface.
- SQLite: A lightweight relational database used for storing user data and blog posts.
- werkzeug.security: A library used for hashing passwords for secure authentication.
- Flask_login: A library used for managing user sessions and authentication.
- Flask_wtf: A library used for creating and validating web forms.
- Requests: A library used for making HTTP requests to the weather and news APIs.

## Contributing

If you would like to contribute to the project, please fork the repository and make your changes in a separate branch. Once you are finished, please submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
