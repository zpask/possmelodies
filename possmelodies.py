from itertools import product

normalize = raw_input("Do you want to normalize melodies (remove double sharps, etc)? y/n \n")
normalize = normalize.lower()

normalizedict = {
"C" : "C","D" : "D","E" : "E","F" : "F","G" : "G","A" : "A","B" : "B","C#" : "C#","D#" : "D#","E#" : "F","F#" : "F#","G#" : "G#","A#" : "A#","B#" : "C","Cb" : "Cb","Db" : "Db","Eb" : "Eb","Fb" : "E","Gb" : "Gb","Ab" : "Ab","Bb" : "Bb",
"C##" : "D","D##" : "E","E##" : "F#","F##" : "G","G##" : "A","A##" : "B","B##" : "C#","Cbb" : "Bb","Dbb" : "C","Ebb" : "D","Fbb" : "Eb","Gbb" : "F",
"Abb" : "G","Bbb" : "A",
"C###" : "D#","D###" : "F","E###" : "G","F###" : "G#","G###" : "A#","A###" : "C","B###" : "D","Cbbb" : "A","Dbbb" : "B","Ebbb" : "Db","Fbbb" : "D","Gbbb" : "E","Abbb" : "Gb","Bbbb" : "Ab",
}

chordict = {
#naturals
"cmaj" : ["C", "E", "G"],
"dmaj" : ["D", "F#", "A"],
"emaj" : ["E", "G#", "B"],
"fmaj" : ["F", "A", "C"],
"gmaj" : ["G", "B", "D"],
"amaj" : ["A", "C#", "E"],
"bmaj" : ["B", "D#", "F#"],

"cmin" : ["C", "Eb", "G"],
"dmin" : ["D", "F", "A"],
"emin" : ["E", "G", "B"],
"fmin" : ["F", "Ab", "C"],
"gmin" : ["G", "Bb", "D"],
"amin" : ["A", "C", "E"],
"bmin" : ["B", "D", "F#"],

"cdim" : ["C", "Eb", "Gb"],
"ddim" : ["D", "F", "Ab"],
"edim" : ["E", "G", "Bb"],
"fdim" : ["F", "Ab", "Cb"],
"gdim" : ["G", "Bb", "Db"],
"adim" : ["A", "C", "Eb"],
"bdim" : ["B", "D", "F"],

"caug" : ["C", "E", "G#"],
"daug" : ["D", "F#", "A#"],
"eaug" : ["E", "G#", "B#"],
"faug" : ["F", "A", "C#"],
"gaug" : ["G", "B", "D#"],
"aaug" : ["A", "C#", "E#"],
"baug" : ["B", "D#", "F##"],

"csus2": ["C", "D", "G"],
"dsus2": ["D", "E", "A"],
"esus2": ["E", "F#", "B"],
"fsus2": ["F", "G", "C"],
"gsus2": ["G", "A", "D"],
"asus2": ["A", "B", "E"],
"bsus2": ["B", "C#", "F#"],

"csus4": ["C", "F", "G"],
"dsus4": ["D", "G", "A"],
"esus4": ["E", "A", "B"],
"fsus4": ["F", "Bb", "C"],
"gsus4": ["G", "C", "D"],
"asus4": ["A", "D", "E"],
"bsus4": ["B", "E", "F#"],

"cmaj7" : ["C", "E", "G", "B"],
"dmaj7" : ["D", "F#", "A", "C#"],
"emaj7" : ["E", "G#", "B", "D#"],
"fmaj7" : ["F", "A", "C", "E"],
"gmaj7" : ["G", "B", "D", "F#"],
"amaj7" : ["A", "C#", "E", "G#"],
"bmaj7" : ["B", "D#", "F#", "A#"],

"cmin7" : ["C", "Eb", "G", "Bb"],
"dmin7" : ["D", "F", "A", "C"],
"emin7" : ["E", "G", "B", "D"],
"fmin7" : ["F", "Ab", "C", "Eb"],
"gmin7" : ["G", "Bb", "D", "F"],
"amin7" : ["A", "C", "E", "G"],
"bmin7" : ["B", "D", "F#", "A"],

"c7" : ["C", "E", "G", "Bb"],
"d7" : ["D", "F#", "A", "C"],
"e7" : ["E", "G#", "B", "D"],
"f7" : ["F", "A", "C", "Eb"],
"g7" : ["G", "B", "D", "F"],
"a7" : ["A", "C#", "E", "G"],
"b7" : ["B", "D#", "F#", "A"],

"cdim7" : ["C", "Eb", "Gb", "Bbb"],
"ddim7" : ["D", "F", "Ab", "Cb"],
"edim7" : ["E", "G", "Bb", "Db"],
"fdim7" : ["F", "Ab", "Cb", "Ebb"],
"gdim7" : ["G", "Bb", "Db", "Fb"],
"adim7" : ["A", "C", "Eb", "Gb"],
"bdim7" : ["B", "D", "F", "Ab"],

"c-7" : ["C", "Eb", "Gb", "Bb"],
"d-7" : ["D", "F", "Ab", "C"],
"e-7" : ["E", "G", "Bb", "D"],
"f-7" : ["F", "Ab", "Cb", "Eb"],
"g-7" : ["G", "Bb", "Db", "F"],
"a-7" : ["A", "C", "Eb", "G"],
"b-7" : ["B", "D", "F", "A"],

"cmm7" : ["C", "Eb", "G", "B"],
"dmm7" : ["D", "F", "A", "C#"],
"emm7" : ["E", "G", "B", "D#"],
"fmm7" : ["F", "Ab", "C", "E"],
"gmm7" : ["G", "Bb", "D", "F#"],
"amm7" : ["A", "C", "E", "G#"],
"bmm7" : ["B", "D", "F#", "A#"],

"caug7" : ["C", "E", "G#", "B"],
"daug7" : ["D", "F#", "A#", "C#"],
"eaug7" : ["E", "G#", "B#", "D#"],
"faug7" : ["F", "A", "C#", "E"],
"gaug7" : ["G", "B", "D#", "F#"],
"aaug7" : ["A", "C#", "E#", "G#"],
"baug7" : ["B", "D#", "F##", "A#"],

#sharps
"c#maj" : ["C#", "E#", "G#"],
"d#maj" : ["D#", "F##", "A#"],
"e#maj" : ["E#", "G##", "B#"],
"f#maj" : ["F#", "A#", "C#"],
"g#maj" : ["G#", "B#", "D#"],
"a#maj" : ["A#", "C##", "E#"],
"b#maj" : ["B#", "D##", "F##"],

"c#min" : ["C#", "E", "G#"],
"d#min" : ["D#", "F#", "A#"],
"e#min" : ["E#", "G#", "B#"],
"f#min" : ["F#", "A", "C#"],
"g#min" : ["G#", "B", "D#"],
"a#min" : ["A#", "C#", "E#"],
"b#min" : ["B#", "D#", "F##"],

"c#dim" : ["C#", "E", "G"],
"d#dim" : ["D#", "F#", "A"],
"e#dim" : ["E#", "G#", "B"],
"f#dim" : ["F#", "A", "C"],
"g#dim" : ["G#", "B", "D"],
"a#dim" : ["A#", "C#", "E"],
"b#dim" : ["B#", "D#", "F#"],

"c#aug" : ["C#", "E#", "G##"],
"d#aug" : ["D#", "F##", "A##"],
"e#aug" : ["E#", "G##", "B##"],
"f#aug" : ["F#", "A#", "C##"],
"g#aug" : ["G#", "B#", "D##"],
"a#aug" : ["A#", "C##", "E##"],
"b#aug" : ["B#", "D##", "F###"],

"c#sus2": ["C#", "D#", "G#"],
"d#sus2": ["D#", "E#", "A#"],
"e#sus2": ["E#", "F##", "B#"],
"f#sus2": ["F#", "G#", "C#"],
"g#sus2": ["G#", "A#", "D#"],
"a#sus2": ["A#", "B#", "E#"],
"b#sus2": ["B#", "C##", "F##"],

"c#sus4": ["C#", "F#", "G#"],
"d#sus4": ["D#", "G#", "A#"],
"e#sus4": ["E#", "A#", "B#"],
"f#sus4": ["F#", "B", "C#"],
"g#sus4": ["G#", "C#", "D#"],
"a#sus4": ["A#", "D#", "E#"],
"b#sus4": ["B#", "E#", "F##"],

"c#maj7" : ["C#", "E#", "G#", "B#"],
"d#maj7" : ["D#", "F##", "A#", "C##"],
"e#maj7" : ["E#", "G##", "B#", "D##"],
"f#maj7" : ["F#", "A#", "C#", "E#"],
"g#maj7" : ["G#", "B#", "D#", "F##"],
"a#maj7" : ["A#", "C##", "E#", "G##"],
"b#maj7" : ["B#", "D##", "F##", "A##"],

"c#min7" : ["C#", "E", "G#", "B"],
"d#min7" : ["D#", "F#", "A#", "C#"],
"e#min7" : ["E#", "G#", "B#", "D#"],
"f#min7" : ["F#", "A", "C#", "E"],
"g#min7" : ["G#", "B", "D#", "F#"],
"a#min7" : ["A#", "C#", "E#", "G#"],
"b#min7" : ["B#", "D#", "F##", "A#"],

"c#7" : ["C#", "E#", "G#", "B"],
"d#7" : ["D#", "F##", "A#", "C#"],
"e#7" : ["E#", "G##", "B#", "D#"],
"f#7" : ["F#", "A#", "C#", "E"],
"g#7" : ["G#", "B#", "D#", "F#"],
"a#7" : ["A#", "C##", "E#", "G#"],
"b#7" : ["B#", "D##", "F##", "A#"],

"c#dim7" : ["C#", "E", "G", "Bb"],
"d#dim7" : ["D#", "F#", "A", "C"],
"e#dim7" : ["E#", "G#", "B", "D"],
"f#dim7" : ["F#", "A", "C", "Eb"],
"g#dim7" : ["G#", "B", "D", "F"],
"a#dim7" : ["A#", "C#", "E", "G"],
"b#dim7" : ["B#", "D#", "F#", "A"],

"c#-7" : ["C#", "E", "G", "B"],
"d#-7" : ["D#", "F#", "A", "C#"],
"e#-7" : ["E#", "G#", "B", "D#"],
"f#-7" : ["F#", "A", "C", "E"],
"g#-7" : ["G#", "B", "D", "F#"],
"a#-7" : ["A#", "C#", "E", "G#"],
"b#-7" : ["B#", "D#", "F#", "A#"],

"c#mm7" : ["C#", "E", "G#", "B#"],
"d#mm7" : ["D#", "F#", "A#", "C##"],
"e#mm7" : ["E#", "G#", "B#", "D##"],
"f#mm7" : ["F#", "A", "C#", "E#"],
"g#mm7" : ["G#", "B", "D#", "F##"],
"a#mm7" : ["A#", "C#", "E#", "G##"],
"b#mm7" : ["B#", "D#", "F##", "A##"],

"c#aug7" : ["C#", "E#", "G##", "B#"],
"d#aug7" : ["D#", "F##", "A##", "C##"],
"e#aug7" : ["E#", "G##", "B##", "D##"],
"f#aug7" : ["F#", "A#", "C##", "E#"],
"g#aug7" : ["G#", "B#", "D##", "F##"],
"a#aug7" : ["A#", "C##", "E##", "G##"],
"b#aug7" : ["B#", "D##", "F###", "A##"],

#flats
"cbmaj" : ["Cb", "Eb", "Gb"],
"dbmaj" : ["Db", "F", "Ab"],
"ebmaj" : ["Eb", "G", "Bb"],
"fbmaj" : ["Fb", "Ab", "Cb"],
"gbmaj" : ["Gb", "Bb", "Db"],
"abmaj" : ["Ab", "C", "Eb"],
"bbmaj" : ["Bb", "D", "F"],

"cbmin" : ["Cb", "Ebb", "Gb"],
"dbmin" : ["Db", "Fb", "Ab"],
"ebmin" : ["Eb", "Gb", "Bb"],
"fbmin" : ["Fb", "Abb", "Cb"],
"gbmin" : ["Gb", "Bbb", "Db"],
"abmin" : ["Ab", "Cb", "Eb"],
"bbmin" : ["Bb", "Db", "F"],

"cbdim" : ["Cb", "Ebb", "Gbb"],
"dbdim" : ["Db", "Fb", "Abb"],
"ebdim" : ["Eb", "Gb", "Bbb"],
"fbdim" : ["Fb", "Abb", "Cbb"],
"gbdim" : ["Gb", "Bbb", "Dbb"],
"abdim" : ["Ab", "Cb", "Ebb"],
"bbdim" : ["Bb", "Db", "Fb"],

"cbaug" : ["Cb", "Eb", "G"],
"dbaug" : ["Db", "F", "A"],
"ebaug" : ["Eb", "G", "B"],
"fbaug" : ["Fb", "Ab", "C"],
"gbaug" : ["Gb", "Bb", "D"],
"abaug" : ["Ab", "C", "E"],
"bbaug" : ["Bb", "D", "F#"],

"cbsus2": ["Cb", "Db", "Gb"],
"dbsus2": ["Db", "Eb", "Ab"],
"ebsus2": ["Eb", "F", "Bb"],
"fbsus2": ["Fb", "Gb", "Cb"],
"gbsus2": ["Gb", "Ab", "Db"],
"absus2": ["Ab", "Bb", "Eb"],
"bbsus2": ["Bb", "C", "F"],

"cbsus4": ["Cb", "Fb", "Gb"],
"dbsus4": ["Db", "Gb", "Ab"],
"ebsus4": ["Eb", "Ab", "Bb"],
"fbsus4": ["Fb", "Bbb", "Cb"],
"gbsus4": ["Gb", "Cb", "Db"],
"absus4": ["Ab", "Db", "Eb"],
"bbsus4": ["Bb", "Eb", "F"],

"cbmaj7" : ["Cb", "Eb", "Gb", "Bb"],
"dbmaj7" : ["Db", "F", "Ab", "Cb"],
"ebmaj7" : ["Eb", "G", "Bb", "D"],
"fbmaj7" : ["Fb", "Ab", "Cb", "Eb"],
"gbmaj7" : ["Gb", "Bb", "Db", "F"],
"abmaj7" : ["Ab", "C", "Eb", "G"],
"bbmaj7" : ["Bb", "D", "F", "A"],

"cbmin7" : ["Cb", "Ebb", "Gb", "Bbb"],
"dbmin7" : ["Db", "Fb", "Ab", "Cb"],
"ebmin7" : ["Eb", "Gb", "Bb", "Db"],
"fbmin7" : ["Fb", "Abb", "Cb", "Ebb"],
"gbmin7" : ["Gb", "Bbb", "Db", "Fb"],
"abmin7" : ["Ab", "Cb", "Eb", "Gb"],
"bbmin7" : ["Bb", "Db", "F", "Ab"],

"cb7" : ["Cb", "Eb", "Gb", "Bbb"],
"db7" : ["Db", "F", "Ab", "Cb"],
"eb7" : ["Eb", "G", "Bb", "Db"],
"fb7" : ["Fb", "Ab", "Cb", "Ebb"],
"gb7" : ["Gb", "Bb", "Db", "Fb"],
"ab7" : ["Ab", "C", "Eb", "Gb"],
"bb7" : ["Bb", "D", "F", "Ab"],

"cbdim7" : ["Cb", "Ebb", "Gbb", "Bbbb"],
"dbdim7" : ["Db", "Fb", "Abb", "Cbb"],
"ebdim7" : ["Eb", "Gb", "Bbb", "Dbb"],
"fbdim7" : ["Fb", "Abb", "Cbb", "Ebbb"],
"gbdim7" : ["Gb", "Bbb", "Dbb", "Fbb"],
"abdim7" : ["Ab", "Cb", "Ebb", "Gbb"],
"bbdim7" : ["Bb", "Db", "Fb", "Abb"],

"cb-7" : ["Cb", "Ebb", "Gbb", "Bbb"],
"db-7" : ["Db", "Fb", "Abb", "Cb"],
"eb-7" : ["Eb", "Gb", "Bbb", "Db"],
"fb-7" : ["Fb", "Abb", "Cbb", "Ebb"],
"gb-7" : ["Gb", "Bbb", "Dbb", "Fb"],
"ab-7" : ["Ab", "Cb", "Ebb", "Gb"],
"bb-7" : ["Bb", "Db", "Fb", "Ab"],

"cbmm7" : ["Cb", "Ebb", "Gb", "Bb"],
"dbmm7" : ["Db", "Fb", "Ab", "C"],
"ebmm7" : ["Eb", "Gb", "Bb", "D"],
"fbmm7" : ["Fb", "Abb", "Cb", "Eb"],
"gbmm7" : ["Gb", "Bbb", "Db", "F"],
"abmm7" : ["Ab", "Cb", "Eb", "G"],
"bbmm7" : ["Bb", "Db", "F", "A"],

"cbaug7" : ["Cb", "Eb", "G", "Bb"],
"dbaug7" : ["Db", "F", "A", "C"],
"ebaug7" : ["Eb", "G", "B", "D"],
"fbaug7" : ["Fb", "Ab", "C", "Eb"],
"gbaug7" : ["Gb", "Bb", "D", "F"],
"abaug7" : ["Ab", "C", "E", "G"],
"bbaug7" : ["Bb", "D", "F#", "A"],
}

while True:
	response = raw_input("Enter progression. Type 'help' for more info, type 'quit' to quit. \n")
	response = response.lower()
	progression = []
	result = []
	
	if response == "quit":
		break
	if response == "help":
		print ""
		print "separate chords by space"
		print "for c major, type cmaj"
		print "for c minor, type cmin"
		print "for c diminished, type cdim"
		print "for c augmented, type caug"
		print "for c suspended 2, type csus2"
		print "for c suspended 4, type csus4"
		print "for c major seventh, type cmaj7"
		print "for c minor seventh, type cmin7"
		print "for c dominant seventh, type c7"
		print "for c diminished seventh, type cdim7"
		print "for c half diminished seventh, type c-7"
		print "for c minor major, type cmm7"
		print "for c augmented major, type caug7"
		print "for c sharp major, type c#maj"
		print "for c flat major, type cbmaj"
		print "don't use double sharps or double flats"
		print ""
	else:
		for word in response.split():
			progression.append(word)
		for item in progression:
			result.append(chordict[item])
		if normalize == "y":
			for item in result:
				for number in range(0, len(item)):
					item[number] = normalizedict[item[number]]
		actualresult = list(product(*result))
		for item in actualresult:
			print item
