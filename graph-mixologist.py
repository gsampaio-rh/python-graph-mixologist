from pyvis.network import Network
from pyvis.options import Layout
import pandas as pd

# Predefined Cocktail Recipes
# Define a dictionary containing cocktail recipes with ingredients and their proportions.
cocktail_recipes = {
    "Mojito": {"Rum": 50, "Mint": 10, "Lime Juice": 25, "Soda": 75},
    "Martini": {"Gin": 60, "Dry Vermouth": 10},
    "Old Fashioned": {"Bourbon": 45, "Angostura Bitters": 2, "Sugar": 1},
    "Margarita": {"Tequila": 50, "Lime Juice": 20, "Triple Sec": 20},
    "Pina Colada": {"Rum": 50, "Coconut Cream": 25, "Pineapple Juice": 25},
    "Cosmopolitan": {"Vodka": 40, "Triple Sec": 20, "Lime Juice": 20},
    "Whiskey Sour": {"Whiskey": 45, "Lemon Juice": 25, "Sugar": 10},
    "Negroni": {"Gin": 30, "Campari": 30, "Sweet Vermouth": 30},
    "Bloody Mary": {"Vodka": 50, "Tomato Juice": 100, "Tabasco": 5},
    "Tequila Sunrise": {"Tequila": 50, "Orange Juice": 100, "Grenadine": 10},
    "Daiquiri": {"Rum": 45, "Lime Juice": 25, "Simple Syrup": 15},
    "Long Island Iced Tea": {"Vodka": 15, "Tequila": 15, "Rum": 15, "Gin": 15, "Triple Sec": 15, "Lemon Juice": 25, "Cola": 30},
    "Mai Tai": {"Rum": 40, "Lime Juice": 20, "Orgeat Syrup": 15, "Triple Sec": 15},
    "Espresso Martini": {"Vodka": 50, "Coffee Liqueur": 25, "Espresso": 25},
    "Tom Collins": {"Gin": 45, "Lemon Juice": 30, "Simple Syrup": 10, "Soda": 60},
    "Manhattan": {"Whiskey": 50, "Sweet Vermouth": 20, "Angostura Bitters": 2},
    "Sazerac": {"Rye Whiskey": 50, "Peychaud's Bitters": 5, "Absinthe": 5, "Sugar": 1},
    "Sidecar": {"Cognac": 50, "Triple Sec": 20, "Lemon Juice": 20},
    "Dark 'n Stormy": {"Rum": 50, "Ginger Beer": 100, "Lime Juice": 10},
    "French 75": {"Gin": 30, "Champagne": 90, "Lemon Juice": 10, "Simple Syrup": 5}
}

# User Selection Interface
# Create a function to interact with the user and allow them to select a cocktail.
def select_cocktail():
    while True:
        print("\nWelcome to the Cocktail Graph Generator!")
        print("Please select a cocktail from the following list:")
        print("0. Cosmic Web of All Cocktails")
        
        for idx, cocktail in enumerate(cocktail_recipes.keys(), 1):
            print(f"{idx}. {cocktail}")

        try:
            user_choice = int(input("Enter the number corresponding to your choice: "))
            
            if user_choice == 0:
                return 'Cosmic Web'
            elif 1 <= user_choice <= len(cocktail_recipes):
                selected_cocktail = list(cocktail_recipes.keys())[user_choice - 1]
                print(f"You have selected: {selected_cocktail}")
                return selected_cocktail
            else:
                print("Invalid selection. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")

# Initialize the PyVis network with specific settings.
# This function returns a configured network object.
def initVisNetwork():
    # Initialize the PyVis network
    nt = Network(height="750px", width="30%", bgcolor="#101c26ff", font_color="white", select_menu=True)
    # nt.show_buttons(filter_=['physics'])
    # nt.show_buttons(filter_=['nodes'])

    return nt

# Enhanced Graph Generation using PyVis
# Generate a graph for a selected cocktail.
# It adds nodes and edges for ingredients and proportions.
# The graph is then displayed and saved as an HTML file.
def generate_cocktail_graph(selected_cocktail):
    # Fetch the recipe for the selected cocktail
    recipe = cocktail_recipes[selected_cocktail]

    nt = initVisNetwork()

    # Add nodes and edges
    nt.add_node(selected_cocktail, label=selected_cocktail, color='red')
    for ingredient, proportion in recipe.items():
        nt.add_node(ingredient, label=ingredient, color='blue')
        nt.add_edge(selected_cocktail, ingredient, value=proportion)

    # Set the physics layout to improve visualization
    nt.barnes_hut()

    # Save the graph as an HTML file
    graph_html = f"{selected_cocktail}_Recipe_Network.html"
    nt.show(graph_html, notebook=False)

# Enhanced Cosmic Web Generation using PyVis
# Generate a cosmic web graph that connects all cocktails and ingredients. 
# It sets up nodes and edges for each, and the resulting graph is displayed and saved as HTML.
def generate_cosmic_web():
    # Initialize the PyVis network
    nt = initVisNetwork()
  
    added_nodes = set()  # To track added nodes

    for cocktail, recipe in cocktail_recipes.items():
        nt.add_node(cocktail, shape="circle", label=cocktail, color='rgba(166, 45, 45, 1)')
        for ingredient, proportion in recipe.items():
            if ingredient not in added_nodes:
                nt.add_node(ingredient, label=ingredient, color='rgba(28, 65, 140, 1)')
                added_nodes.add(ingredient)  # Add to the set of added nodes
            nt.add_edge(cocktail, ingredient, value=proportion)

    # Set the physics layout to improve visualization
    nt.force_atlas_2based()

    # Render the HTML using the template
    graph_html = "Cosmic_Web_of_Cocktails.html"
    
    nt.show(graph_html, notebook=False)

# Main Function
# The main program loop where the user interacts with the cocktail graph generator. 
# It allows users to select cocktails and explore their ingredients' relationships.
# The loop continues until the user decides to exit.
def main():
    while True:
        selected_option = select_cocktail()
        
        if selected_option == 'Cosmic Web':
            generate_cosmic_web()
        elif selected_option:
            generate_cocktail_graph(selected_option)

        another = input("Would you like to explore further? (y/n): ")
        if another.lower() != 'y':
            print("Thank you for using the Cocktail Graph Generator. Farewell!")
            break

# Invoke the Main Function to start the program
if __name__ == "__main__":
    main()
