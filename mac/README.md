# Iterm
  * Go to https://www.iterm2.com/
  * Download iTerm and drag it to your Applications folder

# Homebrew
  * Go to https://brew.sh/
  * Open iTerm (see previous step)
  * Paste the Ruby command in the terminal

# Sublime text
  * Go to https://www.sublimetext.com/3
  * Sublime text command line:
    `$ ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl`

# Python

## Installing Python

```bash
# For latest Python
$ brew install python

# For a specific python version
# You get this link by going to the Github of Homebrew and 
# copying the .rb file from a specific commit as mentioned 
# here: https://stackoverflow.com/questions/51125013/how-can-i-install-a-previous-version-of-python-3-in-macos-using-homebrew
brew install --ignore-dependencies https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb
```

If you dont mind updating your `PATH` variable, then you can add the Homebrew Python before the system Python in the search path. 

```bash
# Update bash profile
$ echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile
$ source ~/.bash_profile

# Check Python executable path
# Should give /usr/local/bin/python  
$ which python
```

If you dont want to modify your `PATH` variable, you can skip the above steps and first set up your virtual environment and have the virtualenv activation on startup. To start installing packages using `pip` you must have `openssl` installed which you can install as

```bash
$ brew install openssl
```

# Python environment

At this point your development Python is different from the system Python that comes bundled with Mac OSX. Now we want to install some useful libraries. Instead of installing it against the global Python we just created, we will create little virtual environments, that will allow us to prevent package conflicts by having different versions of the packages if needed.

To install the virtual environment with the Homebrew Python, you must make sure to use the Homebrew pip. I'm assuming that you installed Homebrew Python 3. So you should be using `pip3` for the virtual environment installation.

``` bash
# Virtual environment
$ pip3 install virtualenv

# Create a folder to house all your virtual environments
$ mkdir ~/work/code/virtualenvs
$ cd ~/work/code/virtualenvs

# Create your basic, workhorse virtualenvironment that you'll use for most things
$ virtualenv base

# Activate the `base` virtualenvironment
# Add the following line to ~/.bash_profile
$ source ~/work/code/virtualenvs/base/bin/activate
```

Once the virtual environment is activated, `python` and `pip` refer to their Homebrew versions and you no longer have to refer them as `python3` or `pip3`. Now install various packages.

```bash
# Python scientific stack
$ pip install numpy scipy matplotlib ipython jupyter scikit-learn scikit-image pandas

# Set the Matplotlib backend
$ echo 'backend: TkAgg' >> ~/.matplotlib/matplotlibrc

# Vision
$ pip install opencv-contrib-python
$ pip install pyopengl pyopengl-accelerate

# Deep learning
pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl
pip install keras

# Supporting packages
pip install mysql-connector opengraph wget flask flask_cors PyQt5 s3cmd
```

# Java (SE)
Let us set up our Java environment.

```bash

# Use Homebrew to install Java
$ brew cask install java

# Set your JAVA_HOME environment variable. Add this line to your ~/.bash_profile.
$ export JAVA_HOME=$(/usr/libexec/java_home)
```

# Java environment

```bash

#Maven
$ brew install maven
```

# Intellij idea
Idea is great great multi-language IDE (Java, Scala, Python, Bash)

  * https://www.jetbrains.com/idea/#chooseYourEdition
  * Intellij is a primarily Java IDEA, so we need to Install Python plugin
    * Open Intellij -> Settings
    * Search for 'plugins' and click the highlighted option
    * Under Plugins, search for 'Python community edition'
    * You wont get any results. Click 'Browse repositories'
    * Select 'Python Community Edition' and install it
    * Thats it, your IntelliJ is now a respectable Python IDE (though not Pycharm level)

# Scala [optional]

Scala allows you to write scripts using pre-existing Java code. It is also a statically typed functional language that is used to build Spark, among other frameworks. For many reasons, it’d be helpful to be familiar with it.

```bash
#Scala
$ brew install scala
```

# Postgresql [optional]

A local SQL installation is often handy for quick data summurization (mean,
median, max/min, counts etc), cleansing and selective exporting (clean CSV of
particular rows/columns). Notably, a host of high-performance commercial
analytic databases (e.g. Vertica, Netezza) are derived from Postgres core.
Below is the setup of Postgresql, a SQL flavor with a lot of handy analytic
functions. This is not a SQL tutorial or even a Postgres tutorial (excellent
tutorials are available online). This is merely for installation, if you
haven't done it in a while.

```bash
# Installation of Postgres 9.6.2
$ brew install postgres

# Add following lines to your ~/.bash_profile
# Postgres start/stop
alias pgstart="brew services start postgresql"
alias pgstop="brew services stop postgresql"


# Activate your updated bash_profile
$ source ~/.bash_profile
```

Before using Postgres you need to start the server using

```bash
$ pgstart
```

After you're done, stop postgres using

```bash
$ pgstop
```

# Optional

## Disable all gestures
  * Settings -> Trackpad
  * Uncheck all gestures

## Disable Siri
  * Settings -> Siri
  * Uncheck 'Enable Siri'

## Swap control and caps lock buttons
  * Go to Settings -> keyboard -> Modifier keys
  * Swap 'control' and 'caps lock'
