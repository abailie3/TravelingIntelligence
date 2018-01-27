##Guidelines for contributing to TravelingIntelligence
[Back to README](README.md)

So you want to help with this project? Great! I have laid out some guidelines for all contributors to ensure efficient and productive environment.
I ask that everyone who would like to contribute please read and follow these guidelines.

___

###Test Driven Development:
This project aims at following the Test Driven Development (TDD) philosophy. In short, this means that the first step when developing a new feature/improvement is not writing actual code, it is writing a test for that new feature. Below is a more detailed description of the ideal workflow:
1. ***Identify a new feature or improvement:*** This could be a fix from the issue list, a new feature, a feature improvement, or etc.*
2. ***Write tests for the new feature:*** The tests should be written such that they cover all cases, both normal and edge cases. Ideally, each function and class should have a test associated with it. See more guidelines on writing tests in the "Writing Tests" section below.
3. ***Run new tests:*** Run "test_all.py" to run the tests. All of your new tests should fail. If they don't then there's likely no reason to add the new feature.
4. ***Write working code:*** This doesn't have to be pretty, just get something down on paper that passes the tests. We'll clean up later.
5. ***Run tests:*** If they all pass go to 6, else go back to 4.
6. ***Clean-up:*** Make efficiency improvements, refactor for readability, or break out pieces for code re-use. If you do break out pieces into separate functions, make sure to write tests for these! Frequently re-run tests to ensure that nothing went awry while cleaning up.
7. ***Document new code:*** See *[Documentation](#documentation)* section.  

\* I intentionally left out refactoring code for style or an efficiency improvement here. In this case, a new test would not have to be created, since no new feature is being added and the functionality isn't being changed. Instead, after the changes are made the code should still pass all of the existing code for that module.
 
###Writing tests:
As mentioned in the *Test Driven Development* section above, tests are very important to the success of this project! As such, here are some guidelines for writing tests. 
* **Each Module (eg. something.py) should have a test module:** If I am adding a new module named "newmod.py" I should have a test module named "test_newmod.py" in the "tests" folder.
* **Each Class should have a test class:** If I am adding the class named "NewClass" to the "newmod.py" module, then I should add a class named "NewClassTestCase" to the "test_newmod.py" module. Please follow the example in one of the previously made test modules. 
* **Each function (and class constructor) should have a test function:** If I am adding a new function named "new_func" to the class named "NewClass," then I should add a "test_new_func" method to the "NewClassTestCase" class within "test_newmod.py." If I am adding a function that is not part of a class, then I should add it to a generic test class within the test module. If testing a private function, the preceding underscores can be left out. Eg. "test_private_func" is an acceptable name for the test function for the "\__private_func\__" function. 
* **Proper test formatting:** Each test function should be commented with a short description of what the test is testing. Within each test function, there should be short sub-tests that test the normal and edge cases for the function. Each sub-test should be commented to indicate what that sub-test is testing. Ideally each test-module should include short tests that are easily understood without need for futher comments. However, certain cases arise where more detailed tests must be written. In theses cases, the test code shall be well documented to show how/why the test is being performed.  
* **All tests should be combined:** Since this is currently a small project, all tests should be combined into a test suite in the "test_all.py" module. This way, all new code can be tested against all tests for the project. Please follow the directions in "test_all.py".
___

###Documentation
####-Classes-
Classes merely require a description of what the purpose of the class is. Below is an example:
    
    class DistanceMeasure(ABC):
    """
    Abstract class for various ways of accounting for distance.
    """
All class methods should follow the functions standards below.
####-Functions-
Below is an example of the documentation standard for functions 

        def __safe_idx__(arr_name: str, idx) -> str:
        """
        This method creates a line of code that safe indexes an array. Safe indexing here means indexing such that
        there is no possibility of indexing out of bounds (assuming the array is not of length 0).
        :param arr_name: (str) Name of the variable representing the array.
        :param idx: (int -or- float) Index of the array to grab. If float is provided it will be truncated to int.
        :return: (str) An un-indented string of the line of code.
        """
Let's break it down into each element:
* **Function description:** A brief description of what the function does.

        This method creates a line of code that safe indexes an array. Safe indexing here means indexing such that
        there is no possibility of indexing out of bounds (assuming the array is not of length 0).

* **Parameter description:** In the form "parameter name: (type) description," with a brief description of the parameter. If the parameter is a data structure such as a list or dictionary, the form  of this data structure should be described.

        :param arr_name: (str) Name of the variable representing the array.
        :param idx: (int -or- float) Index of the array to grab. If float is provided it will be truncated to int.

* **Return description:** In the form "(type) description," with a brief description of the parameter. If the return type is a data structure such as a list or dictionary, the form  of this data structure should be described.

        :return: (str) An un-indented string of the line of code.


[Back to README](README.md)
___
Copyright (c) 2018 Austin Bailie, All rights reserved.