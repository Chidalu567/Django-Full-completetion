import sys #import sys module

if len(sys.argv) !=4 or '--help' in sys.argv[1:]:
    print('Usage :file_name <arg1> <arg2> <arg3>',file=sys.stderr); #print error message
    sys.exit(1); #exit program
file=open(sys.argv[1]+'.txt','rb'); #open file for binary reading
'''This sys module helps in handling command line arguments'''