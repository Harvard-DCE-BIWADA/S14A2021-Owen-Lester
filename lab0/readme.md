## Lab 0

#### Initial system setup
For labs we will be using several technologies - to avoid any system-specific hiccups, we highly recommend you install or setup the following in advance:
1. A shell (the user interface for interacting with the OS).
    + A nice tool for understanding commands: [ExplainShell](https://explainshell.com/).
    + Mac users okay with Terminal.
    + Linux users likely already have this handled with Bash or similar.
    + Windows users have lots of options, including the new [Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab).
2. An IDE (ingegrated development environment) or code editor.
    + [PyCharm](https://www.jetbrains.com/pycharm/) is a paid subscription (but offers a free 1 year subscription for
  students) that brands itself as "The python IDE for professional developers".
    + [Sublime Text](https://www.sublimetext.com/) is a free and "sophisticated text editor for
code, markup and prose".
3. A [Github](https://github.com/) account for version control.
    + Signup for the [Student Developer Pack](https://education.github.com/pack) to get loads of free goodies.
    + Install Git on your computer - there is pretty good direction from [Github Help](https://help.github.com/en/github/getting-started-with-github/set-up-git) on setup.
    + It's also worthwhile setting up connection via [SSH](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh).
4. The [Anaconda](https://www.anaconda.com/products/individual) distribution for Python and data science.
    + [Install](https://docs.anaconda.com/anaconda/install/) Anaconda (full version) or Miniconda (mini version) on
     MacOS, Windows or Linux.
5. [Heroku](https://www.heroku.com/) for deployment.
    + Setup a [free account](https://signup.heroku.com/login).
    + Please follow this [guide](https://devcenter.heroku.com/articles/heroku-cli) to setup Heroku's CLI (command
 line interface).
6. [PostgreSQL](https://www.postgresql.org/): The World's Most Advanced Open Source Relational Database.
    + Follow the tutorials: [installation](https://www.postgresqltutorial.com/install-postgresql/) and [connection](https://www.postgresqltutorial.com/connect-to-postgresql-database/)
    + Download the latest version of Postgres from [EDB](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads), which includes: PostgresSQL Server, pgAdmin 4, Stack Builder, Command Line Tools
        + OR, Mac users may want to use [Homebrew](https://wiki.postgresql.org/wiki/Homebrew) for installation.
        + OR, another Mac alternative is to download [Postgres App](https://postgresapp.com/)
    + Confirm success: 
        + For EDB, by opening SQL Shell (psql), and entering: `SELECT version();`
        + For homebrew, in terminal: `psql postgres`
        + For Postgres App, open application.
7. AWS (Amazon Web Services)
    + Signup for a [free tier](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc).
    + Will use RDS for Postgres - a great [tutorial](https://aws.amazon.com/getting-started/tutorials/create-connect-postgresql-db/).
 
 Windows specific information can be found in resources/readme-wsl.md or resources/readme-linux_or_wsl.md
 Linux specific information can be found in resources/readme-linux_or_wsl.md
 Mac Specific information can be found in resources/readme-macos.md
