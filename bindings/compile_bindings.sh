c++ -O3 -shared -std=c++11 -fPIC    \
-I ../include                         \
-I lgmres ../lgmres.cpp             \
`python-config --cflags --ldflags` \
bindings.cpp -o LGMRES.so
