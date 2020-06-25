import subprocess
import os

# Create a directory for the script/mp3 to live
home_dir = os.path.expanduser('~')
stonks_dir = os.path.join(home_dir, '.stonks')
script_directory = os.path.dirname(os.path.abspath(__file__))

subprocess.call(['launchctl', 'unload', os.path.join(stonks_dir, 'STONKS.plist')])
subprocess.call(['rm', '-rf', stonks_dir])
