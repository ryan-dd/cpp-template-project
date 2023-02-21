# cpp-template-project

[![Build Status](https://github.com/ryan-dd/cpp-template-project/actions/workflows/build.yml/badge.svg)](https://github.com/ryan-dd/cpp-template-project/actions/workflows/build.yml)
[![CodeQL Status](https://github.com/ryan-dd/cpp-template-project/actions/workflows/codeql.yml/badge.svg)](https://github.com/ryan-dd/cpp-template-project/actions/workflows/codeql.yml)

A template repo to set up a project for a C++ library. Targeted for Linux or MacOS with gcc or clang.

# Features

- Includes robust project warnings for gcc and clang
- Sanitizer options
- Clang Tidy, cppcheck, and include-what-you-use support
- Autogenerates documentation from the source code via Doxygen
- Tests with gTest
- Generates code coverage report from tests
- Able to be included in a cmake project as a submodule, or with cmake FetchContent
- After system installation, can be found in a cmake project with `find_package`
- Optionally uses conan for dependency management, with ability to create conan package for the library from build artifacts.

# Dependencies

Requires [CMake](https://cmake.org) to build. 

For installing dependencies, either [Conan](https://conan.io) or your favorite system package manager can be used.

For generating coverage reports, gcov and gcovr must be installed on the system.

The static analyzers must also be installed to use them.

# Build

## With conan 

```bash
conan install . -if build
conan build . -if build
```

## Without conan

Before building, install dependencies listed in `build_requirements` and `requirements` methods of conanfile.py.

```bash
cmake -S . -B build
cmake --build build
```

# Misc commands

Run tests and generate code coverage reports from tests:

```bash
cmake --build build --target coverage
```

Install library on system after building:

```bash
cmake --install build
```

# Contributing

Contributions that fix errata are much appreciated. Feel free to reach out to the author about any issues.
