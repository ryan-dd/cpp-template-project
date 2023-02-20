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

if (SampleProject_ENABLE_SANITIZERS)
  enable_sanitizers(unit_tests
    SampleProject_ENABLE_SANITIZER_ADDRESS
    SampleProject_ENABLE_SANITIZER_LEAK
    SampleProject_ENABLE_SANITIZER_UNDEFINED_BEHAVIOR
    SampleProject_ENABLE_SANITIZER_THREAD
    SampleProject_ENABLE_SANITIZER_MEMORY)
endif()
