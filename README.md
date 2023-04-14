# Blog 180

Blog 180 is a simple blogging application built with Django. Users can create, edit, and delete posts. Non-users can view the posts but cannot interact with them. Users can only edit and delete their own posts. The application is deployed at [lucassantossa.pythonanywhere.com](http://lucassantossa.pythonanywhere.com/).

## Features

- User authentication (login, logout, and sign up)
- Create, edit, and delete posts
- Restrict post interaction to authenticated users
- Display the author of each post
- Tailwind CSS integration for quick styling

## Installation and Setup

To run the project locally, follow these steps:

1. Clone the repository to your local machine:

git clone https://github.com/lucasSantosSa/blog180.git


2. Change into the project directory:

cd blog180


3. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate # For Linux and macOS
venv\Scripts\activate # For Windows


4. Install the required packages:

pip install -r requirements.txt


5. Run the database migrations:

python manage.py migrate


6. Start the development server:

python manage.py runserver


7. Visit `http://127.0.0.1:8000/` in your web browser to see the application running.

## Deployment

The application is deployed on PythonAnywhere. For instructions on how to deploy your own version of the application, please refer to the [PythonAnywhere documentation](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/).

## Author

Lucas Santos - [GitHub](https://github.com/lucasSantosSa)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
