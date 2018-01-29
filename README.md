# README #
#Logs Analysis Project
An internal reporting tool that uses information of large database from a newspaper website and draw business conclusions from this information.
### Project as requirement to complete Udacity full stack developer course.

> Lawrence Nara

## About the project

This is a python class that uses information of large database from a newspaper website and draw business conclusions from the information. The database contains newspaper articles and web server log for the site. The log has a database row for each time a reader loaded a web page. The database contains three tables:
* The **authors** table includes information about the authors of articles.
* The **articles** table includes the articles themselves.
* The **log** table includes one entry for each time a user has accessed the site.

#### The project tries to report:
* Most popular three articles of all time.
* Most popular article authors of all time.
* Days on which more than 1% of requests lead to errors.

## Installation

### To install, you'll need:
- Python2
- Vagrant
- VirtualBox

### How to install
1. Install Vagrant And VirtualBox
2. Clone this repository

### Setup database

Launch Vagrant VM by running `vagrant up`, you can then log in with `vagrant ssh` for linux and `winpty vagrant ssh` for windows

* <h4>Download the <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">data</a></h4>
You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To load the data into your database, use the command `psql -d news -f newsdata.sql`

### To execute the program
 run `python log_analysis.py` from the command line.
 
### The expected output
![project_results.jpg](https://github.com/nara-l/log_analysis_udacity_project/blob/master/project_results.PNG)

## Issues

  For any errors or other issues please contact me for update at lawrence.naraAtgmail.com
