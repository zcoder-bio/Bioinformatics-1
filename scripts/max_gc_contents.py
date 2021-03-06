#!/usr/bin/env python
import sys

from util import dna_stats
from util import parserUtil

if __name__ == "__main__":
    f = open(sys.argv[1])
    l = map(lambda a: a.strip(), f.readlines()) 
    parser = parserUtil.fastaParser(l)
    parser.parse()
    s = dna_stats.DNAMultiStats(parser.sequences, parser.names)
    (max_contents, max_name) = s.max_gc_contents()
    print max_name
    print max_contents * 100
