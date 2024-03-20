<h1 align="center">HolbertonBnB</h1>
<p align="center">AirBnB clone.</p>

<p align="center">
	<img src="./misc_stuff/hbnb.png" alt="HolbertonBnB logo">
</p>

---

## Project Description

This project is a clone of the Famous "AirBnB" website (But it doesn't exactly look like it :smile:)<br>
Hbnb(this project) is a fully fledged Web application, with a database storage, a back-end API, and front-end interfacing in a clone of AirBnB.

**Currently the implemented features are:**
- The back-end console(Command Interpreter)
- The Static web page of our website

## Command Interpreter(Backend-console) :man_technologist:

This first step is very important because what is built during this step will be used with all other
following steps: HTML/CSS templating, database storage, API, front-end integration…

**What will be the Use of this Console?**

- To create your data model
- Manage (create, update, destroy, etc) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine (For now json files are used)

<p align="center">
    <img src="./misc_stuff/console.png" alt="Console_storage link">
</p>

**How to use the Console?**

The shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## <a href="https://github.com/Bikaze/AirBnB_clone/tree/main/web_static">Web static</a>

After the command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

- Create simple HTML static pages
- Style guide
- Fake contents
- No Javascript
- No data loaded from anything

**This is our progress. We we've implemented the console and now we're making a static webpage for our website**

<p align="center">
    <img src="./misc_stuff/hbnb_step1.png" alt="front-end html">
</p>
