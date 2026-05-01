import sys
from parser import  LogParser
from analyzer import Analyzer
from repot import ReportGenerator

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py log.txt")
        return
    
    filename = sys.argv[1]

    parser = LogParser()
    analyzer = Analyzer()
    reporter = ReportGenerator()

    entries = parser.parse_file(filename)
    total_failed = analyzer.count_failed_logins(entries)
    suspicious = analyzer.detect_suspicious_ips(entries)

    report = reporter.generate_report(total_failed, suspicious)
    print(report)

if __name__ == "__main__":
    main()
