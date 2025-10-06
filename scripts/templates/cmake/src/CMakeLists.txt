# Define the shared library target
add_library(lib{{ELEMENT_NAME}} SHARED {{ELEMENT_NAME}}.cc)

# Add custom install commands for SST registration
add_custom_target(install_${PROJECT_NAME}
    COMMAND sst-register {{ELEMENT_NAME}} {{ELEMENT_NAME}}_LIBDIR=${CMAKE_CURRENT_BINARY_DIR}
    COMMAND sst-register SST_ELEMENT_SOURCE {{ELEMENT_NAME}}=${CMAKE_CURRENT_SOURCE_DIR}
    COMMAND sst-register SST_ELEMENT_TESTS {{ELEMENT_NAME}}=${CMAKE_CURRENT_SOURCE_DIR}/../tests
    COMMENT "Registering SST element {{ELEMENT_NAME}}"
)

# Add a clean target
add_custom_target(clean_${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E remove lib{{ELEMENT_NAME}}.so
    COMMENT "Cleaning up generated files"
)

# Ensure install and clean targets are available
add_dependencies(lib{{ELEMENT_NAME}} install_${PROJECT_NAME})
add_dependencies(install_${PROJECT_NAME} clean_${PROJECT_NAME})

install(TARGETS sstdata DESTINATION ${SST_ELEMENT_LIBRARY_LIBDIR})
install(CODE "execute_process(COMMAND sst-register sstdata sstdata_LIBDIR=${SST_ELEMENT_LIBRARY_LIBDIR})")
