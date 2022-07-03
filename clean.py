#!/usr/bin/python
import sys
import time
import math
from subprocess import PIPE, run

try:
    (scriptname, directory, orgnzbname, jobname, reportnumber, category, group, postprocstatus, url) = sys.argv
except:
    try:
        directory = sys.argv[1]
        jobname = sys.argv[3]
    except:
        print("No commandline parameters found")
        sys.exit(1)

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

dir_clean=escape_special_chars(directory, " ';:()$&*,<=>?@^`{|}")
cmd=f'docker run --rm -v {dir_clean}:/clean:rw -v /opt/plexcleaner:/config ptr727/plexcleaner /PlexCleaner/PlexCleaner --settingsfile /config/PlexCleaner.json --logfile /config/PlexCleaner.log process --mediafiles /clean --parallel --threadcount 10'
print(cmd)
print("--------------")
start_time = time.time()

result = run([cmd], stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
print(result.returncode, result.stdout, result.stderr)

end_time = time.time()
time_lapsed = end_time - start_time
runtime = time_convert(time_lapsed)

print("--------------")
print(f"Clean succeeded ({runtime})")

# Success code
sys.exit(0)
