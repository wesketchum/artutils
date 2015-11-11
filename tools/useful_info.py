#!/usr/bin/python

def PrintNewOriginRepoInstructions():
    print "\n-----------------------------------------"
    print "\nTo point your repository at a new 'origin' repository:"
    print "git remote remove origin"
    print "git remote add origin <location_of_your_git_repo>\n"

def PrintMoveProject(my_project="myproject"):
    print "\n-----------------------------------------"
    print "\nTo move a project:"
    print "cd $MRB_SOURCE"
    print "mv ubuseranalysis "+my_project
    print "mrb uc"
    print "\n\n(note, do the last line if you just need to update what gets built,"
    print " based on what you have in your srcs area)\n"
        
def PrintBuildInstructions():
    print "\n-----------------------------------------"
    print "\nTo build cleanly, do the following:"
    print "cd $MRB_BUILDDIR"
    print "mrb z; mrbsetenv"
    print "mrb i -j4"
    print "mrbslp"
    print "\nTo build after this, without having having added new projects:"
    print "cd $MRB_BUILDDIR"
    print "make install -j8\n"
    print "\nAlternative mrb/make commandes using ninja:"
    print "mrb i --generator=ninja"
    print "ninja install\n"
        
    
if __name__=="__main__":
    PrintBuildInstructions()
    PrintNewOriginRepoInstructions()
    PrintMoveProject()
    print "\n"
