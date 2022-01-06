def make_car(manufacturer, model, **options):
    options['manufacturer']: 'manufacturer'
    options['model']: model
    return options
print(make_car('ran', 'shen', abc='woaini'))


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
print(build_profile('ran', 'shen', abc='woaini'))
