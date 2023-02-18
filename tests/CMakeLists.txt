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
enable_sanitizers(unit_tests)
gtest_discover_tests(unit_tests)

if (CMAKE_BUILD_TYPE STREQUAL "Debug")
  append_coverage_compiler_flags_to_target(unit_tests)
  setup_target_for_coverage_gcovr_html(
      NAME coverage # target name
      EXECUTABLE ctest -j
      DEPENDENCIES unit_tests
  )
endif()


