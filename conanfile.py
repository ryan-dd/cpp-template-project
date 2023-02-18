from conans import ConanFile, CMake, tools
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
import re
import os

class SampleProjectConan(ConanFile):
    name = "SampleProject"
    version = "1.0.0"
    url = "https://github.com/ryan-dd/cpp-template-project"
    license = "MIT"
    description = "C++ template project"
    settings = "os", "compiler", "arch", "build_type"
    generators = "CMakeToolchain", "CMakeDeps"

    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto"
    }

    options = {
        "build_tests": [True, False],
        "build_docs": [True, False],
        "build_shared_libs": [True, False]
        }

    default_options = {
        "build_tests": True,
        "build_docs": True,
        "build_shared_libs": False
        }

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables['SampleProject_BUILD_TESTS'] = self.options.build_tests
        tc.variables['SampleProject_BUILD_DOCS'] = self.options.build_docs
        tc.variables['SampleProject_BUILD_SHARED_LIBS'] = self.options.build_shared_libs
        tc.generate()

    def build_requirements(self):
        if(self.options.build_tests):
            self.test_requires("gtest/[>=1.8.1]")
        if(self.options.build_docs):
            self.tool_requires("doxygen/[>=1.9.1]")

    def requirements(self):
        self.requires("spdlog/[>=1.11.0]")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        tools.rmdir(os.path.join(self.package_folder, "lib", "cmake"))

    def package_info(self):
        self.cpp_info.libs.append("SampleProject")
