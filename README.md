# Automated Emails
Big organizations receive countless applications, and answering to each of them is very time consuming. I built an automated email sending program using Python. You input a contact list with motives for writing, and email templates and it sends a personally tailored email to the contact list.

## How To Use

### Candidate List
The candidateList.txt file offers a CSV (comma separated value) template that can be used for writing down the contact list. You can change this to whatever meets your needs, but it at least needs an email address and a keyword to tell which email template to use. Right now, **update** is the field in which you specify what template  -*or reason to send the email*- the program is going to use for each individual.

**Remember to NOT leave a space after the comma!**

### Templates
While browsing the current templates that were written for Google's STEP Internship you can notice that variables that are to be personalized to each candidate. You can build your own templates as long as you follow these three steps:

1. The header must always be in the following format:
```
From: From <{sender}>
To: To <{receiver}>
Subject: (Write wichever subject is most useful for your particular purpose)
```
2. Make sure that the candidateList.txt has a field for every variable you need to use for your template.
3. Make sure to insert a line of code that reads the variable from candidateList.txt. There is a comment to show you where this line should go! Don't worry if you don't know how to code, just follow the template: variable_name = row["variable_name"]

**Feel free to contact me with any question**
