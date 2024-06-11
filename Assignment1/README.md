# Setup
**First, accept the Assignment Invitation on BB**, then download (clone) Assignment 1 locally, which will allow you to work on your scripts and upload (push) them back up to GitHub.

1. Clone your assignment repository into your ~/ops445/a1 directory using SSH:
```bash
git clone git@github.com:OPS445A-F22/assignment1-yourgithubusername.git ~/ops445/a1/
```

# Submission
1. Run the testing script. You can use this script to run the tests as stated in the Assignment 1 wiki page.  
The total marks for the 12 test run is 30 points.  
Please note that this test run script does not check your script docstring or your function docstring.  
```bash
cd ~/ops445/a1/
pwd #confirm that you are in the right directory
python3 ./CheckA1.py
```

2. Paste the testing script output into *a1_output.txt*:
```bash
vi ~/ops445/a1/a1_output.txt
```

3. Commit and push (upload) your assignment work:
```bash
git add assign1.py
git commit -m "Individual message or note."
git push
```
4. Once you have pushed to Github, you must also submit your *a1_youruserid.py* to Blackboard. 

You can make changes to your scripts and reupload as many times as you like. Make sure you commit+push to do so.

**Note:** Your assignment is automatically submitted at the due date and time using the last published code. Any changes you publish after the due date won't be marked or seen by your professor.

