# Lab 3 Answers

## Part 1: Git

### 1.1. List the contents of the lab03-exercises repo immediately after initialization
```
# paste code here
drwxrwxrwx 1 root root 4096 Sep  5 10:58 .
drwxrwxrwx 1 root root 4096 Sep  5 10:36 ..
drwxrwxrwx 1 root root 4096 Sep  5 10:58 .git
-rwxrwxrwx 1 root root   27 Sep  5 10:40 README.md

```

### 1.2. Paste the output of your `git status` command
```
# paste code here
git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)

```

### 1.3. Paste the output of the state of your repository after committing your README.md file
```
# paste code here
git status
On branch main
nothing to commit, working tree clean

```

### 1.4. Copy your `git log` output
```
# paste code here
git log 
commit fc6356579ed42b06e5c8d2b6b626773ce8896722 (HEAD -> main)
Author: root <root@ChristiansCPU>
Date:   Thu Sep 5 11:31:53 2024 -0400

    add README.md to the repository

```

### 1.5. Copy your `git diff` output
```
# paste code here
diff --git a/README.md b/README.md
index 9a8d849..cff67cd 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,3 @@
-# Hello, this is my header!
\ No newline at end of file
+# Hello, this is my header!
+# Find All Duplicates
+# Write a function (or static method in the case of Java) that accepts a list of integers and returns a list of only those integers that appear more than once.
\ No newline at end of file

```


### 1.6. Reflection

We've learned 6 git subcommands now. Describe each of them in your own words in the section below:

* git init - Initializes a git repository in the current directory. 
* git status - says current branch, and staged files, as well as committed files. 
* git add - adds files to the staging area for commiting 
* git commit - records staged changes to files that were added to the staging area. 
* git log - Lists your history of commits. 
* git diff - Says what is different with each commit vs its original. 


### 1.7. Practice: Find All Duplicates (Java)
Make sure you implement the `FindDuplicates.java` class as specified in the instructions (with the nested loops implementation).

## Part 2: GitHub

### 2.1. Practice: Find All Duplicates (Python)
Make sure you implement the `find_duplicates.py` file as specified in the instructions (with the nested loops implementation).


## Part 3: Branching

### 3.1. Implement the More Efficient Version of the "Find Duplicates" problem
Implement the more efficient Version of the "Find Duplicates" problem using a dictionary (or hashmap) data structure instead of nested loops. You may do this in either your Python file or in the Java file that you’ve already made. Do this by adding a second function/method to your Java/Python file with a slightly different name.


### 3.2. Link to Repo
Please make sure that the new repo that you made today on GitHub is public, and paste a link to it below.

```bash
# paste your new repo link here...
https://github.com/Csluder2/lab03-exercises
```

### 3.3. What do the three "Merge pull request" options mean? 
Describe each of them in your own words.
Create a merge commit: 
Preserves full history with a single commit, makes it more complicated due to keeping everything. 
Squash and merge:
Reduces number of commits, but loses commit history within the pull request. History is cleaner because of this. 
Rebase and merge: Brings commits from pull requests onto base branch, by a fast forward merge. There can be some conflicts from this method

