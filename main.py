"""
Main file for cybersecurity log analyzer.
"""
import sys
from parser import LogParser
from analyzer import Analyzer
from repot import ReportGenerator

def main():
    """
    Run the cybersecurity log analyzer.
    """

    if len(sys.argv) != 2:
        print("Usage: python3 main.py log.txt")
        return

    filename = sys.argv[1]

    parser = LogParser()
    analyzer = Analyzer()
    reporter = ReportGenerator()

    try:
        entries = parser.parse_file(filename)

    except FileNotFoundError:
        print("Error: File not found.")
        return

    total_failed = analyzer.count_failed_logins(entries)

    total_successful = analyzer.count_successful_logins(
        entries
    )

    suspicious_ips = analyzer.detect_suspicious_ips(
        entries
    )

    report = reporter.generate_report(
        total_failed,
        total_successful,
        suspicious_ips
    )

    print(report)


if __name__ == "__main__":
    main()
