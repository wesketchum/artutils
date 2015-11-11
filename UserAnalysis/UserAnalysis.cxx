#ifndef TEST_USERANALYSIS_CXX
#define TEST_USERANALYSIS_CXX

#include "UserAnalysis.hh"
#include <iostream>

test::UserAnalysis::UserAnalysis()
  : fAlgName("UserAnalysis")
{}

void test::UserAnalysis::SetupOutputTree(TTree* tfs_tree){
  fTree = tfs_tree;

  std::string title = fAlgName + " Tree";
  fTree->SetObject(fTree->GetName(),title.c_str());
}

void test::UserAnalysis::RunAnalysis(){
  PrintInfo();
}

void test::UserAnalysis::PrintInfo(){
  std::cout << "\n================================== UserAnalysis ==========================" << std::endl;
  std::cout << "This is a ub_UserAnalysis class called " << fAlgName << std::endl;
  std::cout << "\tThere is an output tree called "
	    << fTree->GetName() << " (" << fTree->GetTitle() << ")" << std::endl;
  std::cout << "==========================================================================\n" << std::endl;
}

#endif
