from setuptools import find_packages, setup
from typing import List
setup(
    name="sensor",
    version="0.0.1",
    author="Gaurav",
    author_email="gkumardav1996@gmail.com",
    packages=find_packages(),
    install_requires=[],
)

"""
# Import necessary functions from setuptools module
from setuptools import find_packages, setup

# Import List from typing module for type annotations
from typing import List

# Define a function to read and return the list of requirements
def get_requirements() -> List[str]:
    # Initialize an empty list to store the requirements
    requirement_list: List[str] = []
    # Open the requirements.txt file in read mode
    with open('requirements.txt', 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Strip any leading/trailing whitespace (including newlines) from the line
            requirement = line.strip()
            # Check if the requirement is not an empty string and does not start with '-e'
            if requirement and not requirement.startswith('-e'):
                # Append the requirement to the list
                requirement_list.append(requirement)
    # Return the list of requirements
    return requirement_list

# Call the setup function to specify the package details
setup(
    name="sensor",  # Name of the package
    version="0.0.1",  # Version of the package
    author="Gaurav",  # Author of the package
    author_email="gkumardav1996@gmail.com",  # Author's email
    packages=find_packages(),  # Automatically find and include all packages in the distribution
    install_requires=get_requirements(),  # List of dependencies to install, obtained from get_requirements function
)

"""
"""
# Import necessary functions from setuptools module
from setuptools import find_packages, setup

# Import List from typing module for type annotations
from typing import List

# Define a function to read and return the list of requirements
def get_requirements() -> List[str]:
    # Initialize an empty list to store the requirements
    requirement_list: List[str] = []
    # Open the requirements.txt file in read mode
    with open('requirements.txt', 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Strip any leading/trailing whitespace (including newlines) from the line
            requirement = line.strip()
            # Check if the requirement is not an empty string
            if requirement:
                # Append the requirement to the list
                requirement_list.append(requirement)
    # Return the list of requirements
    return requirement_list

# Call the setup function to specify the package details
setup(
    name="sensor",  # Name of the package
    version="0.0.1",  # Version of the package
    author="Gaurav",  # Author of the package
    author_email="gkumardav1996@gmail.com",  # Author's email
    packages=find_packages(),  # Automatically find and include all packages in the distribution
    install_requires=get_requirements(),  # List of dependencies to install, obtained from get_requirements function
)
"""

