/********************************************************************************
** Form generated from reading UI file 'assetsmanager.ui'
**
** Created by: Qt User Interface Compiler version 6.5.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ASSETSMANAGER_H
#define UI_ASSETSMANAGER_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include "nodegraphwidget.h"

QT_BEGIN_NAMESPACE

class Ui_AssetsManager
{
public:
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    NodeGraphWidget *graphicsView;
    QVBoxLayout *verticalLayout;
    QListWidget *listWidget;
    QPushButton *pushButton;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *AssetsManager)
    {
        if (AssetsManager->objectName().isEmpty())
            AssetsManager->setObjectName("AssetsManager");
        AssetsManager->resize(800, 600);
        centralwidget = new QWidget(AssetsManager);
        centralwidget->setObjectName("centralwidget");
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setObjectName("gridLayout");
        graphicsView = new NodeGraphWidget(centralwidget);
        graphicsView->setObjectName("graphicsView");
        graphicsView->setMinimumSize(QSize(600, 0));
        graphicsView->setMaximumSize(QSize(600, 16777215));

        gridLayout->addWidget(graphicsView, 0, 0, 1, 1);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(0);
        verticalLayout->setObjectName("verticalLayout");
        verticalLayout->setSizeConstraint(QLayout::SetDefaultConstraint);
        listWidget = new QListWidget(centralwidget);
        listWidget->setObjectName("listWidget");
        listWidget->setMaximumSize(QSize(200, 16777215));

        verticalLayout->addWidget(listWidget);

        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName("pushButton");
        pushButton->setMaximumSize(QSize(200, 16777215));

        verticalLayout->addWidget(pushButton);


        gridLayout->addLayout(verticalLayout, 0, 1, 1, 1);

        AssetsManager->setCentralWidget(centralwidget);
        menubar = new QMenuBar(AssetsManager);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 800, 21));
        AssetsManager->setMenuBar(menubar);
        statusbar = new QStatusBar(AssetsManager);
        statusbar->setObjectName("statusbar");
        AssetsManager->setStatusBar(statusbar);

        retranslateUi(AssetsManager);

        QMetaObject::connectSlotsByName(AssetsManager);
    } // setupUi

    void retranslateUi(QMainWindow *AssetsManager)
    {
        AssetsManager->setWindowTitle(QCoreApplication::translate("AssetsManager", "AssetsManager", nullptr));
        pushButton->setText(QCoreApplication::translate("AssetsManager", "PushButton", nullptr));
    } // retranslateUi

};

namespace Ui {
    class AssetsManager: public Ui_AssetsManager {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ASSETSMANAGER_H
