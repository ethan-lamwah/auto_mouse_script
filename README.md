# auto_mouse_script
This is a simple python script to keep your system awake by auto moving mouse around at certain intervals.

## Setup
1. It's recommended to use virtual environment when you're working on python projects. By doing this can help you avoid the dependencies conflicts with python project on other operating systems. (Learn how to create a python virtual environment using [virtualenv](https://virtualenv.pypa.io/en/latest/user_guide.html#introduction))

2. Install packages
    ```
    pip install -r requirements.txt
    ```

3. Run the script 
    ```
    python -m script [interval]
    ```
    Specify the *interval* if you want to move the mouse at every specified minutes. Default is 5 minutes.

## Abort the runnning script
`crtl + c` to abort the program at any time.

## Setup zsh command to run the script in MAC
1. Create a `.command` file and use below sample command. 
2. Replace `[project_dir]` to your project directory.
3. Save and ready to go!

```bash
#! /bin/zsh
echo -n "Changing directory..."
cd '/[project_dir]/' && echo "Done"
echo -n "Activating venv..."
source venv/bin/activate && echo "Done"
echo "Running script...(ctrl+c to terminate)"
python -m script 3
echo "Deactivating venv..."
deactivate
echo "Ready to exit"
```

*If you want to **suspend** the running process in Linux, press `CTRL+Z`. To resume it, type `fg` in command line.*

```bash
# CTRL+Z is pressed
zsh: suspended  python -m script 1
# fg is typed
user-mac auto_mouse_script % fg
[1]  + continued  python -m script 1
```

# PyAutoGUI
> PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard. 

Checkout this amazing module [PyAutoGUI](https://github.com/asweigart/pyautogui) for more information and example usage on keyboard and mouse control.