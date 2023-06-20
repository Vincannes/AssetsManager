#ifndef NODEGRAPHWIDGET_H
#define NODEGRAPHWIDGET_H

#include <QGraphicsView>
#include <QObject>

class NodeGraphWidget : public QGraphicsView
{
    Q_OBJECT

public:
    NodeGraphWidget(QObject *parent = 0);

protected:
    void wheelEvent(QWheelEvent *event);

private slots:
    void setupMatrix();

private:
    int viewZoom;
    float zoom_in_factor;
    bool zoom_clamp;
    int zoom;
    int zoom_step;
    int zoom_range[2];

};
#endif // NODEGRAPHWIDGET_H
