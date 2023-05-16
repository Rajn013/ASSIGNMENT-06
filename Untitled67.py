#!/usr/bin/env python
# coding: utf-8

# Q1. Describe three applications for exception processing.

# Error Handling: Exception processing is used to handle and manage errors that can occur during program execution, allowing for graceful recovery, error reporting, and corrective actions.
# 
# Resource Management: Exception processing ensures proper acquisition and release of resources such as file handles, database connections, and network sockets. It helps prevent resource leaks and guarantees proper cleanup even in the presence of exceptions.
# 
# Program Flow Control: Exception processing enables structured handling of exceptional cases and allows for customized program flow based on specific conditions. It provides a mechanism to transfer control from one part of the program to another based on exceptional situations.

# Q2. What happens if you don't do something extra to treat an exception?
# 

# Handling exceptions allows you to control how your program reacts to unexpected situations. If you don't handle an exception, it will stop the program and show an error message. By handling exceptions, you can prevent program crashes and ensure your code behaves as intended even when problems occur.

# Q3. What are your options for recovering from an exception in your script?
# 

# Catch and Handle the Exception: Use a try-except block to catch the exception and provide instructions on what to do when it occurs. You can write code within the except block to handle the exception, perform recovery actions, show error messages, or take alternative paths in your script.
# 
# Retry Mechanism: If the exception is caused by temporary conditions, you can implement a retry mechanism. Put the problematic code inside a loop and catch the exception. Then, retry the code block until it succeeds or until a maximum number of attempts is reached. This can be useful for operations like network connections or API calls.
# 
# Graceful Degradation: If the exception is not critical or the failed operation is not essential, you can gracefully degrade the functionality. Instead of terminating the script or raising an error, provide alternative functionality or fallback options that allow your script to continue running without interruption.

# Q4. Describe two methods for triggering exceptions in your script.
# 

# Using the raise statement: You can use the raise statement to explicitly raise an exception at a specific point in your code. This allows you to generate an exception of a particular type and optionally provide an error message
#  
#  
#  Invoking built-in functions or methods that raise exceptions: Certain built-in functions or methods are designed to raise specific exceptions in certain situations. By invoking these functions or methods, you can trigger exceptions
#         

# Q5. Identify two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists.
# 

# Using the finally block: The finally block is used in conjunction with the try-except block to specify a set of statements that will be executed regardless of whether an exception is raised or not. The code within the finally block is guaranteed to run before the program exits. This is useful for performing cleanup tasks or releasing resources that need to be executed regardless of the outcome.
# 
# Using the atexit module: The atexit module provides a way to register functions that will be called when the program is about to exit, whether normally or due to an exception. You can use the atexit.register() function to register one or more functions that will be executed at program termination.

# In[ ]:




