"""
This module is responsible for creating a cleaner output
"""

class ReportGenerator:
    """
    creates a text summar of analysis results

    total failed: the number of failed login attempts
    suspicousip: a list of suspicous ips
    """

    lines = []
    lines.append("--Log Report--")
    lines.append(f"Total failed logins: {total_failed}")
    lines.append(f"Suspicious IPs: {len(suspicious_ips)}")

    if suspicious_ips:
        lines.append("Flagged IP addresses:")
        for ip_address in suspicious_ips:
            lines.append(f"- {ip_address}")
        else:
            lines.append("No suspicious IPs detected.")

    return "\n".join(lines)