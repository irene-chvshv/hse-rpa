# HSE. RPA seminar

**Date**: 11.10.2021
**Recording**: *will be soon*

## ResearchGate robot description

The robot is used to automate the process of ResearchGate literature collection for the user-defined topic. Result of the process is an email with attached excel with info about each found article.


#### Used libraries

* [selenium](https://selenium-python.readthedocs.io/) - web-browser automation
* [pandas](https://pandas.pydata.org/) - work with datatables
* [smtplib](https://docs.python.org/3/library/smtplib.html) \ [email](https://docs.python.org/3/library/email.examples.html) - email creating and sending
* wcm - function for working with Windows credential manager

#### Algorithm 

1. User define a topic, page quantity, and email for the result email
2. Robot creates links for each query page
3. Robot collects links to the article from each page
4. Robot scraps article's info and download source docs if available
5. Robot writes all info to excel and send email


#### How to use

1. Clone git repository to your computer
2. Create a virtual environment (optional)
3. Install packages from ```requirements.txt```
4. Make setup correcting ```conf.py``` file
5. Run script ```articles_search.py```

## Homework

### Obligatory

Write the robot with the same logic for https://www.semanticscholar.org/ website.

Robot functionality:
* Search by specific topic on the X page
* Get title, author, source, description, citations count, article file (if available)
Note, that you need to pick the topic with at least 1 article's docs available.

The final git repo \ .zip archive should contains the following files:
* readme.md with robot description
* requiremnts.txt
* link to the video of robot work (feel free to use [loom](https://www.loom.com/) for recording)
* robot's python script
* example of result email

The link to the github repo \ .zip archive should be send by email to [dmitry.fedorov@mazars.ru](mailto:Dmitry.Fedorov@mazars.ru) with [iurii.piunov@mazars.ru](mailto:iurii.piunov@mazars.ru) in CC.
Topic must be: *"HSE_RPA_{Surname} {Name}"*

### Additionaly

**Goal**: seect the master thesis topic with the most resources available 

1. Take multiple master thesis topics from hand-written paper \ pdf without text recognition using OCR (topics are not English)
2. Translate topics to English
3. Collect resources for each topic
5. Select topic with most vied resources
5. Pack all docs related to the selected topic to the .zip archive and send it by email


Email for questions: [dmitry.fedorov@mazars.ru](mailto:Dmitry.Fedorov@mazars.ru)