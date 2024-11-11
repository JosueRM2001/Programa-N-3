# Presentation
This is a project that was developed with Python.

## Description
This project shows a welcome page with a message and a button that will change the color of the page.

It is a simple program to show how a program developed in the Python programming language works.

## Project Structure
*Contains the Following*
- Origin.py: File in charge of page structure and style.
- Dockerfile: Configuration of the Docker image.

## Development Requirements
- *Docker Desktop* (if you want to run it in a container)
- *Visual Studio Code* (optional, but recommended)
- *The Python extension for Visual Studio Code* (to improve support and syntax highlighting).
- *GitHub Desktop* (if you want to clone and use the project)

## Docker Hub
## Steps to generate the image and container for Docker Hub
- *Step #1*

Open the cmd terminal on your computer (you must have Docker Desktop installed).

- *Step #2*

Run the following command, which will generate the image:

docker pull erickjrm/programpython:latest

- *Step #3*

Then run the following command, which generates the container and the port.

docker run -d -p 5000:5000 --name python erickjrm/programpython:latest

- *Step #4*

Open the Docker Desktop to see if the image is created correctly and send it to run to view.

## Program-N-3 Project
## Steps to run the project locally on your computer
- *Step #1*

Clone the project repository on your machine with the following link (you must have GitHub Desktop installed):

https://github.com/JosueRM2001/Programa-N-3.git

- *Step #2*

Open the project with Visual Estudio Code (you must have VisualEstudio Code installed, if possible the most recent version).

- *Step #3*
- Open the visual studio code terminal and run the following command:
  
  pip install flask


- *Step #4*

Install the following extensions in Visual Estudio Code:

- Python
- Docker

*With this you will be able to run the project without problems locally*.
