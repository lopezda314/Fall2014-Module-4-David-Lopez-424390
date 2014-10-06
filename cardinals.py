#David Lopez CSE 330
#Module 4. Used to compute batting averages

#! /usr/bin/env python
import sys, os, re

#check that user put in file path
if len(sys.argv) < 2:
	sys.exit(" Unrecognizable input.Please input the file path of the Cardinals season you want sorted")

#file to be opened
filename = sys.argv[1]

#filenotfound catch
if not os.path.exists(filename):
	sys.exit("Error: File %s not found" % sys.argv[1])

f = open(filename)
#3 dictionaries to store stats with player name
players_bats = dict()
players_hits = dict()
players_avg = dict()
#main loop, for each line of file, find name, bats and hits and assign them to appropriate dictionary
for line in f:
	string = line
	name_regex = re.compile(r"(((\w*)\s(\w*))\sbatted)\s(\d*)(?:\stimes\swith\s)(\d*)")
	name_ex = name_regex.match(string)
	if name_ex is not None:
		name = name_ex.group(2)
		bats = name_ex.group(5)
		hits = name_ex.group(6)
		if name not in players_bats:
			players_bats[name] = float(bats)
			players_hits[name] = float(hits)
		else:
			players_bats[name] += float(bats)
			players_hits[name] += float(hits)
#use bats and hits dict to compute batting averages
for player in players_bats:
	players_avg[player] = round((players_hits.get(player)/players_bats.get(player)),3)

#push avg dict to a list, sort it then print.
sorted_list = sorted(players_avg, key=players_avg.get, reverse = True)
for item in sorted_list:
	print "%s : %.3f" %(item, players_avg[item])