#!/usr/bin/python
import sys
import subprocess

try:
    (scriptname, directory, orgnzbname, jobname, reportnumber, category, group, postprocstatus, url) = sys.argv
except:
    try:
	    directory = sys.argv[1]
	    jobname = sys.argv[3]
    except:
        print("No commandline parameters found")
        sys.exit(1)

DOCKERRUN=f"docker run --rm -v {directory}:/clean:rw -v /opt/plexcleaner:/config ptr727/plexcleaner /PlexCleaner/PlexCleaner --settingsfile /config/PlexCleaner.json --logfile /config/PlexCleaner.log process --mediafiles /clean --parallel --threadcount 10"

print(DOCKERRUN)

with open("/tmp/output.log", "a") as output:
    subprocess.call(DOCKERRUN, shell=True, stdout=output, stderr=output)

# Success code
sys.exit(0)
