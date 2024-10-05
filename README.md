# **Planet Dynamics Software**

Planet Dynamics is an interactive educational software designed to teach high school students about **SDG 13 – Climate Action**. The platform offers a rich variety of interactive learning components, quizzes, data visualizations, and a blog feature to promote collaborative learning and environmental awareness.

## **Features**
- **Interactive Lessons**: Story-based lessons about climate change and its impact.
- **Quizzes**: Assess understanding with climate-related quizzes.
- **Audio Lessons**: Designed for blind and visually impaired users, offering an inclusive learning experience.
- **Interactive Earth Map**: Visualize climate conditions at various locations around the globe.
- **Graphical Statistics**: View animated graphs on climate data like CO₂ emissions, methane emissions, sea level rise, and ozone layer depletion over time.
- **Blog Feature**: Share and write blogs on climate action, allowing users to engage and share knowledge.

---

## **Installation and Setup Instructions**

### **Step 1: Install Required Dependencies**

Run the following command to install the necessary dependencies for the project:

```bash
pip install customtkinter tkinter pillow mysql-connector-python CTkMessagebox pygame tkintermapview pandas numpy requests tkinterweb matplotlib
```

### **Step 2: Configure the Database**

You need to update the database configuration in the `main.py` file before running the application.

1. Open the `main.py` file.
2. Modify the following lines to match your database server credentials:
   
   - **Line 29**: Replace `"localhost"` with your database server host name.
   - **Line 30**: Replace `"root"` with your database user name.
   - **Line 31**: Replace `"password"` with your database password.
   - **Line 32**: Ensure that the database name is set to `"planet_dynamics"`.
   - **Line 33**: Replace `4306` with your database port number if it's different.

```python
# Database Configuration (Modify these lines)
host = "localhost"  # Replace with your database server host name
user = "root"       # Replace with your database user name
password = "password"  # Replace with your database password
db = "planet_dynamics"  # Ensure the database name is planet_dynamics
port = 3306  # Replace with your database port number
```

### **Step 3: Set Up the Database**

1. Import the provided database schema by running the `database.sql` file in your MySQL server.
2. You can execute the SQL file using a tool like phpMyAdmin or by running the following command in your terminal:

```bash
mysql -u root -p planet_dynamics < database.sql
```

Make sure to replace `root` with your MySQL username and provide the appropriate password.

---

## **Running the Application**

Once you have installed the dependencies and configured the database, you can run the application by executing the `main.py` file.

```bash
python main.py
```

---

## **Technologies Used**
- **Python**: Backend and data processing.
- **CustomTkinter**: GUI framework for Python applications.
- **MySQL**: Database for storing user information and climate data.
- **Pygame**: Audio lesson support for visually impaired users.
- **Matplotlib**: For generating animated graphs and visualizations.
- **tkintermapview**: Provides the interactive earth map.
- **Requests & Pandas**: Used for processing and analyzing climate data from external sources.

---

## **Contributing**
Contributions are welcome! If you have ideas for improving the platform, feel free to fork this repository, make your changes, and submit a pull request.

---

## **License**
This project is licensed under the MIT License.

---

By following these steps, you should be able to successfully run and use the **Planet Dynamics Software** on your local machine. If you encounter any issues, feel free to create an issue in this repository. Enjoy learning about climate action and contributing to SDG 13!

---

