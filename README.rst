Creeper's Lament Website
========================

This project contains the complete source code for the website for the
Creeper's Lament Minecraft SMP server. Feel free to take and adapt this to
your needs, or submit pull requests if you'd like to help improve the site. 

Licensing
---------

All source code contained within is licensed under Creative Commons,
Attribution 3.0 Unported, which you may find at 
http://creativecommons.org/licenses/by/3.0/
  
Basic Installation
------------------

Before proceeding, make sure you have the following installed:

* pip
* virtualenv
* virtualenvwrapper (make sure you add the bash hooks)

Installation looks something like this, though it may differ based on
your environment::

    git clone git://github.com/gtaylor/creeperslament.git
    mkvirtualenv creeperslament
    workon creeperslament
    cd creeperslament
    pip install -r deployment/requirements.txt
    ./manage.py syncdb
    ./manage.py runserver

If ``mkvirtualenv`` or ``workon`` don't work, you probably don't have
virtualenvwrapper configured correctly. See
http://www.doughellmann.com/projects/virtualenvwrapper/ for more instructions.