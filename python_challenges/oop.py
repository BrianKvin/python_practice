def my_str():
    message = "Python "
    new_msg = message + "is " + message
    new_msg.replace(message, "Great")
    return new_msg

print(my_str())