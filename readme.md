# HSE. RPA seminar
***
**Date**: 17.10.2021
**Recording**: https://www.loom.com/share/35cbae77e41c422580058f80f87ec6d7
***
The main goal of the robot is to get the information about the articles on the theme "Secure distributed training" from the https://www.semanticscholar.org/
### The robot functions
* #### Search articles by specific topic on N pages
* #### Get title, author, source, description, number of citations, article file (if available)  
* #### Send an e-mail with report and article files

### The */conf.py* is used to configure robot
* #### query - The theme of the articles to search
* #### num_page - The number of pages
* #### receiver - The email of the receiver
* #### login - The email of the sender ( Is empty in repository for security reasons )
* #### password - The password of the sender ( Is empty in repository for security reasons )

### The */main.py* is the main file of robot, which is used to run it
