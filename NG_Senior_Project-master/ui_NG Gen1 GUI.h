/********************************************************************************
** Form generated from reading UI file 'NG Gen1 GUIz87516.ui'
**
** Created by: Qt User Interface Compiler version 5.9.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef NG_20_GEN1_20_GUIZ87516_H
#define NG_20_GEN1_20_GUIZ87516_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QLabel *cTempLabel;
    QLCDNumber *currentTemp;
    QPushButton *alertsButton;
    QPushButton *emergencyStop;
    QToolButton *dataButton;
    QToolButton *settingsButton;
    QLabel *dtempLabel;
    QLCDNumber *desiredTemp;
    QDoubleSpinBox *TempSet;
    QDialogButtonBox *tempSetButton;
    QButtonGroup *toolbarGroup;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(498, 276);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        MainWindow->setAutoFillBackground(true);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        cTempLabel = new QLabel(centralwidget);
        cTempLabel->setObjectName(QStringLiteral("cTempLabel"));
        cTempLabel->setGeometry(QRect(280, 9, 181, 21));
        QFont font;
        font.setPointSize(16);
        font.setBold(true);
        font.setUnderline(false);
        font.setWeight(75);
        cTempLabel->setFont(font);
        currentTemp = new QLCDNumber(centralwidget);
        currentTemp->setObjectName(QStringLiteral("currentTemp"));
        currentTemp->setGeometry(QRect(280, 30, 181, 81));
        QFont font1;
        font1.setBold(false);
        font1.setWeight(50);
        currentTemp->setFont(font1);
        currentTemp->setAutoFillBackground(true);
        currentTemp->setFrameShadow(QFrame::Plain);
        currentTemp->setLineWidth(3);
        alertsButton = new QPushButton(centralwidget);
        toolbarGroup = new QButtonGroup(MainWindow);
        toolbarGroup->setObjectName(QStringLiteral("toolbarGroup"));
        toolbarGroup->addButton(alertsButton);
        alertsButton->setObjectName(QStringLiteral("alertsButton"));
        alertsButton->setGeometry(QRect(170, 30, 71, 21));
        QFont font2;
        font2.setPointSize(16);
        font2.setBold(false);
        font2.setItalic(false);
        font2.setUnderline(false);
        font2.setWeight(50);
        font2.setStrikeOut(false);
        alertsButton->setFont(font2);
        alertsButton->setIconSize(QSize(20, 20));
        emergencyStop = new QPushButton(centralwidget);
        emergencyStop->setObjectName(QStringLiteral("emergencyStop"));
        emergencyStop->setGeometry(QRect(50, 210, 191, 31));
        dataButton = new QToolButton(centralwidget);
        toolbarGroup->addButton(dataButton);
        dataButton->setObjectName(QStringLiteral("dataButton"));
        dataButton->setGeometry(QRect(110, 30, 61, 21));
        QFont font3;
        font3.setPointSize(16);
        dataButton->setFont(font3);
        settingsButton = new QToolButton(centralwidget);
        toolbarGroup->addButton(settingsButton);
        settingsButton->setObjectName(QStringLiteral("settingsButton"));
        settingsButton->setGeometry(QRect(30, 30, 81, 21));
        settingsButton->setFont(font3);
        dtempLabel = new QLabel(centralwidget);
        dtempLabel->setObjectName(QStringLiteral("dtempLabel"));
        dtempLabel->setGeometry(QRect(280, 149, 181, 21));
        dtempLabel->setFont(font);
        desiredTemp = new QLCDNumber(centralwidget);
        desiredTemp->setObjectName(QStringLiteral("desiredTemp"));
        desiredTemp->setGeometry(QRect(280, 170, 181, 81));
        desiredTemp->setFont(font1);
        desiredTemp->setAutoFillBackground(true);
        desiredTemp->setFrameShadow(QFrame::Plain);
        desiredTemp->setLineWidth(3);
        TempSet = new QDoubleSpinBox(centralwidget);
        TempSet->setObjectName(QStringLiteral("TempSet"));
        TempSet->setGeometry(QRect(100, 90, 91, 31));
        TempSet->setMinimum(4);
        TempSet->setMaximum(300);
        tempSetButton = new QDialogButtonBox(centralwidget);
        tempSetButton->setObjectName(QStringLiteral("tempSetButton"));
        tempSetButton->setGeometry(QRect(50, 130, 171, 51));
        tempSetButton->setAcceptDrops(false);
        tempSetButton->setStandardButtons(QDialogButtonBox::Apply|QDialogButtonBox::Cancel);
        tempSetButton->setCenterButtons(true);
        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);
        QObject::connect(emergencyStop, SIGNAL(clicked()), desiredTemp, SLOT(close()));
        QObject::connect(tempSetButton, SIGNAL(clicked(QAbstractButton*)), TempSet, SLOT(close()));
        QObject::connect(tempSetButton, SIGNAL(rejected()), TempSet, SLOT(show()));
        QObject::connect(TempSet, SIGNAL(valueChanged(double)), desiredTemp, SLOT(display(double)));
        QObject::connect(emergencyStop, SIGNAL(clicked()), TempSet, SLOT(hide()));
        QObject::connect(emergencyStop, SIGNAL(clicked()), tempSetButton, SLOT(hide()));

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", Q_NULLPTR));
        cTempLabel->setText(QApplication::translate("MainWindow", "Current Temp(K)", Q_NULLPTR));
        alertsButton->setText(QApplication::translate("MainWindow", "Alerts", Q_NULLPTR));
        emergencyStop->setText(QApplication::translate("MainWindow", "Emergency STOP", Q_NULLPTR));
        dataButton->setText(QApplication::translate("MainWindow", "Data", Q_NULLPTR));
        settingsButton->setText(QApplication::translate("MainWindow", "Settings", Q_NULLPTR));
        dtempLabel->setText(QApplication::translate("MainWindow", "Desired Temp(K)", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // NG_20_GEN1_20_GUIZ87516_H
