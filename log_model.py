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

if __name__ == "__main__":
    pass