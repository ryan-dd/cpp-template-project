cmake_minimum_required(VERSION 3.21)

set(SampleProject_VERSION 1.0.0)

project(SampleProject 
  VERSION ${SampleProject_VERSION} 
  DESCRIPTION "A sample template cmake project" 
  LANGUAGES CXX)

# Add path to cmake utility functions
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
include(CompilerWarnings)
include(Sanitizers)

if (PROJECT_IS_TOP_LEVEL) 
  # Only use these options if this project is not a subdirectory of another project 
  set(CMAKE_CXX_STANDARD 20)
  set(CMAKE_CXX_STANDARD_REQUIRED ON)
  set(CMAKE_CXX_EXTENSIONS OFF)
  set(CMAKE_EXPORT_COMPILE_COMMANDS ON) # for LSP support
  set(CMAKE_FIND_PACKAGE_PREFER_CONFIG ON)

  include(StaticAnalyzers)

  option(SampleProject_BUILD_TESTS "Enable building tests" ON)
  option(SampleProject_BUILD_DOCS "Enable building docs" ON)
  option(SampleProject_ENABLE_SANITIZERS "Enable Sanitizers" OFF)

  if (SampleProject_BUILD_TESTS AND CMAKE_BUILD_TYPE STREQUAL "Debug")
    option(SampleProject_ENABLE_COVERAGE "Enable coverage target for tests" ON)
  endif()

  if (SampleProject_ENABLE_SANITIZERS)
    # Default to address and UB sanitizers
    option(SampleProject_ENABLE_SANITIZER_ADDRESS "Enable address sanitizer" ON)
    option(SampleProject_ENABLE_SANITIZER_UNDEFINED_BEHAVIOR "Enable UB sanitizer" ON)
  endif()
endif()

if (SampleProject_BUILD_TESTS AND SampleProject_ENABLE_COVERAGE)
    include(CodeCoverage)
    append_coverage_compiler_flags()
    setup_target_for_coverage_gcovr_html(
        NAME coverage
        EXECUTABLE ctest -j
        DEPENDENCIES unit_tests
        BASE_DIRECTORY src
    )
endif()

option(SampleProject_BUILD_SHARED_LIBS "Build project libraries as shared libraries" OFF)
option(SampleProject_fPIC "Enable position independent code" ON)
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

