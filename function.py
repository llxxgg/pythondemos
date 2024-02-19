# def greet_user(username):
#     """显示简单的问候语。"""
#     print(f"hello, {username.title()}!")


# greet_user("chris")


# def describe_pet(pet_name, animal_type='dog'):
#     """显示宠物的信息"""
#     print(f"\n I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet(pet_name="hellokitty")


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# musician = get_formatted_name("jimi", "hendrix")
# print(musician)


# def build_profile(first, last, **user_info):
#     user_info['first_nmae'] = first
#     user_info['last_name'] = last
#     return user_info


# user_profile = build_profile(
#     'albert', 'einstein', location='princeton', field='physics')
# print(user_profile)
