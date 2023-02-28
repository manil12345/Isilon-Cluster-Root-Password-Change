# Isilon-Cluster-Root-Password-Change

This Python script allows you to change the root password on multiple Isilon clusters using the OneFS API. The fully qualified domain names (FQDNs) of the Isilon clusters are stored in a CSV file, which you will be prompted to provide the location for. The script will then ask for the old and new passwords for the root account, hiding the input for security.


The CSV file should have one FQDN per line, like so:
cluster1.example.com
cluster2.example.com
cluster3.example.com


This script will change the root password on each cluster sequentially, so it may take some time if you are changing the password on multiple clusters.

The script will only attempt to change the root password if it can successfully authenticate with the OneFS API using the old password. If authentication fails, the script will skip that cluster and move on to the next one.
