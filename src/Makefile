C++ = g++

ifndef os
   os = LINUX
endif

ifndef arch
   arch = AMD64
endif

CCFLAGS = -Wall -D$(os) -finline-functions -g

ifeq ($(arch), IA32)
   CCFLAGS += -DIA32 #-mcpu=pentiumpro -march=pentiumpro -mmmx -msse
endif

ifeq ($(arch), POWERPC)
   CCFLAGS += -mcpu=powerpc
endif

ifeq ($(arch), IA64)
   CCFLAGS += -DIA64
endif

ifeq ($(arch), SPARC)
   CCFLAGS += -DSPARC
endif

LDFLAGS = -L../src -ludt -lstdc++ -lpthread -lm -lssl -lcrypto

ifeq ($(os), UNIX)
   LDFLAGS += -lsocket
endif

ifeq ($(os), OSX)
   LDFLAGS += -I/usr/local/opt/libudt/include/udt -L/usr/local/opt/libudt/lib
   CCFLAGS += -I/usr/local/opt/libudt/include/udt

   LDFLAGS += -I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib
   CCFLAGS += -I/usr/local/opt/openssl/include
endif

ifeq ($(os), SUNOS)
   LDFLAGS += -lrt -lsocket
endif

DIR = $(shell pwd)

APP = version.h udr

all: $(APP)

version.h:
	./version.sh

%.o: %.cpp
	$(C++) $(CCFLAGS) $< -c

udr: udr.o udr_threads.o udr_util.o udr_options.o
	$(C++) $^ -o $@ $(LDFLAGS)

clean:
	rm -f *.o $(APP)

install:
	export PATH=$(DIR):$$PATH
