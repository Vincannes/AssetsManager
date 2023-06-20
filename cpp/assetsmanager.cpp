#include "assetsmanager.h"
#include "./ui_assetsmanager.h"

AssetsManager::AssetsManager(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::AssetsManager)
{
    ui->setupUi(this);
}

AssetsManager::~AssetsManager()
{
    delete ui;
}

