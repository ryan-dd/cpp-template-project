find_package(GTest REQUIRED)
include(GoogleTest) # for gtest cmake macros

add_executable(unit_tests 
  SampleTest.cpp
)

target_link_libraries(unit_tests 
  PRIVATE
    ${PROJECT_NAME}
    GTest::gtest
    GTest::gtest_main
)

set_project_warnings(unit_tests)
gtest_discover_tests(unit_tests)

