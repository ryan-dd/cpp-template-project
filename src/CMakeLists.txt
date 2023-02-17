add_library(${PROJECT_NAME}
  SampleClass.cpp
)

set_project_warnings(${PROJECT_NAME})

target_include_directories(${PROJECT_NAME} 
  PUBLIC 
    "$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>"
    "$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>"
  PRIVATE
    "$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include/${PROJECT_NAME}>"
)

# Add namespaced alias
set(namespace "${PROJECT_NAME}")
add_library("${namespace}::${PROJECT_NAME}" ALIAS "${PROJECT_NAME}")

# Generate CMake files for finding the package after installation
set(version_config_file "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake")
set(project_config_file "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake")
set(targets_export_filename "${PROJECT_NAME}Targets")

include(GNUInstallDirs)
set(cmake_config_install_dir "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}")

include(CMakePackageConfigHelpers)
write_basic_package_version_file( "${version_config_file}" COMPATIBILITY AnyNewerVersion)
configure_package_config_file(
  "${PROJECT_SOURCE_DIR}/cmake/Config.cmake.in" "${project_config_file}" 
  INSTALL_DESTINATION "${cmake_config_install_dir}")

# Install commands
install (TARGETS ${PROJECT_NAME}
  EXPORT "${targets_export_filename}"
  LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}"
  ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}"
  RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}"
  INCLUDES DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}")

install( DIRECTORY ${PROJECT_SOURCE_DIR}/include/
  DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}"
  FILES_MATCHING PATTERN "*.h")

install(
    FILES "${project_config_file}" "${version_config_file}"
    DESTINATION "${cmake_config_install_dir}"
)

install(
    EXPORT "${targets_export_filename}"
    NAMESPACE "${namespace}::"
    DESTINATION "${cmake_config_install_dir}"
)

