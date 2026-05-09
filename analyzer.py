"""
This module examimes the parsed log entries and find suspicous behavoir like reapeated failed login atempts
from the same IP address
"""

class Analyzer:
    """
    Analyzes log entries for suspicous activity
    """

    def count_failed_logins(self, entries):
        """
        Docstring for count_failed_logins
        
        :param entries: A list of LogEntry objects
        """
        count = 0

        for entry in entries:
            if entry.is_failed_login():
                count += 1

        return count
    
    def failed_attempts_by_ip(self, entries):
        """
        Docstring for failed_attempts_by_ip
        
        :param entries: A list of LogEntry objects

        Returns: Dictronary of where the IP values are and what the number of failed login attemps are
        """

        attempts = {}

        for entry in entries:
            if entry.is_failed_login():

                if entry.ip_addr not in attempts:
                    attempts[entry.ip_addr] = 0

                attempts[entry.ip_addr] += 1

        return attempts
    
    def count_successful_logins(self, entries):
        """
        Count successful login attempts.

        Args:
            entries (list): List of LogEntry objects.

        Returns:
            int: Number of successful logins.
        """

        count = 0

        for entry in entries:
            if entry.is_successful_login():
                count += 1

        return count

    def detect_suspicious_ips(self, entries, threshold=3):
        """
        Identify IP address with failed login counts of 3 or above.

        :param entries: List of LogEntry objects
        :param threshold: The minimum number of failed attempts required for an IP to be considered suspicious

        Returns: list of suspicous ips
        """

        attempts = self.failed_attempts_by_ip(entries)

        suspicious = []

        for ip_address, count in attempts.items():

            if count >= threshold:
                suspicious.append(ip_address)

        return suspicious
