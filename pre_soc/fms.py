import argparse
from utilities import *
from ed import edit_distance

parser = argparse.ArgumentParser(description='Provides FMS of strings S and S1')
parser.add_argument('S', help='First Sentence')
parser.add_argument('S1', help='Second Sentence')
args = parser.parse_args()

#Applying some preprocessing on input data.
s_sentence = preprocess(args.S)
s1_sentence = preprocess(args.S1)

#Testing Input data
assertion(s_sentence != "", "S should be there.\nSee -h for help")
assertion(s1_sentence != "", "S1 should be there.\nSee -h for help")

sl = tuple(s_sentence.split())
sl1 = tuple(s1_sentence.split())

#Find Edit Distance
ed = edit_distance(sl, sl1)*1.0

ll = len(sl) if len(sl) > len(sl1) else len(sl1)

fms = 1.0 - (ed/ll)

print ('%.02f' %(fms*100))