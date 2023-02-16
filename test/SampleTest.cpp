#include <gtest/gtest.h>
#include "SampleClass.h"

TEST(SampleTest, doSomething)
{
  SampleClass::do_something();
  ASSERT_TRUE(true);
}

