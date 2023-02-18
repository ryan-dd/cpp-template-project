cmake_minimum_required(VERSION 3.21)

set(SampleProject_VERSION 1.0.0)

project(SampleProject 
  VERSION ${SampleProject_VERSION} 
  DESCRIPTION "A sample template cmake project" 
  LANGUAGES CXX)

if(PROJECT_IS_TOP_LEVEL) 
  # Only use these options if this CMakeLists.txt is not being used by another project 
  set(CMAKE_CXX_STANDARD 20)
  set(CMAKE_CXX_STANDARD_REQUIRED ON)
  set(CMAKE_POSITION_INDEPENDENT_CODE ON)
  set(CMAKE_CXX_EXTENSIONS OFF)
  set(CMAKE_EXPORT_COMPILE_COMMANDS ON) # for LSP support
  set(CMAKE_FIND_PACKAGE_PREFER_CONFIG ON)

  if(NOT DEFINED SampleProject_BUILD_TESTS)
    set(SampleProject_BUILD_TESTS ON)
  endif()

  if(NOT DEFINED SampleProject_BUILD_DOCS)
    set(SampleProject_BUILD_DOCS ON)
  endif()
endif()

# Add cmake utility functions
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
include(CompilerWarnings)
include(StaticAnalyzers)
include(Sanitizers)

if (CMAKE_BUILD_TYPE STREQUAL "Debug" AND SampleProject_BUILD_TESTS)
  # Only do code coverage in debug with tests
  include(CodeCoverage)
  append_coverage_compiler_flags()
endif()

add_subdirectory(src)

if (SampleProject_BUILD_TESTS)
  include(CTest)
  enable_testing()
  add_subdirectory(tests)
endif()

if (SampleProject_BUILD_DOCS)
  include(Doxygen)
  set(DOXYGEN_THEME "awesome-sidebar")
  enable_doxygen("${DOXYGEN_THEME}")
endif()

