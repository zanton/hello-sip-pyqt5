#include "hello.h"

Hello::Hello() {
  s = QString("Hello World");
}

void
Hello::printme() {
  QByteArray ba = s.toLatin1();
  printf("%s from C++\n", ba.data());
}

void
Hello::draw(long qp_ptr) {
  QPainter * qp = reinterpret_cast<QPainter*>(qp_ptr);
  qp->setPen(Qt::blue);
  qp->setBrush(Qt::blue);
  qp->drawRect(100, 120, 50, 30);
  qp->drawText(200, 135, "I'm drawn in C++");
}
