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

# PyAutoGUI
> PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard. 

Checkout this amazing module [PyAutoGUI](https://github.com/asweigart/pyautogui) for more information and example usage on keyboard and mouse control.