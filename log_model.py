"""
Data modules for the cyber security log analyzer project

This module, LogEntry class, stores information from one parsed log line. A LogEntry object represents a single
authentication event that can later be analyzer for suspicous behavoir 
"""


class LogEntry:

    def __init__(self, timestamp, ip_addr, username, status):
        """
        Init the LogEntry class
        
        :param self: Init self
        :param timestamp: Date and time of event
        :param ip_addr: IP address associted with the event
        :param username: Finds usernames based on event
        :param status: Tells status of login or not
        """

        self.timestamp = timestamp
        self.ip_addr = ip_addr
        self.username = username
        self.status = status

    def is_failed_login(self):
        """
        Docstring for is_failed_login, checks log for failed login attempts. Uses usernames and authenticaion to check who logged in 
        and if it was succesful or not
    
        :param self: True unless the statment is 'Fail'
        """

        return self.status.upper() == "FAIL"

    def is_successful_login(self):
        """
        Checks if login was successful.
        """

        return self.status.upper() == "SUCCESS"

    def __str__(self):
        """
        Docstring for __str__
    
        Return a readable string for the long entry
        :param self: Formatted string describing the log entry
        """

        return (
            f"{self.timestamp} | "
            f"{self.ip_addr} | "
            f"{self.username} | "
            f"{self.status}"
        )
