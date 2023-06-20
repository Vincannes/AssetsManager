#ifndef ASSETSMANAGER_H
#define ASSETSMANAGER_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class AssetsManager; }
QT_END_NAMESPACE

class AssetsManager : public QMainWindow
{
    Q_OBJECT

public:
    AssetsManager(QWidget *parent = nullptr);
    ~AssetsManager();

private:
    Ui::AssetsManager *ui;
};
#endif // ASSETSMANAGER_H
