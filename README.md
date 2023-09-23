# CarolApp Monitor

![logo](assets/images/logo.png)

<p align="center">
    <a href="https://codecov.io/gh/RWallan/carol-app-monitor" target="_blank"> 
    <img src="https://codecov.io/gh/RWallan/carol-app-monitor/branch/main/graph/badge.svg?token=zP2gCNgi0t"/> 
    </a>
    <a href="https://github.com/RWallan/carol-app-monitor/actions/workflows/test_pipeline.yml" target="_blank"> 
    <img src="https://github.com/RWallan/carol-app-monitor/actions/workflows/test_pipeline.yml/badge.svg"/> 
    </a>
    <a href="https://github.com/RWallan/carol-app-monitor" target="_blank"><img src="https://img.shields.io/github/issues/RWallan/carol-app-monitor">
    </a>
</p>

---

**Documentation:** [https://github.com/RWallan/carol-app-monitor/tree/main/docs](https://github.com/RWallan/carol-app-monitor/tree/main/docs)

**Source code:** [https://github.com/RWallan/carol-app-monitor](https://github.com/RWallan/carol-app-monitor)

---

The CarolApp Monitor is a simple and useful application to monitor and automatically restart online CarolApps if they are not running. A CarolApp is an application developed in TOTVS Carol platform that offers specific business solutions.

Using the CarolApp Monitor is simple!

You just need to configure a batch CarolApp that allows you to easily personalize a schedule. With it, you can define specific time stamps to verify the CarolApp status and to automatically restart it if needed. This way, the CarolApp Monitor guarantees the continuous availability of your apps in TOTVS Carol platform.

## Why to use CarolApp Monitor:

Sometimes a CarolApp can stop working and you must to get some time to check which apps has stopped and turn them on :disappointed: .

So thinking about it, CarolApp Monitor will monitor your online apps and restart if they stop without the necessity of you expand your time :rocket:.

The key features are:

* **Simple :sweat_smile:**: Simple to configure and install in your Carol tenant.
* **Intuitive :smiling_face_with_3_hearts:**: With fews steps you'll ready to use.
* **No coding :no_entry_sign:**: It's not necessary to be a Python expert coder to use.
* **Fast to learn :fast_forward:**: Great documentation and support to instruct how to configure and install the CarolApp Monitor.

## What CarolApp Monitor do: [ADD Flowchart]

CarolApp Monitor will look periodically all online CarolApps searching if anyone isn't running and restart your services one by one.

![FlowChart](assets/images/flowchart.png)

## Requirements

Python 3.10+

CarolApp Monitor has been developed on the shoulders of:

* [Poetry](https://python-poetry.org/docs/) for Python dependency management.
* [Pycarol](https://pycarol.readthedocs.io/en/2.54.15/index.html) for CarolApp processes informations.

## What is TOTVS Carol

Created in 2015, TOTVS Carol it's a plataform of data and AI developed by TOTVS. The plataform it's an advanced solution of data management that can connect with different fonts of data to analyze informations and show result that support decision makes.

This way, TOTVS Carol enable informations rastreability strategies, development and deployement of machine leaning algorithms, helping with predictions and also with projects of computation vision and natural language process (NLP).

With that, TOTVS Carol enables:

* **Forecast and prevision** :chart_with_upwards_trend:: You can analyze your past data to predict the future.
* **Recomendations** :white_check_mark:: With machine learning algorithms the plataform can understand action patterns made by humans and create recomendations of how to act in similar processes.
* **Otimization** :simple-googleoptimize:: More performance and padronization with Deep Neural Network.
* **Computational vision** :eye:: You can work with real time data generated with your cameras using facial recognization.
* **Conversation experience** :material-chat:: Using NLP it's possible to create entire structure of conversations.

## Installation

To use this project in your tenants, you'll need to create and build a CarolApp. 

First, make the download `manifest.json` that include all settings to build your CarolApp. To make the download, just click in the button above :wink:.

<center>
    <a href="./assets/manifest.json" download="manifest.json"></a>
</center>

After that, we'll configure your batch CarolApp. To configure this app, you'll need:

1. Create the CarolApp
1. Build the App
1. Add a schedule to your process.

And it's done! :partying_face:

## License
This project is licensed under the terms of the MIT license.
