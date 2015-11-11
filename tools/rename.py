#!/usr/bin/python

import sys, argparse, os
from useful_info import *

parser = argparse.ArgumentParser(description='Rename UserAnalysis example')
parser.add_argument('name',metavar='<class name 1>',type=str, nargs=1,
                    help='New name for your analysis class (replaces UserAnalysis). Must follow C++ naming conventions.')
parser.add_argument('art_name',metavar='<class name 2>',type=str, nargs=1,
                    help='New name for your art::EDAnalyzer class (replaces UserAnalyzer). Must follow C++ naming conventions.')
parser.add_argument('namespace',metavar='<namespace>',type=str, nargs=1,
                    help='New namspace for this analysis class (replaces test). Must be all lower case, no punctuation.')
parser.add_argument('project',metavar='<project name>',type=str, nargs=1,
                    help='New name for this project (replaces ubuseranalysis). Must be all lower case, no punctuation.')

def CheckLowercase(word):
    for c in word[0]:
        if c.islower()!=True:
            return False
    return True
def CheckIsAlpha(word):
    return word[0].isalpha()
def CheckIfBeginsWithDigit(word):
    return (word[0][0].isdigit()==False)

def CheckName(args):
    if(CheckIfBeginsWithDigit(args.name)==False):
        print "New name for this analysis class must follow C++ naming conventions."
        return False
    return True
def CheckArtName(args):
    if(CheckIfBeginsWithDigit(args.art_name)==False):
        print "New name for this art::EDAnalyzer class must follow C++ naming conventions."
        return False
    return True
def CheckNamespace(args):
    if((CheckLowercase(args.namespace) and CheckIsAlpha(args.namespace))==False):
        print "New name for this namespace must be all lower case, no punctuation."
        return False
    return True
def CheckProject(args):
    if((CheckLowercase(args.namespace) and CheckIsAlpha(args.namespace))==False):
        print "New name for this project must be all lower case, no punctuation."
        return False
    return True

#http://stackoverflow.com/questions/4128144/replace-string-within-file-contents
def inplace_change(filename, old_string, new_string):
    print "Processing file "+ filename + " changing " + old_string + " to " + new_string
    s=open(filename).read()
    if old_string in s:
        #print 'Changing "{old_string}" to "{new_string}"'.format(**locals())
        s=s.replace(old_string, new_string)
        f=open(filename, 'w')
        f.write(s)
        f.flush()
        f.close()
    else:
        print 'No occurances of "{old_string}" found.'.format(**locals())    

if __name__=="__main__":
    args = parser.parse_args()

    if( args.name==args.art_name):
        sys.exit("Can't have two similar class names.")

    if( CheckName(args)==False or CheckArtName(args)==False or CheckNamespace(args)==False or CheckProject(args)==False ):
        sys.exit("Exiting.")
    
    my_class_name = args.name[0]
    my_analyzer_name = args.art_name[0]
    my_namespace = args.namespace[0]
    my_project = args.project[0]

    #CMake file first
    inplace_change("CMakeLists.txt","UserAnalysis",my_class_name)
    inplace_change("CMakeLists.txt","UserAnalyzer",my_analyzer_name)
    inplace_change("CMakeLists.txt","ubuseranalysis",my_project)

    #ups file
    inplace_change("ups/product_deps","ubuseranalysis",my_project)

    #now UserAnalysis directory
    inplace_change("UserAnalysis/CMakeLists.txt","UserAnalysis",my_class_name)
    inplace_change("UserAnalysis/UserAnalysis.hh","UserAnalysis",my_class_name)
    inplace_change("UserAnalysis/UserAnalysis.cxx","UserAnalysis",my_class_name)
    inplace_change("UserAnalysis/UserAnalysis.hh","test",my_namespace)
    inplace_change("UserAnalysis/UserAnalysis.cxx","test",my_namespace)
    os.rename("UserAnalysis/UserAnalysis.hh","UserAnalysis/"+my_class_name+".hh")
    os.rename("UserAnalysis/UserAnalysis.cxx","UserAnalysis/"+my_class_name+".cxx")
    os.rename("UserAnalysis",my_class_name)
            
    #now UserAnalyzer directory
    inplace_change("UserAnalyzer/CMakeLists.txt","UserAnalysis",my_class_name)
    inplace_change("UserAnalyzer/UserAnalyzer_module.cc","UserAnalysis",my_class_name)
    inplace_change("UserAnalyzer/UserAnalyzer_module.cc","UserAnalyzer",my_analyzer_name)
    inplace_change("UserAnalyzer/run_UserAnalyzer.fcl","UserAnalyzer",my_analyzer_name)
    inplace_change("UserAnalyzer/UserAnalyzer_module.cc","test",my_namespace)
    os.rename("UserAnalyzer/UserAnalyzer_module.cc","UserAnalyzer/"+my_analyzer_name+"_module.cc")
    os.rename("UserAnalyzer/run_UserAnalyzer.fcl","UserAnalyzer/run_"+my_analyzer_name+".fcl")
    os.rename("UserAnalyzer",my_analyzer_name)

    #top level CMake file
    inplace_change("../CMakeLists.txt","ubuseranalysis",my_project)

    PrintNewOriginRepoInstructions()
    PrintMoveProject(my_project)
    PrintBuildInstructions()
    
    #os.mkdir(my_class_name)
    #os.mkdir(my_class_name+"LArSoft")

    
