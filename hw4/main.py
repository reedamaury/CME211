import sys

import truss

inputdir_joint = sys.arg[0]
inputdir_beam =  sys.arg[1]
outputfile = sys.arg[2]


if len(sys.argv) < 2:
    print('Usage:')
    print('  python3 {} <joints data directory> <beams data directory> <optional plot output file>'.format(sys.argv[0]))
    sys.exit(0)


if len(outputfile) > 0:
    truss.Truss.PlotGeometry(outputfile)


try:
    a = truss.Truss(inputdir_joint, inputdir_beam)
except RuntimeError as e:
    print('ERROR: {}'.format(e))
    sys.exit(2)

print(a)