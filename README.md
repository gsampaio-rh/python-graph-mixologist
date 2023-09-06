# Cocktail Graph Generator

Welcome to the Cocktail Graph Generator, a magical tool that allows you to explore the relationships between various cocktails and their ingredients. With this Python-based program, you can visualize and learn about the world of mixology in a fun and interactive way.
## Table of Contents
- [Cocktail Graph Generator](#cocktail-graph-generator)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
  - [Adding More Cocktails](#adding-more-cocktails)
  - [Contributing](#contributing)
  - [License](#license)
## Introduction

The Cocktail Graph Generator is a Python application that leverages the power of PyVis to create interactive graphs representing cocktails and their ingredients. It allows you to:

- Explore individual cocktail recipes in a visual format.
- Discover how ingredients are shared among different cocktails.
- Generate a "Cosmic Web" of all cocktails to see their interconnectedness.

Whether you're a mixology enthusiast or simply curious about the art of cocktail-making, this tool offers a unique way to delve into the world of cocktails.
## Features

- Interactive visualization of cocktail recipes.
- A selection interface for choosing cocktails.
- Option to generate a cosmic web of all cocktails.
- Easy customization and expansion of the cocktail database.
- Visualizations saved as HTML files for future reference.
## Getting Started

To get started with the Cocktail Graph Generator, follow these steps:

1. **Clone the Repository:** Clone this repository to your local machine.

    ```shell
    git clone https://github.com/yourusername/cocktail-graph-generator.git
    ```

2. **Install Dependencies:** Make sure you have Python and the required libraries installed. You can install the necessary dependencies using pip:

    ```shell
    pip install pyvis pandas
    ```

3. **Run the Program:** Execute the `cocktail_graph.py` script to start the Cocktail Graph Generator.

    ```shell
    python cocktail_graph.py
    ```

4. **Explore Cocktails:** Follow the on-screen instructions to explore cocktail recipes and their relationships.

## Usage

- When you run the program, you'll be presented with a selection interface to choose a cocktail to explore.

- You can either select a specific cocktail to see its recipe graph or choose the "Cosmic Web" option to view a graph connecting all cocktails.

- The generated graphs are saved as HTML files in the project directory for easy access.

## Adding More Cocktails

To expand the collection of cocktails in the generator, simply edit the `cocktail_recipes` dictionary in the `cocktail_graph.py` file. You can add more cocktails by following the existing pattern:

```python
cocktail_recipes = {
    # Existing cocktail recipes here...

    "New Cocktail 1": {"Ingredient A": 40, "Ingredient B": 20, "Ingredient C": 10},
    "New Cocktail 2": {"Ingredient X": 30, "Ingredient Y": 25, "Ingredient Z": 15},
    # Add more as needed...
}
```

Feel free to customize the new cocktails and their ingredients to your liking.
## Contributing
Contributions to this project are welcome! If you have ideas for improvements, new features, or bug fixes, please submit a pull request or open an issue on the GitHub repository.
## License
This project is licensed under the MIT License, which means you are free to use, modify, and distribute the code for both personal and commercial purposes.