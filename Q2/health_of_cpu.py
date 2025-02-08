# Python script to monitor the health of the CPU.

# Import psutil to monitor CPU usage
import psutil  

# Define CPU usage threshold
THRESHOLD = 5

# Printing to inform the user that the program has started monitoring the CPU Usage
print("Monitoring CPU usage... (Press Ctrl+C to stop)")

# try catch loop to handle exceptions
try:
    # Infinite loop for continuous monitoring
    while True:
        # Get CPU usage over 1 second
        cpu_usage = psutil.cpu_percent(interval=1)
        # Check if CPU usage exceeds threshold
        if cpu_usage > THRESHOLD:
            # Print alert
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
except KeyboardInterrupt:
    # Gracefully exit on Ctrl+C
    print("\nMonitoring stopped by user.")
except Exception as e:
    # Print error message if something goes wrong
    print(f"An error occurred: {e}")