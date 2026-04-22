"""

Environment Configuration Script
Build a Python script that automates the developer environment setup process. This simulates real-world scenarios where developers need to configure their local environment.

Requirements:

Check if Python is installed and print version
Validate Python version (must be 3.8 or higher)
Create a project directory structure (src/, tests/, docs/, logs/)
Generate a requirements.txt file with basic packages
Create a .gitignore file with common Python patterns
Print a summary report with colored output (use ANSI escape codes)
Handle errors gracefully with try-except blocks
Real-World Application: DevOps teams use similar scripts to automate environment setup for new developers joining the team.

"""
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

import sys 
import platform

# Step 1 : Check if Python is Installed and print version.
try:
    version = platform.python_version()
    
    # method 1
    print("Python Version : ", sys.version)
    
    #method 2
    v = sys.version_info
    print(f"Python version major : {v.major}, minor : {v.minor}, micro : {v.micro}")
    
    # Using platform for a cleaner version string
    print(f"Platform Version: {version}")

    # Step 2 : Validate Python version (must be 3.8 or higher)
    if v.major < 3 and v.minor < 8:
        raise CustomException('Verison not Valid.')

except Exception as e:
    if isinstance(e, AttributeError):
        print('Error may be because of v.major, v.minor attributes if version is older then 2.7') 
    else:
        print(f'Step 1 or Step 2 Error {e}')


# Step 3 : Create a project directory structure (src/, tests/, docs/, logs/)
try:
    from pathlib import Path
    
    Path('Day-01/Assignment/src').mkdir(parents=True, exist_ok=True)
    Path('Day-01/Assignment/test').mkdir(parents=True, exist_ok=True)
    Path('Day-01/Assignment/docs').mkdir(parents=True, exist_ok=True)
    Path('Day-01/Assignment/logs').mkdir(parents=True, exist_ok=True)

except Exception as e:
    if isinstance(e,FileExistsError):
        print('Step 3 : File already exist.')
    else:
        print(f'Step 3 Error : {e}')

# Step 4 : Generate a requirements.txt file with basic packages
try:
    packages = ['Numpy']
    with open('requirements.txt',"w") as file:
        file.writelines(packages)

except Exception as e:
    if type(e) is IsADirectoryError:
        print('Error in Step 4 : Directory already Exist.')
    else:
        print(f"Step 4 error: {e}")


# Step 5 : Create a .gitignore file with common Python patterns
try:
    content = """
    .env
    venv/
    logs/
    docs/
    """
    
    with open('.gitignore', "w") as file:
        file.write(content.strip())
    
except Exception as e:
    if type(e) is IsADirectoryError:
        print('Error in Step 4 : Directory already Exist.')
    else:
        print(f"Step 4 error: {e}")


# Step 5 : Print a summary report with colored output (use ANSI escape codes)
try :
    ansi_code = {
        "HEADER" : '\033[95m',
        "BOLD" : '\033[1m',
        "UNDERLINE" : '\033[4m',
        "RESET" : '\033[0m',
        "OKGREEN" : '\033[92m'
    
    }
    
    summary = f"""
    {ansi_code['OKGREEN']}Information Technology (IT){ansi_code['RESET']} is the broad field of using computers, software, networks, and physical infrastructure to create, process, store, secure, and exchange all forms of digital information. While humans have managed information for centuries, modern IT focuses on programmable, general-purpose machines that solve complex problems and automate repetitive tasks.
    """
    
    
    
    print(f"{ansi_code['HEADER']}{ansi_code['BOLD']}{ansi_code['UNDERLINE']} SUMMMARY {ansi_code['RESET']}")
    
    print(summary)

except Exception as e:
    if type(e) is SyntaxError:
        print('Step 5 Error in Syntax')
    else:
        print(f'Step 5 Error : {e}')