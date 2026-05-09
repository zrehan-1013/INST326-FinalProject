"""
This module is responsible for creating a cleaner output
"""

class ReportGenerator:
    """
    creates a text summary of analysis results

    total failed: the number of failed login attempts
    suspicousip: a list of suspicous ips
    """
    def generate_report(
        self,
        total_failed,
        total_successful,
        suspicious_ips
        ):
        """
        Generate formatted report.

        Args:
            total_failed (int): Failed login count.
            total_successful (int): Successful login count.
            suspicious_ips (list): List of suspicious IPs.

        Returns:
            str: Formatted report string.
        """

        lines = []

        lines.append("-- Log Report --")
        lines.append(
            f"Total successful logins: {total_successful}"
        )
        lines.append(
            f"Total failed logins: {total_failed}"
        )
        lines.append(
            f"Suspicious IPs: {len(suspicious_ips)}"
        )

        if suspicious_ips:
            lines.append("Flagged IP addresses:")

            for ip_addr in suspicious_ips:
                lines.append(f"- {ip_addr}")

        else:
            lines.append("No suspicious IPs detected.")

        return "\n".join(lines)

    
