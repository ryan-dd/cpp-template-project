find_package(GTest REQUIRED)

add_executable(unit_tests 
  SampleTest.cpp
)

target_link_libraries(unit_tests 
  PRIVATE
    ${PROJECT_NAME}
    GTest::gtest
    GTest::gtest_main
)

enable_sanitizers(unit_tests)
gtest_discover_tests(unit_tests)

