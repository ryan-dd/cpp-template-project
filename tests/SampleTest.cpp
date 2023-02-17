#include <gtest/gtest.h>
#include "SampleProject/SampleClass.h"

TEST(SampleTest, doSomething)
{
  SampleClass::do_something();
  ASSERT_TRUE(true);
}

