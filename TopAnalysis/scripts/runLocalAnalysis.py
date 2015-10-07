import os
import sys
import optparse
import ROOT

def main():

    #configuration
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('-i', '--in',       dest='input',       help='input directory with files or single file',  default=None,       type='string')
    parser.add_option('-o', '--out',      dest='outDir',      help='output directory',                           default='analysis', type='string')
    parser.add_option(      '--ch',       dest='channel',     help='channel',                                    default=13,         type=int)
    parser.add_option(      '--charge',   dest='charge',      help='charge',                                     default=0,         type=int)
    (opt, args) = parser.parse_args()

    ROOT.AutoLibraryLoader.enable()
    ROOT.gSystem.Load('libTopLJets2015TopAnalysis.so')
    ROOT.gROOT.LoadMacro('src/ReadTree.cc+')
    from ROOT import ReadTree
    print ReadTree
    if '.root' in opt.input:
        ReadTree(opt.input,opt.outDir,opt.channel,opt.charge,1.0,False)
        

"""
for execution from another script
"""
if __name__ == "__main__":
    sys.exit(main())
