# CMakeList.txt : CMake project for Trading212Desk, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.8)

project ("trading212-desk")

# Set C++ version
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Set Qt path
list(APPEND CMAKE_PREFIX_PATH "C:/Qt/6.1.2/msvc2019_64")

# Set Qt Auto MOC, RCC, & UIC
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

# Add source to this project's executable.
add_executable(
	Trading212Desk
	resources.qrc
	"src/main.cpp"
	"src/network/dns_over_https.cpp"
	"src/network/net_request.cpp"
	"src/network/dns_entry.cpp"
)

# Add Qt library files
find_package(Qt6 COMPONENTS Core Quick Widgets REQUIRED)
target_link_libraries(Trading212Desk Qt6::Core Qt6::Quick Qt6::Widgets)