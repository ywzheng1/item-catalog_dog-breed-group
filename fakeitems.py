from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()


# Items for Sporting Group
category1 = Category(name="Sporting Group", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Golden Retriever", user_id=1, description="Known for their kind eyes, loyalty, and enthusiasm for life, the golden retriever is one of the most popular dog breeds in the United States. Though historically bred as hunting dogs in the Scottish Highlands, goldens also make excellent family dogs. The dogs usually get along well with children and are incredibly affectionate and intelligent. Golden retrievers make wonderful service dogs and are often very successful as guide, assistance, or search and rescue dogs.", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Pointer", user_id=1,  description="The pointer dog is a powerful yet graceful dog breed, with a very clear job: to point. The hardworking, even-tempered breed has a centuries-long history of pointing game birds. High-energy pointers are capable of great speed and agility, making them a perfect companion for runners, cyclists, or anyone who is athletic. Their affectionate, loyal natural means they are an ideal family pet.", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Brittany", user_id=1, description="The pointer dog is a powerful yet graceful dog breed, with a very clear job: to point. The hardworking, even-tempered breed has a centuries-long history of pointing game birds. High-energy pointers are capable of great speed and agility, making them a perfect companion for runners, cyclists, or anyone who is athletic. Their affectionate, loyal natural means they are an ideal family pet.", category=category1)

session.add(item3)
session.commit()

# Items for Hound Group
category2 = Category(name="Hound Group", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Beagle", user_id=1, description="The beagle is one of the most popular and recognizable dog breeds. Beagles are energetic, carefree, and optimistic dogs but they can have a stubborn streak. The beagle is an ideal breed for active households. The comical and even-tempered demeanor of this breed makes it a great choice for families with children, but remember that not all dogs get along with kids, regardless of breed.", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Greyhound", user_id=1,  description="With the ability to run at speeds upwards of 45 miles per hour, the Greyhound is the fastest dog breed in the world. Their long legs and narrow, streamlined bodies make Greyhounds racers by design. The breed's history traces back to the times of the Ancient Egyptians, Romans, and Greeks, who probably had Greyhounds or similar dogs.", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Basenji", user_id=1, description="The Basenji is among the most distinct of all dog breeds, particularly since it's been identified via DNA to have descended from the gray wolf. This small, elegant dog is probably best known for its lack of barking. However, the breed will sometimes whine and make noises that resemble yodeling.", category=category2)

session.add(item3)
session.commit()

# Items for Toy Group
category3 = Category(name="Toy Group", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Chinese Crested", user_id=1, description="Not many dogs turn heads more than a Chinese crested will. These dainty little dogs are famously hairless with large poufs of hair on their heads, paws, and tails. But about half of Chinese crested dogs are actually powderpuffs, a variation of the breed that has fur throughout their bodies. But when considering which pet to bring home, it is important to go beyond looks. The Chinese crested is also a bright, affectionate little dog with a cheerful personality. This breed is surprisingly energetic and quite trainable, giving them a winning personality to go with their unique looks.", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Chihuahua", user_id=1, description="The Chihuahua is a tiny but confident dog.", category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Japanese Chin", user_id=1, description="The Japanese Chin, also referred to as a Japanese Spaniel, is a relatively rare toy breed with a distinctly noble and ancient heritage. Despite the name, they were thought to originate in China before becoming popular in Japan. They are known for being even-tempered, loyal and affectionate. They are often described as being 'cat-like' and can be fond of curling up on an owners lap.", category=category3)

session.add(item3)
session.commit()

# Items for Non-Sporting Group
category4 = Category(name="Non-Sporting Group", user_id=1)

session.add(category4)
session.commit()

item1 = CategoryItem(name="Lhasa Apso", user_id=1, description="The Lhasa apso is a relatively small but quite sturdy dog with a long and dense double hair coat. This breed is known to be happy and playful, but also independent and mischievous. They have a history of thousands of years as a tiny guard dog. This breed also excels as a hearing ear dog for people with hearing loss.", category=category4)

session.add(item1)
session.commit()

# Items for Working Group
category5 = Category(name="Working Group", user_id=1)

session.add(category5)
session.commit()

item1 = CategoryItem(name="Boxer", user_id=1, description="The boxer is an energetic, intelligent, athletic, and loyal dog breed with a sweet and playful temperament that makes it an ideal companion. Boxers often get along very well with children and possess an instinct to protect the family, making them wonderful family dogs, despite their history as fighting dogs. Boxers have become incredibly popular in the United States, but the breed dates back to 16th-century Europe.", category=category5)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Bernese Mountain Dog", user_id=1, description="The Bernese Mountain Dog, which originated in Switzerland, is a gentle giant with its large frame and striking tri-colored coat. An excellent family dog, the Bernese Mountain Dog gets along well with children and most other pets and loves to be included in all family activities. Breed aficionados love the Bernese Mountain Dogs intelligence and devotion to family.", category=category5)

session.add(item2)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
