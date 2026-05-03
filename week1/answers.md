# ROS2 Basic Concepts Answers

## 1. Definitions

- **Node:** A node is a single executable program in ROS2 that performs a specific task such as publishing data, subscribing to data, or processing information.

- **Topic:** A topic is a named communication channel used by nodes to send and receive messages asynchronously.

- **Package:** A package is an organized folder containing ROS2 code, configuration files, and dependencies needed to run a specific application.

- **Workspace:** A workspace is a directory where multiple ROS2 packages are developed, built, and managed together.

---

## 2. Why Sourcing is Required

Sourcing a workspace updates the terminal environment so ROS2 can locate the packages, executables, and dependencies inside that workspace.  
If you do **not source the workspace**, ROS2 will not recognize your newly built packages, and commands like `ros2 run` will fail to find them.

---

## 3. Purpose of `colcon build`

`colcon build` is used to compile and build all ROS2 packages inside a workspace.

After building, it generates the following folders:

- **build/** – Contains temporary build files used during compilation.
- **install/** – Contains the installed packages and executables used when running ROS2 programs.
- **log/** – Stores logs generated during the build process.

---

## 4. Purpose of `entry_points` Console Script in `setup.py`

The `entry_points` console script in `setup.py` creates command-line executables that allow users to run ROS2 nodes easily using commands like `ros2 run`.  
It maps a command name to the Python function that should be executed when that command is called.

---

## 5. Publisher–Subscriber Diagram
    +------------------+
    |   Publisher Node |
    |  (sends data)    |
    +--------+---------+
             |
             |   Topic: /example_topic
             v
    +--------+---------+
    |  Subscriber Node |
    |  (receives data) |
    +------------------+

Explanation:
- The **publisher node** sends messages to a **topic**.
- The **subscriber node** listens to the same topic and receives the messages.
