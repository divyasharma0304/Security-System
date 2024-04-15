**FSM Security System**

This project implements a finite state machine (FSM) in Python to simulate a basic security system with user authentication. The system utilizes the Tkinter library for building a graphical user interface (GUI) that interacts with the FSM logic.

**What is a Finite State Machine (FSM)?**

An FSM is a mathematical model that can be in a finite number of states at any given time. It transitions between these states based on specific inputs (events) and outputs (actions). FSMs are widely used to model and control systems in various domains, including security systems, vending machines, traffic lights, and more.

**Project Goals**

* Implement a security system FSM with at least 4 states and 4 transitions using Python.
* Develop a user-friendly GUI using Tkinter to interact with the FSM.
* Simulate user login scenarios with username and password verification.

**System Functionality**

* The user can set up a username and password through a dedicated window. This information is stored securely in a text file.
* The login window allows users to enter their credentials.
* The FSM validates the entered username and password based on the stored information.
* Upon successful login, the system displays a "Login Successful" message.
* In case of incorrect password attempts, the system offers options to try again or reset the username and password.
* When the user enters an invalid username, an error message ("User not found") is displayed.

**Project Components**

* **Python Code (fsm.py):** This file contains the core FSM logic using Python.
* **State Diagram:** A visual representation of the FSM states and transitions.
![image](https://github.com/divyasharma0304/Security-System/assets/108946390/5d7e6d39-a518-4d30-8852-2309b47065ef)
* **GUI:** The Tkinter GUI will be designed with the following windows:
    * **Main Window:** The starting point of the application.
      ![Main Window](https://github.com/divyasharma0304/Security-System/assets/108946390/91a80690-6947-45d9-aaad-bfca378e7f05)
    * **Set-Up Window:** For configuring username and password.
      ![Set-Up Window](https://github.com/divyasharma0304/Security-System/assets/108946390/de615b76-9065-4a68-ba42-7f9b4c09117e)
    * **Set-Up Success Window:** Confirms successful setup.
      ![Set-Up Success](https://github.com/divyasharma0304/Security-System/assets/108946390/9c890206-4848-437e-8bd6-415d0245b008)
    * **Login Window:** For entering login credentials.
      ![Login Window](https://github.com/divyasharma0304/Security-System/assets/108946390/d090c91a-5c16-45c4-bb27-9fdf33f8b0a3)
    * **Login Successful Window:** Displayed upon successful login.
      ![Login Successfull Window](https://github.com/divyasharma0304/Security-System/assets/108946390/3ac67eaf-ea72-41b9-b2ef-7dfc7e155c13)
    * **Login Failure Window:** Appears after incorrect password attempts.
      ![Login Failure Window](https://github.com/divyasharma0304/Security-System/assets/108946390/48da97c2-6a7e-4dbd-8707-833139a59619)
    * **User Not Found Window:** Message displayed for invalid username.
      ![image](https://github.com/divyasharma0304/Security-System/assets/108946390/5ef59d80-2866-4c2a-91f8-bd74867ee0fb)


**Instructions**

1. Clone or download the project repository.
2. Install the required libraries: `pip install python-tkinter`
3. Navigate to the project directory in your terminal.
4. Run the program using `python fsm.py`.
5. Interact with the GUI to experience the security system simulation.

**Further Enhancements (Optional)**

* Implement additional security measures like password strength checks or lockout after multiple failed attempts.
* Integrate database storage for user credentials instead of a plain text file.
* Expand the system functionality beyond basic login, such as granting access to secured resources or managing multiple users.

**Note:**

This project provides a foundational understanding of FSMs in a security system context. It can be further customized and extended based on your specific requirements.
