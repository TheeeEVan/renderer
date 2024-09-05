# Renderer

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/0-percent-optimized.svg)](https://forthebadge.com)

A *very slow imperfect* object renderer using only pygame's 2D functionality.

<img src="./assets/cube.gif" alt="spinning cube" width="300"/><img src="./assets/monkey.gif" alt="spinning monkey" width="300"/>

This served as my Computer Science 30 (Grade 12) final project. We were tasked with making a substantial project that demonstrated the use of Object Oriented Programming (OOP).

## Quick Start

Just copy and paste into your terminal, select an object, and you will see it.

```
git clone https://github.com/TheeeEVan/renderer
cd renderer
pip3 install -r requirements.txt
python3 main.py
```

*Note: This guide assumes that you have git, python3, and pip installed properly.*

## Requirements
This project uses the following packages
- pygame

## Issues
You will notice with more complex shapes such as the monkey some faces render improperly. This is mainly because I did not properly implement z-buffering. Instead I cheated through z buffering by simply taking the average z of all vertices of a face, then drawing faces starting with the furthest back ones. This works flawlessly with simple shapes such as the cube, however with more complex shapes issues arise. This choice was mainly due to time limitations.
