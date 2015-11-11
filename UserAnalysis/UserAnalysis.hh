/**
 * \file UserAnalysis.h
 *
 * 
 * \brief Little sample program for establishing a user analysis space.
 *
 * @author wketchum
*/

#ifndef TEST_USERANALYSIS_H
#define TEST_USERANALYSIS_H

#include <string>

#include "TTree.h"

namespace test{
  class UserAnalysis;
}

class test::UserAnalysis{
  
public:
  
  /// Default constructor
  UserAnalysis();

  /// Default destructor
  virtual ~UserAnalysis(){};

  void RunAnalysis();
  void SetupOutputTree(TTree*);
  
 private:

  std::string fAlgName;
  TTree*      fTree;
  
  void PrintInfo();

  
};

#endif
