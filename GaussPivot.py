{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOt2XFh0AVCtqktAB94D6Y6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/WFVieira-hub/Met_Matematicos/blob/master/GaussPivot.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BWEsTlHapDb9",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy as np\n",
        "\n",
        "def gauss(M,f):\n",
        "    n = len(f)\n",
        "    A = np.zeros((n,n+1))\n",
        "    A[:,:-1] = M\n",
        "    A[:,-1] = f\n",
        "\n",
        "    for i in range(0, n):\n",
        "        # Search for maximum in this column\n",
        "        maxEl = abs(A[i][i])\n",
        "        maxRow = i\n",
        "        for k in range(i + 1, n):\n",
        "            if abs(A[k][i]) > maxEl:\n",
        "                maxEl = abs(A[k][i])\n",
        "                maxRow = k\n",
        "\n",
        "        # Swap maximum row with current row (column by column)\n",
        "        for k in range(i, n + 1):\n",
        "            tmp = A[maxRow][k]\n",
        "            A[maxRow][k] = A[i][k]\n",
        "            A[i][k] = tmp\n",
        "\n",
        "        # Make all rows below this one 0 in current column\n",
        "        for k in range(i + 1, n):\n",
        "            c = -A[k][i] / A[i][i]\n",
        "            for j in range(i, n + 1):\n",
        "                if i == j:\n",
        "                    A[k][j] = 0\n",
        "                else:\n",
        "                    A[k][j] += c * A[i][j]\n",
        "\n",
        "    # Solve equation Ax=b for an upper triangular matrix A\n",
        "    x = [0 for i in range(n)]\n",
        "    for i in range(n - 1, -1, -1):\n",
        "        x[i] = A[i][n] / A[i][i]\n",
        "        for k in range(i - 1, -1, -1):\n",
        "            A[k][n] -= A[k][i] * x[i]\n",
        "    return x"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}