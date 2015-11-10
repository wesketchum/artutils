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
  
 private:

  std::string fAlgName;
  
  void PrintInfo();

  
};

#endif
