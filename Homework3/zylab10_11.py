# Syed Ali
# 1799248

# start by creating FoodItem class
class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):   # setting constructor up with parameters
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

# Code below is copied from lab
# on line 15 I had fix the parameter name "num_servings" so that no errors are displayed
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_calories(self, num_serving):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_serving
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == "__main__":
    food_1 = FoodItem()

    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())

    food_2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)

    num_servings = float(input())

    food_1.print_info()
    print(f'Number of calories for {num_servings:.2f} serving(s): {food_1.get_calories(num_servings):.2f}')

    print()

    food_2.print_info()
    print(f'Number of calories for {num_servings:.2f} serving(s): {food_2.get_calories(num_servings):.2f}')
