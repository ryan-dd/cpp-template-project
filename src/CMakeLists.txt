### Add library ###
set(SRCS SampleClass.cpp)

if (SampleProject_BUILD_SHARED_LIBS)
  add_library(${PROJECT_NAME} SHARED ${SRCS})
else()
  # Either build static (default) or allow cmake var BUILD_SHARED_LIBS to determine build type
  add_library(${PROJECT_NAME} ${SRCS})
endif()

target_include_directories(${PROJECT_NAME} 
  PUBLIC 
    "$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>"
    "$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>"
  PRIVATE
    "$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include/${PROJECT_NAME}>"
)

find_package(spdlog REQUIRED)
target_link_libraries(${PROJECT_NAME} PRIVATE spdlog::spdlog)

get_target_property(target_type ${PROJECT_NAME} TYPE)
if (target_type STREQUAL STATIC_LIBRARY AND SampleProject_fPIC)
  set_property(TARGET ${PROJECT_NAME} PROPERTY POSITION_INDEPENDENT_CODE ON)
endif()

# Require consumers to use C++20
target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_20)

set_project_warnings(${PROJECT_NAME})

if (SampleProject_ENABLE_SANITIZERS)
  enable_sanitizers(${PROJECT_NAME}
    SampleProject_ENABLE_SANITIZER_ADDRESS
    SampleProject_ENABLE_SANITIZER_LEAK
    SampleProject_ENABLE_SANITIZER_UNDEFINED_BEHAVIOR
    SampleProject_ENABLE_SANITIZER_THREAD
    SampleProject_ENABLE_SANITIZER_MEMORY)
endif()

# Add namespaced alias
set(namespace "${PROJECT_NAME}")
add_library("${namespace}::${PROJECT_NAME}" ALIAS "${PROJECT_NAME}")

### Generate CMake files for finding the package after installation ###
set(version_config_file "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake")
set(project_config_file "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake")
set(targets_export_filename "${PROJECT_NAME}Targets")

include(GNUInstallDirs)
set(config_install_dir "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}")

include(CMakePackageConfigHelpers)
write_basic_package_version_file( "${version_config_file}" COMPATIBILITY SameMajorVersion)
configure_package_config_file(
  "${PROJECT_SOURCE_DIR}/cmake/Config.cmake.in" "${project_config_file}" 
  INSTALL_DESTINATION "${config_install_dir}")

# Install commands
install (TARGETS ${PROJECT_NAME}
  EXPORT "${targets_export_filename}"
  LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}"
  ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}"
  RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}"
  INCLUDES DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}")

install( DIRECTORY ${PROJECT_SOURCE_DIR}/include/
  DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}"
  FILES_MATCHING 
  PATTERN "*.h"
  PATTERN "*.hpp"
)

install(
    FILES "${project_config_file}" "${version_config_file}"
    DESTINATION "${config_install_dir}"
)

install(
    EXPORT "${targets_export_filename}"
    NAMESPACE "${namespace}::"
    DESTINATION "${config_install_dir}"
)

