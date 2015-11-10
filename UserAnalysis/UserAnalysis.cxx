#ifndef TEST_USERANALYSIS_CXX
#define TEST_USERANALYSIS_CXX

#include "UserAnalysis.hh"
#include <iostream>

test::UserAnalysis::UserAnalysis()
  : fAlgName("UserAnalysis")
{}

void test::UserAnalysis::RunAnalysis(){
  PrintInfo();
}

void test::UserAnalysis::PrintInfo(){
  std::cout << "\tThis is a ub_UserAnalysis class called " << fAlgName << std::endl;
}

#endif
