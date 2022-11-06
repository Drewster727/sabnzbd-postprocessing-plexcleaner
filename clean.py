#!/usr/bin/python
import sys
import time
import math
import shutil
import re
from subprocess import PIPE, run

cleanPattern = '[HX].?265|HEVC'

def exec_docker(directory):
    print("--------------")
    dir_clean=escape_special_chars(directory, " ';:()$&*,<=>?@^`{|}")
    cmd=f'docker run --rm -v {dir_clean}:/clean:rw -v /opt/plexcleaner:/config ptr727/plexcleaner /PlexCleaner/PlexCleaner --settingsfile /config/PlexCleaner.json --logfile /config/PlexCleaner.log process --mediafiles /clean --parallel --threadcount 10'
    print(cmd)
    result = run([cmd], stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    print(result.returncode, result.stdout, result.stderr)
    print("--------------")

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return "{0}h:{1}m:{2}s".format(int(hours),int(mins),math.ceil(sec))

def escape_special_chars(text, characters):
    for character in characters:
        text = text.replace( character, '\\' + character )
    return text

def move_dir(source, destination):
    dir_parts = source.split('/')
    target = f"{destination}/{dir_parts[len(dir_parts)-1]}"
    print(f"Moving to {target}")
    shutil.move(source, target)

def clean(directory, pattern):
    # clean
    if not re.search(pattern, directory, re.IGNORECASE):
        clean_start_time = time.time()
        exec_docker(directory)
        clean_end_time = time.time()
        clean_runtime = time_convert(clean_end_time - clean_start_time)
        print(f"Clean succeeded ({clean_runtime})")
    else:
        print("Skipping clean. x265/HEVC found in title!")
    
    sys.exit(0)

try:
    (scriptname, directory, orgnzbname, jobname, reportnumber, category, group, postprocstatus, url) = sys.argv
except:
    try:
        directory = sys.argv[1]
        category = sys.argv[5]
    except:
        print("No commandline parameters found")
        sys.exit(1)

clean(directory, cleanPattern)