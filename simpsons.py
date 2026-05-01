from parent_class import Parent, Child

homer = Parent("Homer", "donuts", "bowling", "I like donuts", 36)
marge = Parent("Marge", "lemon meringue pie", "painting", "I don't like donuts", 34)
bart = Child("Bart", "pizza", "skateboarding", "Eat my shorts", 10)
maggie = Child("Maggie", "baby food", "playing with toys", "Goo goo ga ga", 1)
lisa = Child("Lisa", "sushi", "playing the saxophone", "If anyone wants me, I'll be in my room", 8)

homer.speak()
marge.speak()
bart.speak()
lisa.speak()
maggie.speak()