**Update**: You can now use homebrew to install sublime text: `brew install sublime-text`

**Update**: YOu can now use homebrew to install anaconda: `brew install --cask anaconda`

**Update**: You can now use VSCode on Windows with WSL! [https://code.visualstudio.com/docs/remote/wsl](https://code.visualstudio.com/docs/remote/wsl)


## Install Anaconda on Linux (WSL)
1. In a linux terminal window (if using WSL, open Ubuntu as Administrator from the Start menu), then download the anaconda installer:  
    `wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh`
    
or 

    `curl -O https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh`
    
which will download the installer to your current directory.

2. Ensure the installer is executable, type:  
    `chmod +x Anaconda3-2020.02-Linux-x86_64.sh`
    
3. Execute the installer, type:  
    `./Anaconda3-2020.02-Linux-x86_64.sh`
    
4. Follow the prompts, to install, using default values when asked. This will install Anaconda in your user directory, and set up your paths to work properly. 

5. Enable the `conda` command by typing:  
    `source ./anaconda3/bin/activate`  

6. Once done, delete the installer, type:  
    `rm Anaconda3-2020.02-Linux-x86_64.sh`  

7. Ensure that the rest of your system is up to date by typing:  
    `sudo apt update; sudo apt upgrade -y`  

**If you are running WSL You will need to re-install an editor/IDE in this same environment for it to use Anaconda!**

To install sublime text, type the following commands and choose the default answers when asked:

```
    wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -  
    
    sudo apt install apt-transport-https
    
    echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
    
    sudo apt update 
    
    sudo apt install sublime-text
```
    
Once done, you can just run sublime by calling:  
    `sublime . &`  

I prefer Atom on linux, which you can install with:  
    `sudo apt install atom`  
    
Or install your favorite IDE using whatever method it requires for linux. NOTE: Windows editors/IDEs cannot use this anaconda install! All work must be done in this environment!
