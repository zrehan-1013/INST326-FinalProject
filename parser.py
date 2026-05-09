"""
Docstring for parser, Parses functions

This module is responsible for readin the log file and convertiing each line
into LogEntry objects. It sepereates input and the parsing to have a seperation
to make it easier to read
"""

from log_model import LogEntry


class LogParser:
    """
    Parse raw log lines into LogEntry objects.
    """

    def parse_line(self, line):
        """
        Parase raw log lines into LogEntry objects.
        
        Expected formate:
        timestamp, ip_addr, username, status
        
        Example:
        2026-04-10 09:15:00,192.168.1.7,admin,FAIL

        Args:
        line: One raw line from log file
        """

        parts = line.strip().split(",")

        if len(parts) != 4:
            raise ValueError("Invalid format")

        timestamp, ip_addr, username, status = parts

        return LogEntry(
            timestamp,
            ip_addr,
            username,
            status
        )

    def parse_file(self, filename):
        """
        Read a log file and parse each line into the logentry objects
    
        :param filename: The name of the file to parse
        """

        entries = []

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    entries.append(
                        self.parse_line(line)
                    )

        return entries
