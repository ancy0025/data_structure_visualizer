{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNaj6AySWoc0bvYywfPr5Lp",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ancy0025/data_structure_visualizer/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "UeqHZIn2oeny",
        "outputId": "470eaf36-73cc-4531-acdd-a901a6e93c53",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.44.1-py3-none-any.whl.metadata (8.9 kB)\n",
            "Requirement already satisfied: graphviz in /usr/local/lib/python3.11/dist-packages (0.20.3)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.11/dist-packages (3.4.2)\n",
            "Requirement already satisfied: matplotlib in /usr/local/lib/python3.11/dist-packages (3.10.0)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.1.8)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.1.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.29.4)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.1.2)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.13.2)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.11/dist-packages (from matplotlib) (1.3.2)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.11/dist-packages (from matplotlib) (0.12.1)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.11/dist-packages (from matplotlib) (4.57.0)\n",
            "Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.11/dist-packages (from matplotlib) (1.4.8)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.11/dist-packages (from matplotlib) (3.2.3)\n",
            "Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.11/dist-packages (from matplotlib) (2.8.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (1.35.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.7->matplotlib) (1.17.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2025.1.31)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.3.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.24.0)\n",
            "Downloading streamlit-1.44.1-py3-none-any.whl (9.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.8/9.8 MB\u001b[0m \u001b[31m52.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m56.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m4.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.44.1 watchdog-6.0.0\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit graphviz networkx matplotlib\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "import graphviz\n",
        "import networkx as nx\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# Title of the app\n",
        "st.title(\"📊 Data Structure Visualizer\")\n",
        "\n",
        "# Sidebar menu to choose data structure\n",
        "menu = st.sidebar.selectbox(\n",
        "    \"Choose a Data Structure\",\n",
        "    [\"Array\", \"Stack\", \"Queue\", \"Linked List\", \"Tree\", \"Graph\"]\n",
        ")\n",
        "\n",
        "# Array Visualizer\n",
        "if menu == \"Array\":\n",
        "    st.header(\"📦 Array Visualizer\")\n",
        "    array_input = st.text_input(\"Enter array elements (comma-separated)\", \"10,20,30,40\")\n",
        "    if array_input:\n",
        "        array = [int(x.strip()) for x in array_input.split(\",\")]\n",
        "        st.write(\"✅ Array: \", array)\n",
        "\n",
        "# Stack Visualizer\n",
        "elif menu == \"Stack\":\n",
        "    st.header(\"📚 Stack (LIFO) Visualizer\")\n",
        "    stack_input = st.text_input(\"Enter stack elements (comma-separated)\", \"1,2,3,4\")\n",
        "    if stack_input:\n",
        "        stack = [int(x.strip()) for x in stack_input.split(\",\")]\n",
        "        st.write(\"✅ Current Stack (Top → Bottom): \", stack[::-1])\n",
        "\n",
        "# Queue Visualizer\n",
        "elif menu == \"Queue\":\n",
        "    st.header(\"🚶‍♂️ Queue (FIFO) Visualizer\")\n",
        "    queue_input = st.text_input(\"Enter queue elements (comma-separated)\", \"5,6,7,8\")\n",
        "    if queue_input:\n",
        "        queue = [int(x.strip()) for x in queue_input.split(\",\")]\n",
        "        st.write(\"✅ Current Queue (Front → Rear): \", queue)\n",
        "\n",
        "# Linked List Visualizer\n",
        "elif menu == \"Linked List\":\n",
        "    st.header(\"🔗 Linked List Visualizer\")\n",
        "    ll_input = st.text_input(\"Enter linked list elements (comma-separated)\", \"11,22,33,44\")\n",
        "    if ll_input:\n",
        "        ll = [x.strip() for x in ll_input.split(\",\")]\n",
        "        code = \"head -> \" + \" -> \".join(ll) + \" -> None\"\n",
        "        st.code(code, language='python')\n",
        "\n",
        "# Binary Tree Visualizer\n",
        "elif menu == \"Tree\":\n",
        "    st.header(\"🌳 Binary Tree Visualizer\")\n",
        "    st.write(\"Example 3-node Binary Tree\")\n",
        "    dot = graphviz.Digraph()\n",
        "    dot.node(\"A\", \"1\")\n",
        "    dot.node(\"B\", \"2\")\n",
        "    dot.node(\"C\", \"3\")\n",
        "    dot.edges([\"AB\", \"AC\"])\n",
        "    st.graphviz_chart(dot)\n",
        "\n",
        "# Graph Visualizer\n",
        "elif menu == \"Graph\":\n",
        "    st.header(\"🗺️ Graph Visualizer\")\n",
        "    graph_input = st.text_input(\"Enter graph edges\", \"1-2,2-3,3-4,4-1\")\n",
        "    if graph_input:\n",
        "        G = nx.Graph()\n",
        "        edges = [tuple(edge.strip().split(\"-\")) for edge in graph_input.split(\",\")]\n",
        "        G.add_edges_from(edges)\n",
        "        pos = nx.spring_layout(G)\n",
        "        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1600, font_size=18)\n",
        "        st.pyplot(plt)\n"
      ],
      "metadata": {
        "id": "OdrBxiE0oqzK",
        "outputId": "f5864c00-6d8a-46fa-a65c-fac27a80def9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "omi-_pMnosj8"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}