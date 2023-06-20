#include "nodegraphwidget.h"
#include <QDebug>
#include <QWheelEvent>
#include <qmath.h>

NodeGraphWidget::NodeGraphWidget(QObject *parent):
    QGraphicsView(),
    viewZoom(0)
{
    this->zoom_in_factor=1.25;
    this->zoom_clamp=false;
    this->zoom=10;
    this->zoom_step=1;
    this->zoom_range[0] = 0;
    this->zoom_range[1] = 10;
}

void NodeGraphWidget::wheelEvent(QWheelEvent *event)
{
    //viewZoom += (event->delta() / 40);
    //setupMatrix();
}

void NodeGraphWidget::setupMatrix()
{
//    qreal scale = qPow( qreal(2), viewZoom / qreal(50) );
//    QMatrix matrix;
//    matrix.scale(scale, scale);
//    setMatrix(matrix);
    update();
}
