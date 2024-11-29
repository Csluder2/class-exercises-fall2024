# Lab 5: Package Management Tutorial
Please complete the hands-on activities associated with this lab outlined in the <a href="https://csci338.github.io/fall2024/assignments/lab05" target="_blank">Lab 5 Instructions</a> (on the course website). When you're done, answer the following questions. Feel free to use Google / ChatGPT to help you think about these questions (but keep in mind that you'll need to know them for the midterm exam).

## Part 1. Operating System Package Managers
Answer the questions for either Homebrew or apt (depending on whether you're using Linux / WSL or Windows)
1. What is Homebrew / apt, and why is it useful?
In my case I use apt, and it is useful to mantain and install software. Specifically necessary dependencies for certain projects like this assignment. 
2. What does the `update` command do (either `brew update` or `apt-get update`)?
for apt-get update, it gets package information from repositories, allowing it to know about potentially newer versions of packages. 

3. Where are the packages that are managed by Homebrew / apt stored on your local computer?
/var/cache/apt/archives/

## Part 2.
1. What is a python virtual environment?
An isolated space where you can work on python projects/assignments, completely separate from your system installed python (which allows you to set up dependencies or libraries without affecting it).

2. What is Poetry, and how is it different from other Python package managers like pip?
Poetry is a dependency manager for Python projects that handles dependencies and packaging. Its more integrated and user-friendly than something like pip, it automatically handles situations like a lock file for instance that pip doesn't. 
3. What happened when you issued the `poetry new poetry-demo` command?
It creates a new directory called poetry-demo, creates a pyproject.toml file, a subdirectory of the same name, an empty __init__.py file, and a tests directory. 

4. How do you run a python file using the poetry virtual environment?
With the following command: poetry run python name_of_file.py

5. What is the purpose of the `poetry.lock` file?
The purpose of the poetry.lock file is to lock dependencies
specific versions required for projects. It makes it easier to reproduce the same results, as well as makes it easier install packages. 

## Part 3.
1. What are some of the things that `package.json` is used for?
It is used for documentation as well as managing packaging. It lists all dependencies required for a project to run, as well as letting you use the NPM command to install and manage said dependencies. 

2. Why wouldn't you want to check in the `node_modules` directory into GitHub?
The size of it can lead to many issues with mismanagement between platforms. Using a package.json is just more effecient and easier to handle. 

