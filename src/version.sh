#!/bin/bash
if [ -d ../.git ]; then git describe --tags > version ; fi;

version=`cat version`

printf "#ifndef VERSION_H\n#define VERSION_H\n" > version.h
#printf "extern const char * version = \"%s" "$version" >> version.h
printf "static const char * version = \"%s" "$version" >> version.h
printf "\";\n#endif" >> version.h
