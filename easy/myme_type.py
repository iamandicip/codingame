import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
mapping = {}
files = []

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mapping[ext.lower()] = mt
    
for i in range(q):
    fname = input()  # One file name per line.
    files.append(fname)
    
    try:
        idx = fname.rindex(".")
        
        try:
            ext = fname[idx + 1:]
            mime = mapping[ext.lower()]
            
        except KeyError:
            print("couldn't mime type for file ", fname, file=sys.stderr) 
            mime = "UNKNOWN"
        
    except ValueError:
        print("couldn't find '.' in ", fname, file=sys.stderr)
        mime = "UNKNOWN"
        
    print(mime)
    
# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.