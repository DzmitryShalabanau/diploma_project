# QA automation
## Final Diploma Project
### User interface automation tests for www.5element.by with Pyton and Selenium

This is final project on TeachMeSkills QA automation on Python courses for getting
diploma.This project contains UI tests of login, personal cabinet, catalog, cart, comparison page, footer and header
elements. Project can be run with two browsers Chrome and Edge. The design pattern of
this project is Page Object Model. 
and contains the following:

* data with urls and personal users and shop information
* folder with drivers for chrome and edge
* elements (Header and Footer)
* helpers with base methods for pages
* locators of elements for pages
* methods for pages
* tests of single pages
* README file with information about the project
* Makefile for running tests
* folders for allure report results
* Conftest - file with project settings
(pytest fixtures for driver and single tests )

To launch the project do the following  
1. Clone the repository to your computer:
git clone https://github.com/DzmitryShalabanau/final_diploma_project
2. Install the dependencies specified in the requirements.txt file
using the pip install -r requirements.txt command.
3. Set up environment variables to access www.5element.by
4. Run the Makefile using the commands in it    
5. Start allure - allure serve allure_results_chrome or edge

#### Summarizing General information on the project

* PEP8 recommendations are followed for coding style, naming variables, functions 
and files. The structure of project provides easy work and navigation.
* Git version control system is used. All changes pushed in a separate branch and
then merged into master branch. The history of changes and commits is available in the project repository.
* UI tests cover main functionality of www.5element.by website.
* Allure report in project provides easy tracking of test results and helps to analyze errors during operations.
* The project provides a Dockerfile for easy installation and running of the project in a Docker container. This allows you to create isolated and portable environments for developing and testing your project.


Author:<br>
Dzmitry Shalabanau, automation QA on Python engineer.

Contacts:<br>
email: bettertogo@gmail.com





 