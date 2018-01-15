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

```bash
$ brew install python

#Update bash profile
$ echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile
$ source ~/.bash_profile

# Check Python executable path
# Should give /usr/local/bin/python  
$ which python
```


# Python environment

At this point your development Python is different from the system Python that comes bundled with Mac OSX. Now we want to install some useful libraries. Instead of installing it against the global Python we just created, we will create little virtual environments, that will allow us to prevent package conflicts by having different versions of the packages if needed.

``` bash
# Virtual environment
$ pip install virtualenv

# Create a folder to house all your virtual environments
$ mkdir ~/work/code/virtualenvs
$ cd ~/work/code/virtualenvs

# Create your basic, workhorse virtualenvironment that you'll use for most things
$ virtualenv base

# Activate the `base` virtualenvironment
$ source base/bin/activate

# Numpy
$ pip install numpy

# Scipy
$ pip install scipy

# IPython
$ pip install ipython

# Jupyter
$ pip install jupyter

# Scikit learn
$ pip install scikit-learn

# Matplotlib (for plotting)
$ pip install matplotlib

# Set the Matplotlib backend
$ echo 'backend: TkAgg' >> ~/.matplotlib/matplotlibrc

# Pandas
$ pip install pandas
```

# Java (SE)
Streammosaic end product is in Java, so let us set up our Java environment.

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

# Octave
For some projects, we internally use MATLAB for data generation and quick modeling tests. Octave is open-source alternative to MATLAB. As long as your MATLAB scripts don't use specialized toolkits, they should be easily portable to octave. Below are the steps to Octave installation. Note that these steps are customized for MacOS Sierra (10.12.2) and will most likely change in future versions of the OS.

```bash
# Update and upgrade brew
$ brew update
$ brew upgrade

# Install Xquartz for the window system
$ brew cask install xquartz

# Tap Homebrew science
$ brew tap homebrew/science

# Install the gcc package (the default one that came
# with the OS does not include gfortran)
$ brew install gcc

# Install fltk and gnuplot
$ brew install fltk
$ brew install gnuplot --with-qt

# Install Octave
$ brew install octave
```

Next modify the `~/.octaverc` file to help Gnuplot play with Octave

```bash
# Place the following commands in ~/.octaverc
setenv("GNUTERM", "qt");
graphics_toolkit("gnuplot");
PS1("octave>>");
```

Test Octave installation

## Octave GUI

Type `octave` on the command line. In the window that opens up, type the following. (The `octave>>` is the prompt and doesnt need to be typed)

```matlab
octave>> x = 0 : 0.1 : 10; y = sin(pi * x); plot(x,y,'o')
```

A plot window with sinusoid should show up.

## Octave command-line shell

Type `octave-cli` on the command line. This time you'll get the Octave shell. Type the same command.

```matlab
octave>> x = 0 : 0.1 : 10; y = sin(pi * x); plot(x,y,'o')
```

## Octave as a script (to be invoked/scheduled from Bash)

Create a `octave_test.m` file in your current directory, and place the following commands.

```matlab
fig1 = figure;
x = 0 : 0.1 : 10;
y = sin(pi * x);
plot(x, y);
print(fig1, 'sinecurve', '-dpng');

fig2 = figure;
surf(peaks);
print(fig2, 'surfaceplot', '-dpng');
```

Run the file using `octave` command (Just as you'd run a Python file)

```bash
$ octave octave_test.m
```

You should now have image files `sinecurve.png` and `surfaceplot.png` in your working directory.

# h2o with Python

If you're a Python person, it is straightforward to get started with
h2o using Python. h2o is written in Java. So the Java <--> Python
communication happens over HTTP. The h2o cluster is launched
independently (at default port 54321), and the h2o Python bindings use
the `requests` library to communicate with the core engine. This setup
is great for quick model testing and gaining familiarity with h2o, but
large models are likely to be bottlenecked by data movement.

The setup steps are as follows.

  1. Download h2o from https://h2o-release.s3.amazonaws.com/h2o/rel-tverberg/5/index.html

    a. Follow the instructions for unzipping and launching the cluster    
    b. Go to `http://localhost:54321` and verify cluster startup

  2. Click the "install in Python" link on the above webpage and follow the steps

Verify h2o installation and its communication with Python

  1. Download a sample datafile from https://s3.amazonaws.com/h2o-public-test-data/smalldata/logreg/prostate.csv.

  2. Create a python script with following contents.

```python

import h2o
from h2o.estimators.gbm import H2OGradientBoostingEstimator

h2o.init()
df = h2o.import_file(path="path/to/prostate.csv") # Put proper path
df.describe()
train = df.drop("ID")
vol = train['VOL']
vol[vol == 0] = None
gle = train['GLEASON']
gle[gle == 0] = None
train['CAPSULE'] = train['CAPSULE'].asfactor()

# See that the data is ready
train.describe()

my_gbm = H2OGradientBoostingEstimator(distribution = "bernoulli", ntrees=50, learn_rate=0.1)
my_gbm.train(x=list(range(1,train.ncol)), y="CAPSULE", training_frame=train, validation_frame=train)
my_gbm_metrics = my_gbm.model_performance(train)
my_gbm_metrics.show()

```

# Postgresql

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
