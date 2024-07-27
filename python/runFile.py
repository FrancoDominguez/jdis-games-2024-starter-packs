import subprocess
import time

def run_program():
  # Replace 'python your_script.py' with your command to run the runtime
  subprocess.run(['python', 'run_bot.py','-t', '555e42bd-db28-4599-92a8-061f9ca95048'])

while True:
  try:
    run_program()
  except Exception as e:
    print(f"Error occurred: {e}")
  time.sleep(1)