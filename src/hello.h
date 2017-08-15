#ifndef _HELLO_H_
#define _HELLO_H_

#include <QString>
#include <QByteArray>
#include <QPainter>

class Hello {
  QString s;
public:
  Hello();
  void printme();
  void draw(long qp_ptr);
};

#endif
