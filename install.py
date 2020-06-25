import subprocess
import os

# Create a directory for the script/mp3 to live
home_dir = os.path.expanduser('~')
stonks_dir = os.path.join(home_dir, '.stonks')
script_directory = os.path.dirname(os.path.abspath(__file__))

try:
    os.makedirs(stonks_dir)
    print('Created stonks dir at %s' % stonks_dir)
except FileExistsError:
    print('Stonks dir already exists at %s' % stonks_dir)

# Configure the plist file for the current user
with open('./STONKS.plist', 'r') as f:
    plist = f.read()
    plist = plist.replace('*SCRIPT_PATH*', os.path.join(stonks_dir, 'stonks.py'))

with open(os.path.join(stonks_dir, 'STONKS.plist'), 'w') as f:
    f.write(plist)
    print('Writing customized launch file')

# Copy the python script to the stonks dir
print('Copying python script into %s' % stonks_dir)
subprocess.call(['cp', os.path.join(script_directory, 'stonks.py'), os.path.join(stonks_dir, 'stonks.py')])
subprocess.call(['chmod', '+x', os.path.join(stonks_dir, 'stonks.py')])

# Install the launcher
print('Installing launcher')
subprocess.call(['launchctl', 'unload', os.path.join(stonks_dir, 'STONKS.plist')])
subprocess.call(['launchctl', 'load', os.path.join(stonks_dir, 'STONKS.plist')])
