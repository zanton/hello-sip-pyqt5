%Module hello

%Import QtCore/QtCoremod.sip

class Hello {

%TypeHeaderCode
#include "../src/hello.h"
%End

public:
  Hello();
  void printme();
  void draw(long);
};
