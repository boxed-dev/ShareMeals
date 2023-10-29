# ShareMeals Web Application (Group Project)

## Description
ShareMeals is a web application that connects donors and non-governmental organizations (NGOs) to facilitate the sharing of meals. Donors can offer surplus food to NGOs, and NGOs can request food donations. This application is built using Flask, MySQL, and Jinja2.

## Prerequisites
Before running this application, make sure you have the following prerequisites:

- Python
- Flask
- MySQL database

## Installation

1. Clone the repository or download the application to your local machine.

2. Install the required Python libraries:

   ```bash
   pip install Flask flask-mysqldb
   ```

3. Set up the MySQL database:

   - Create a MySQL database named `sharemeals`.
   - Update the `app.config['MYSQL_*']` variables in the script with your MySQL database credentials.

4. Create the necessary tables:

   - You can create the required database tables using a MySQL client or a script. A sample database structure is provided for reference.

## Usage

1. Run the application using Python:

   ```bash
   python your_app_name.py
   ```

   Replace `your_app_name.py` with the actual name of your Python script.

2. Access the application in your web browser at `http://localhost:5000`.

## Functionality

### Donor Features

- **Sign Up as a Donor:**
  - Donors can sign up with a username, email, password, contact information, and address.
  - Donor information is stored in the database.

- **Log In as a Donor:**
  - Donors can log in using their username and password.
  - Authentication is performed against the stored database entries.

- **View NGOs Requesting Donations:**
  - Donors can see a list of NGOs requesting food donations.

### NGO Features

- **Sign Up as an NGO:**
  - NGOs can sign up with a name, email, password, contact information, an about section, and a tagline.
  - NGO information is stored in the database.

- **Log In as an NGO:**
  - NGOs can log in using their username and password.
  - Authentication is performed against the stored database entries.

- **Request Donations:**
  - NGOs can request donations by setting their request status to "yes" in the database.

- **View Donor List:**
  - NGOs can see a list of donors who have signed up for meal donations.

### Common Features

- **Home Page:**
  - A landing page where users can find information about the application.

- **Donation Lists:**
  - Users can view lists of donors (for NGOs) and NGOs (for donors).

## Customize and Enhance

This application is a basic example and can be extended and customized to meet specific requirements. You can:

- Enhance the user interface with HTML and CSS.
- Implement more robust error handling and validation.
- Add more features like user profiles, user-specific dashboards, and user messaging.
- Secure your application by implementing user authentication and authorization.
- Deploy the application to a production server for real-world use.

## Disclaimer

This application is a starting point for building a meal-sharing platform. It should be further developed, tested, and secured before being used in a production environment. Be mindful of security and privacy concerns.

Feel free to contribute to this project and make it even better!

---

🍽️ For questions and support, please contact me: [Your Contact Information]

🔗 Feel free to contribute to this project and make it even better!
