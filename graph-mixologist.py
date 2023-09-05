import matplotlib.pyplot as plt

# Predefined Cocktail Recipes
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
def select_cocktail():
    while True:
        print("Welcome to the Cocktail Graph Generator!")
        print("Please select a cocktail from the following list:")
        
        # Display available cocktails
        for idx, cocktail in enumerate(cocktail_recipes.keys(), 1):
            print(f"{idx}. {cocktail}")

        try:
            # User input for cocktail selection
            user_choice = int(input("Enter the number corresponding to your cocktail choice: "))
            
            # Validate user input and fetch the corresponding recipe
            if 1 <= user_choice <= len(cocktail_recipes):
                selected_cocktail = list(cocktail_recipes.keys())[user_choice - 1]
                print(f"You have selected: {selected_cocktail}")
                return selected_cocktail
            else:
                print("Invalid selection. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")

# Example usage:
# selected_cocktail = select_cocktail()
# if selected_cocktail:
#     print("Proceeding to graph generation...")

# Graph Generation
def generate_graph(selected_cocktail):
    # Fetch the recipe for the selected cocktail
    recipe = cocktail_recipes[selected_cocktail]
    
    # Data Preparation
    ingredients = list(recipe.keys())
    proportions = list(recipe.values())
    
    # Create the bar graph
    plt.figure(figsize=(10, 6))
    plt.barh(ingredients, proportions, color='skyblue')
    plt.xlabel('Quantity')
    plt.ylabel('Ingredients')
    plt.title(f'{selected_cocktail} Recipe')
    plt.grid(True)
    
    # Save the graph as an image
    plt.savefig(f"{selected_cocktail}_Recipe.png")
    plt.show()

# Example usage:
# generate_graph("Mojito")

# Component 5: Main Function

def main():
    while True:
        # User selects a cocktail
        selected_cocktail = select_cocktail()
        
        if selected_cocktail:
            # Generate the graph for the selected cocktail
            generate_graph(selected_cocktail)
            
            # Ask if the user wants to generate another graph
            another = input("Would you like to generate another graph? (y/n): ")
            if another.lower() != 'y':
                print("Thank you for using the Magical Cocktail Graph Generator. Farewell!")
                break

# Invoke the Main Function to start the program
if __name__ == "__main__":
    main()
