# CMakeList.txt : CMake project for Trading212Desk, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.12)

project ("trading212-desk")

# Set project's path
set(PROJECT_SOURCE_DIR ${PROJECT_SOURCE_DIR}/src)

# Set C++ version
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Set Qt path
list(APPEND CMAKE_PREFIX_PATH "C:/Qt/6.2.0/msvc2019_64")

# Set Qt Auto MOC, RCC, & UIC
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

# Collect all .cpp files
file(GLOB_RECURSE CPP_FILES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} CONFIGURE_DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp ${CMAKE_CURRENT_SOURCE_DIR}/src/*.h)

message(${PROJECT_SOURCE_DIR})
message("${CPP_FILES}")

# Add source to this project's executable.
add_executable(
	Trading212Desk
	resources.qrc
	${CPP_FILES}
)

#	"src/main.cpp"
#	"src/network/dns_over_https.cpp"
#	"src/network/net_request.cpp"
#	"src/network/dns_entry.cpp"
#  "src/views/main_view.cpp" "src/views/login_view.h" "src/views/login_vew.cpp")

# Add Qt library files
find_package(Qt6 COMPONENTS Core Quick Widgets REQUIRED)
target_link_libraries(Trading212Desk Qt6::Core Qt6::Quick Qt6::Widgets)

target_include_directories(Trading212Desk PRIVATE ${PROJECT_SOURCE_DIR})